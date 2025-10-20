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

    // Contact form submission
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                message: document.getElementById('message').value
            };
            
            // Show loading state
            const submitBtn = document.getElementById('submitButton');
            const loadingSpinner = document.getElementById('loadingSpinner');
            const submitText = document.getElementById('submitText');
            
            submitBtn.disabled = true;
            loadingSpinner.classList.remove('d-none');
            submitText.textContent = 'Sending...';
            
            // Send form data to the API endpoint
            fetch('/api/contact', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                // Reset form
                contactForm.reset();
                
                // Show success message
                const successMessage = document.getElementById('successMessage');
                successMessage.classList.remove('d-none');
                
                // Hide success message after 5 seconds
                setTimeout(() => {
                    successMessage.classList.add('d-none');
                }, 5000);
                
                // Reset button
                submitBtn.disabled = false;
                loadingSpinner.classList.add('d-none');
                submitText.textContent = 'Send Message';
            })
            .catch(error => {
                console.error('Error:', error);
                
                // Show error message
                const errorMessage = document.getElementById('errorMessage');
                const errorText = document.getElementById('errorText');
                errorText.textContent = 'An error occurred. Please try again later.';
                errorMessage.classList.remove('d-none');
                
                // Hide error message after 5 seconds
                setTimeout(() => {
                    errorMessage.classList.add('d-none');
                }, 5000);
                
                // Reset button
                submitBtn.disabled = false;
                loadingSpinner.classList.add('d-none');
                submitText.textContent = 'Send Message';
            });
        });
    }

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
});