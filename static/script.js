// Custom JavaScript for UB Group website

// Hero Section Background Image Rotation
let currentImageIndex = 0;
let heroImages = [];

function initHeroImages() {
    const heroBackground = document.getElementById('heroBackground');
    if (!heroBackground) {
        console.log('Hero background element not found');
        return;
    }

    // Get image paths from data attribute
    const imagesData = heroBackground.getAttribute('data-images');
    console.log('Hero images data:', imagesData);
    
    if (imagesData) {
        try {
            heroImages = JSON.parse(imagesData);
            console.log('Parsed hero images:', heroImages);
        } catch (e) {
            console.error('Error parsing hero images:', e);
            return;
        }
    }

    // Images are already full URLs from Flask url_for(), no conversion needed
    console.log('Final hero images array:', heroImages);
    
    // Preload first hero image immediately to improve LCP
    if (heroImages.length > 0) {
        // Create preloaded images array
        heroImages.preloaded = [];
        
        // Preload first image immediately (highest priority)
        const firstImage = new Image();
        firstImage.onload = () => {
            heroImages.preloaded[0] = true;
            console.log('First hero image loaded');
            // Start rotation only after first image loads
            setTimeout(() => {
                setInterval(() => rotateHeroImages(), 3000); // Changed to 3 seconds for better visibility
            }, 1000); // Start after 1 second
        };
        firstImage.onerror = () => {
            console.error('Failed to load first hero image:', heroImages[0]);
        };
        firstImage.src = heroImages[0];
        
        // Preload other images in background
        heroImages.forEach((imgSrc, index) => {
            if (index > 0) {
                const img = new Image();
                img.onload = () => {
                    heroImages.preloaded[index] = true;
                    console.log(`Hero image ${index} loaded:`, imgSrc);
                };
                img.onerror = () => {
                    console.error(`Failed to load hero image ${index}:`, imgSrc);
                };
                img.src = imgSrc;
            }
        });
    } else {
        console.error('No hero images found');
    }
}

function rotateHeroImages() {
    if (heroImages.length === 0) {
        console.log('No hero images to rotate');
        return;
    }

    // Cache DOM elements to avoid repeated queries
    if (!rotateHeroImages.heroBackground) {
        rotateHeroImages.heroBackground = document.getElementById('heroBackground');
    }
    const heroBackground = rotateHeroImages.heroBackground;
    if (!heroBackground) {
        console.log('Hero background element not found during rotation');
        return;
    }

    // Get current image element (cached query)
    const currentImage = heroBackground.querySelector('.hero-bg-image');
    if (!currentImage) {
        console.log('Current hero image element not found');
        return;
    }

    console.log('Rotating to next image. Current index:', currentImageIndex);

    // Create new image element
    const newImage = document.createElement('div');
    newImage.className = 'hero-bg-image';
    
    // Move to next image
    currentImageIndex = (currentImageIndex + 1) % heroImages.length;
    const nextImageUrl = heroImages[currentImageIndex];
    console.log('Next image URL:', nextImageUrl);
    
    newImage.style.backgroundImage = `url('${nextImageUrl}')`;
    
    // Add img element for LCP discovery (except for first image which already has one)
    if (currentImageIndex > 0) {
        const img = document.createElement('img');
        img.src = nextImageUrl;
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
        
        console.log('Added new image and marked old image as exiting');
        
        // Remove old image after animation completes
        setTimeout(() => {
            if (currentImage.parentNode) {
                currentImage.remove();
                console.log('Removed old image from DOM');
            }
        }, 2000);
    });
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