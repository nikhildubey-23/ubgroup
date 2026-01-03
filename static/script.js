// Custom JavaScript for UB Group website

// Smooth scrolling for anchor links (if needed in future)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add any additional interactivity here
console.log('UB Group website loaded successfully!');
