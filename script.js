// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', function() {
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    
    navToggle.addEventListener('click', function() {
        navToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
        
        // Prevent body scroll when menu is open
        if (navMenu.classList.contains('active')) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = '';
        }
    });
    
    // Close mobile menu when clicking on links
    const navLinks = document.querySelectorAll('.nav-link, .nav-btn');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navToggle.classList.remove('active');
            navMenu.classList.remove('active');
            document.body.style.overflow = '';
        });
    });
    
    // Smooth scrolling for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offsetTop = target.offsetTop - 70; // Account for fixed nav height
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Newsletter form submission
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;
            
            if (email) {
                // Show success message (you would integrate with your actual newsletter service)
                const formGroup = this.querySelector('.form-group');
                const successMessage = document.createElement('div');
                successMessage.innerHTML = '<p style="color: #fff; margin-top: 1rem;">✓ Thanks! You\'ll receive your first pattern pack next Monday.</p>';
                formGroup.appendChild(successMessage);
                
                // Reset form after 3 seconds
                setTimeout(() => {
                    this.reset();
                    successMessage.remove();
                }, 3000);
            }
        });
    }
    
    // Pattern card hover effects and interactions
    const patternCards = document.querySelectorAll('.pattern-card');
    patternCards.forEach(card => {
        card.addEventListener('click', function() {
            // Navigate to all patterns page
            window.location.href = 'all-patterns.html';
        });
        
        // Add pointer cursor to indicate clickability
        card.style.cursor = 'pointer';
    });
    
    // Add scroll effect to navigation
    let lastScrollTop = 0;
    const nav = document.querySelector('.nav');
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > lastScrollTop && scrollTop > 100) {
            // Scrolling down
            nav.style.transform = 'translateY(-100%)';
        } else {
            // Scrolling up
            nav.style.transform = 'translateY(0)';
        }
        
        lastScrollTop = scrollTop;
    });
    
    // Add transition to nav for smooth hide/show
    nav.style.transition = 'transform 0.3s ease-in-out';
});