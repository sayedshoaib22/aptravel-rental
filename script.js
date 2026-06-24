// AP Travel & Rental — optimized site interactions
document.addEventListener('DOMContentLoaded', () => {
  // FIXED MOBILE MENU JS
  const yearEl = document.getElementById('year');
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  const hamburger = document.querySelector('.nav-toggle.hamburger');
  const navMenu = document.querySelector('.nav-links');
  const navBar = document.getElementById('navBar');

  if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => {
      const isOpen = navMenu.classList.toggle('open');
      hamburger.classList.toggle('active', isOpen);
      navMenu.classList.toggle('active', isOpen);
      hamburger.setAttribute('aria-expanded', String(isOpen));
      if (navBar) {
        navBar.classList.toggle('menu-open', isOpen);
      }
      document.body.classList.toggle('menu-open', isOpen);
    });

    navMenu.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
        navMenu.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
        if (navBar) {
          navBar.classList.remove('menu-open');
        }
        document.body.classList.remove('menu-open');
      });
    });
  }

  // FIXED RAIL TOGGLE
  const railToggle = document.getElementById('railToggle');
  const rail = document.getElementById('rail');
  if (railToggle && rail) {
    railToggle.addEventListener('click', () => {
      const isOpen = rail.classList.toggle('open');
      railToggle.setAttribute('aria-expanded', String(isOpen));
    });

    rail.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        rail.classList.remove('open');
        railToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // FIXED CONTACT FORM
  const form = document.getElementById('contactForm');
  const status = document.getElementById('formStatus');
  if (form && status) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = form.name.value.trim();
      if (!name) {
        return;
      }
      status.textContent = `Thanks ${name}, we've received your enquiry. Our team will call you shortly.`;
      status.style.color = 'var(--blue)';
      form.reset();
      setTimeout(() => {
        status.textContent = '';
      }, 5000);
    });

    form.addEventListener('reset', () => {
      status.textContent = '';
    });
  }

  // FIXED FAQ ACCORDION
  const faqButtons = document.querySelectorAll('.faq-q');
  faqButtons.forEach((btn) => {
    btn.addEventListener('click', function () {
      const item = this.closest('.faq-item');
      const answer = item ? item.querySelector('.faq-a') : null;
      if (!item || !answer) {
        return;
      }

      const expanded = this.getAttribute('aria-expanded') === 'true';
      document.querySelectorAll('.faq-q').forEach((other) => {
        if (other !== this) {
          other.setAttribute('aria-expanded', 'false');
          const otherAnswer = other.closest('.faq-item')?.querySelector('.faq-a');
          if (otherAnswer) {
            otherAnswer.style.maxHeight = null;
            other.closest('.faq-item')?.classList.remove('active');
          }
        }
      });

      item.classList.toggle('active', !expanded);
      this.setAttribute('aria-expanded', String(!expanded));
      answer.style.maxHeight = !expanded ? `${answer.scrollHeight}px` : null;
    });
  });

  // FIXED RESPONSIVE ISSUES
  const revealEls = document.querySelectorAll(
    '.fleet-row,.service-grid,.testimonial-card,.why-row,.cargo-svc-card,.cargo-fleet-card,.cargo-service-card,.seo-content,.seo-hub,.seo-sidebar-cta'
  );

  if (window.innerWidth <= 768) {
    revealEls.forEach((el) => {
      el.style.opacity = '1';
      el.style.transform = 'none';
    });
  } else if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.05, rootMargin: '0px 0px -50px 0px' }
    );

    revealEls.forEach((el) => {
      el.style.cssText = 'opacity:0;transform:translateY(24px);transition:opacity .6s ease,transform .6s ease';
      observer.observe(el);
    });
  }

  if ('scrollRestoration' in history) {
    history.scrollRestoration = 'manual';
  }
});