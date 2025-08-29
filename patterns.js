// Pattern filtering functionality
document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const patternCards = document.querySelectorAll('.pattern-card');

    // Filter functionality
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filter = this.getAttribute('data-filter');
            
            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            // Filter patterns
            patternCards.forEach(card => {
                const category = card.getAttribute('data-category');
                
                if (filter === 'all' || category === filter) {
                    card.style.display = 'block';
                    card.style.animation = 'fadeIn 0.3s ease';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
    
    // Pattern purchase functionality
    const buyButtons = document.querySelectorAll('.pattern-buy-btn');
    buyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const patternCard = this.closest('.pattern-card');
            const patternName = patternCard.querySelector('h3').textContent;
            
            // Simple purchase simulation - you would integrate with actual payment processor
            const confirmed = confirm(`Purchase "${patternName}" for $8.99?\n\nThis would redirect to your payment processor.`);
            
            if (confirmed) {
                // Show success state
                this.innerHTML = '✓ Added to Cart';
                this.style.background = '#28a745';
                
                // Reset after 2 seconds
                setTimeout(() => {
                    this.innerHTML = 'Buy Pattern';
                    this.style.background = '';
                }, 2000);
            }
        });
    });
});

// Add fade in animation
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
`;