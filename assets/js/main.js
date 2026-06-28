/* ============================================================
   AP Travel & Rental — Main JS
   ============================================================ */
'use strict';

(() => {
  /* ── Loader ─────────────────────────────────────────────── */
  const loader = document.getElementById('page-loader');
  const loaderFill = document.querySelector('.loader-bar-fill');

  window.addEventListener('load', () => {
    setTimeout(() => {
      loader?.classList.add('hidden');
    }, 1400);
  });

  /* ── Progress bar ────────────────────────────────────────── */
  const progressBar = document.getElementById('progress-bar');
  const updateProgress = () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    if (progressBar) progressBar.style.width = pct + '%';
  };
  window.addEventListener('scroll', updateProgress, { passive: true });

  /* ── Year ────────────────────────────────────────────────── */
  const yearEls = document.querySelectorAll('.js-year');
  yearEls.forEach(el => el.textContent = new Date().getFullYear());

  /* ── Dark mode ───────────────────────────────────────────── */
  const toggle = document.getElementById('darkToggle');
  const setTheme = (dark) => {
    document.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light');
    localStorage.setItem('theme', dark ? 'dark' : 'light');
    if (toggle) toggle.textContent = dark ? '☀️' : '🌙';
  };
  const savedTheme = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  setTheme(savedTheme === 'dark' || (!savedTheme && prefersDark));
  toggle?.addEventListener('click', () => {
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    setTheme(!isDark);
  });

  /* ── Navbar ──────────────────────────────────────────────── */
  const navbar = document.getElementById('navbar');
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('navLinks');

  window.addEventListener('scroll', () => {
    navbar?.classList.toggle('scrolled', window.scrollY > 30);
  }, { passive: true });

  hamburger?.addEventListener('click', () => {
    const open = navLinks.classList.toggle('open');
    hamburger.classList.toggle('active', open);
    hamburger.setAttribute('aria-expanded', open);
  });

  navLinks?.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
      hamburger?.classList.remove('active');
      hamburger?.setAttribute('aria-expanded', 'false');
    });
  });

  /* ── Active link ─────────────────────────────────────────── */
  const path = window.location.pathname;
  navLinks?.querySelectorAll('a').forEach(a => {
    if (a.getAttribute('href') === path || (path !== '/' && path.startsWith(a.getAttribute('href')))) {
      a.classList.add('active');
    }
  });

  /* ── Scroll reveal ───────────────────────────────────────── */
  const revealEls = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
  const revealObs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        revealObs.unobserve(e.target);
      }
    });
  }, { threshold: 0.1 });
  revealEls.forEach(el => revealObs.observe(el));

  /* ── Stat counter ────────────────────────────────────────── */
  const counters = document.querySelectorAll('.stat-num[data-count]');
  const countObs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      const el = e.target;
      const target = parseInt(el.dataset.count);
      const suffix = el.dataset.suffix || '';
      const dur = 1600;
      const start = performance.now();
      const tick = (now) => {
        const pct = Math.min((now - start) / dur, 1);
        const ease = 1 - Math.pow(1 - pct, 3);
        el.querySelector('.count-val').textContent = Math.floor(ease * target) + suffix;
        if (pct < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
      countObs.unobserve(el);
    });
  }, { threshold: 0.5 });
  counters.forEach(c => countObs.observe(c));

  /* ── Testimonial slider ──────────────────────────────────── */
  const track = document.querySelector('.reviews-track');
  const dots = document.querySelectorAll('.dot');
  const prevBtn = document.getElementById('sliderPrev');
  const nextBtn = document.getElementById('sliderNext');

  if (track) {
    let current = 0;
    const cards = track.querySelectorAll('.review-card');
    const total = cards.length;
    let perView = window.innerWidth < 768 ? 1 : window.innerWidth < 1100 ? 2 : 3;
    const maxIndex = total - perView;

    const goTo = (idx) => {
      current = Math.max(0, Math.min(idx, maxIndex));
      const cardW = cards[0].offsetWidth + 24;
      track.style.transform = `translateX(-${current * cardW}px)`;
      dots.forEach((d, i) => d.classList.toggle('active', i === current));
    };

    prevBtn?.addEventListener('click', () => goTo(current - 1));
    nextBtn?.addEventListener('click', () => goTo(current + 1));
    dots.forEach((d, i) => d.addEventListener('click', () => goTo(i)));

    // Auto-play
    let autoPlay = setInterval(() => goTo(current + 1 > maxIndex ? 0 : current + 1), 4500);
    track.addEventListener('mouseenter', () => clearInterval(autoPlay));
    track.addEventListener('mouseleave', () => {
      autoPlay = setInterval(() => goTo(current + 1 > maxIndex ? 0 : current + 1), 4500);
    });

    window.addEventListener('resize', () => {
      perView = window.innerWidth < 768 ? 1 : window.innerWidth < 1100 ? 2 : 3;
      goTo(0);
    });
  }

  /* ── FAQ accordion ───────────────────────────────────────── */
  document.querySelectorAll('.faq-item').forEach(item => {
    item.querySelector('.faq-q')?.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(i => i.classList.remove('open'));
      if (!isOpen) item.classList.add('open');
    });
  });

  /* ── Contact form ────────────────────────────────────────── */
  const form = document.getElementById('contactForm');
  const formStatus = document.getElementById('formStatus');
  const API_URL = 'https://vartiss-backend-production-8be8.up.railway.app';

  form?.addEventListener('submit', async e => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(form));
    if (!data.name || !data.phone) return;

    // Optimistic UI: show the same success message immediately
    if (formStatus) {
      formStatus.className = 'form-status success';
      formStatus.textContent = `Thanks ${data.name}! We've received your enquiry and will call you at ${data.phone} shortly.`;
    }

    // Analytics conversion (unchanged)
    if (typeof window.gtag === 'function') {
      window.gtag('event', 'conversion', {
        'send_to': 'AW-18269844622/MMeUCKL__8UcEI7p3odE'
      });
    }

    // Send to backend
    const url = `${API_URL}/api/enquiry`;
    console.log('Submitting to:', url);
    try {
      const resp = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: data.name || '',
          phone: data.phone || '',
          email: data.email || '',
          service: data.service || data.subject || '',
          message: data.message || ''
        })
      });
      console.log('Response:', resp.status);
      const json = await resp.json().catch(async () => {
        try { const t = await resp.text(); return { text: t }; } catch(e){ return null; }
      });
      if (!resp.ok) {
        console.error('Server error:', json);
        if (formStatus) {
          formStatus.className = 'form-status error';
          formStatus.textContent = 'Sorry, we could not send your enquiry. Please try again later.';
        }
      }
    } catch (err) {
      console.error('Enquiry error', err);
      if (formStatus) {
        formStatus.className = 'form-status error';
        formStatus.textContent = 'Network error sending enquiry. Please try again later.';
      }
    } finally {
      form.reset();
      setTimeout(() => {
        if (formStatus) formStatus.className = 'form-status';
      }, 6000);
    }
  });

  /* ── Back to top ─────────────────────────────────────────── */
  const topBtn = document.getElementById('backTop');
  window.addEventListener('scroll', () => {
    topBtn?.classList.toggle('visible', window.scrollY > 400);
  }, { passive: true });
  topBtn?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  /* ── Lazy images ─────────────────────────────────────────── */
  const lazyImgs = document.querySelectorAll('img[loading="lazy"]');
  if ('IntersectionObserver' in window) {
    const imgObs = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          const img = e.target;
          if (img.dataset.src) img.src = img.dataset.src;
          img.classList.add('loaded');
          imgObs.unobserve(img);
        }
      });
    });
    lazyImgs.forEach(img => imgObs.observe(img));
  }

})();