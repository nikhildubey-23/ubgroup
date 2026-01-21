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
    
    // Preload first hero image immediately to improve LCP
    if (heroImages.length > 0) {
        // Create preloaded images array
        heroImages.preloaded = [];
        
        // Preload first image immediately (highest priority)
        const firstImage = new Image();
        firstImage.onload = () => {
            heroImages.preloaded[0] = true;
            // Start rotation only after first image loads
            setTimeout(() => {
                setInterval(() => requestAnimationFrame(rotateHeroImages), 2000);
            }, 100);
        };
        firstImage.src = heroImages[0];
        
        // Preload other images in background
        heroImages.forEach((imgSrc, index) => {
            if (index > 0) {
                const img = new Image();
                img.onload = () => {
                    heroImages.preloaded[index] = true;
                };
                img.src = imgSrc;
            }
        });
    }
}

function rotateHeroImages() {
    if (heroImages.length === 0) return;

    // Cache DOM elements to avoid repeated queries
    if (!rotateHeroImages.heroBackground) {
        rotateHeroImages.heroBackground = document.getElementById('heroBackground');
    }
    const heroBackground = rotateHeroImages.heroBackground;
    if (!heroBackground) return;

    // Get current image element (cached query)
    const currentImage = heroBackground.querySelector('.hero-bg-image');
    if (!currentImage) return;

    // Create new image element
    const newImage = document.createElement('div');
    newImage.className = 'hero-bg-image';
    
    // Move to next image
    currentImageIndex = (currentImageIndex + 1) % heroImages.length;
    newImage.style.backgroundImage = `url('${heroImages[currentImageIndex]}')`;
    
    // Add img element for LCP discovery (except for first image which already has one)
    if (currentImageIndex > 0) {
        const img = document.createElement('img');
        img.src = heroImages[currentImageIndex];
        img.alt = `UB Group Hero Background ${currentImageIndex + 1}`;
        img.loading = 'eager';
        img.style.display = 'none';
        newImage.appendChild(img);
    }

    // Batch DOM operations to reduce reflows
    requestAnimationFrame(() => {
        // Add to background
        heroBackground.appendChild(newImage);

        // Animate old image out
        currentImage.classList.add('exiting');
        
        // Remove old image after animation completes
        setTimeout(() => {
            if (currentImage.parentNode) {
                currentImage.remove();
            }
        }, 2000);
    });
}
}

// Leadership Carousel Initialization
function initLeadershipCarousel() {
    const carousel = document.getElementById('leadershipCarousel');
    if (!carousel) return;

    // Get all carousel items (single query)
    const items = carousel.querySelectorAll('.leadership-carousel-item');
    if (!items.length) return;
    
    // Create document fragment to batch DOM operations
    const fragment = document.createDocumentFragment();
    
    // Clone all items and append them for seamless loop
    items.forEach(item => {
        const clone = item.cloneNode(true);
        fragment.appendChild(clone);
    });
    
    // Single DOM append operation
    carousel.appendChild(fragment);
}

// Smooth scrolling for anchor links (if needed in future)
// Use event delegation to avoid multiple event listeners
document.addEventListener('click', function(e) {
    const anchor = e.target.closest('a[href^="#"]');
    if (anchor) {
        e.preventDefault();
        const targetId = anchor.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth'
            });
        }
    }
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
