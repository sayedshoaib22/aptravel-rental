from pathlib import Path
from datetime import datetime

root = Path(__file__).resolve().parent

COMMON_NAV = '''<nav class="nav-menu" aria-label="Primary navigation">
      <a href="/index.html" class="{home_active}">Home</a>
      <a href="/fleet/" class="{fleet_active}">Fleet</a>
      <a href="/bus-rental-mumbai/" class="{bus_active}">Bus Rental</a>
      <a href="/corporate-bus-rental-mumbai/" class="{corporate_active}">Corporate</a>
      <a href="/wedding-bus-rental-mumbai/" class="{wedding_active}">Wedding</a>
      <a href="/outstation-bus-rental-mumbai/" class="{outstation_active}">Outstation</a>
      <a href="/tempo-traveller-rental-mumbai/" class="{tempo_active}">Tempo</a>
      <a href="/cargo/" class="{cargo_active}">Cargo</a>
      <a href="/about/" class="{about_active}">About</a>
      <a href="/contact/" class="{contact_active}">Contact</a>
    </nav>'''

HEADER_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta name="description" content="{description}">
  <meta name="keywords" content="bus rental Mumbai, cargo logistics Mumbai, corporate transport, airport transfer, School Trip, tempo traveller, freight service">
  <meta name="author" content="AP Travel & Rental">
  <meta name="theme-color" content="#0F172A">
  <link rel="canonical" href="https://aptravelrental.in{canonical}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@400;500;600;700;800&display=swap" as="style">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{assets_prefix}css/styles.css">
  <title>{title}</title>
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="https://aptravelrental.in{canonical}">
  <meta property="og:image" content="https://aptravelrental.in/images/blue-star.webp">
  <meta property="og:site_name" content="AP Travel & Rental">
  <meta property="og:locale" content="en_IN">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="https://aptravelrental.in/images/blue-star.webp">
</head>
<body class="page" data-theme="light">
  <a class="skip-link" href="#main">Skip to main content</a>
  <div id="progress-bar" aria-hidden="true"></div>
  <div class="loading-screen">
    <div class="loading-inner">
      <div class="loader" aria-hidden="true"></div>
      <p class="loading-text">Loading premium transport service…</p>
    </div>
  </div>
  <header class="nav" role="banner">
    <div class="nav-brand">
      <span class="brand-mark">AP</span>
      <div>
        <strong>AP Travel & Rental</strong>
        <span>Premium transport in Mumbai</span>
      </div>
    </div>
    {nav}
    <div class="nav-actions">
      <a class="topbar-btn secondary" href="tel:+919322099980">Call Us</a>
      <button class="dark-toggle" aria-label="Toggle dark mode">🌙</button>
      <button class="hamburger" type="button" aria-label="Open navigation" aria-controls="nav-menu"><span></span><span></span><span></span></button>
    </div>
  </header>
'''

FOOTER_TEMPLATE = '''
  <footer class="footer">
    <div class="container footer-grid">
      <div>
        <p class="brand-mark">AP</p>
        <div><strong>AP Travel & Rental</strong><p class="footer-text">Trusted bus rental and cargo logistics from Mumbai.</p></div>
      </div>
      <div class="footer-links">
        <h4>Quick links</h4>
        <a href="/index.html">Home</a>
        <a href="/fleet/">Fleet</a>
        <a href="/cargo/">Cargo</a>
        <a href="/contact/">Contact</a>
      </div>
      <div class="footer-links">
        <h4>Services</h4>
        <a href="/bus-rental-mumbai/">Bus Rental</a>
        <a href="/tempo-traveller-rental-mumbai/">Tempo Traveller</a>
        <a href="/corporate-bus-rental-mumbai/">Corporate</a>
        <a href="/wedding-bus-rental-mumbai/">Wedding</a>
      </div>
      <div>
        <h4>Contact</h4>
        <a href="tel:+919322099980">+91 93220 99980</a>
        <a href="mailto:info@apcargos.in">info@apcargos.in</a>
        <span>Vrindavan, Sion-Chembur Road, Chunabhatti, Mumbai 400022</span>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>© {year} AP Travel & Rental. All rights reserved.</p>
      <div class="social-list">
        <a href="https://www.facebook.com/aptravelrental" target="_blank" rel="noopener noreferrer" aria-label="Facebook">F</a>
        <a href="https://www.instagram.com/aptravelrental" target="_blank" rel="noopener noreferrer" aria-label="Instagram">I</a>
        <a href="https://www.youtube.com/@aptravelrental" target="_blank" rel="noopener noreferrer" aria-label="YouTube">Y</a>
      </div>
    </div>
  </footer>
  <div class="floating-actions" aria-label="Quick actions">
    <a class="float-btn" href="https://wa.me/919322099980" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp us">W</a>
    <a class="float-btn call" href="tel:+919322099980" aria-label="Call us">☎</a>
    <button class="float-btn back-to-top" type="button" aria-label="Back to top">↑</button>
  </div>
  <script src="{assets_prefix}js/script.js" defer></script>
</body>
</html>'''

PAGES = {
    'index.html': {
        'title': 'AP Travel & Rental | Premium Bus Rental & Cargo Services in Mumbai',
        'description': 'Premium bus rental and cargo services in Mumbai. Reliable transport solutions for corporate travel, airport transfers, school trips, weddings, and logistics.',
        'canonical': '/',
        'hero_title': 'Premium Bus Rental & Cargo Services in Mumbai',
        'hero_text': 'Reliable transportation solutions across Mumbai and Maharashtra with luxury coaches, tempo travellers, and secure logistics.',
        'hero_image': 'images/blue-star.webp',
        'active': 'Home',
        'assets_prefix': 'assets/',
        'content': '''
  <main id="main">
    <section class="hero" aria-labelledby="hero-heading">
      <img class="hero-bg" src="images/blue-star.webp" alt="Premium coach and cargo transport" loading="eager" fetchpriority="high">
      <div class="hero-overlay" aria-hidden="true"></div>
      <div class="hero-content container">
        <span class="hero-eyebrow">Mumbai’s trusted transport partner</span>
        <h1 id="hero-heading">Premium Bus Rental & Cargo Services<br>for Every Journey.</h1>
        <p class="hero-copy">Dependable passenger transport and logistics from Sion, Mumbai. Book corporate shuttles, wedding coaches, school trips, airport transfers, or cargo delivery with 24/7 support.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="/contact/">Get a Free Quote</a>
          <a class="btn btn-ghost" href="https://wa.me/919322099980" target="_blank" rel="noopener noreferrer">WhatsApp Us</a>
          <a class="btn btn-secondary" href="tel:+919322099980">Call +91 93220 99980</a>
        </div>
        <div class="hero-stats" role="list">
          <div class="stat-item" role="listitem"><span class="stat-num">10+</span><span class="stat-label">Years experience</span></div>
          <div class="stat-item" role="listitem"><span class="stat-num">5000+</span><span class="stat-label">Happy customers</span></div>
          <div class="stat-item" role="listitem"><span class="stat-num">100+</span><span class="stat-label">Vehicles available</span></div>
          <div class="stat-item" role="listitem"><span class="stat-num">24/7</span><span class="stat-label">Support</span></div>
        </div>
      </div>
    </section>

    <section class="container section" id="services" aria-labelledby="services-heading">
      <div class="section-header">
        <span class="section-tag">What we offer</span>
        <h2 class="section-title" id="services-heading">Services built for passengers and cargo across every Mumbai route.</h2>
        <p class="section-copy">From airport transfers to household shifting, AP Travel & Rental delivers dependable transport with transparent pricing and premium service.</p>
      </div>
      <div class="cards-grid">
        <article class="card service-card"><span>🚍</span><h3>Bus Rental</h3><p>Luxury AC coaches for events, tours, and corporate transfers.</p><a class="card-link" href="/bus-rental-mumbai/">Learn more</a></article>
        <article class="card service-card"><span>🛻</span><h3>Tempo Traveller</h3><p>Flexible tempo travel for small groups, airport transfers, and tours.</p><a class="card-link" href="/tempo-traveller-rental-mumbai/">Learn more</a></article>
        <article class="card service-card"><span>✈️</span><h3>Airport Transfer</h3><p>Punctual pickup and drop service with flight monitoring.</p><a class="card-link" href="/contact/">Book now</a></article>
        <article class="card service-card"><span>🏢</span><h3>Corporate Travel</h3><p>Executive shuttles and employee transport for businesses.</p><a class="card-link" href="/corporate-bus-rental-mumbai/">Learn more</a></article>
        <article class="card service-card"><span>🎒</span><h3>School Trip</h3><p>Safe school trips with experienced drivers and sanitized coaches.</p><a class="card-link" href="/contact/">Enquire</a></article>
        <article class="card service-card"><span>📦</span><h3>Cargo Logistics</h3><p>Secure household shifting and interstate freight services.</p><a class="card-link" href="/cargo/">Learn more</a></article>
      </div>
    </section>

    <section class="container section">
      <div class="section-header">
        <span class="section-tag">Our fleet</span>
        <h2 class="section-title">Premium vehicles for every travel requirement.</h2>
        <p class="section-copy">Explore our executive coaches, luxury buses, and cargo-ready transport options designed for comfort and reliability.</p>
      </div>
      <div class="fleet-grid">
        <article class="fleet-card"><img src="images/blue-star.webp" alt="KGN Luxury AC Bus" loading="lazy"><h3>KGN Luxury AC Bus</h3><p>45 seats, AC, reclining chairs, ideal for tours and corporate groups.</p><a class="card-link" href="/contact/">Book now</a></article>
        <article class="fleet-card"><img src="images/KGN_BLUE.webp" alt="KGN Executive Bus" loading="lazy"><h3>KGN Executive Bus</h3><p>40 seats, premium interiors and large luggage space for events.</p><a class="card-link" href="/contact/">Book now</a></article>
        <article class="fleet-card"><img src="images/blue-star-right.webp" alt="Blue Star Executive Coach" loading="lazy"><h3>Blue Star Executive Coach</h3><p>Executive comfort for long-distance routes and outstation travel.</p><a class="card-link" href="/contact/">Book now</a></article>
      </div>
    </section>

    <section class="container section">
      <div class="section-header">
        <span class="section-tag">Why choose us</span>
        <h2 class="section-title">Trusted transport standards for passengers and packages.</h2>
      </div>
      <div class="cards-grid">
        <article class="card why-card"><span>👨‍✈️</span><h3>Verified Drivers</h3><p>Professional operators trained for safety and punctual service.</p></article>
        <article class="card why-card"><span>🧼</span><h3>Sanitized Vehicles</h3><p>Clean, disinfected coaches and cargo vehicles before every trip.</p></article>
        <article class="card why-card"><span>💸</span><h3>Transparent Pricing</h3><p>Clear quotes with no hidden charges for buses and cargo services.</p></article>
        <article class="card why-card"><span>📡</span><h3>GPS Tracking</h3><p>Route visibility and on-the-go updates for passenger and cargo bookings.</p></article>
        <article class="card why-card"><span>📞</span><h3>24/7 Support</h3><p>Booking assistance and journey support available anytime.</p></article>
        <article class="card why-card"><span>⏱️</span><h3>On-Time Service</h3><p>Dependable pickups and delivery windows for every booking.</p></article>
      </div>
    </section>

    <section class="container section">
      <div class="section-header">
        <span class="section-tag">Cargo services</span>
        <h2 class="section-title">Flexible cargo solutions for business and household moves.</h2>
        <p class="section-copy">Same-day delivery, interstate freight, and secure shifting with expert handling.</p>
      </div>
      <div class="cargo-grid">
        <article class="cargo-card"><h3>Same Day Delivery</h3><p>Fast local delivery within Mumbai with careful packaging.</p></article>
        <article class="cargo-card"><h3>Interstate Logistics</h3><p>Freight services connecting Mumbai to Pune, Bengaluru, Hyderabad, and beyond.</p></article>
        <article class="cargo-card"><h3>Business Cargo</h3><p>Reliable transport for office shipments and retail inventory.</p></article>
        <article class="cargo-card"><h3>Household Shifting</h3><p>Secure moving service for furniture, appliances, and personal goods.</p></article>
      </div>
    </section>

    <section class="container section">
      <div class="section-header">
        <span class="section-tag">Customer reviews</span>
        <h2 class="section-title">Trusted by families and businesses across Mumbai.</h2>
      </div>
      <div class="testimonial-grid">
        <article class="testimonial-card"><p>"AP Travel delivered a flawless corporate shuttle for our team. The coach was clean, the driver was professional, and the support was excellent."</p><strong>Rohit K.</strong></article>
        <article class="testimonial-card"><p>"Booked a tempo traveller for a family outing and the journey was comfortable. Pickup was on time and the vehicle was sanitized."</p><strong>Neha S.</strong></article>
        <article class="testimonial-card"><p>"Cargo service made our office move easy. Every item was handled carefully and the truck arrived exactly when promised."</p><strong>Priya M.</strong></article>
      </div>
    </section>

    <section class="container section">
      <div class="section-header">
        <span class="section-tag">Coverage area</span>
        <h2 class="section-title">Serving Mumbai, Navi Mumbai, Thane, Pune, and wider Maharashtra.</h2>
      </div>
      <div class="coverage-grid">
        <article class="coverage-card"><h3>Mumbai</h3><p>Citywide passenger transport, airport transfers, and local cargo service.</p></article>
        <article class="coverage-card"><h3>Navi Mumbai</h3><p>Corporate shuttles, school routes, and logistics across the node city.</p></article>
        <article class="coverage-card"><h3>Thane</h3><p>Reliable bus rental, event transport, and household shifting services.</p></article>
        <article class="coverage-card"><h3>Pune</h3><p>Intercity coach routes and cargo logistics between Mumbai and Pune.</p></article>
        <article class="coverage-card"><h3>Maharashtra</h3><p>Statewide coverage for travel and freight with scalable capacity.</p></article>
      </div>
    </section>

    <section class="container section" id="faq">
      <div class="section-header">
        <span class="section-tag">FAQ</span>
        <h2 class="section-title">Common questions about booking, pricing, and cargo delivery.</h2>
      </div>
      <div class="faq-list">
        <article class="faq-card"><button class="faq-question" type="button"><span>What is the bus booking process?</span><span class="faq-icon">+</span></button><div class="faq-answer"><p>Call or WhatsApp us with your trip details and we will provide a quote and confirm availability quickly.</p></div></article>
        <article class="faq-card"><button class="faq-question" type="button"><span>How are prices calculated?</span><span class="faq-icon">+</span></button><div class="faq-answer"><p>Pricing depends on vehicle type, distance, duration, and service requirements. We give clear quotes with all charges included.</p></div></article>
        <article class="faq-card"><button class="faq-question" type="button"><span>What payment methods do you accept?</span><span class="faq-icon">+</span></button><div class="faq-answer"><p>We accept UPI, bank transfer, and cash. A deposit may be required to confirm your booking.</p></div></article>
        <article class="faq-card"><button class="faq-question" type="button"><span>What is your cancellation policy?</span><span class="faq-icon">+</span></button><div class="faq-answer"><p>Cancellations are handled with advance notice. Contact our support team to discuss any changes and applicable charges.</p></div></article>
        <article class="faq-card"><button class="faq-question" type="button"><span>How long does cargo delivery take?</span><span class="faq-icon">+</span></button><div class="faq-answer"><p>Delivery timings depend on your route. We offer same-day local delivery and scheduled interstate logistics based on your needs.</p></div></article>
      </div>
    </section>

    <section class="container section" id="contact">
      <div class="section-header">
        <span class="section-tag">Contact</span>
        <h2 class="section-title">Get in touch for a tailored quote and fast booking support.</h2>
      </div>
      <div class="contact-grid">
        <section class="contact-card">
          <h3>Send your details</h3>
          <form id="contactForm">
            <div class="form-row"><label for="name">Name</label><input id="name" name="name" type="text" placeholder="Your name" required></div>
            <div class="form-row"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" placeholder="+91 93220 99980" required></div>
            <div class="form-row"><label for="email">Email</label><input id="email" name="email" type="email" placeholder="name@example.com"></div>
            <div class="form-row"><label for="message">Message</label><textarea id="message" name="message" rows="5" placeholder="Tell us your trip or cargo details" required></textarea></div>
            <div class="form-actions"><button class="btn btn-primary" type="submit">Submit Enquiry</button><button class="btn btn-ghost" type="reset">Reset</button></div>
            <p id="formStatus" aria-live="polite"></p>
          </form>
        </section>
        <aside class="contact-card">
          <h3>Contact details</h3>
          <div class="meta-row"><strong>Phone:</strong><a href="tel:+919322099980">+91 93220 99980</a></div>
          <div class="meta-row"><strong>Phone:</strong><a href="tel:+919769901140">+91 97699 01140</a></div>
          <div class="meta-row"><strong>Email:</strong><a href="mailto:info@apcargos.in">info@apcargos.in</a></div>
          <div class="meta-row"><strong>Address:</strong><span>Vrindavan, Opp. Omkar Building, Sion-Chembur Road, Chunabhatti, Mumbai 400022</span></div>
          <div class="feature-row"><span>24/7 support</span><span>Priority booking</span><span>Vehicle tracking</span></div>
        </aside>
      </div>
    </section>
  </main>
'''
    },
}

SUBPAGE_TEMPLATES = {
    'about/index.html': {
        'title': 'About AP Travel & Rental | Mumbai Bus Rental & Cargo Services',
        'description': 'About AP Travel & Rental: premium bus rental and cargo logistics in Mumbai with over 10 years of trusted service.',
        'canonical': '/about/',
        'hero_title': 'A decade of premium transport in Mumbai',
        'hero_text': 'AP Travel & Rental provides luxury coach rentals, reliable cargo services, and citywide travel solutions with a strong local presence in Sion.',
        'hero_image': 'images/blue-star-inside.webp',
        'active': 'About',
        'content': '''
  <main id="main">
    <section class="hero" aria-labelledby="hero-heading">
      <img class="hero-bg" src="../images/blue-star-inside.webp" alt="About AP Travel & Rental" loading="eager" fetchpriority="high">
      <div class="hero-overlay" aria-hidden="true"></div>
      <div class="hero-content container">
        <span class="hero-eyebrow">Our story</span>
        <h1 id="hero-heading">A premium transport partner for Mumbai and Maharashtra.</h1>
        <p class="hero-copy">We started with a small coach lineup in Sion and grew into a trusted operator for business travel, weddings, school routes, and cargo logistics.</p>
        <div class="hero-actions"><a class="btn btn-primary" href="/contact/">Contact Us</a><a class="btn btn-ghost" href="tel:+919322099980">Call Now</a></div>
      </div>
    </section>
    <section class="container section">
      <div class="section-header"><span class="section-tag">Our mission</span><h2 class="section-title">Offer premium mobility solutions with absolute reliability.</h2><p class="section-copy">Our service is built on transparency, safety, and a deep commitment to keeping travel and logistics on schedule.</p></div>
      <div class="cards-grid">
        <article class="card service-card"><span>🏆</span><h3>Reliable service</h3><p>On-time pickups, secure cargo handling, and consistent communication.</p></article>
        <article class="card service-card"><span>🧴</span><h3>Sanitized fleet</h3><p>Each vehicle receives thorough cleaning before departure.</p></article>
        <article class="card service-card"><span>📊</span><h3>Transparent pricing</h3><p>Clear quotes with all major fees included and no surprise charges.</p></article>
      </div>
    </section>
    <section class="container section">
      <div class="section-header"><span class="section-tag">Our values</span><h2 class="section-title">Safety, comfort and trust on every route.</h2></div>
      <div class="cards-grid">
        <article class="card why-card"><span>✔️</span><h3>Verified Drivers</h3><p>Experienced professionals for every passenger and cargo route.</p></article>
        <article class="card why-card"><span>💼</span><h3>Corporate-ready</h3><p>Executive coaches and reliable employee transport solutions.</p></article>
        <article class="card why-card"><span>📦</span><h3>Integrated logistics</h3><p>Household shifting and business cargo handled with care.</p></article>
      </div>
    </section>
  </main>
'''
    },
    'contact/index.html': {
        'title': 'Contact AP Travel & Rental | Bus & Cargo Booking Mumbai',
        'description': 'Contact AP Travel & Rental for premium bus rental and cargo booking in Mumbai. Call +91 93220 99980 or +91 97699 01140.',
        'canonical': '/contact/',
        'hero_title': 'Contact AP Travel & Rental',
        'hero_text': 'Reach our team for a quote on bus rental, airport transfer, School Trip, or cargo logistics.',
        'hero_image': 'images/cargo-font.webp',
        'active': 'Contact',
        'content': '''
  <main id="main">
    <section class="hero" aria-labelledby="hero-heading">
      <img class="hero-bg" src="../images/cargo-font.webp" alt="Contact AP Travel & Rental" loading="eager" fetchpriority="high">
      <div class="hero-overlay" aria-hidden="true"></div>
      <div class="hero-content container">
        <span class="hero-eyebrow">Talk to our team</span>
        <h1 id="hero-heading">Get a quote or book your next trip today.</h1>
        <p class="hero-copy">Call, WhatsApp, or submit your requirements and our booking team will reply with a tailored transport plan.</p>
        <div class="hero-actions"><a class="btn btn-primary" href="tel:+919322099980">Call Now</a><a class="btn btn-ghost" href="https://wa.me/919322099980" target="_blank" rel="noopener noreferrer">WhatsApp</a></div>
      </div>
    </section>
    <section class="container section">
      <div class="contact-grid">
        <section class="contact-card"><h3>Send an enquiry</h3><form id="contactForm"><div class="form-row"><label for="name">Name</label><input id="name" name="name" type="text" placeholder="Your name" required></div><div class="form-row"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" placeholder="+91 93220 99980" required></div><div class="form-row"><label for="email">Email</label><input id="email" name="email" type="email" placeholder="name@example.com"></div><div class="form-row"><label for="message">Message</label><textarea id="message" name="message" rows="5" placeholder="Your transport or cargo details" required></textarea></div><div class="form-actions"><button class="btn btn-primary" type="submit">Submit Enquiry</button><button class="btn btn-ghost" type="reset">Reset</button></div><p id="formStatus" aria-live="polite"></p></form></section>
        <aside class="contact-card"><h3>Contact details</h3><div class="meta-row"><strong>Phone:</strong><a href="tel:+919322099980">+91 93220 99980</a></div><div class="meta-row"><strong>Phone:</strong><a href="tel:+919769901140">+91 97699 01140</a></div><div class="meta-row"><strong>Email:</strong><a href="mailto:info@apcargos.in">info@apcargos.in</a></div><div class="meta-row"><strong>Address:</strong><span>Vrindavan, Opp. Omkar Building, Sion-Chembur Road, Chunabhatti, Mumbai 400022</span></div><div class="feature-row"><span>24/7 booking support</span><span>Fast response</span><span>WhatsApp enquiries</span></div></aside>
      </div>
      <div class="map-card"><iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3768.146672719445!2d72.8645!3d19.0410!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7b695fd0e79eb%3A0x48dfe3ef04cc4071!2sSion%2C%20Mumbai!5e0!3m2!1sen!2sin!4v1710000000000!5m2!1sen!2sin" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
    </section>
  </main>
'''
    }
}

SERVICE_PAGES = {
    'fleet/index.html': {
        'title': 'Fleet | AP Travel & Rental — Luxury Bus Rental Mumbai',
        'description': 'View the premium bus fleet at AP Travel & Rental. Luxury AC coaches, executive buses, and cargo-ready transport across Mumbai.',
        'canonical': '/fleet/',
        'hero_title': 'Elite Bus Fleet in Mumbai',
        'hero_text': 'Explore our premium fleet of luxury AC coaches and executive vehicles for comfortable group travel.',
        'hero_image': 'images/blue-star-right.webp',
        'active': 'Fleet',
        'content': '''
  <main id="main">
    <section class="hero" aria-labelledby="hero-heading">
      <img class="hero-bg" src="../images/blue-star-right.webp" alt="Elite bus fleet" loading="eager" fetchpriority="high">
      <div class="hero-overlay" aria-hidden="true"></div>
      <div class="hero-content container">
        <span class="hero-eyebrow">Our fleet</span>
        <h1 id="hero-heading">Modern luxury buses for every journey.</h1>
        <p class="hero-copy">Clean coaches maintained to premium standards and ready for corporate, wedding, tourism, and outstation travel.</p>
        <div class="hero-actions"><a class="btn btn-primary" href="/contact/">Book a Vehicle</a><a class="btn btn-ghost" href="tel:+919322099980">Call Now</a></div>
      </div>
    </section>
    <section class="container section">
      <div class="section-header"><span class="section-tag">Featured vehicles</span><h2 class="section-title">Our trusted travel companions.</h2></div>
      <div class="fleet-grid"><article class="fleet-card"><img src="../images/blue-star.webp" alt="KGN Luxury AC Bus" loading="lazy"><h3>KGN Luxury AC Bus</h3><p>45 seats, air-conditioned and comfortable for longer trips.</p><a class="card-link" href="/contact/">Book now</a></article><article class="fleet-card"><img src="../images/KGN_BLUE.webp" alt="KGN Executive Bus" loading="lazy"><h3>KGN Executive Bus</h3><p>Premium interiors and ample luggage room for weddings and events.</p><a class="card-link" href="/contact/">Book now</a></article><article class="fleet-card"><img src="../images/blue-star-right.webp" alt="Blue Star Executive Coach" loading="lazy"><h3>Blue Star Executive Coach</h3><p>Executive comfort for outstation journeys and corporate travel.</p><a class="card-link" href="/contact/">Book now</a></article></div>
    </section>
  </main>
'''
    },
    'cargo/index.html': {
        'title': 'Cargo & Logistics | AP Travel & Rental Mumbai',
        'description': 'Cargo and logistics services in Mumbai. Same-day delivery, interstate freight, business cargo, and household shifting by AP Travel & Rental.',
        'canonical': '/cargo/',
        'hero_title': 'Cargo & Logistics Services',
        'hero_text': 'Flexible cargo solutions across Mumbai and Maharashtra with secure handling and expert support.',
        'hero_image': 'images/cargo-inside.webp',
        'active': 'Cargo',
        'content': '''
  <main id="main">
    <section class="hero" aria-labelledby="hero-heading">
      <img class="hero-bg" src="../images/cargo-inside.webp" alt="Cargo logistics service" loading="eager" fetchpriority="high">
      <div class="hero-overlay" aria-hidden="true"></div>
      <div class="hero-content container">
        <span class="hero-eyebrow">Cargo solutions</span>
        <h1 id="hero-heading">Secure cargo transport for business and home moves.</h1>
        <p class="hero-copy">Same-day delivery, interstate logistics, and household shifting with route transparency and secure handling.</p>
        <div class="hero-actions"><a class="btn btn-primary" href="/contact/">Get a Quote</a><a class="btn btn-ghost" href="https://wa.me/919322099980" target="_blank" rel="noopener noreferrer">WhatsApp</a></div>
      </div>
    </section>
    <section class="container section"><div class="section-header"><span class="section-tag">Our services</span><h2 class="section-title">Tailored logistics for every shipment.</h2></div><div class="cargo-grid"><article class="cargo-card"><h3>Same Day Delivery</h3><p>Local cargo pickup and delivery with careful handling.</p></article><article class="cargo-card"><h3>Interstate Logistics</h3><p>Freight service connecting Mumbai with major cities nationwide.</p></article><article class="cargo-card"><h3>Business Cargo</h3><p>Dependable transportation for commercial goods.</p></article><article class="cargo-card"><h3>Household Shifting</h3><p>Safe moving service for personal belongings and furniture.</p></article></div></section>
  </main>
'''
    },
    '/cargo-service-mumbai//index.html': {
        'title': 'Cargo Service Mumbai | AP Travel & Rental',
        'description': 'Cargo service in Mumbai with AP Travel & Rental. Same-day delivery, interstate logistics, and household shifting.',
        'canonical': '//cargo-service-mumbai//',
        'hero_title': 'Cargo Service in Mumbai',
        'hero_text': 'Trusted cargo services for local delivery, interstate freight, and household shifting across Mumbai.',
        'hero_image': 'images/cargo-inside.webp',
        'active': 'Cargo',
        'content': '''
  <main id="main">
    <section class="hero" aria-labelledby="hero-heading">
      <img class="hero-bg" src="../images/cargo-inside.webp" alt="Cargo service Mumbai" loading="eager" fetchpriority="high">
      <div class="hero-overlay" aria-hidden="true"></div>
      <div class="hero-content container">
        <span class="hero-eyebrow">Cargo service</span>
        <h1 id="hero-heading">Reliable cargo logistics within Mumbai.</h1>
        <p class="hero-copy">From urgent local shipping to interstate freight, we handle goods with care and speed.</p>
        <div class="hero-actions"><a class="btn btn-primary" href="/contact/">Request a Quote</a><a class="btn btn-ghost" href="tel:+919322099980">Call Now</a></div>
      </div>
    </section>
  </main>
'''
    },
    'bus-rental-mumbai/index.html': {
        'title': 'Bus Rental Mumbai | AP Travel & Rental',
        'description': 'Book bus rental services in Mumbai with AP Travel & Rental. Luxury AC coaches for corporate, wedding, school, and outstation travel.',
        'canonical': '/bus-rental-mumbai/',
        'hero_title': 'Bus Rental Services in Mumbai',
        'hero_text': 'Luxury AC coaches for corporate events, weddings, school trips, and outstation journeys.',
        'hero_image': 'images/blue-star.webp',
        'active': 'Bus Rental',
        'content': '''
  <main id="main">
    <section class="hero" aria-labelledby="hero-heading">
      <img class="hero-bg" src="../images/blue-star.webp" alt="Bus rental Mumbai" loading="eager" fetchpriority="high">
      <div class="hero-overlay" aria-hidden="true"></div>
      <div class="hero-content container">
        <span class="hero-eyebrow">Bus rental</span>
        <h1 id="hero-heading">Luxury bus rental for every Mumbai route.</h1>
        <p class="hero-copy">Comfortable AC coaches for weddings, corporate travel, school trips, and outstation tours.</p>
        <div class="hero-actions"><a class="btn btn-primary" href="/contact/">Book a Bus</a><a class="btn btn-ghost" href="tel:+919322099980">Call Now</a></div>
      </div>
    </section>
  </main>
'''
    },
    'corporate-bus-rental-mumbai/index.html': {
        'title': 'Corporate Bus Rental Mumbai | AP Travel & Rental',
        'description': 'Corporate bus rental in Mumbai for employee shuttles, event transport, and airport transfers.',
        'canonical': '/corporate-bus-rental-mumbai/',
        'hero_title': 'Corporate Bus Rental in Mumbai',
        'hero_text': 'Executive transportation for companies with reliable shuttles and conference transfer services.',
        'hero_image': 'images/blue-star.webp',
        'active': 'Corporate',
        'content': '''
  <main id="main">
    <section class="hero" aria-labelledby="hero-heading">
      <img class="hero-bg" src="../images/blue-star.webp" alt="Corporate bus rental" loading="eager" fetchpriority="high">
      <div class="hero-overlay" aria-hidden="true"></div>
      <div class="hero-content container">
        <span class="hero-eyebrow">Corporate transport</span>
        <h1 id="hero-heading">Executive bus rental for companies and events.</h1>
        <p class="hero-copy">Professional corporate shuttles, employee transport, and airport transfer solutions.</p>
        <div class="hero-actions"><a class="btn btn-primary" href="/contact/">Book Corporate Transport</a><a class="btn btn-ghost" href="tel:+919322099980">Call Now</a></div>
      </div>
    </section>
  </main>
'''
    },
    'outstation-bus-rental-mumbai/index.html': {
        'title': 'Outstation Bus Rental Mumbai | AP Travel & Rental',
        'description': 'Outstation bus rental from Mumbai for long-distance travel, tours, and family trips.',
        'canonical': '/outstation-bus-rental-mumbai/',
        'hero_title': 'Outstation Bus Rental from Mumbai',
        'hero_text': 'Comfortable long-distance bus rentals for tours, family travel, and group journeys.',
        'hero_image': 'images/blue-star-right.webp',
        'active': 'Outstation',
        'content': '''
  <main id="main">
    <section class="hero" aria-labelledby="hero-heading">
      <img class="hero-bg" src="../images/blue-star-right.webp" alt="Outstation bus rental" loading="eager" fetchpriority="high">
      <div class="hero-overlay" aria-hidden="true"></div>
      <div class="hero-content container">
        <span class="hero-eyebrow">Outstation travel</span>
        <h1 id="hero-heading">Long-distance bus rentals made easy.</h1>
        <p class="hero-copy">Premium coaches for highways and outstation routes with reliable drivers and comfort.</p>
        <div class="hero-actions"><a class="btn btn-primary" href="/contact/">Book Outstation Travel</a><a class="btn btn-ghost" href="tel:+919322099980">Call Now</a></div>
      </div>
    </section>
  </main>
'''
    },
    'tempo-traveller-rental-mumbai/index.html': {
        'title': 'Tempo Traveller Rental Mumbai | AP Travel & Rental',
        'description': 'Tempo traveller rental in Mumbai for small groups, city transfers, and package tours.',
        'canonical': '/tempo-traveller-rental-mumbai/',
        'hero_title': 'Tempo Traveller Rental in Mumbai',
        'hero_text': 'Flexible tempo traveller bookings for smaller groups, airport transfers, and city tours.',
        'hero_image': 'images/blue-star-inside.webp',
        'active': 'Tempo',
        'content': '''
  <main id="main">
    <section class="hero" aria-labelledby="hero-heading">
      <img class="hero-bg" src="../images/blue-star-inside.webp" alt="Tempo traveller rental" loading="eager" fetchpriority="high">
      <div class="hero-overlay" aria-hidden="true"></div>
      <div class="hero-content container">
        <span class="hero-eyebrow">Tempo traveller</span>
        <h1 id="hero-heading">Comfortable tempo traveller rentals for small groups.</h1>
        <p class="hero-copy">Agile transport for airport runs, family outings, and short tours in Mumbai.</p>
        <div class="hero-actions"><a class="btn btn-primary" href="/contact/">Rent Now</a><a class="btn btn-ghost" href="tel:+919322099980">Call Now</a></div>
      </div>
    </section>
  </main>
'''
    },
    'wedding-bus-rental-mumbai/index.html': {
        'title': 'Wedding Bus Rental Mumbai | AP Travel & Rental',
        'description': 'Wedding bus rental in Mumbai for guest transport, family travel, and celebration routes.',
        'canonical': '/wedding-bus-rental-mumbai/',
        'hero_title': 'Wedding Bus Rental in Mumbai',
        'hero_text': 'Premium guest transport for wedding celebrations with punctual, reliable coach service.',
        'hero_image': 'images/blue-star.webp',
        'active': 'Wedding',
        'content': '''
  <main id="main">
    <section class="hero" aria-labelledby="hero-heading">
      <img class="hero-bg" src="../images/blue-star.webp" alt="Wedding bus rental" loading="eager" fetchpriority="high">
      <div class="hero-overlay" aria-hidden="true"></div>
      <div class="hero-content container">
        <span class="hero-eyebrow">Wedding transport</span>
        <h1 id="hero-heading">Elegant bus rental for weddings and celebrations.</h1>
        <p class="hero-copy">Secure, stylish guest transport with premium coaches and professional drivers.</p>
        <div class="hero-actions"><a class="btn btn-primary" href="/contact/">Plan Wedding Transport</a><a class="btn btn-ghost" href="tel:+919322099980">Call Now</a></div>
      </div>
    </section>
  </main>
'''
    }
}

PAGE_TEMPLATES = {}
PAGE_TEMPLATES.update(PAGES)
PAGE_TEMPLATES.update(SUBPAGE_TEMPLATES)
PAGE_TEMPLATES.update(SERVICE_PAGES)


def build_nav(active):
    return COMMON_NAV.format(
        home_active='active' if active == 'Home' else '',
        fleet_active='active' if active == 'Fleet' else '',
        bus_active='active' if active == 'Bus Rental' else '',
        corporate_active='active' if active == 'Corporate' else '',
        wedding_active='active' if active == 'Wedding' else '',
        outstation_active='active' if active == 'Outstation' else '',
        tempo_active='active' if active == 'Tempo' else '',
        cargo_active='active' if active == 'Cargo' else '',
        about_active='active' if active == 'About' else '',
        contact_active='active' if active == 'Contact' else ''
    )


def build_page(path, config):
    output_path = root / path
    assets_prefix = config.get('assets_prefix', '../assets/') if '/' in path else 'assets/'
    nav_html = build_nav(config['active'])
    body = HEADER_TEMPLATE.format(
        title=config['title'],
        description=config['description'],
        canonical=config['canonical'],
        assets_prefix=assets_prefix,
        nav=nav_html
    ) + config['content'] + FOOTER_TEMPLATE.format(assets_prefix=assets_prefix, year=datetime.now().year)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(body, encoding='utf-8')
    print(f'Wrote {path}')


if __name__ == '__main__':
    for path, config in PAGE_TEMPLATES.items():
        build_page(path, config)

    robots = '''User-agent: *
Allow: /
Disallow: /admin/
Disallow: /private/
Disallow: /temp/
Sitemap: https://aptravelrental.in/sitemap.xml
'''
    (root / 'robots.txt').write_text(robots, encoding='utf-8')

    sitemap_urls = [
        '/',
        '/about/',
        '/contact/',
        '/fleet/',
        '/cargo/',
        '//cargo-service-mumbai//',
        '/bus-rental-mumbai/',
        '/corporate-bus-rental-mumbai/',
        '/outstation-bus-rental-mumbai/',
        '/tempo-traveller-rental-mumbai/',
        '/wedding-bus-rental-mumbai/'
    ]
    now = datetime.utcnow().strftime('%Y-%m-%d')
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in sitemap_urls:
        sitemap.extend([
            '  <url>',
            f'    <loc>https://aptravelrental.in{url}</loc>',
            f'    <lastmod>{now}</lastmod>',
            '    <changefreq>monthly</changefreq>',
            '    <priority>0.8</priority>',
            '  </url>'
        ])
    sitemap.append('</urlset>')
    (root / 'sitemap.xml').write_text('\n'.join(sitemap), encoding='utf-8')
    print('Updated robots.txt and sitemap.xml')
