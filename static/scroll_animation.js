/* scroll_animation.js */
document.addEventListener("DOMContentLoaded", () => {
    const animatedElements = document.querySelectorAll(".animate-on-scroll");

    if (!animatedElements.length) {
        return;
    }

    // Use requestAnimationFrame for better performance
    const observer = new IntersectionObserver((entries, observer) => {
        requestAnimationFrame(() => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // Batch DOM writes
                    entry.target.classList.add("is-visible");
                    observer.unobserve(entry.target);
                }
            });
        });
    }, {
        threshold: 0.1, // Trigger when 10% of element is visible
        rootMargin: '50px 0px -50px 0px' // Start observing a bit earlier
    });

    // Observe elements in batches
    animatedElements.forEach(element => {
        observer.observe(element);
    });
});
