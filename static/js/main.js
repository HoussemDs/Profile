document.addEventListener('DOMContentLoaded', function() {
    // Typing animation for the hero section
    if (document.querySelector('.typed-text')) {
        const typedTextElement = document.querySelector('.typed-text');
        const textToType = typedTextElement.getAttribute('data-text').split(',');
        let currentTextIndex = 0;
        let currentCharIndex = 0;
        let isDeleting = false;
        let typingSpeed = 100; // Base typing speed in ms

        function typeText() {
            const currentText = textToType[currentTextIndex];
            
            if (isDeleting) {
                // Deleting text
                typedTextElement.textContent = currentText.substring(0, currentCharIndex - 1);
                currentCharIndex--;
                typingSpeed = 50; // Faster when deleting
            } else {
                // Typing text
                typedTextElement.textContent = currentText.substring(0, currentCharIndex + 1);
                currentCharIndex++;
                typingSpeed = 100; // Normal speed when typing
            }
            
            // Check if word is complete
            if (!isDeleting && currentCharIndex === currentText.length) {
                // Pause at the end of a word
                isDeleting = true;
                typingSpeed = 1000; // Wait before deleting
            } else if (isDeleting && currentCharIndex === 0) {
                // Move to next word
                isDeleting = false;
                currentTextIndex = (currentTextIndex + 1) % textToType.length;
                typingSpeed = 500; // Pause before typing next word
            }
            
            setTimeout(typeText, typingSpeed);
        }
        
        // Start the typing animation
        setTimeout(typeText, 1000);
    }

    // Particle animation for hero background
    if (document.getElementById('particles-js')) {
        particlesJS('particles-js', {
            particles: {
                number: { value: 80, density: { enable: true, value_area: 800 } },
                color: { value: '#00FFFF' },
                shape: { type: 'circle' },
                opacity: { value: 0.5, random: true },
                size: { value: 3, random: true },
                line_linked: {
                    enable: true,
                    distance: 150,
                    color: '#9D4EDD',
                    opacity: 0.4,
                    width: 1
                },
                move: {
                    enable: true,
                    speed: 2,
                    direction: 'none',
                    random: true,
                    straight: false,
                    out_mode: 'out',
                    bounce: false
                }
            },
            interactivity: {
                detect_on: 'canvas',
                events: {
                    onhover: { enable: true, mode: 'grab' },
                    onclick: { enable: true, mode: 'push' },
                    resize: true
                },
                modes: {
                    grab: { distance: 140, line_linked: { opacity: 1 } },
                    push: { particles_nb: 4 }
                }
            },
            retina_detect: true
        });
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70, // Offset for fixed navbar
                    behavior: 'smooth'
                });
            }
        });
    });

    // No contact form submission logic

    // Animate elements when they come into view
    const animateOnScroll = function() {
        const elements = document.querySelectorAll('.animate-on-scroll');
        
        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementPosition < windowHeight - 100) {
                element.classList.add('animated');
            }
        });
    };
    
    // Run once on page load
    animateOnScroll();
    
    // Run on scroll
    window.addEventListener('scroll', animateOnScroll);

    // Simple expand/collapse for each project details (toggle only the clicked one)
    const projectDetails = document.querySelectorAll('.collapse.project-details');
    projectDetails.forEach(details => {
        details.addEventListener('show.bs.collapse', function() {
            const video = details.querySelector('video[data-src]');
            if (video && !video.getAttribute('src')) {
                const src = video.getAttribute('data-src');
                video.setAttribute('src', src);
                video.load();
            }
            const card = details.closest('.project-card');
            const btn = card ? card.querySelector('[data-bs-target="#' + details.id + '"]') : null;
            if (btn) {
                btn.textContent = 'Show Less';
            }
        });
        details.addEventListener('hide.bs.collapse', function() {
            const card = details.closest('.project-card');
            const btn = card ? card.querySelector('[data-bs-target="#' + details.id + '"]') : null;
            if (btn) {
                btn.textContent = 'Show More';
            }
        });
    });

    // Auto-expand behavior removed to keep navigation simple

    // No contact form logic — page uses static contact info
});