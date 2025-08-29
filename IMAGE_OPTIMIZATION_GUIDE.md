# Pattern Pioneer Image Optimization Guide

Your 25MB images are too large for web! Here's how to optimize them:

## 🎯 **Target Specs for Web:**
- **Size:** 50-200KB (instead of 25MB)
- **Dimensions:** 800x800px (perfect for your pattern cards)
- **Format:** JPEG (best compression for patterns)
- **Quality:** 85% (great balance of quality/size)

## **Method 1: Automated Script (Easiest)**

### Prerequisites:
```bash
pip install Pillow
```

### Usage:
1. **Put your large pattern images** in a folder (e.g., `raw-patterns/`)
2. **Run the script**:
   ```bash
   python optimize-images.py raw-patterns/
   ```
3. **Script will create `images/` folder** with optimized versions
4. **Automatically names them** `pattern1.jpg`, `pattern2.jpg`, etc.

### Advanced Options:
```bash
# Custom settings
python optimize-images.py raw-patterns/ --max-size 1000 --quality 90

# Different output folder  
python optimize-images.py raw-patterns/ --output-dir web-images/
```

## **Method 2: Online Tools (No Install)**

### TinyPNG (Recommended):
1. **Go to**: https://tinypng.com/
2. **Upload your images** (up to 20 at once)
3. **Download optimized versions**
4. **Rename to**: `pattern1.jpg`, `pattern2.jpg`, etc.

### Squoosh by Google:
1. **Go to**: https://squoosh.app/
2. **Drag and drop** your image
3. **Adjust settings**: JPEG, 85% quality, resize to 800px
4. **Download optimized version**

## **Method 3: Built-in Tools**

### Windows (Paint):
1. **Open image in Paint**
2. **Resize**: Home → Resize → 800x800 pixels
3. **Save As**: JPEG format

### Mac (Preview):
1. **Open image in Preview**
2. **Tools → Adjust Size**: 800x800 pixels
3. **Export**: JPEG, adjust quality slider

### Photoshop:
1. **File → Export → Export As**
2. **Format**: JPEG
3. **Quality**: 85%
4. **Resize**: 800x800px

## **What the Script Does:**
- ✅ **Automatically resizes** to 800x800px (perfect for web)
- ✅ **Compresses** from 25MB to ~100KB (250x smaller!)
- ✅ **Maintains quality** with smart compression
- ✅ **Fixes rotation** issues automatically
- ✅ **Batch processes** all 6 images at once
- ✅ **Names correctly** for your website

## **Before vs After:**
```
Before: pattern-original.tiff (25MB, 4096x4096px)
After:  pattern1.jpg (120KB, 800x800px)
Result: 99.5% smaller, perfect for web!
```

## **Next Steps After Optimization:**
1. **Copy optimized images** to your website's `images/` folder
2. **Push to GitHub**: `git add images/ && git commit -m "Add optimized pattern images"`
3. **Your website automatically displays them**

**Recommendation**: Use the automated script - it's specifically designed for your Pattern Pioneer images and handles everything automatically!

Run this and your 25MB images become web-ready in seconds!