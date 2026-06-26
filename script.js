// AP Travel & Rental — Updated for new redesigned site

document.addEventListener('DOMContentLoaded', () => {
  // Year injection
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Nav toggle for mobile
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');
  const navBar = document.getElementById('navBar');

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
      const isOpen = navLinks.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen);
      if (navBar) navBar.classList.toggle('menu-open', isOpen);
    });

    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
        if (navBar) navBar.classList.remove('menu-open');
      });
    });
  }

  // Sticky nav shadow on scroll
  if (navBar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 10) {
        navBar.classList.add('nav-scrolled');
      } else {
        navBar.classList.remove('nav-scrolled');
      }
    });
  }

  // Active nav link highlighting based on current path
  const currentPath = window.location.pathname;
  navLinks?.querySelectorAll('a').forEach(link => {
    const href = link.getAttribute('href');
    if (currentPath === href || currentPath.startsWith(href + '/')) {
      link.classList.add('active');
    }
  });

  // Contact form handler
  const form = document.getElementById('contactForm');
  const status = document.getElementById('formStatus');
  if (form) {
    form.addEventListener('submit', e => {
      e.preventDefault();
      const name = form.name?.value.trim();
      if (!name) return;
      if (status) {
        status.textContent = `Thanks ${name}, we've received your enquiry. Our team will call you shortly.`;
        status.style.color = 'var(--amber)';
      }
      form.reset();
      setTimeout(() => {
        if (status) status.textContent = '';
      }, 5000);
    });
    form.addEventListener('reset', () => {
      if (status) status.textContent = '';
    });
  }

  // Scroll reveal for elements
  const revealElements = document.querySelectorAll('.fleet-card, .svc-card, .why-card, .tcard, .hub-link');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in-up');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  revealElements.forEach(el => observer.observe(el));
});
