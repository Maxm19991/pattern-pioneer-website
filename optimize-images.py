#!/usr/bin/env python3
"""
Pattern Pioneer Image Optimization Script
Converts large pattern images (25MB+) to web-optimized versions
"""

import os
import sys
from PIL import Image, ImageOps
import argparse

def optimize_pattern_image(input_path, output_path, max_size=800, quality=85, crop_zoom=2.0):
    """
    Optimize a pattern image for web display
    
    Args:
        input_path: Path to original large image
        output_path: Path where optimized image will be saved
        max_size: Maximum width/height in pixels (default 800px for web display)
        quality: JPEG quality 1-100 (default 85 for good quality/size balance)
        crop_zoom: Crop zoom factor (2.0 = 200% crop from center)
    """
    try:
        # Open and process image
        with Image.open(input_path) as img:
            print(f"Original size: {img.size}, Format: {img.format}")
            
            # Convert to RGB if necessary (for JPEG output)
            if img.mode in ('RGBA', 'P', 'LA'):
                # Create white background for transparent images
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'RGBA':
                    background.paste(img, mask=img.split()[-1])
                else:
                    background.paste(img)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Auto-orient image (fix rotation)
            img = ImageOps.exif_transpose(img)
            
            # Apply crop zoom if specified
            if crop_zoom > 1.0:
                width, height = img.size
                
                # Calculate crop dimensions (smaller area = more zoom)
                crop_width = int(width / crop_zoom)
                crop_height = int(height / crop_zoom)
                
                # Calculate center crop coordinates
                left = (width - crop_width) // 2
                top = (height - crop_height) // 2
                right = left + crop_width
                bottom = top + crop_height
                
                # Crop from center
                img = img.crop((left, top, right, bottom))
                print(f"Cropped to {crop_zoom}x zoom: {img.size}")
            
            # Resize while maintaining aspect ratio
            img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
            
            # Save optimized version
            img.save(output_path, 'JPEG', quality=quality, optimize=True)
            
            # Get file sizes
            original_size = os.path.getsize(input_path) / (1024 * 1024)  # MB
            optimized_size = os.path.getsize(output_path) / 1024  # KB
            
            print(f"SUCCESS: Optimized: {original_size:.1f}MB -> {optimized_size:.0f}KB")
            print(f"   New size: {img.size}")
            
    except Exception as e:
        print(f"ERROR processing {input_path}: {e}")

def batch_optimize_patterns(input_dir, output_dir="images", pattern_names=None):
    """
    Batch optimize pattern images for Pattern Pioneer website
    """
    if pattern_names is None:
        pattern_names = [
            "pattern1.jpg", "pattern2.jpg", "pattern3.jpg", 
            "pattern4.jpg", "pattern5.jpg", "pattern6.jpg"
        ]
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all image files from input directory
    image_extensions = ('.jpg', '.jpeg', '.png', '.tiff', '.tif', '.bmp')
    image_files = []
    
    for file in os.listdir(input_dir):
        if file.lower().endswith(image_extensions):
            image_files.append(file)
    
    image_files.sort()  # Sort to get consistent order
    
    print(f"Found {len(image_files)} images in {input_dir}")
    print("=" * 50)
    
    # Process up to 6 images (for website)
    for i, filename in enumerate(image_files[:6]):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, pattern_names[i])
        
        print(f"Processing {i+1}/6: {filename} -> {pattern_names[i]}")
        optimize_pattern_image(input_path, output_path, crop_zoom=2.0)
        print()

def main():
    parser = argparse.ArgumentParser(description='Optimize Pattern Pioneer images for web')
    parser.add_argument('input_dir', help='Directory containing large pattern images')
    parser.add_argument('--output-dir', default='images', help='Output directory (default: images)')
    parser.add_argument('--max-size', type=int, default=800, help='Max width/height in pixels (default: 800)')
    parser.add_argument('--quality', type=int, default=85, help='JPEG quality 1-100 (default: 85)')
    parser.add_argument('--crop-zoom', type=float, default=2.0, help='Crop zoom factor (default: 2.0 for 200%% crop)')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_dir):
        print(f"ERROR: Input directory '{args.input_dir}' does not exist")
        return 1
    
    print(f"Pattern Pioneer Image Optimizer")
    print(f"Input: {args.input_dir}")
    print(f"Output: {args.output_dir}")
    print(f"Settings: {args.max_size}px max, {args.quality}% quality")
    print("=" * 50)
    
    batch_optimize_patterns(args.input_dir, args.output_dir)
    
    print("SUCCESS: Optimization complete!")
    print(f"Optimized images saved to: {args.output_dir}/")
    print("Ready to upload to your website!")

if __name__ == '__main__':
    sys.exit(main())