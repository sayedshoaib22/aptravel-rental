(function () {
  const GOOGLE_REVIEW_URL = 'https://maps.app.goo.gl/YL9VJGDTUyHfHasf9';
  const STORAGE_KEY = 'aptravel_review_popup_status';
  const DELAY_MS = 15000;
  const SCROLL_THRESHOLD = 0.7;
  const MAYBE_LATER_DAYS = 7;
  const REVIEW_HIDE_DAYS = 30;
  const MS_PER_DAY = 86400000;

  const now = () => Date.now();

  const loadState = () => {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (error) {
      return {};
    }
  };

  const saveState = (state) => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (error) {
      console.warn('Unable to save review popup state', error);
    }
  };

  const isHidden = () => {
    const state = loadState();
    if (state.neverShow) return true;
    if (typeof state.hideUntil === 'number' && now() < state.hideUntil) return true;
    return false;
  };

  const setHideUntil = (days) => {
    const state = loadState();
    state.hideUntil = now() + days * MS_PER_DAY;
    delete state.neverShow;
    saveState(state);
  };

  const setNeverShow = () => {
    const state = loadState();
    state.neverShow = true;
    delete state.hideUntil;
    saveState(state);
  };

  const getRootPath = () => {
    if (window.location.origin && window.location.origin !== 'null') {
      return window.location.origin;
    }
    return '';
  };

  const getAssetUrl = (fileName) => {
    const root = getRootPath();
    return root + '/' + fileName;
  };

  const loadCss = () => {
    if (document.querySelector('link[data-review-popup]')) return;
    const link = document.createElement('link');
    link.setAttribute('rel', 'stylesheet');
    link.setAttribute('href', getAssetUrl('review-popup.css'));
    link.setAttribute('data-review-popup', '');
    document.head.appendChild(link);
  };

  const createPopup = async () => {
    try {
      const response = await fetch(getAssetUrl('review-popup.html'), { cache: 'no-cache' });
      if (!response.ok) return null;
      const html = await response.text();
      const wrapper = document.createElement('div');
      wrapper.innerHTML = html.trim();
      return wrapper.firstElementChild;
    } catch (error) {
      console.warn('Review popup template failed to load', error);
      return null;
    }
  };

  let popupOverlay = null;
  let popupPanel = null;
  let hasOpened = false;
  let hasBeenClosedThisSession = false;

  const openPopup = () => {
    if (!popupOverlay || hasOpened || hasBeenClosedThisSession || isHidden()) return;
    popupOverlay.setAttribute('aria-hidden', 'false');
    popupOverlay.classList.add('visible');
    document.body.classList.add('review-popup-open');
    popupPanel?.focus();
    hasOpened = true;
  };

  const closePopup = () => {
    if (!popupOverlay) return;
    popupOverlay.setAttribute('aria-hidden', 'true');
    popupOverlay.classList.remove('visible');
    document.body.classList.remove('review-popup-open');
    hasBeenClosedThisSession = true;
  };

  const handleAction = (action, event) => {
    if (event) event.preventDefault();
    if (action === 'write-review') {
      setHideUntil(REVIEW_HIDE_DAYS);
      window.open(GOOGLE_REVIEW_URL, '_blank', 'noopener');
    } else if (action === 'maybe-later') {
      setHideUntil(MAYBE_LATER_DAYS);
    } else if (action === 'never-show') {
      setNeverShow();
    }
    closePopup();
  };

  const bindEvents = () => {
    if (!popupOverlay) return;
    popupPanel = popupOverlay.querySelector('.review-popup-panel');
    const closeButton = popupOverlay.querySelector('.review-popup-close');
    const writeButton = popupOverlay.querySelector('[data-action="write-review"]');
    const laterButton = popupOverlay.querySelector('[data-action="maybe-later"]');
    const neverButton = popupOverlay.querySelector('[data-action="never-show"]');

    closeButton?.addEventListener('click', closePopup);
    writeButton?.addEventListener('click', (event) => handleAction('write-review', event));
    laterButton?.addEventListener('click', () => handleAction('maybe-later'));
    neverButton?.addEventListener('click', () => handleAction('never-show'));
    popupOverlay.addEventListener('click', (event) => {
      if (event.target === popupOverlay) closePopup();
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && popupOverlay.classList.contains('visible')) {
        event.preventDefault();
        closePopup();
      }
    });
  };

  const createTriggers = () => {
    const showOnce = () => {
      if (!hasOpened && !hasBeenClosedThisSession && !isHidden()) {
        openPopup();
      }
    };

    window.setTimeout(showOnce, DELAY_MS);

    const onScroll = () => {
      const scrolled = (window.scrollY + window.innerHeight) / document.documentElement.scrollHeight;
      if (scrolled >= SCROLL_THRESHOLD) {
        showOnce();
        window.removeEventListener('scroll', onScroll, { passive: true });
      }
    };
    window.addEventListener('scroll', onScroll, { passive: true });

    const onMouseLeave = (event) => {
      if (event.clientY <= 0 && window.innerWidth > 768) {
        showOnce();
        document.removeEventListener('mouseleave', onMouseLeave);
      }
    };
    document.addEventListener('mouseleave', onMouseLeave);
  };

  const init = async () => {
    if (isHidden()) return;
    loadCss();
    const popup = await createPopup();
    if (!popup) return;
    document.body.appendChild(popup);
    popupOverlay = document.getElementById('review-popup-overlay');
    bindEvents();
    createTriggers();
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
