// Custom JavaScript for UB Group website

// Hero Section Background Image Rotation
let currentImageIndex = 0;
let heroImages = [];

function initHeroImages() {
    const heroBackground = document.getElementById('heroBackground');
    if (!heroBackground) return;

    // Get image paths from data attribute
    const imagesData = heroBackground.getAttribute('data-images');
    if (imagesData) {
        heroImages = JSON.parse(imagesData);
    }

    // Convert relative paths to full URLs with /static/ prefix
    heroImages = heroImages.map(img => '/static/' + img);
    
    // Start rotating images
    if (heroImages.length > 0) {
        setInterval(rotateHeroImages, 2000);
    }
}

function rotateHeroImages() {
    const heroBackground = document.getElementById('heroBackground');
    if (!heroBackground || heroImages.length === 0) return;

    // Get the current image element
    const currentImage = heroBackground.querySelector('.hero-bg-image');

    // Create new image element
    const newImage = document.createElement('div');
    newImage.className = 'hero-bg-image';
    
    // Move to next image
    currentImageIndex = (currentImageIndex + 1) % heroImages.length;
    newImage.style.backgroundImage = `url('${heroImages[currentImageIndex]}')`;

    // Add to background
    heroBackground.appendChild(newImage);

    // Animate old image out and wait for new image animation
    if (currentImage) {
        currentImage.classList.add('exiting');
        
        // Remove old image after animation completes
        setTimeout(() => {
            currentImage.remove();
        }, 2000);
    }
}

// Leadership Carousel Initialization
function initLeadershipCarousel() {
    const carousel = document.getElementById('leadershipCarousel');
    if (!carousel) return;

    // Get all carousel items
    const items = carousel.querySelectorAll('.leadership-carousel-item');
    
    // Clone all items and append them for seamless loop
    items.forEach(item => {
        const clone = item.cloneNode(true);
        carousel.appendChild(clone);
    });
}

// Smooth scrolling for anchor links (if needed in future)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Initialize on DOM ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        initHeroImages();
        initLeadershipCarousel();
    });
} else {
    initHeroImages();
    initLeadershipCarousel();
}

// Add any additional interactivity here
console.log('UB Group website loaded successfully!');
