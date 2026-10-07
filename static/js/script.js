   const typingTextElement = document.getElementById('typing-text');
    const roles = [
        'Angehende Fachinformatikerin',
        'Anwendungsentwicklung (IHK)',
        'Python & Flask Developerin',
        'Motivierte Problem-Löserin'
    ];
    let roleIndex = 0, charIndex = 0, isDeleting = false;

    function typeEffect() {
        const currentRole = roles[roleIndex];
        if (isDeleting) {
            typingTextElement.textContent = currentRole.substring(0, charIndex - 1);
            charIndex--;
        } else {
            typingTextElement.textContent = currentRole.substring(0, charIndex + 1);
            charIndex++;
        }
        let typingSpeed = isDeleting ? 40 : 80;
        if (!isDeleting && charIndex === currentRole.length) {
            typingSpeed = 2000;
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            roleIndex = (roleIndex + 1) % roles.length;
            typingSpeed = 500;
        }
        setTimeout(typeEffect, typingSpeed);
    }
    document.addEventListener('DOMContentLoaded', typeEffect);

    function toggleTimelineDetail(element) {
        const detailBox = element.querySelector('.timeline-detail');
        const arrow = element.querySelector('.detail-arrow');
        if (detailBox) {
            detailBox.classList.toggle('hidden');
            if (arrow) arrow.style.transform = detailBox.classList.contains('hidden') ? 'rotate(0deg)' : 'rotate(180deg)';
        }
    }

    function filterTimeline(category) {
        const items = document.querySelectorAll('.timeline-item');
        const buttons = document.querySelectorAll('.timeline-filter-btn');
        buttons.forEach(btn => {
            btn.classList.remove('accent-pink');
            btn.classList.add('text-gray-400');
        });
        event.currentTarget.classList.remove('text-gray-400');
        event.currentTarget.classList.add('accent-pink');

        items.forEach(item => {
            if (category === 'all' || item.getAttribute('data-category') === category) {
                item.style.display = 'flex';
            } else {
                item.style.display = 'none';
            }
        });
    }