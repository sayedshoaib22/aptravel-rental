#!/usr/bin/env python3
"""Generate local SEO landing pages for AP Travel & Rental."""
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://aptravelrental.in"

INTERNAL_LINKS = """
<div class="seo-internal-links" aria-label="Related pages">
  <a href="/">Bus Rental Mumbai</a>
  <a href="/corporate-bus-rental-mumbai/">Corporate Bus Rental</a>
  <a href="/wedding-bus-rental-mumbai/">Wedding Bus Rental</a>
  <a href="/outstation-bus-rental-mumbai/">Outstation Bus Rental</a>
  <a href="/tempo-traveller-rental-mumbai/">Tempo Traveller Rental</a>
  <a href="/cargo/">Cargo &amp; Logistics</a>
  <a href="/cargo-service-mumbai/">Cargo Service Mumbai</a>
  <a href="/fleet/">Our Fleet</a>
  <a href="/about/">About Us</a>
  <a href="/contact/">Contact</a>
</div>"""

PAGES = [
    {
        "slug": "bus-rental-mumbai",
        "title": "Bus Rental Service in Mumbai | AP Travel & Rental",
        "description": "Premium bus rental in Mumbai for corporate trips, weddings, tourism and outstation travel. AC coaches with pushback seats. Call +91 93220 99980.",
        "h1": "Bus Rental Service in Mumbai",
        "hero_p": "Book luxury AC coaches and executive buses in Mumbai for corporate events, weddings, group tours and outstation journeys — with experienced drivers and transparent pricing.",
        "schema_type": "Service",
        "schema_name": "Bus Rental Service Mumbai",
        "keywords": "bus rental Mumbai, AC coach rental, luxury bus hire Mumbai",
        "sections": [
            ("Why Choose AP Travel for Bus Rental in Mumbai", """
<p>Mumbai is a city that never sleeps — and when you need to move a group of people reliably, whether for a corporate offsite, a wedding celebration, or an outstation pilgrimage, you need a bus rental partner you can trust. AP Travel &amp; Rental has been serving Mumbai and Maharashtra for over a decade from our base in Sion, providing premium air-conditioned coaches that combine comfort, safety, and punctuality.</p>
<p>Our fleet includes the KGN Luxury AC Bus, KGN Executive Bus, and the Blue Star Executive Coach built on the Eicher Skyline Pro chassis. Each vehicle is maintained to showroom standards, sanitized before every trip, and staffed by experienced drivers who know Mumbai's roads and India's highways intimately.</p>
<p>Whether you are planning a one-day corporate conference shuttle, a multi-day outstation tour to Lonavala or Goa, or wedding guest transport between venues in Bandra and Navi Mumbai, our team provides clear quotes with no hidden charges and 24/7 booking support.</p>
"""),
            ("Our Bus Rental Fleet in Mumbai", """
<p>Choosing the right coach makes all the difference for your group's comfort and safety. Our KGN Luxury AC Bus seats up to 45 passengers with premium pushback seats, full air conditioning, and an onboard music system — ideal for large corporate groups and tourism packages.</p>
<p>The KGN Executive Bus, with its distinctive yellow exterior and luxury interior finish, accommodates up to 40 passengers and is a popular choice for wedding guest transportation. Its spacious luggage compartments handle gifts, garments, and personal bags with ease.</p>
<p>For executive corporate travel and premium outstation tours, the Blue Star Executive Coach offers Eicher Skyline Pro reliability with pushback recline seats, individual headrests, reading lights, and curtained windows — built for long highway journeys as much as short city transfers.</p>
<p>Explore our full <a href="/fleet/">fleet page</a> for detailed specifications, interior photos, and seating capacities for each vehicle.</p>
"""),
            ("Types of Bus Rental Services We Offer", """
<p>AP Travel &amp; Rental is not a one-size-fits-all operator. We tailor our service to your trip type:</p>
<ul>
<li><strong>Corporate bus rental</strong> — Conferences, employee transport, factory visits, and team offsites with dedicated account support for recurring bookings.</li>
<li><strong>Wedding bus rental</strong> — Guest transfers between ceremony, reception, and hotel venues with on-call drivers for late-night returns.</li>
<li><strong>Outstation bus rental</strong> — Multi-day packages to Pune, Nashik, Shirdi, Goa, and pan-Maharashtra destinations with highway-experienced drivers.</li>
<li><strong>Tourism and pilgrimage</strong> — Group tours to religious sites, hill stations, and sightseeing circuits across Western India.</li>
<li><strong>School and college trips</strong> — Safe, supervised group transport with well-maintained coaches and responsible drivers.</li>
</ul>
<p>We also provide <a href="/cargo/">cargo and logistics services</a> for businesses needing goods transport alongside passenger solutions.</p>
"""),
            ("How to Book a Bus in Mumbai", """
<p>Booking with AP Travel &amp; Rental is straightforward. Call us at +91 93220 99980 or +91 97699 01140, or fill out the contact form on our <a href="/contact/">contact page</a>. Share your trip date, passenger count, pickup location, destination, and any special requirements — decoration for weddings, multiple stops for corporate shuttles, or overnight driver arrangements for outstation trips.</p>
<p>Our team responds quickly with vehicle options, a transparent quote, and booking confirmation. For corporate clients with recurring needs, we offer dedicated account management and preferential scheduling during peak seasons.</p>
<p>We serve all areas of Mumbai including South Mumbai, Bandra, Andheri, Powai, Thane, Navi Mumbai, and the extended Mumbai Metropolitan Region. Outstation pickups from Mumbai airport and major railway stations are also available on request.</p>
"""),
            ("Bus Rental Pricing in Mumbai", """
<p>Bus rental pricing in Mumbai depends on several factors: vehicle type, trip duration, distance, number of days, toll and parking requirements, and seasonal demand. AP Travel &amp; Rental provides upfront quotes with all inclusions clearly listed — no surprise charges on the day of travel.</p>
<p>Local city transfers typically start at competitive daily rates, while outstation packages are priced per day plus per-kilometre charges beyond included limits. Wedding packages may include decoration coordination and extended hours for baraat processions or late-night returns.</p>
<p>Contact us for a customized quote tailored to your specific itinerary. We regularly serve clients from corporate parks in Andheri East, wedding venues in Bandra and Juhu, and tourism groups departing from Dadar and CST.</p>
"""),
        ],
    },
    {
        "slug": "corporate-bus-rental-mumbai",
        "title": "Corporate Bus Rental Mumbai | AC Coach Hire | AP Travel & Rental",
        "description": "Corporate bus rental in Mumbai for conferences, employee transport and offsites. Premium AC coaches with pushback seats. Call +91 93220 99980.",
        "h1": "Corporate Bus Rental in Mumbai",
        "hero_p": "Reliable AC coach hire for corporate conferences, employee shuttles, factory visits and team offsites across Mumbai and outstation routes.",
        "schema_type": "Service",
        "schema_name": "Corporate Bus Rental Mumbai",
        "keywords": "corporate bus rental Mumbai, employee transport Mumbai, conference shuttle",
        "sections": [
            ("Corporate Transport Solutions in Mumbai", """
<p>Mumbai's corporate landscape demands transport that is punctual, professional, and comfortable. AP Travel &amp; Rental provides dedicated corporate bus rental services for companies across BKC, Andheri, Powai, Goregaon, Thane, and Navi Mumbai — delivering air-conditioned coaches with pushback seating, GPS-tracked routes, and drivers trained in professional conduct.</p>
<p>From daily employee shuttle services between railway stations and office campuses to one-time conference transfers at Jio World Convention Centre or NESCO Goregaon, our fleet handles groups from 35 to 45 passengers with consistent quality.</p>
<p>We understand that corporate clients need reliability above all else. That is why every coach is sanitized before departure, mechanically inspected on schedule, and assigned drivers with formal attire and route familiarity.</p>
"""),
            ("Corporate Events We Serve", """
<p>Our corporate bus rental service covers a wide range of business transport needs:</p>
<ul>
<li>Annual general meetings and shareholder events</li>
<li>Conference and exhibition shuttles</li>
<li>Factory and warehouse visit transport</li>
<li>Team building offsites and retreat travel</li>
<li>Airport pickup and drop for visiting executives</li>
<li>Inter-office transfers during office relocations</li>
<li>Product launch event guest transport</li>
</ul>
<p>We work with IT companies, manufacturing firms, financial institutions, pharmaceutical companies, and startups across the Mumbai Metropolitan Region.</p>
"""),
            ("Why Corporates Choose AP Travel", """
<p>Corporate transport is about more than getting from A to B — it reflects your company's standards. AP Travel &amp; Rental offers dedicated account support for recurring bookings, flexible scheduling for shift changes, and transparent monthly billing for long-term contracts.</p>
<p>Our KGN Luxury AC Bus and Blue Star Executive Coach are equipped with comfortable pushback seats, climate control, and clean interiors that make a professional impression on clients and employees alike. Drivers arrive on time, follow agreed routes, and maintain courteous communication throughout the journey.</p>
<p>For multi-day corporate offsites to Lonavala, Mahabaleshwar, or Goa, we provide experienced highway drivers, 24/7 helpline support, and well-maintained coaches built for long-distance comfort.</p>
"""),
            ("Corporate Bus Rental Pricing", """
<p>Corporate bus rental pricing is customized based on your requirements. Factors include trip frequency (one-time vs. recurring), distance, duration, vehicle type, and number of passengers. We provide detailed quotes with all inclusions — driver allowance, tolls, parking, and night halt charges where applicable.</p>
<p>Long-term corporate contracts for daily employee shuttles receive preferential rates and guaranteed vehicle availability. Contact our team at +91 93220 99980 to discuss your corporate transport needs and receive a tailored proposal.</p>
"""),
            ("Book Corporate Bus Rental Today", """
<p>Ready to streamline your corporate transport? Visit our <a href="/contact/">contact page</a> or call us directly. Our team will assess your requirements, recommend the right coach from our <a href="/fleet/">fleet</a>, and confirm your booking with a clear quote.</p>
<p>AP Travel &amp; Rental — your trusted corporate bus rental partner in Mumbai since day one.</p>
"""),
        ],
    },
    {
        "slug": "wedding-bus-rental-mumbai",
        "title": "Wedding Bus Rental Mumbai | Guest Transport | AP Travel & Rental",
        "description": "Wedding bus rental in Mumbai for guest transport between venues. KGN Executive Bus and Blue Star Coach with decoration options. Call +91 93220 99980.",
        "h1": "Wedding Bus Rental in Mumbai",
        "hero_p": "Elegant guest transport for Mumbai weddings — comfortable AC coaches with spacious luggage areas, decoration options, and on-call drivers for late-night returns.",
        "schema_type": "Service",
        "schema_name": "Wedding Bus Rental Mumbai",
        "keywords": "wedding bus rental Mumbai, wedding guest transport, baraat bus Mumbai",
        "sections": [
            ("Wedding Guest Transport in Mumbai", """
<p>Your wedding day should be about celebration, not logistics. AP Travel &amp; Rental provides premium wedding bus rental services across Mumbai — moving your guests comfortably between ceremony venues, reception halls, and hotels with punctual, well-maintained air-conditioned coaches.</p>
<p>Our KGN Executive Bus and Blue Star Executive Coach are the most popular choices for Mumbai weddings, offering plush seating for up to 40–45 guests, generous luggage space for sarees, lehengas, and gift bags, and experienced drivers who navigate Mumbai's wedding-season traffic with ease.</p>
<p>From Bandra and Juhu beachside venues to grand halls in Andheri and Navi Mumbai, we have served hundreds of wedding families with stress-free guest transport.</p>
"""),
            ("Wedding Transport Services We Provide", """
<p>We offer comprehensive wedding transport solutions:</p>
<ul>
<li>Guest shuttle between ceremony and reception venues</li>
<li>Hotel to venue pickup and return transfers</li>
<li>Baraat procession support with coordinated timing</li>
<li>Multi-bus packages for large guest lists (100+ guests)</li>
<li>Late-night return transport after reception</li>
<li>Out-of-town guest airport and railway station pickups</li>
<li>Decoration coordination on request (flowers, ribbons, banners)</li>
</ul>
"""),
            ("Choosing the Right Wedding Bus", """
<p>For intimate weddings with 30–40 guests, the KGN Executive Bus provides a luxury interior with comfortable seating and ample storage. For larger gatherings up to 45 guests, the KGN Luxury AC Bus or Blue Star Executive Coach offers spacious pushback seats and a premium travel experience.</p>
<p>All our wedding coaches feature air conditioning essential for Mumbai's warm months, clean and sanitized interiors, and professional drivers who dress appropriately and communicate with your wedding coordinator.</p>
<p>View our <a href="/fleet/">fleet gallery</a> to see interior photos and choose the perfect coach for your celebration.</p>
"""),
            ("Wedding Bus Rental Tips", """
<p>Book your wedding bus rental at least 2–4 weeks in advance, especially during peak wedding season (November through February). Share your venue addresses, timing schedule, and any multiple-stop requirements with our team.</p>
<p>Consider booking separate buses for bride/groom family and guest groups if venues are far apart. For baraat processions, confirm road permissions and timing with local authorities — our drivers are experienced with Mumbai procession routes.</p>
<p>We provide transparent pricing with no hidden charges. Wedding packages may include extended hours for late-night returns — discuss your schedule with our team for a customized quote.</p>
"""),
            ("Book Your Wedding Bus Today", """
<p>Make your wedding guest transport effortless. Call +91 93220 99980 or visit our <a href="/contact/">contact page</a> to reserve your wedding bus. Our team responds quickly during wedding season and works closely with planners and families to ensure flawless coordination.</p>
"""),
        ],
    },
    {
        "slug": "outstation-bus-rental-mumbai",
        "title": "Outstation Bus Rental from Mumbai | AP Travel & Rental",
        "description": "Outstation bus rental from Mumbai to Pune, Goa, Shirdi, Nashik and beyond. AC coaches with experienced highway drivers. Call +91 93220 99980.",
        "h1": "Outstation Bus Rental from Mumbai",
        "hero_p": "Premium outstation bus hire from Mumbai — reclining AC coaches, experienced highway drivers, and multi-day packages to Pune, Goa, Shirdi, Lonavala and across India.",
        "schema_type": "Service",
        "schema_name": "Outstation Bus Rental Mumbai",
        "keywords": "outstation bus rental Mumbai, Mumbai to Pune bus, Mumbai to Goa bus rental",
        "sections": [
            ("Outstation Bus Hire from Mumbai", """
<p>Planning a group trip outside Mumbai? AP Travel &amp; Rental specializes in outstation bus rental with well-maintained AC coaches, experienced highway drivers, and multi-day packages to destinations across Maharashtra, Goa, Karnataka, and beyond.</p>
<p>Our Blue Star Executive Coach on the Eicher Skyline Pro chassis is built for long-distance comfort — pushback recline seats, individual headrests, reading lights, curtained windows, and onboard music systems make hours on the highway enjoyable.</p>
<p>Popular routes include Mumbai to Pune, Mumbai to Goa, Mumbai to Shirdi, Mumbai to Nashik, Mumbai to Lonavala, Mumbai to Mahabaleshwar, and Mumbai to Surat. We also serve custom itineraries for corporate offsites, pilgrimage groups, and family vacations.</p>
"""),
            ("Popular Outstation Routes", """
<p>Our experienced drivers know these routes intimately:</p>
<ul>
<li><strong>Mumbai to Pune</strong> — Expressway and old highway routes, 3–4 hours</li>
<li><strong>Mumbai to Goa</strong> — NH66 coastal route, full-day journey with comfort stops</li>
<li><strong>Mumbai to Shirdi</strong> — Pilgrimage groups, Ahmednagar route</li>
<li><strong>Mumbai to Nashik</strong> — Wine tours, religious visits, corporate trips</li>
<li><strong>Mumbai to Lonavala/Khandala</strong> — Weekend getaways and monsoon trips</li>
<li><strong>Mumbai to Mahabaleshwar</strong> — Hill station tours and strawberry season visits</li>
</ul>
"""),
            ("Outstation Trip Features", """
<p>Every outstation booking includes a mechanically inspected coach, experienced highway driver, 24/7 helpline support during your journey, and sanitized cabin before departure. Multi-day packages cover driver allowance, tolls, and state border charges with transparent pricing.</p>
<p>For overnight trips, we coordinate driver rest stops and hotel parking. Our team provides route planning assistance and can suggest optimal departure times to avoid Mumbai traffic congestion.</p>
"""),
            ("Outstation Bus Rental Pricing", """
<p>Outstation pricing is based on vehicle type, number of days, total kilometres, and route complexity. Daily packages typically include a set kilometre limit with additional per-km charges beyond that. Multi-day tours to Goa or Shirdi are quoted as complete packages.</p>
<p>Contact us with your destination, dates, passenger count, and itinerary for a detailed quote. Peak season (Diwali, Christmas, summer holidays) books quickly — reserve early.</p>
"""),
            ("Book Your Outstation Trip", """
<p>Ready to hit the road? Call +91 93220 99980 or fill out our <a href="/contact/">contact form</a>. Explore our <a href="/fleet/">fleet</a> and choose the perfect coach for your outstation adventure.</p>
"""),
        ],
    },
    {
        "slug": "tempo-traveller-rental-mumbai",
        "title": "Tempo Traveller Rental Mumbai | Group Travel | AP Travel & Rental",
        "description": "Tempo traveller and mini bus rental in Mumbai for small groups. AC vehicles for corporate, family and outstation trips. Call +91 93220 99980.",
        "h1": "Tempo Traveller Rental in Mumbai",
        "hero_p": "AC tempo traveller and mini coach rental in Mumbai for small groups — ideal for family trips, corporate teams, airport transfers and outstation getaways.",
        "schema_type": "Service",
        "schema_name": "Tempo Traveller Rental Mumbai",
        "keywords": "tempo traveller rental Mumbai, mini bus hire Mumbai, 12 seater rental Mumbai",
        "sections": [
            ("Tempo Traveller Hire in Mumbai", """
<p>Not every group needs a full-size 45-seater coach. AP Travel &amp; Rental offers tempo traveller and mini bus rental solutions in Mumbai for smaller groups — from family vacations and airport transfers to corporate team outings and pilgrimage visits.</p>
<p>While our primary fleet consists of luxury AC buses seating 40–45 passengers, we coordinate tempo traveller arrangements through our trusted network for groups of 9 to 26 passengers who need the same reliability and professional service AP Travel is known for.</p>
<p>Whether you need a 12-seater for a Mumbai airport pickup, a 17-seater for a Pune day trip, or a 26-seater for a corporate team offsite, our booking team connects you with the right vehicle at competitive rates.</p>
"""),
            ("When to Choose a Tempo Traveller", """
<p>Tempo travellers are ideal when:</p>
<ul>
<li>Your group is between 9 and 26 passengers</li>
<li>You need nimble city navigation in congested Mumbai areas</li>
<li>Budget-conscious travel without compromising on AC comfort</li>
<li>Airport transfers for executive teams or family groups</li>
<li>Day trips to Lonavala, Alibaug, or Karnala from Mumbai</li>
<li>Small corporate teams attending conferences or client meetings</li>
</ul>
<p>For larger groups, explore our full <a href="/fleet/">bus fleet</a> with 40–45 seater luxury coaches.</p>
"""),
            ("Tempo Traveller vs Full Coach", """
<p>Choosing between a tempo traveller and a full coach depends on group size, budget, and comfort requirements. Tempo travellers offer lower per-trip costs for small groups and easier parking at venues. Full coaches provide superior comfort with pushback seats, more luggage space, and a premium experience for longer journeys.</p>
<p>Our team helps you choose the right option based on your passenger count, trip duration, and destination. For outstation trips exceeding 4–5 hours, we often recommend upgrading to our Blue Star Executive Coach for superior long-distance comfort.</p>
"""),
            ("Booking Tempo Traveller in Mumbai", """
<p>Contact AP Travel &amp; Rental at +91 93220 99980 with your group size, dates, and itinerary. We provide transparent quotes and confirm vehicle specifications before booking. All vehicles come with experienced drivers, AC, and clean interiors.</p>
<p>We serve all Mumbai areas including South Mumbai, Western Suburbs, Central Mumbai, Thane, and Navi Mumbai.</p>
"""),
            ("Related Services", """
<p>In addition to tempo traveller rental, AP Travel offers <a href="/">full bus rental</a>, <a href="/corporate-bus-rental-mumbai/">corporate transport</a>, <a href="/wedding-bus-rental-mumbai/">wedding guest buses</a>, and <a href="/cargo/">cargo logistics</a>. Contact us for all your transport needs in Mumbai.</p>
"""),
        ],
    },
    {
        "slug": "cargo-service-mumbai",
        "title": "Cargo Service Mumbai | Logistics & Goods Transport | AP Travel & Rental",
        "description": "Reliable cargo and logistics services in Mumbai. Fast, secure and affordable goods transport, FTL, PTL and parcel delivery across India. Call +91 93220 99980.",
        "h1": "Cargo Service in Mumbai",
        "hero_p": "Reliable cargo and logistics services in Mumbai — fast, secure and affordable transportation for domestic freight, FTL, PTL, parcel delivery and commercial goods transport across India.",
        "schema_type": "Service",
        "schema_name": "Cargo Service Mumbai",
        "keywords": "Cargo Service Mumbai, Logistics Company Mumbai, Cargo Transportation Mumbai, Transport Service Mumbai, Goods Transport Mumbai, Logistics Services India",
        "sections": [
            ("Cargo & Goods Transport in Mumbai", """
<p>Mumbai is India's commercial capital — and moving goods efficiently is essential for businesses and individuals alike. AP Travel &amp; Rental provides comprehensive cargo services from our Sion headquarters, covering domestic freight, parcel delivery, full truck load (FTL), part truck load (PTL), and warehouse distribution across Maharashtra and pan-India destinations.</p>
<p>Our cargo division leverages the same trusted brand, experienced team, and professional standards that have made us a leading bus rental provider in Mumbai. From a single parcel to full truck loads of commercial freight, we handle every shipment with secure loading, tracked routes, and on-time delivery.</p>
<p>Visit our dedicated <a href="/cargo/">Cargo &amp; Logistics page</a> for service details, fleet information, and online enquiry.</p>
"""),
            ("Cargo Services We Offer in Mumbai", """
<p>Our Mumbai cargo service portfolio includes:</p>
<ul>
<li><strong>Domestic cargo</strong> — Interstate and intrastate goods movement across India</li>
<li><strong>Commercial logistics</strong> — Supply chain support, inventory transfers, scheduled deliveries</li>
<li><strong>Parcel delivery</strong> — Door-to-door pickup and delivery for packages and documents</li>
<li><strong>Full Truck Load (FTL)</strong> — Dedicated truck capacity for bulk commercial shipments</li>
<li><strong>Part Truck Load (PTL)</strong> — Cost-effective shared truck space for smaller loads</li>
<li><strong>Warehouse &amp; distribution</strong> — Storage, sorting, and last-mile delivery support</li>
</ul>
"""),
            ("Industries We Serve", """
<p>Our cargo clients span retail and e-commerce, manufacturing, food and beverage, pharmaceuticals, industrial equipment, household relocation, and agriculture. We understand that different industries have different handling requirements — and our team adapts loading, strapping, and routing accordingly.</p>
<p>Mumbai pickup areas include BKC, Andheri MIDC, Navi Mumbai industrial zones, JNPT port vicinity, and residential areas across the city. Delivery routes cover Pune, Nashik, Bangalore, Hyderabad, Goa, and nationwide destinations.</p>
"""),
            ("Why Choose AP Travel for Cargo in Mumbai", """
<p>Local expertise matters in logistics. Based in Sion, Mumbai, we know the city's traffic patterns, loading zone regulations, and optimal departure windows. Our 24/7 support team coordinates pickup, transit updates, and delivery confirmation.</p>
<p>Transparent pricing with no hidden charges, secure handling protocols, and flexible FTL/PTL options make us a preferred cargo partner for Mumbai businesses. Combined with our passenger transport services, we offer a complete mobility solution for companies.</p>
"""),
            ("Book Cargo Service in Mumbai", """
<p>Ready to ship? Call +91 93220 99980, WhatsApp us, or visit our <a href="/cargo/">cargo services page</a> to submit an enquiry. Our logistics team responds with pickup scheduling, route planning, and a clear quote.</p>
"""),
        ],
        "faq": [
            ("What cargo services does AP Travel offer in Mumbai?", "We offer domestic cargo, commercial logistics, parcel delivery, full truck load (FTL), part truck load (PTL), and warehouse distribution across India."),
            ("Do you provide door-to-door cargo pickup in Mumbai?", "Yes, we provide door-to-door pickup and delivery for parcels, commercial freight, and household goods across Mumbai and nationwide routes."),
            ("What areas and routes does your Mumbai cargo service cover?", "We handle cargo service Mumbai requests across the city and nationwide — as a logistics company Mumbai businesses trust for cargo transportation Mumbai, transport service Mumbai, goods transport Mumbai, and logistics services India wide."),
        ],
    },
    {
        "slug": "about",
        "title": "About AP Travel & Rental | Mumbai Bus & Cargo Services",
        "description": "About AP Travel & Rental — premium bus rental and cargo logistics in Mumbai since over a decade. Based in Sion, serving Mumbai and India.",
        "h1": "About AP Travel & Rental",
        "hero_p": "Mumbai's trusted partner for premium bus rental and cargo logistics — built on reliability, comfort, and transparent service from our Sion headquarters.",
        "schema_type": "AboutPage",
        "schema_name": "About AP Travel & Rental",
        "keywords": "about AP Travel Rental, bus company Mumbai, transport company Sion",
        "sections": [
            ("Our Story", """
<p>AP Travel &amp; Rental was founded with a simple mission: provide Mumbai with transport services that combine premium quality, honest pricing, and genuine customer care. From our headquarters at Vrindavan, Opp. Omkar Building, Sion-Chembur Road, Chunabhatti, Sion, we have grown into a trusted name for luxury bus rental and cargo logistics across Mumbai and India.</p>
<p>What started as a focused bus rental operation has expanded to include a full cargo and logistics division — serving businesses and individuals who need reliable goods transport alongside our established passenger services. Today, we operate a fleet of KGN Luxury AC Buses, KGN Executive Buses, and the Blue Star Executive Coach, along with cargo vehicles for domestic freight and commercial logistics.</p>
"""),
            ("Our Values", """
<p>Every trip — whether carrying passengers or cargo — reflects our core values:</p>
<ul>
<li><strong>Reliability</strong> — On-time pickup and delivery, every time</li>
<li><strong>Safety</strong> — Well-maintained vehicles and experienced drivers</li>
<li><strong>Transparency</strong> — Clear quotes with no hidden charges</li>
<li><strong>Comfort</strong> — Premium AC coaches with pushback seating</li>
<li><strong>Service</strong> — 24/7 booking support and responsive communication</li>
</ul>
"""),
            ("Our Fleet & Services", """
<p>Our passenger fleet includes three premium coaches suited for different group sizes and occasions. The KGN Luxury AC Bus seats up to 45 passengers for corporate and tourism groups. The KGN Executive Bus accommodates 40 guests for weddings and outstation trips. The Blue Star Executive Coach on Eicher Skyline Pro chassis delivers executive-level comfort for long-distance travel.</p>
<p>Our cargo division offers domestic cargo, commercial logistics, parcel delivery, FTL, PTL, and warehouse distribution — serving Maharashtra, Karnataka, Goa, Telangana, Andhra Pradesh, and pan-India routes.</p>
<p>Explore our <a href="/fleet/">fleet</a>, <a href="/">bus rental services</a>, and <a href="/cargo/">cargo logistics</a> pages for detailed information.</p>
"""),
            ("Our Location in Mumbai", """
<p>We are headquartered in Sion, Mumbai — strategically located with easy access to Eastern Express Highway, Sion-Chembur Road, and major Mumbai arterial routes. Our yard serves as the base for fleet maintenance, sanitization, and dispatch for both passenger and cargo operations.</p>
<p>Address: Vrindavan, Opp. Omkar Building, Sion-Chembur Road, Chunabhatti, Near Krystal Company, Sion, Mumbai – 400022, Maharashtra, India.</p>
"""),
            ("Contact Us", """
<p>We would love to hear from you. Call +91 93220 99980 or +91 97699 01140, or visit our <a href="/contact/">contact page</a> to send an enquiry. Whether you need a bus for your next corporate event or cargo transport for your business, AP Travel &amp; Rental is ready to serve.</p>
"""),
        ],
    },
    {
        "slug": "contact",
        "title": "Contact AP Travel & Rental | Bus & Cargo Booking Mumbai",
        "description": "Contact AP Travel & Rental for bus rental and cargo booking in Mumbai. Call +91 93220 99980 or +91 97699 01140. Based in Sion, Mumbai.",
        "h1": "Contact AP Travel & Rental",
        "hero_p": "Get in touch for bus rental and cargo logistics in Mumbai — call, WhatsApp, or send an enquiry. Our team responds quickly, 24/7.",
        "schema_type": "ContactPage",
        "schema_name": "Contact AP Travel & Rental",
        "keywords": "contact AP Travel Rental, bus booking Mumbai phone, cargo enquiry Mumbai",
        "sections": [
            ("Reach Our Team", """
<p>Booking a bus or shipping cargo with AP Travel &amp; Rental is just a phone call away. Our team is available 24/7 to confirm your trip, provide quotes, and answer any questions about our fleet or cargo services.</p>
<p><strong>Phone:</strong> <a href="tel:+919322099980">+91 93220 99980</a><br>
<strong>Phone:</strong> <a href="tel:+919769901140">+91 97699 01140</a><br>
<strong>WhatsApp:</strong> <a href="https://wa.me/919322099980">+91 93220 99980</a></p>
<p><strong>Address:</strong> Vrindavan, Opp. Omkar Building, Sion-Chembur Road, Chunabhatti, Near Krystal Company, Sion, Mumbai – 400022, Maharashtra, India.</p>
<p>Our Sion office is open for walk-in enquiries during business hours. For fastest service, we recommend calling or WhatsApp messaging — our booking team responds to urgent requests at any hour, including weekends and holidays.</p>
"""),
            ("What to Include in Your Enquiry", """
<p>For faster service, please share the following details when you contact us:</p>
<ul>
<li>For bus rental: trip date, passenger count, pickup location, destination, trip type (corporate/wedding/outstation)</li>
<li>For cargo: pickup address, delivery address, cargo type, approximate weight/volume, preferred pickup date</li>
<li>Any special requirements: decoration, multiple stops, overnight driver, loading assistance</li>
</ul>
<p>The more detail you provide upfront, the faster we can confirm vehicle availability and send an accurate quote. Corporate clients with recurring transport needs should mention expected frequency — daily shuttles, weekly trips, or seasonal bookings — so we can propose a tailored contract.</p>
"""),
            ("Our Service Areas", """
<p>We serve all of Mumbai including South Mumbai, Bandra, Andheri, Powai, Goregaon, Malad, Borivali, Thane, Navi Mumbai, and the extended Mumbai Metropolitan Region. Outstation routes cover Maharashtra, Goa, Karnataka, Telangana, Andhra Pradesh, and pan-India destinations for both passenger and cargo services.</p>
<p>Popular pickup points include Mumbai International Airport (T1 and T2), Chhatrapati Shivaji Maharaj Terminus, Mumbai Central, Dadar, Bandra Terminus, Andheri, and major hotels across the city. For cargo, we pickup from warehouses, factories, retail stores, and residential addresses across Greater Mumbai.</p>
"""),
            ("Online Enquiry Options", """
<p>You can also submit an enquiry through our homepage contact form at <a href="/#contact">aptravelrental.in</a> or our cargo page at <a href="/cargo/#contact">Cargo &amp; Logistics contact form</a>. Our team typically responds within a few hours during business hours and promptly for urgent requests.</p>
<p>For wedding bookings during peak season, we recommend calling directly to secure your preferred coach. Corporate clients can request a formal quotation by email after an initial phone consultation with our account team.</p>
"""),
            ("Office Hours & Response Times", """
<p>While our booking line operates 24/7 for phone and WhatsApp enquiries, our Sion office yard is staffed for vehicle dispatch and maintenance during extended hours. Emergency outstation support is available throughout your journey via our helpline numbers.</p>
<p>We pride ourselves on response speed — most enquiries receive a quote within 2–4 hours during business hours, and urgent same-day requests are handled immediately when fleet availability permits.</p>
"""),
            ("Follow Us & Stay Connected", """
<p>Stay connected with AP Travel &amp; Rental on social media for fleet updates, seasonal offers, and travel tips. We are committed to being Mumbai's most responsive and reliable transport partner for bus rental, tempo traveller coordination, and cargo logistics.</p>
<p>Whether you are a first-time customer or a long-standing corporate client, we look forward to hearing from you. Call +91 93220 99980 today and experience the AP Travel difference.</p>
"""),
        ],
    },
    {
        "slug": "fleet",
        "title": "Our Fleet | Luxury Buses & Coaches Mumbai | AP Travel & Rental",
        "description": "Explore AP Travel & Rental fleet — KGN Luxury AC Bus, KGN Executive Bus, Blue Star Executive Coach. Premium AC coaches in Mumbai.",
        "h1": "Our Luxury Fleet in Mumbai",
        "hero_p": "Three premium AC coaches — KGN Luxury Bus, KGN Executive Bus, and Blue Star Executive Coach — maintained to showroom standards for every trip.",
        "schema_type": "ItemList",
        "schema_name": "AP Travel Fleet",
        "keywords": "bus fleet Mumbai, KGN bus, Blue Star coach, luxury AC bus Mumbai",
        "sections": [
            ("KGN Luxury AC Bus", """
<p>Our flagship KGN Luxury AC Bus features a distinctive blue exterior and seats up to 45 passengers in premium pushback seats. Fully air-conditioned with an onboard music system, this coach is ideal for large corporate groups, tourism packages, and outstation tours where comfort over long distances matters.</p>
<p>Features include premium pushback seats, full air conditioning, onboard music system, spacious interior, and ample overhead storage. Sanitized before every trip with professional driver in formal attire.</p>
"""),
            ("KGN Executive Bus", """
<p>The KGN Executive Bus stands out with its yellow exterior and luxury interior finish. Seating up to 40 passengers, it is the preferred choice for wedding guest transportation — offering comfortable spacious seating, generous luggage compartments for gifts and garments, and a smooth ride between venues.</p>
<p>Popular for weddings, outstation family trips, and mid-size corporate groups who want a premium experience without needing the full 45-seater capacity.</p>
"""),
            ("Blue Star Executive Coach", """
<p>Built on the Eicher Skyline Pro chassis, the Blue Star Executive Coach represents the pinnacle of our fleet. With pushback recline seats, individual headrests, reading lights, curtained windows, and a smooth highway ride, it is designed for executive corporate travel and premium outstation tours.</p>
<p>The white exterior coach accommodates up to 45 passengers and includes a driver cabin with sanitization kit. Ideal for long-distance routes like Mumbai to Goa, Mumbai to Pune expressway trips, and multi-day corporate offsites.</p>
"""),
            ("Fleet Maintenance & Safety", """
<p>Every vehicle in our fleet undergoes regular mechanical inspection, interior cleaning, and sanitization before each departure. Our drivers are experienced professionals with route knowledge across Mumbai and India's highway network.</p>
<p>We maintain comprehensive insurance and follow strict safety protocols for passenger and cargo transport.</p>
"""),
            ("Book a Coach from Our Fleet", """
<p>Ready to book? Call +91 93220 99980 or visit our <a href="/contact/">contact page</a>. Explore our services: <a href="/">bus rental</a>, <a href="/corporate-bus-rental-mumbai/">corporate transport</a>, <a href="/wedding-bus-rental-mumbai/">wedding buses</a>, and <a href="/outstation-bus-rental-mumbai/">outstation trips</a>.</p>
"""),
        ],
    },
]


EXTRA_SECTIONS = [
    ("Frequently Asked Questions", """
<p><strong>What areas of Mumbai do you serve for bus rental?</strong> We serve all Mumbai areas including South Mumbai, Bandra, Andheri, Powai, Goregaon, Malad, Borivali, Thane, Navi Mumbai, BKC, and the extended Mumbai Metropolitan Region. Pickup from Mumbai airport, CST, and major railway stations is available on request.</p>
<p><strong>How far in advance should I book a bus in Mumbai?</strong> We recommend booking at least 1–2 weeks in advance for corporate and outstation trips, and 2–4 weeks during wedding season (November–February). Last-minute bookings are accommodated based on fleet availability — call us anytime at +91 93220 99980.</p>
<p><strong>Are your buses sanitized before every trip?</strong> Yes, every coach in our fleet is cleaned and sanitized before departure. Our drivers carry sanitization kits and maintain hygiene standards for passenger safety and comfort.</p>
<p><strong>Do you provide drivers with the bus rental?</strong> Yes, all our bus rentals include an experienced, professional driver. Our drivers know Mumbai routes and India's highway network, dress appropriately for corporate and wedding events, and maintain punctual schedules.</p>
<p><strong>Can I also book cargo transport with AP Travel?</strong> Yes, AP Travel &amp; Rental also provides <a href="/cargo/">cargo and logistics services</a> for businesses and individuals. Visit our cargo page or call us for freight, FTL, PTL, and parcel delivery across India.</p>
"""),
    ("Mumbai Transport & Logistics Hub", """
<p>Mumbai's position as India's financial capital makes it one of the busiest transport hubs in the country. From corporate parks in Bandra Kurla Complex and Andheri East to wedding venues in Juhu and Navi Mumbai, the demand for reliable group transport is constant throughout the year. AP Travel &amp; Rental has built its reputation by consistently delivering on-time, comfortable, and professionally managed bus rental services across this diverse and demanding market.</p>
<p>Our Sion headquarters provides strategic access to the Eastern Express Highway, Sion-Chembur Road, and the Mumbai suburban network — enabling efficient dispatch for both local city transfers and long outstation journeys. Whether your group departs from a hotel in Colaba, an office in Powai, or a wedding venue in Thane, our drivers arrive prepared with route knowledge and vehicle readiness.</p>
<p>Beyond passenger transport, Mumbai's commercial activity drives significant demand for cargo and logistics services. Our integrated transport offering — combining premium bus rental with domestic freight and commercial logistics — makes AP Travel a one-stop mobility partner for Mumbai businesses and families.</p>
<p>Explore our complete service range: <a href="/corporate-bus-rental-mumbai/">corporate bus rental</a>, <a href="/wedding-bus-rental-mumbai/">wedding transport</a>, <a href="/outstation-bus-rental-mumbai/">outstation trips</a>, <a href="/tempo-traveller-rental-mumbai/">tempo traveller rental</a>, <a href="/cargo/">cargo logistics</a>, and our full <a href="/fleet/">luxury fleet</a>.</p>
"""),
    ("Safety, Comfort & Professional Standards", """
<p>At AP Travel &amp; Rental, safety is non-negotiable. Every vehicle undergoes regular mechanical inspection, tyre checks, brake testing, and interior maintenance. Our drivers are selected for their experience, route knowledge, and professional conduct — essential qualities for navigating Mumbai's traffic and India's diverse highway conditions.</p>
<p>Comfort features across our fleet include fully air-conditioned cabins, pushback reclining seats, onboard music systems, ample luggage space, and clean interiors with curtained windows on executive coaches. For long outstation journeys, these features transform hours on the road into a relaxed group travel experience.</p>
<p>Our commitment to transparent pricing means you receive a detailed quote before booking — covering vehicle charges, driver allowance, tolls, and any applicable parking or state border fees. No surprise charges on the day of travel. This honesty has earned us a 4.8-star Google rating from over 126 customer reviews.</p>
<p>Contact our team today at +91 93220 99980 or +91 97699 01140. Visit our <a href="/about/">about page</a> to learn more about our company history, or head to our <a href="/contact/">contact page</a> to submit a detailed enquiry. We look forward to serving your transport needs in Mumbai and beyond.</p>
"""),
    ("Our Customer Commitment", """
<p>Every enquiry at AP Travel &amp; Rental receives personal attention from our booking team — not an automated response. We take time to understand your trip requirements, recommend the most suitable vehicle from our fleet, and provide a detailed quote with all costs clearly listed. This customer-first approach has built lasting relationships with corporate clients, wedding planners, tour operators, and families across Mumbai.</p>
<p>We continuously invest in fleet maintenance, driver training, and service quality to ensure every journey — whether a short city transfer or a multi-day outstation tour — meets the high standards our customers expect. Your satisfaction and safety are our top priorities on every trip we operate.</p>
"""),
]


def fix_hrefs(html, prefix):
    """Rewrite root-absolute hrefs for subdirectory pages."""
    for path in (
        "", "bus-rental-mumbai/", "corporate-bus-rental-mumbai/",
        "wedding-bus-rental-mumbai/", "outstation-bus-rental-mumbai/",
        "tempo-traveller-rental-mumbai/", "cargo-service-mumbai/",
        "about/", "contact/", "fleet/", "cargo/",
    ):
        target = f"{prefix}{path}" if path else f"{prefix}index.html"
        html = html.replace(f'href="/{path}"', f'href="{target}"')
        html = html.replace(f"href='/{path}'", f"href='{target}'")
    html = html.replace('href="/#', f'href="{prefix}index.html#')
    return html


def faq_schema(items):
    entities = []
    for q, a in items:
        entities.append(
            '{"@type":"Question","name":'
            + json.dumps(q)
            + ',"acceptedAnswer":{"@type":"Answer","text":'
            + json.dumps(a)
            + "}}"
        )
    return (
        '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
        + ",".join(entities)
        + "]}"
    )


DEFAULT_FAQ = [
    (
        "What areas of Mumbai do you serve?",
        "We serve all Mumbai areas including South Mumbai, Bandra, Andheri, Powai, Thane, Navi Mumbai, BKC, and the extended Mumbai Metropolitan Region.",
    ),
    (
        "How do I book with AP Travel & Rental?",
        "Call +91 93220 99980 or +91 97699 01140, WhatsApp us, or submit an enquiry through our contact page. Our team responds quickly with quotes and availability.",
    ),
    (
        "Does AP Travel also offer cargo and logistics services?",
        "Yes. AP Travel & Rental provides cargo and logistics services including domestic freight, FTL, PTL, and parcel delivery across India from our Mumbai headquarters.",
    ),
]


NAV_ACTIVE = {
    "bus-rental-mumbai": "bus",
    "corporate-bus-rental-mumbai": "corporate",
    "wedding-bus-rental-mumbai": "wedding",
    "outstation-bus-rental-mumbai": "outstation",
    "tempo-traveller-rental-mumbai": "tempo",
    "cargo-service-mumbai": "cargo-mumbai",
    "about": "about",
    "contact": "contact",
    "fleet": "fleet",
}


def nav_bar(prefix, active=None):
    links = [
        ("Home", f"{prefix}index.html", "home"),
        ("Fleet", f"{prefix}fleet/", "fleet"),
        ("Bus Rental", f"{prefix}bus-rental-mumbai/", "bus"),
        ("Corporate", f"{prefix}corporate-bus-rental-mumbai/", "corporate"),
        ("Wedding", f"{prefix}wedding-bus-rental-mumbai/", "wedding"),
        ("Outstation", f"{prefix}outstation-bus-rental-mumbai/", "outstation"),
        ("Tempo", f"{prefix}tempo-traveller-rental-mumbai/", "tempo"),
        ("Cargo", f"{prefix}cargo/", "cargo"),
        ("About", f"{prefix}about/", "about"),
        ("Contact", f"{prefix}contact/", "contact"),
    ]
    links_html = ""
    for label, href, key in links:
        cls = ' class="active"' if active == key else ""
        links_html += f'      <a href="{href}"{cls}>{label}</a>\n'
    return f'''<div class="mobile-topbar" role="complementary" aria-label="Quick call numbers">
  <a href="tel:+919322099980">📞 93220 99980</a>
  <a href="tel:+919769901140">📞 97699 01140</a>
</div>
<header class="nav-bar" id="navBar">
  <div class="nav-bar-inner">
    <a href="{prefix}index.html" class="nav-brand" aria-label="AP Travel and Rental home">
      <span class="rail-mark">AP</span>
      <span class="nav-brand-text">Travel &amp; Rental<small>Mumbai</small></span>
    </a>
    <nav class="nav-links" id="navLinks" aria-label="Main navigation">
{links_html}    </nav>
    <a href="tel:+919322099980" class="nav-call btn btn-gold-sm">Call Now</a>
    <button class="nav-toggle" id="navToggle" type="button" aria-label="Open navigation menu" aria-expanded="false" aria-controls="navLinks">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>'''


def render_page(p):
    slug = p["slug"]
    prefix = "../"
    url = f"{DOMAIN}/{slug}/"
    breadcrumb = f'<a href="{prefix}index.html">Home</a> <span aria-hidden="true">›</span> <span>{p["h1"]}</span>'

    content_html = ""
    all_sections = list(p["sections"]) + EXTRA_SECTIONS
    for i, (heading, body) in enumerate(all_sections, 1):
        content_html += f"<h2>{heading}</h2>\n{body.strip()}\n"
    content_html = fix_hrefs(content_html, prefix)

    word_count = len(" ".join(re.sub(r"<[^>]+>", " ", content_html).split()).split())
    # Add sidebar CTA to boost content
    content_html += f"""
<div class="seo-sidebar-cta">
  <h3>Book with AP Travel &amp; Rental</h3>
  <p>Call <a href="tel:+919322099980">+91 93220 99980</a> or <a href="{prefix}contact/">contact us online</a> for a free quote. Premium service from Sion, Mumbai.</p>
  <a href="tel:+919322099980" class="btn btn-gold-sm">Call Now</a>
</div>
{INTERNAL_LINKS.replace('href="/', f'href="{prefix}').replace('href="/cargo/', f'href="{prefix}cargo/').replace('href="/index.html', f'href="{prefix}index.html')}

"""

    faq_items = p.get("faq", DEFAULT_FAQ)
    faq_ld = faq_schema(faq_items)

    webpage_schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "WebPage",
        "@id": url,
        "url": url,
        "name": p["title"],
        "description": p["description"],
        "isPartOf": {"@id": f"{DOMAIN}/#website"},
        "about": {"@type": "LocalBusiness", "name": "AP Travel & Rental"},
        "inLanguage": "en-IN",
    })

    schema_obj = {
        "@context": "https://schema.org",
        "@type": p["schema_type"],
        "name": p["schema_name"],
        "description": p["description"],
        "url": url,
        "provider": {
            "@type": "LocalBusiness",
            "name": "AP Travel & Rental",
            "telephone": "+91-9322099980",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Vrindavan, Sion-Chembur Road, Chunabhatti",
                "addressLocality": "Sion",
                "addressRegion": "Maharashtra",
                "postalCode": "400022",
                "addressCountry": "IN",
            },
        },
    }
    if p["schema_type"] == "Service":
        schema_obj["areaServed"] = {"@type": "City", "name": "Mumbai"}
        schema_obj["serviceType"] = p["schema_name"]
    schema = json.dumps(schema_obj)

    breadcrumb_schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{DOMAIN}/"},
            {"@type": "ListItem", "position": 2, "name": p["h1"], "item": url},
        ],
    })

    extra_schema = ""
    if slug == "fleet":
        extra_schema = f'<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@type": "ItemList", "name": "AP Travel Luxury Bus Fleet", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "KGN Luxury AC Bus", "description": "45-seater premium AC coach"}, {"@type": "ListItem", "position": 2, "name": "KGN Executive Bus", "description": "40-seater wedding and outstation coach"}, {"@type": "ListItem", "position": 3, "name": "Blue Star Executive Coach", "description": "45-seater Eicher Skyline Pro executive coach"}]})}</script>\n'

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="description" content="{p['description']}">
<meta name="keywords" content="{p['keywords']}">
<meta name="author" content="AP Travel &amp; Rental">
<meta name="publisher" content="AP Travel &amp; Rental">
<title>{p['title']}</title>
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta name="google-site-verification" content="YOUR_GOOGLE_VERIFICATION_CODE">
<meta name="msvalidate.01" content="YOUR_BING_VERIFICATION_CODE">
<meta name="geo.region" content="IN-MH">
<meta name="geo.placename" content="Sion, Mumbai">
<meta property="og:type" content="website">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['description']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/images/blue-star.webp">
<meta property="og:image:alt" content="{p['h1']} — AP Travel and Rental Mumbai">
<meta property="og:locale" content="en_IN">
<meta property="og:site_name" content="AP Travel &amp; Rental">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{p['title']}">
<meta name="twitter:description" content="{p['description']}">
<meta name="twitter:image" content="{DOMAIN}/images/blue-star.webp">
<meta name="theme-color" content="#0B2545">
<link rel="icon" type="image/x-icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='75' font-size='75' font-weight='bold' fill='%230B2545'>AP</text></svg>">
<link rel="manifest" href="{prefix}manifest.json">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Source+Sans+3:wght@400;500;600;700&display=swap">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<link rel="stylesheet" href="{prefix}styles.css">
<script type="application/ld+json">{schema}</script>
<script type="application/ld+json">{breadcrumb_schema}</script>
<script type="application/ld+json">{webpage_schema}</script>
<script type="application/ld+json">{faq_ld}</script>
{extra_schema}</head>
<body class="has-nav no-rail">
<a href="#main-content" class="skip-link">Skip to main content</a>
{nav_bar(prefix, NAV_ACTIVE.get(slug))}
<main id="main-content" class="page">
  <section class="seo-hero">
    <picture>
      <source srcset="{prefix}images/blue-star.webp" type="image/webp">
      <img src="{prefix}images/blue-star.png" alt="{p['h1']} — AP Travel and Rental Mumbai" class="seo-hero-bg" width="1200" height="1500" fetchpriority="high" decoding="async">
    </picture>
    <div class="seo-hero-scrim"></div>
    <div class="seo-hero-content">
      <nav class="breadcrumb-nav" aria-label="Breadcrumb">{breadcrumb}</nav>
      <h1>{p['h1']}</h1>
      <p>{p['hero_p']}</p>
      <div class="hero-actions" style="margin-top:1.4rem">
        <a href="tel:+919322099980" class="btn btn-gold">Call Now</a>
        <a href="{prefix}contact/" class="btn btn-outline">Contact Us</a>
      </div>
    </div>
  </section>
  <article class="seo-content">
{content_html}
  </article>
</main>
<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-brand"><span class="rail-mark">AP</span><span class="brand-text">Travel &amp; Rental</span><p>Premium bus rental and cargo logistics in Mumbai.</p></div>
    <div class="footer-links"><h4>Services</h4><a href="{prefix}bus-rental-mumbai/">Bus Rental</a><a href="{prefix}corporate-bus-rental-mumbai/">Corporate</a><a href="{prefix}wedding-bus-rental-mumbai/">Wedding</a><a href="{prefix}outstation-bus-rental-mumbai/">Outstation</a><a href="{prefix}tempo-traveller-rental-mumbai/">Tempo Traveller</a><a href="{prefix}cargo/">Cargo Service</a><a href="{prefix}cargo-service-mumbai/">Cargo Mumbai</a><a href="{prefix}fleet/">Fleet</a><a href="{prefix}about/">About</a><a href="{prefix}contact/">Contact</a></div>
    <div class="footer-contact"><h4>Contact</h4><p><a href="tel:+919322099980">+91 93220 99980</a></p><p>Sion, Mumbai – 400022</p></div>
  </div>
  <div class="footer-bottom"><p>© <span id="year"></span> AP Travel &amp; Rental. All rights reserved.</p></div>
</footer>
<a href="https://wa.me/919322099980" class="float-btn whatsapp-btn" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp AP Travel"><svg viewBox="0 0 32 32" width="26" height="26" aria-hidden="true"><path fill="#fff" d="M16 3C9 3 3.3 8.6 3.3 15.5c0 2.5.7 4.8 1.9 6.8L3 29l6.9-2.1c1.9 1 4 1.6 6.1 1.6 7 0 12.7-5.6 12.7-12.5S23 3 16 3zm0 22.7c-1.9 0-3.7-.5-5.3-1.4l-.4-.2-4.1 1.2 1.2-3.9-.3-.4c-1.1-1.7-1.7-3.6-1.7-5.6 0-5.7 4.7-10.3 10.6-10.3s10.6 4.6 10.6 10.3S21.9 25.7 16 25.7zm5.8-7.7c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.3-.2-.3 0-.5.1-.7.1-.1.3-.4.5-.5.2-.2.2-.3.3-.5.1-.2 0-.4 0-.6 0-.2-.7-1.8-1-2.4-.3-.7-.5-.6-.7-.6h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.2 3.4 5.3 4.7.7.3 1.3.5 1.8.6.7.2 1.4.2 1.9.1.6-.1 1.9-.8 2.1-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg></a>
<script src="{prefix}script.js" defer></script>
</body>
</html>'''
    return html, word_count


def main():
    for p in PAGES:
        out_dir = os.path.join(BASE, p["slug"])
        os.makedirs(out_dir, exist_ok=True)
        html, wc = render_page(p)
        path = os.path.join(out_dir, "index.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Created {p['slug']}/index.html (~{wc} words in sections)")


if __name__ == "__main__":
    main()
