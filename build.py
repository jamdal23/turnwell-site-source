#!/usr/bin/env python3
"""Turnwell rebuild - static site generator."""
import os
import re

OUT = os.path.dirname(os.path.abspath(__file__))
BASE = "/"  # production: site lives at domain root

HEADER = """<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="/"><img src="/assets/img/turnwell-logo-rev.png" alt="Turnwell"></a>
    <button class="menu-toggle" aria-label="Menu">&#9776;</button>
    <nav class="main-nav">
      <a href="/">Home</a>
      <a href="/about/">About</a>
      <a href="/services/">Services</a>
      <div class="nav-drop">
        <button type="button">Products &#9662;</button>
        <div class="drop-menu">
          <a href="/products/optical-turnstiles/">Optical Turnstiles</a>
          <a href="/products/data-center-high-security/">Data Center & High Security</a>
          <a href="/products/full-height-turnstiles/">Full-Height Turnstiles</a>
          <a href="/products/waist-high-turnstiles/">Waist-High Turnstiles</a>
          <a href="/products/pedestrian-gates/">Pedestrian Gates</a>
          <a href="/products/specialty/">Specialty</a>
        </div>
      </div>
      <a href="/gallery/">Gallery</a>
      <a href="/contact/">Contact</a>
      <a class="header-phone" href="tel:+18447418241">844-741-8241</a>
    </nav>
  </div>
</header>"""

FOOTER = """<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="/assets/img/turnwell-logo-rev.png" alt="Turnwell">
        <p>Turnwell is a licensed General Contractor specializing in the installation of turnstiles, revolving doors, interlocks, and fencing.</p>
      </div>
      <div>
        <h4>Products</h4>
        <ul class="footer-links">
          <li><a href="/products/optical-turnstiles/">Optical Turnstiles</a></li>
          <li><a href="/products/data-center-high-security/">Data Center & High Security</a></li>
          <li><a href="/products/full-height-turnstiles/">Full-Height Turnstiles</a></li>
          <li><a href="/products/waist-high-turnstiles/">Waist-High Turnstiles</a></li>
          <li><a href="/products/pedestrian-gates/">Pedestrian Gates</a></li>
          <li><a href="/products/specialty/">Specialty</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact Us</h4>
        <ul class="footer-links">
          <li>Wake Forest, NC</li>
          <li><a href="tel:+18447418241">844-741-8241</a></li>
          <li><a href="mailto:info@turnwellusa.com">info@turnwellusa.com</a></li>
          <li><a href="https://www.linkedin.com/company/79628003/" target="_blank" rel="noopener">LinkedIn</a></li>
          <li><a href="/contact/">Request a Consultation</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Turnwell, LLC &mdash; All Rights Reserved</span>
      <span>Turnkey entry-control experts</span>
    </div>
  </div>
</footer>
<script src="/assets/js/main.js"></script>"""

CTA_BAND = """<section class="section">
  <div class="wrap">
    <div class="cta-band">
      <div>
        <h2>Make sure your project turns out right with Turnwell.</h2>
        <p>Tell us about your project &mdash; we&rsquo;ll recommend the right entry-control solution.</p>
      </div>
      <a class="btn btn-ghost" href="/contact/">Request a Free Consultation</a>
    </div>
  </div>
</section>"""

CONSULT_FORM = """<section class="section section-soft">
  <div class="wrap">
    <div class="grid-2">
      <div>
        <div class="eyebrow">Get in touch</div>
        <h2 class="section-title">Request a Free Consultation</h2>
        <p class="section-sub">Have a question? Send the form and we&rsquo;ll be in touch. Turnwell respects your privacy and never sells or shares your information.</p>
        <p style="font-size:18px"><strong>Prefer to talk?</strong><br>Call us at <a href="tel:+18447418241">844-741-8241</a> or email <a href="mailto:info@turnwellusa.com">info@turnwellusa.com</a>.<br>We have access to many other products that may not be listed on our website.</p>
      </div>
      <div class="form-card">
        <form action="https://formspree.io/f/mrpeazne" method="POST">
          <div class="form-grid">
            <div class="field"><label for="name">Name</label><input id="name" name="name" type="text" required></div>
            <div class="field"><label for="company">Company</label><input id="company" name="company" type="text" required></div>
            <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="text"></div>
            <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required></div>
            <div class="field full"><label for="comments">Comments</label><textarea id="comments" name="comments"></textarea></div>
            <div class="hp" aria-hidden="true"><label>Leave blank<input type="checkbox" name="flytrap" value="true" tabindex="-1" autocomplete="off"></label></div>
          </div>
          <p style="margin-top:18px"><button class="btn btn-primary" type="submit">Send Request</button></p>
        </form>
      </div>
    </div>
  </div>
</section>"""

def page(title, desc, body):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Turnwell</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
<link rel="icon" href="/assets/img/turnwell-logo-rev.png">
</head>
<body>
{HEADER}
<main>
{body}
</main>
{FOOTER}
</body>
</html>"""
    html = re.sub(r'(href|src|data-photos)="/(?!/)', r'\1="', html)
    html = html.replace('|/', '|')
    html = html.replace("<head>", '<head>\n<base href="' + BASE + '">', 1)
    return html

PAGES = {}

# ---------------------------------------------------------------- home
PAGES["index.html"] = page(
"Your Turnkey Experts for Turnstiles, Revolving Doors & More",
"Turnwell LLC — turnkey entry-control experts for turnstiles, revolving doors, interlocks, gates and fencing. Design, installation, and service.",
"""<section class="hero">
  <div class="hero-bg" style="background-image:url('/assets/img/home/home-img-sm.jpg')"></div>
  <div class="hero-inner">
    <span class="hero-kicker">Turnwell, LLC &mdash; Licensed General Contractor</span>
    <h1>Your turnkey experts for turnstiles, revolving doors, and more.</h1>
    <p class="lead">From design and installation to servicing, Turnwell delivers specialized entry-control expertise &mdash; so your project goes smoothly from start to finish.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="/contact/">Request a Free Consultation</a>
      <a class="btn btn-ghost" href="/gallery/">View Our Work</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid-2">
      <div>
        <div class="eyebrow">Comprehensive entry control solutions</div>
        <h2 class="section-title">When it comes to security, don&rsquo;t compromise on quality.</h2>
        <p>Turnwell has sold and installed turnstiles, security revolving doors, and interlocks for universities, the federal government, commercial offices, manufacturing, aviation, and pharmaceutical facilities.</p>
        <p>You get a turnkey experience &mdash; the right product for your needs, installed by trained, experienced professionals, with ongoing service and support.</p>
        <ul class="feature-list">
          <li><span class="check">&#10003;</span> Design, project management, and installation under one roof</li>
          <li><span class="check">&#10003;</span> Specialists in small-to-medium commercial and industrial projects</li>
          <li><span class="check">&#10003;</span> Service and support long after the install is done</li>
        </ul>
      </div>
      <div><img class="rounded-img" src="/assets/img/components/turnkey.jpg" alt="Turnwell turnkey installation"></div>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="wrap">
    <div class="eyebrow">What we do</div>
    <h2 class="section-title">The turnkey experience</h2>
    <p class="section-sub">We&rsquo;ll do as much &mdash; or as little &mdash; as you need. As your general contractor we design and implement the whole project, or we work alongside your preferred vendors. There&rsquo;s more to installation than bolting equipment in place: most jobs need specialized prep work &mdash; demolition, floor and concrete work, fencing, storefront, and access control &mdash; plus adherence to state and local codes.</p>
    <div class="grid-4">
      <div class="card"><div class="card-img"><img src="/assets/img/home/full-height-turnstile.jpg" alt="Full-height turnstiles"></div><div class="card-body"><h3>Full-Height Turnstiles</h3><p>Maximum perimeter security for unmanned entry points.</p><a class="card-link" href="/products/full-height-turnstiles/">Explore &rarr;</a></div></div>
      <div class="card"><div class="card-img"><img src="/assets/img/home/speed-gate.jpg" alt="Optical turnstiles"></div><div class="card-body"><h3>Optical Turnstiles</h3><p>Elegant, high-throughput lanes for lobbies and interiors.</p><a class="card-link" href="/products/optical-turnstiles/">Explore &rarr;</a></div></div>
      <div class="card"><div class="card-img"><img src="/assets/img/home/gate.jpg" alt="Pedestrian gates"></div><div class="card-body"><h3>Pedestrian Gates</h3><p>ADA-compliant passage and flexible pedestrian control.</p><a class="card-link" href="/products/pedestrian-gates/">Explore &rarr;</a></div></div>
      <div class="card"><div class="card-img"><img src="/assets/img/home/revolving-door.jpg" alt="Data center and high security entrances"></div><div class="card-body"><h3>Data Center & High Security</h3><p>Anti-tailgating entrances your auditors can verify.</p><a class="card-link" href="/products/data-center-high-security/">Explore &rarr;</a></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid-2">
      <div>
        <div class="eyebrow">In the field</div>
        <h2 class="section-title">Touch-free entry that keeps things moving</h2>
        <p>See how Turnwell&rsquo;s automated entry system keeps student food services flowing at Olivet Nazarene University.</p>
      </div>
      <div class="video-frame">
        <iframe src="https://player.vimeo.com/video/515824783" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Turnwell entry system at Olivet Nazarene University"></iframe>
      </div>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="wrap">
    <div class="quote-block">
      &ldquo;Working with Turnwell on the Trojan Fitness Center was an excellent experience. Alvarado and Turnwell provided great design team support prior to bid and were an attentive contractor and installer after award. We would definitely recommend Turnwell for pedestrian control solutions.&rdquo;
      <footer>&mdash; Cody Smith, Seay, Seay &amp; Litchfield Architects, PC</footer>
    </div>
    <div class="partner-row" style="margin-top:44px">
      <img src="/assets/img/alvarado-logo.png" alt="Alvarado">
      <img src="/assets/img/dormakaba-provider-logo.png" alt="dormakaba">
    </div>
  </div>
</section>
""" + CTA_BAND + CONSULT_FORM)

# ---------------------------------------------------------------- about
PAGES["about/index.html"] = page(
"About Us",
"Turnwell LLC — a licensed General Contractor specializing in turnstiles, revolving doors, interlocks, gates and fencing. Our story.",
"""<section class="page-hero"><div class="hero-inner wrap">
  <h1>About Us</h1>
  <p>Turnwell is a licensed General Contractor specializing in the installation of turnstiles, revolving doors, interlocks, and fencing.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="eyebrow">Our story</div>
  <h2 class="section-title">In business since 2013</h2>
  <p style="max-width:760px;font-size:17px">Turnwell LLC has been in business since 2013, installing and servicing turnstiles and pedestrian entry systems for clients across the country. What started as a small specialized operation has grown into a trusted partner for universities, corporations, and secure facilities that need their entrances to work &mdash; every time, without exception.</p>
  <p style="max-width:760px;font-size:17px">We handle the full scope: equipment, installation, integration with access control systems, and ongoing service. One contractor, one point of accountability.</p>
</div></section>
""" + CTA_BAND)

# ---------------------------------------------------------------- services
PAGES["services/index.html"] = page(
"Services",
"Turnwell LLC services: general contracting for entry-control projects, revolving door and turnstile service and repair, commercial fencing and canopies, concrete pads and walkways.",
"""<section class="page-hero"><div class="hero-inner wrap">
  <h1>Services</h1>
  <p>From design and installation to servicing &mdash; specialized entry-control expertise for turnstiles, revolving doors, interlocks, gates, and fencing.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="eyebrow">Services offered</div>
  <h2 class="section-title">What we do</h2>
  <p class="section-sub">At Turnwell we pride ourselves on fast, efficient service. Our technicians are trained and ready to solve problems when they arise &mdash; and we&rsquo;ll do it with a smile. Customers love working with us because we always do what we say we&rsquo;re going to do.</p>
  <div class="grid-2">
    <ul class="feature-list">
      <li><span class="check">&#10003;</span> General contracting for small-to-medium projects</li>
      <li><span class="check">&#10003;</span> Revolving door and turnstile service and repair</li>
      <li><span class="check">&#10003;</span> Commercial fencing and canopies</li>
      <li><span class="check">&#10003;</span> Concrete pads and walkways</li>
    </ul>
    <div><img class="rounded-img" src="/assets/img/services-install-1.jpg" alt="Turnwell turnstile installation in progress" style="margin-bottom:20px"><img class="rounded-img" src="/assets/img/services-install-2.jpg" alt="Turnwell technician installing a turnstile"></div>
  </div>
</div></section>
<section class="section section-soft"><div class="wrap">
  <div class="eyebrow">What you can expect</div>
  <h2 class="section-title">The Turnwell standard</h2>
  <ul class="feature-list">
    <li><span class="check">&#10003;</span> Stocked parts for the products we sell</li>
    <li><span class="check">&#10003;</span> Combined 50 years&rsquo; experience in troubleshooting and repair</li>
    <li><span class="check">&#10003;</span> Knowledgeable and friendly technicians</li>
  </ul>
  <p style="margin-top:28px;font-size:18px">Whether your secure entrance equipment needs a tune-up or a full installation, we are the team to handle it. If you don&rsquo;t see what you are looking for, call us at <a href="tel:+18447418241">844-741-8241</a> &mdash; we have access to many other products that may not be listed on our website.</p>
</div></section>
""" + CTA_BAND + CONSULT_FORM)


# ---------------------------------------------------------------- gallery
PAGES["gallery/index.html"] = page(
"Project Gallery",
"Turnwell LLC project gallery — turnstile, speedgate, fencing, and entry-control installations across the country.",
"""<section class="page-hero"><div class="hero-inner wrap">
  <h1>Project Gallery</h1>
  <p>We&rsquo;ve done a lot of work for clients all over the country. Take a look &mdash; for examples of our work, or inspiration for your next project. Click any project to see its photos and videos.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="gallery-grid">
    <div class="g-item" data-title="Axle Logistics" data-loc="Knoxville, TN" data-videos="https://www.youtube.com/embed/vRH105hzCLI" data-photos="/assets/img/gallery/axle-logistics/photo-1.jpg"><div class="g-img"><img src="/assets/img/gallery/axle-logistics/photo-1.jpg" alt="Axle Logistics"></div><div class="g-cap"><span class="loc">Knoxville, TN</span><h3>Axle Logistics</h3><p>New-construction project: installed two sets of Alvarado Argus V60 optical turnstiles in the employee entry &mdash; three lanes in the main entry area and two lanes in the stairwell.</p></div></div>
    <div class="g-item" data-title="Southern Champion Tray" data-loc="Chattanooga, TN" data-videos="https://www.youtube.com/embed/8mhuSY_wIsc|https://www.youtube.com/embed/qSUnI551uvA" data-photos="/assets/img/gallery/southern-champion-tray/photo-1.jpg|/assets/img/gallery/southern-champion-tray/photo-2.jpg|/assets/img/gallery/southern-champion-tray/photo-3.jpg|/assets/img/gallery/southern-champion-tray/photo-4.jpg"><div class="g-img"><img src="/assets/img/gallery/southern-champion-tray/photo-1.jpg" alt="Southern Champion Tray"></div><div class="g-cap"><span class="loc">Chattanooga, TN</span><h3>Southern Champion Tray</h3><p>New-construction project: installed Gunnebo SpeedStile FLs turnstiles with glass partition to create a secure employee entrance.</p></div></div>
    <div class="g-item" data-title="Liberty University" data-loc="Lynchburg, VA" data-videos="https://www.youtube.com/embed/Yd3ecgKpUP8" data-photos="/assets/img/gallery/liberty-reber-thomas/photo-1.jpg|/assets/img/gallery/liberty-reber-thomas/photo-2.jpg|/assets/img/gallery/liberty-reber-thomas/photo-3.jpg|/assets/img/gallery/liberty-reber-thomas/photo-4.jpg|/assets/img/gallery/liberty-reber-thomas/photo-5.jpg|/assets/img/gallery/liberty-reber-thomas/photo-6.jpg"><div class="g-img"><img src="/assets/img/gallery/liberty-reber-thomas/photo-5.jpg" alt="Liberty University Reber-Thomas Dining Hall"></div><div class="g-cap"><span class="loc">Lynchburg, VA</span><h3>Liberty University</h3><p>Two-phase project at the new Reber-Thomas Dining Hall: first installed 8 new Alvarado Argus 40 lanes and relocated the existing turnstiles from the old location; a year later removed the old lanes and added 4 more Argus 40 lanes &mdash; all integrated with the university&rsquo;s Transact campus card system. The phased approach let the university scale throughput as dining demand grew &mdash; no additional staffing required.</p></div></div>
    <div class="g-item" data-title="University of Tennessee" data-loc="Knoxville, TN" data-videos="https://www.youtube.com/embed/d_DXlvcLKC0" data-photos="https://i.ytimg.com/vi/d_DXlvcLKC0/hqdefault.jpg"><div class="g-img"><img src="https://i.ytimg.com/vi/d_DXlvcLKC0/hqdefault.jpg" alt="University of Tennessee dining facility"></div><div class="g-cap"><span class="loc">Knoxville, TN</span><h3>University of Tennessee</h3><p>Installed Alvarado SU5000 barrier optical turnstiles in the new-construction campus dining facility, integrated with the university&rsquo;s CBORD campus card system. Every student is validated on entry, protecting meal-plan revenue without slowing down the line.</p></div></div>
    <div class="g-item" data-title="University of Houston–Downtown" data-loc="Houston, TX" data-videos="https://www.youtube.com/embed/AxROTZ2LuC8" data-photos="/assets/img/gallery/uhd-wellness/photo-1.jpg|/assets/img/gallery/uhd-wellness/photo-2.jpg|/assets/img/gallery/uhd-wellness/photo-3.jpg|/assets/img/gallery/uhd-wellness/photo-4.jpg|/assets/img/gallery/uhd-wellness/photo-5.jpg"><div class="g-img"><img src="/assets/img/gallery/uhd-wellness/photo-3.jpg" alt="University of Houston-Downtown Wellness Center"></div><div class="g-cap"><span class="loc">Houston, TX</span><h3>University of Houston–Downtown</h3><p>Installed Alvarado SU5000 barrier optical turnstiles and a VSG gate at the newly constructed UHD Wellness &amp; Success Center.</p></div></div>
    <div class="g-item" data-title="University of Washington Bothell" data-loc="Bothell, WA" data-videos="https://www.youtube.com/embed/PPcQJhd4LEQ" data-photos="/assets/img/gallery/uw-bothell/photo-1.jpg|/assets/img/gallery/uw-bothell/photo-2.jpg|/assets/img/gallery/uw-bothell/photo-3.jpg|/assets/img/gallery/uw-bothell/photo-4.jpg|/assets/img/gallery/uw-bothell/photo-5.jpg|/assets/img/gallery/uw-bothell/photo-6.jpg"><div class="g-img"><img src="/assets/img/gallery/uw-bothell/photo-1.jpg" alt="University of Washington Bothell"></div><div class="g-cap"><span class="loc">Bothell, WA</span><h3>University of Washington Bothell</h3><p>Installed one entry lane and one exit lane in the campus dining facility using Alvarado Argus 40 turnstiles, integrated with the university&rsquo;s Atrium campus card system &mdash; a modern, high-tech entrance that sets the tone for the dining experience.</p></div></div>
    <div class="g-item" data-title="Western Colorado University" data-loc="Gunnison, CO" data-videos="https://www.youtube.com/embed/4jqsBg7CqYM" data-photos="/assets/img/gallery/western-colorado-university.jpg"><div class="g-img"><img src="/assets/img/gallery/western-colorado-university.jpg" alt="Western Colorado University"></div><div class="g-cap"><span class="loc">Gunnison, CO</span><h3>Western Colorado University</h3><p>Installed two entry lanes and one exit lane in the newly remodeled campus dining facility using Alvarado Argus 40 turnstiles, integrated with the university&rsquo;s Transact campus card system. The lanes keep students moving through at peak meal times without adding front-of-house staff.</p></div></div>
    <div class="g-item" data-title="College of the Holy Cross" data-loc="Worcester, MA" data-videos="https://www.youtube.com/embed/gHdSN36m28M" data-photos="/assets/img/gallery/holy-cross/photo-1.jpg|/assets/img/gallery/holy-cross/photo-2.jpg"><div class="g-img"><img src="/assets/img/gallery/holy-cross/photo-1.jpg" alt="College of the Holy Cross"></div><div class="g-cap"><span class="loc">Worcester, MA</span><h3>College of the Holy Cross</h3><p>Added a single Alvarado Argus 40 lane to the existing dining facility, tied into the college&rsquo;s Atrium campus card system. With its low profile and clean lines, the Argus 40 blends seamlessly into the surrounding space &mdash; security that doesn&rsquo;t look like security.</p></div></div>
    <div class="g-item" data-title="Amazon" data-loc="Raleigh, NC" data-videos="" data-photos="/assets/img/gallery/amazon/photo-1.jpg|/assets/img/gallery/amazon/photo-2.jpg|/assets/img/gallery/amazon/photo-3.jpg|/assets/img/gallery/amazon/photo-4.jpg|/assets/img/gallery/amazon/photo-5.jpg|/assets/img/gallery/amazon/photo-6.jpg|/assets/img/gallery/amazon/photo-7.jpg|/assets/img/gallery/amazon/photo-8.jpg|/assets/img/gallery/amazon/photo-9.jpg"><div class="g-img"><img src="/assets/img/gallery/amazon/main.jpg" alt="Amazon distribution center"></div><div class="g-cap"><span class="loc">Raleigh, NC</span><h3>Amazon</h3><p>Installed a ten-lane array of Boon-Edam Lifeline Swing series in the main lobby of the brand-new distribution center.</p></div></div>
    <div class="g-item" data-title="CMC Steel" data-loc="Birmingham, AL" data-videos="" data-photos="/assets/img/gallery/cmc/photo-1.jpg"><div class="g-img"><img src="/assets/img/gallery/cmc/main.jpg" alt="CMC Steel"></div><div class="g-cap"><span class="loc">Birmingham, AL</span><h3>CMC Steel</h3><p>Provided General Contracting services to secure the employee entrance with an Alvarado full-height tandem turnstile (MSTT), canopy, and decorative aluminum picket fencing.</p></div></div>
    <div class="g-item" data-title="Olivet Nazarene University" data-loc="Bourbonnais, IL" data-videos="" data-photos="/assets/img/gallery/olivette/photo-1.jpg|/assets/img/gallery/olivette/photo-2.jpg|/assets/img/gallery/olivette/photo-3.jpg|/assets/img/gallery/olivette/photo-4.jpg"><div class="g-img"><img src="/assets/img/gallery/olivette/main.jpg" alt="Olivet Nazarene University"></div><div class="g-cap"><span class="loc">Bourbonnais, IL</span><h3>Olivet Nazarene University</h3><p>Furnished the newly renovated cafeteria with sleek dormakaba HSB-E04 barrier optical speedgates, integrated with the university&rsquo;s Blackboard system.</p></div></div>
    <div class="g-item" data-title="Sumter Packaging" data-loc="Charleston, SC" data-videos="" data-photos="/assets/img/gallery/sumpter/photo-1.jpg|/assets/img/gallery/sumpter/photo-2.jpg|/assets/img/gallery/sumpter/photo-3.jpg|/assets/img/gallery/sumpter/photo-4.jpg|/assets/img/gallery/sumpter/photo-5.jpg|/assets/img/gallery/sumpter/photo-6.jpg"><div class="g-img"><img src="/assets/img/gallery/sumpter/main.jpg" alt="Sumter Packaging"></div><div class="g-cap"><span class="loc">Charleston, SC</span><h3>Sumter Packaging</h3><p>Updated the distribution warehouse with 14 ft custom green steel picket fencing with expanded metal infill, plus a safety-yellow Alvarado MST full-height turnstile.</p></div></div>
    <div class="g-item" data-title="Tennessee Tech University" data-loc="Cookeville, TN" data-videos="" data-photos="/assets/img/gallery/ttu/photo-1.jpg|/assets/img/gallery/ttu/photo-2.jpg|/assets/img/gallery/ttu/photo-3.jpg|/assets/img/gallery/ttu/photo-4.jpg|/assets/img/gallery/ttu/photo-5.jpg|/assets/img/gallery/ttu/photo-6.jpg|/assets/img/gallery/ttu/photo-7.jpg"><div class="g-img"><img src="/assets/img/gallery/ttu/main.jpg" alt="Tennessee Tech University"></div><div class="g-cap"><span class="loc">Cookeville, TN</span><h3>Tennessee Tech University</h3><p>Furnished and installed electric gates in the brand-new student recreation center to limit access and control pedestrian traffic.</p></div></div>
    <div class="g-item" data-title="UNC Charlotte" data-loc="Charlotte, NC" data-videos="" data-photos="/assets/img/gallery/unc/photo-1.jpg|/assets/img/gallery/unc/photo-2.jpg|/assets/img/gallery/unc/photo-3.jpg|/assets/img/gallery/unc/photo-4.jpg|/assets/img/gallery/unc/photo-5.jpg"><div class="g-img"><img src="/assets/img/gallery/unc/main.jpg" alt="UNC Charlotte"></div><div class="g-cap"><span class="loc">Charlotte, NC</span><h3>UNC Charlotte</h3><p>Provided the university with Alvarado SU5000 and SU1000 turnstiles and gates featuring their custom logo etched into the clear barrier.</p></div></div>
    <div class="g-item" data-title="Wegmann Automotive" data-loc="Murfreesboro, TN" data-videos="" data-photos="/assets/img/gallery/wegmann/photo-1.jpg|/assets/img/gallery/wegmann/photo-2.jpg|/assets/img/gallery/wegmann/photo-3.jpg|/assets/img/gallery/wegmann/photo-4.jpg|/assets/img/gallery/wegmann/photo-5.jpg|/assets/img/gallery/wegmann/photo-6.jpg"><div class="g-img"><img src="/assets/img/gallery/wegmann/main.jpg" alt="Wegmann Automotive"></div><div class="g-cap"><span class="loc">Murfreesboro, TN</span><h3>Wegmann Automotive</h3><p>General Contracting services to upgrade the employee entrance: dormakaba FTS-E02 full-height turnstiles, black vinyl chain-link fencing, new canopy, concrete pad, and ADA/delivery gates.</p></div></div>
  </div>
  <div class="yt-follow">
    <a class="btn btn-youtube" href="https://www.youtube.com/@turnwellllc4160" target="_blank" rel="noopener">Follow us on YouTube</a>
  </div>
</div></section>
<div class="pmodal" id="pmodal" aria-hidden="true">
  <div class="pmodal-backdrop" id="pmBack"></div>
  <div class="pmodal-box" role="dialog" aria-modal="true">
    <button class="pmodal-close" id="pmClose" aria-label="Close">&times;</button>
    <h3 id="pmTitle"></h3>
    <p class="pmodal-loc" id="pmLoc"></p>
    <div class="pmodal-videos" id="pmVideos"></div>
    <div class="pmodal-viewer">
      <img id="pmImg" src="" alt="">
      <button class="pmodal-arrow pmodal-prev" id="pmPrev" aria-label="Previous photo">&#10094;</button>
      <button class="pmodal-arrow pmodal-next" id="pmNext" aria-label="Next photo">&#10095;</button>
    </div>
    <div class="pmodal-meta"><span id="pmCount"></span></div>
    <div class="pmodal-thumbs" id="pmThumbs"></div>
  </div>
</div>
<script>
(function(){
  var modal=document.getElementById('pmodal'),
      title=document.getElementById('pmTitle'),
      loc=document.getElementById('pmLoc'),
      videos=document.getElementById('pmVideos'),
      img=document.getElementById('pmImg'),
      count=document.getElementById('pmCount'),
      thumbs=document.getElementById('pmThumbs'),
      photos=[],idx=0;
  function render(){
    img.src=photos[idx];
    count.textContent=photos.length>1?((idx+1)+' of '+photos.length):'';
    document.getElementById('pmPrev').style.display=photos.length>1?'':'none';
    document.getElementById('pmNext').style.display=photos.length>1?'':'none';
    thumbs.innerHTML='';
    if(photos.length>1){photos.forEach(function(p,i){
      var t=document.createElement('img');t.src=p;t.alt='Thumbnail '+(i+1);
      if(i===idx)t.className='active';
      t.addEventListener('click',function(){idx=i;render();});
      thumbs.appendChild(t);
    });}
  }
  function open(item){
    title.textContent=item.getAttribute('data-title');
    loc.textContent=item.getAttribute('data-loc');
    var vs=item.getAttribute('data-videos');
    videos.innerHTML='';
    if(vs){vs.split('|').forEach(function(u){
      var w=document.createElement('div');w.className='video-wrap';
      var f=document.createElement('iframe');
      f.src=u;f.title=title.textContent+' video';f.frameBorder='0';
      f.allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
      f.allowFullscreen=true;w.appendChild(f);videos.appendChild(w);
    });}
    photos=item.getAttribute('data-photos').split('|');
    idx=0;render();
    modal.classList.add('open');modal.setAttribute('aria-hidden','false');
    document.body.style.overflow='hidden';
  }
  function close(){
    modal.classList.remove('open');modal.setAttribute('aria-hidden','true');
    document.body.style.overflow='';videos.innerHTML='';
  }
  document.querySelectorAll('.g-item[data-photos]').forEach(function(item){
    item.style.cursor='pointer';
    item.addEventListener('click',function(){open(item);});
  });
  document.getElementById('pmClose').addEventListener('click',close);
  document.getElementById('pmBack').addEventListener('click',close);
  document.getElementById('pmPrev').addEventListener('click',function(e){e.stopPropagation();idx=(idx-1+photos.length)%photos.length;render();});
  document.getElementById('pmNext').addEventListener('click',function(e){e.stopPropagation();idx=(idx+1)%photos.length;render();});
  document.addEventListener('keydown',function(e){
    if(!modal.classList.contains('open'))return;
    if(e.key==='Escape')close();
    if(e.key==='ArrowLeft'&&photos.length>1){idx=(idx-1+photos.length)%photos.length;render();}
    if(e.key==='ArrowRight'&&photos.length>1){idx=(idx+1)%photos.length;render();}
  });
})();
</script>
""" + CTA_BAND)

# ---------------------------------------------------------------- contact
PAGES["contact/index.html"] = page(
"Contact Us",
"Contact Turnwell LLC — request a free consultation for your turnstile, revolving door, or entry-control project. Wake Forest, NC. 844-741-8241.",
"""<section class="page-hero"><div class="hero-inner wrap">
  <h1>Contact Us</h1>
  <p>Turnwell is a licensed General Contractor. We specialize in small-to-medium projects in residential and commercial/industrial applications &mdash; and our project management experience keeps your project on time and on budget.</p>
</div></section>
""" + CONSULT_FORM + """
<section class="section"><div class="wrap">
  <div class="grid-3">
    <div class="card"><div class="card-body"><h3>Call</h3><p><a href="tel:+18447418241">844-741-8241</a></p></div></div>
    <div class="card"><div class="card-body"><h3>Email</h3><p><a href="mailto:info@turnwellusa.com">info@turnwellusa.com</a></p></div></div>
    <div class="card"><div class="card-body"><h3>Visit</h3><p>Wake Forest, NC</p></div></div>
  </div>
</div></section>
""")

# ---------------------------------------------------------------- products
def spec_btns(files):
    out = ['<div class="spec-list">']
    for label, path in files:
        out.append(f'<a class="spec-btn" href="/assets/pdf/{path}" target="_blank" rel="noopener">&#128196; {label}</a>')
    return "\n".join(out) + "</div>"

def product_page(cat_name, cat_url, title, img, desc_paras, features, downloads):
    feats = "\n".join(f'<li><span class="check">&#10003;</span> {f}</li>' for f in features)
    paras = "\n".join(f"<p>{p}</p>" for p in desc_paras)
    body = f"""<section class="page-hero"><div class="hero-inner wrap">
  <p style="margin-bottom:10px"><a href="{cat_url}" style="color:#9fd0f0">&larr; {cat_name}</a></p>
  <h1>{title}</h1>
</div></section>
<section class="section"><div class="wrap">
  <div class="grid-2">
    <div><img class="rounded-img" src="{img}" alt="{title}"></div>
    <div>{paras}</div>
  </div>
  <div style="margin-top:48px">
    <div class="eyebrow">Key features</div>
    <ul class="feature-list">{feats}</ul>
  </div>
  <div style="margin-top:48px">
    <div class="eyebrow">Product downloads</div>
    {spec_btns(downloads)}
  </div>
</div></section>
""" + CTA_BAND
    return body

# ---- category: full-height turnstiles
# ---- category: optical speedgates
# ---- category: gates & swing doors
# ---- category: interlocks & revolving doors
# ================= detail pages =================
PAGES["products/full-height-turnstiles/fts/index.html"] = page(
"FTS Full-Height Turnstiles",
"dormakaba FTS full-height turnstiles — modular design with bicycle gates, ADA swing gates, and canopy options. Spec sheets.",
product_page("Full-Height Turnstiles", "/products/full-height-turnstiles/", "FTS Full-Height Turnstiles",
"/assets/img/products/full-height-turnstiles/fts/main.jpg",
["Our modular FTS system presents multiple design configurations and enhanced security when integrating electronic access control &mdash; allowing secure passage to authorized personnel.",
"Robust full-height turnstiles available with integrated bicycle gates, ADA swing gates, and exclusive custom canopy options. Stainless steel column and bars regardless of finish, with Touch-and-Go drive for smooth operation and long life."],
["End-point locking &mdash; pedestrians are never stuck",
"Double units for areas where space is a concern",
"2-wing rotor for smallest footprint; 3 &amp; 4-wing rotors for higher security",
"Easy connection to fire alarm system",
"Suitable for indoors and outdoors",
"Rotating speed adapts to the pedestrian"],
[("FTS-E01 Spec Sheet", "fts/fts-e01.pdf"),
 ("FTS-E02 Spec Sheet", "fts/fts-e02.pdf"),
 ("FTS-E03 Spec Sheet", "fts/fts-e03.pdf"),
 ("FTS-E04 Spec Sheet", "fts/fts-e04.pdf"),
 ("FTS-E05 Spec Sheet", "fts/fts-e05.pdf"),
 ("FTS-E06 Spec Sheet", "fts/fts-e06.pdf"),
 ("FTS-M02 Spec Sheet", "fts/fts-m02.pdf"),
 ("FTS-M03 Spec Sheet", "fts/fts-m03.pdf")]))

PAGES["products/data-center-high-security/geryon/index.html"] = page(
"Geryon Security Revolving Doors",
"dormakaba Geryon security revolving doors — elegant high-security entry for interiors and entrances.",
product_page("Data Center & High Security", "/products/data-center-high-security/", "Geryon Security Revolving Doors",
"/assets/img/products/interlocks-revolving-doors/geryon/main.jpg",
["Security revolving doors suit both interiors and entrances. Thanks to the high transparency of the glass elements and a wide variety of colors for the metal parts, all models blend elegantly into their surroundings.",
"A sophisticated sensor system &mdash; compliant with the latest standards &mdash; prevents user injury. Depending on security requirements, the door can be equipped with a contact mat, scales, or internal monitoring. Reinforced bullet- and burglar-resistant variants are certified to RC2 and WK3. Options include a rotating unit with emergency-exit function and night closure."],
["End-point locking &mdash; users cannot become stuck",
"Safety sensors per DIN EN 16005",
"RC2 and WK3 resistance classes available",
"All-glass units with underfloor drive",
"Emergency-exit and night-closure options"],
[("Product Brochure", "geryon/geryonsecurityrevolvingdoors.pdf")]))

PAGES["products/data-center-high-security/orthos/index.html"] = page(
"Orthos Personal Interlocks",
"dormakaba Orthos electronically monitored interlocks — maximum security for sensitive building areas.",
product_page("Data Center & High Security", "/products/data-center-high-security/", "Orthos Personal Interlocks",
"/assets/img/products/interlocks-revolving-doors/orthos/main.jpg",
["Orthos electronically monitored security interlocks meet the highest security demands and provide optimal protection for sensitive building areas. The series includes round or rectangular personal interlocks for single passage, and interlocks with a set of doors in a row passable in one direction only.",
"Separation is accomplished by body weight, sensors, or an additional identification checkpoint mid-interlock. Depending on requirements, interlocks can be equipped with contact mats, scales, or internal monitoring &mdash; with bullet- and burglar-resistant variants certified from RC2/WK2 up to WK4."],
["High security via contact mats",
"Optional scales with weight limits",
"Resistance classes RC2/WK2, WK3, up to WK4",
"Round, rectangular, and multi-door configurations",
"Optional wings and folding wings"],
[("PIL Brochure", "orthos-pil-brochure.pdf"),
 ("PIL-M01 Spec Sheet", "orthos/pil-m01.pdf"),
 ("PIL-S01 Spec Sheet", "orthos/pil-s01.pdf")]))

# ----------------------------------------------- new Alvarado lineup (Oct 2026)
PAGES["products/optical-turnstiles/argus/index.html"] = page(
"Argus Optical Turnstiles",
"Alvarado Argus 40/60/80 sensor barriers — glass swinging-barrier optical turnstiles for lobbies that need security without looking like security. Spec sheets and drawings.",
product_page("Optical Turnstiles", "/products/optical-turnstiles/", "Argus 40 / 60 / 80 Sensor Barriers",
"/assets/img/alvarado/argus-1.jpg",
["The Argus line is Alvarado's answer for lobbies where appearance matters as much as access control. These are sensor barriers with clear glass swinging panels &mdash; they read as modern architecture, not security equipment. Three models (40, 60, and 80) cover different lane widths and barrier heights, so you can match the unit to the space instead of forcing the space to fit the unit.",
"Each lane pairs a slim cabinet with an optical sensor array that watches for tailgating and unauthorized passage. When someone presents a valid credential, the glass barrier swings open; if someone tries to follow through behind them, the system flags it. Standard and ADA-width lanes use the same cabinet dimensions, and cabinets can be shared between lanes to build out multi-lane arrays without a forest of pedestals.",
"Turnwell installs Argus lanes in corporate lobbies, elevator banks, and anywhere the front entrance has to impress visitors and still keep unauthorized people out. Finishes and lid colors can be matched to the surrounding interior, and the glass panels can be etched with a logo or left crystal clear."],
["Clear glass swinging barriers in three height options, plus polycarbonate",
"Shared center cabinets build multi-lane arrays with fewer pedestals",
"Same cabinet dimensions for standard and ADA-width lanes",
"LED user guidance lights built into the cabinet",
"Slim cabinets fit lobbies where floor space is tight",
"Multiple cabinet finishes and lid colors to match the interior",
"Optional glass etching and ambient panel lighting",
"Works with new or existing access control systems"],
[("Datasheet", "alvarado/argus-Datasheet-SEC_OPT_Argus_DATA_PDS4612R2-1.pdf"),
 ("Descriptive Specifications", "alvarado/argus-Descriptive-Specifications-SEC_OPT_ARGUS_DESC_PSD4717R2-0.pdf"),
 ("Plan & Elevation Drawings &mdash; Argus 40", "alvarado/argus-Drawings-40-Argus-40-Plan-and-Elevation-Drawings-PDFs.zip"),
 ("Plan & Elevation Drawings &mdash; Argus 60", "alvarado/argus-Drawings-60-Argus-60-Plan-and-Elevation-Drawings-PDFs.zip"),
 ("Plan & Elevation Drawings &mdash; Argus 80", "alvarado/argus-Drawings-80-Argus-80-Plan-and-Elevation-Drawings-PDFs.zip")]))

PAGES["products/optical-turnstiles/argus-v60/index.html"] = page(
"Argus V60 Compact Optical Turnstile",
"Alvarado Argus V60 — a compact optical turnstile with a 9.5-inch cabinet and advanced tailgate detection for tight lobbies. Spec sheets.",
product_page("Optical Turnstiles", "/products/optical-turnstiles/", "Argus V60 Compact Optical Turnstile",
"/assets/img/alvarado/argus-v60-0.jpg",
["The Argus V60 solves a problem we run into a lot: a lobby that needs real optical access control but doesn't have the floor space for full-size lanes. The cabinet is only 9.5 inches deep &mdash; roughly the width of a sheet of paper &mdash; so it fits in elevator lobbies, corridors, and retrofit sites where a standard turnstile lane simply won't go.",
"Small doesn't mean dumbed down. The V60 runs a purpose-built sensor algorithm that can pick up a tailgating attempt from as little as an inch behind the authorized user. Glass swinging barriers, illuminated user guidance, and the same credential-reader compatibility as the larger Argus models all carry over.",
"If you've got a tight entrance and a security requirement, this is usually where the conversation starts. Six standard finishes cover most interiors, and standard and ADA lanes share cabinet dimensions so mixed arrays look uniform."],
["9.5-inch cabinet depth fits tight lobbies, corridors, and retrofits",
"Advanced sensor algorithm detects tailgating attempts within an inch",
"Clear glass swinging barriers",
"Illuminated RFID icon and running lights guide users",
"Standard and ADA lanes use identical cabinet dimensions",
"Six standard finish options",
"Accepts common credential and biometric readers",
"Designed for supervised lobby and elevator-bank applications"],
[("Datasheet", "alvarado/argus-v60-Datasheet-SEC_OPT_Argus_V60_DATA_PDS4894R1-0.pdf"),
 ("Descriptive Specifications", "alvarado/argus-v60-Descriptive-Specifications-SEC_OPT_ARGUS-V60_DESC_PSD4734R1-0.pdf")]))

PAGES["products/optical-turnstiles/su5000/index.html"] = page(
"SU5000 Optical Turnstile",
"Alvarado SU5000 swinging-barrier optical turnstile — slim cabinets, motorized barriers, and high throughput for premium lobbies. Spec sheets and drawings.",
product_page("Optical Turnstiles", "/products/optical-turnstiles/", "SU5000 Swinging-Barrier Optical Turnstile",
"/assets/img/alvarado/su5000-0.png",
["The SU5000 is the workhorse of Alvarado's optical line and one of the most-installed swinging-barrier turnstiles in North America. The headline feature is the cabinet: it's the slimmest in its class, which matters when you're laying out multiple lanes in a lobby and every inch of floor space counts.",
"Operation is straightforward for the user. Present a credential, the motorized barrier swings open away from you, walk through. Behind the scenes, the sensor array watches each passage for tailgating, wrong-way entry, and loitering in the lane. The unit is IP-enabled, so we can push configuration changes and custom audio prompts over the network instead of opening cabinets with a laptop.",
"Three barrier heights cover different security postures, and an optional floor-saver platform means the lanes can be installed without anchoring or trenching &mdash; useful in leased spaces or buildings where you can't core the slab. We've put SU5000s in corporate headquarters, hospitals, and government buildings across the Southeast."],
["Industry's slimmest optical turnstile cabinet saves floor space",
"Motorized swinging barriers open smoothly away from the user",
"Three barrier height options for different security needs",
"Shared center cabinets create clean multi-lane arrays",
"LED user graphics embedded in the cabinet lid",
"IP-enabled: push config and audio updates over the network",
"Optional floor-saver platform &mdash; no anchoring or trenching required",
"Crystal-clear barriers keep sight lines open through the lobby"],
[("Datasheet", "alvarado/su5000-Datasheet-PDS3507R6-0_SEC_OPT_SU5000.pdf"),
 ("Descriptive Specifications", "alvarado/su5000-Descriptive-Specifications-SEC_OPT_SU5000-DESC_PSD3271R4-1.pdf"),
 ("Plan & Elevation Drawings", "alvarado/su5000-Plan-and-Elevation-SEC_OPT_SU5000-STD_DRAW_PDF.zip")]))

PAGES["products/optical-turnstiles/su4500/index.html"] = page(
"SU4500 Compact Optical Turnstile",
"Alvarado SU4500 — the most compact barrier optical turnstile for high-end facilities short on space. Spec sheets and drawings.",
product_page("Optical Turnstiles", "/products/optical-turnstiles/", "SU4500 Compact Optical Turnstile",
"/assets/img/alvarado/su4500-0.png",
["When the lobby is beautiful but small, the SU4500 is the answer. At 38 inches long, it's the most compact barrier-style optical turnstile Alvarado makes &mdash; built for high-end facilities where a full-size lane would eat the entrance.",
"It doesn't give up the important stuff to get small. You still get motorized swinging barriers, the full optical sensor array for tailgate detection, and compatibility with essentially any credential or biometric reader you'd want to mount. Lanes can be ganged with shared center cabinets, and the clear barriers keep the space feeling open.",
"We recommend the SU4500 for boutique offices, upscale residential lobbies, and smaller healthcare or campus buildings where a standard optical lane is overkill but an open doorway isn't an option."],
["38-inch cabinet &mdash; the most compact barrier optical in the line",
"Clear swinging barriers with fixed clear side panels",
"Works with all common credential and biometric readers",
"Shared center cabinets build multi-lane arrays",
"Cabinet finishes and lid colors matched to the interior",
"Optional panel etching and illumination",
"Full tailgate and unauthorized-passage detection",
"Ties into new or existing access control systems"],
[("Descriptive Specifications", "alvarado/su4500-Descriptive-Specifications-SEC_OPT_SU4500_DESC_PSD4364R2-1.pdf"),
 ("Plan & Elevation Drawings", "alvarado/su4500-Plan-and-Elevation-SEC_OPT_SU4500-STD_DRAW-PEF-968_REV-1-1.pdf")]))

PAGES["products/optical-turnstiles/su3000/index.html"] = page(
"SU3000 Drop-Arm Optical Turnstile",
"Alvarado SU3000 drop-arm optical turnstile — slim, stylish optical control with a dropping arm for supervised lobbies. Spec sheets.",
product_page("Optical Turnstiles", "/products/optical-turnstiles/", "SU3000 Drop-Arm Optical Turnstile",
"/assets/img/alvarado/su3000-1.jpg",
["The SU3000 takes a different approach from the swinging-barrier models: instead of glass panels, it uses a slim drop arm. The arm stays up during normal operation and drops out of the way for each authorized passage, then returns. It's a clean look that suits interiors where glass barriers would feel heavy.",
"Under the slim cabinet there's a full optical sensor set watching for tailgating and wrong-way movement, plus the same LED user graphics in the lid you'll find across the SU line. Standard and ADA lanes share cabinet dimensions, and adding one shared cabinet creates an additional lane &mdash; handy when you're expanding an existing array.",
"This is a good fit for corporate lobbies, fitness centers, and amenity spaces that want visible access control without the glass. Like the rest of the line, it integrates with whatever access control system the building already runs."],
["Slim drop-arm design &mdash; a lighter visual alternative to glass barriers",
"Motorized arm drops for each authorized passage",
"Full optical tailgate and wrong-way detection",
"LED user graphics embedded in the cabinet lid",
"Standard and ADA lanes share cabinet dimensions",
"Add lanes with a single shared cabinet",
"Multiple cabinet finishes and lid colors",
"Integrates with new or existing access control systems"],
[("Datasheet", "alvarado/su3000-Datasheet-PDS1035R5-0_SEC_OPT_SU3000_DATA.pdf"),
 ("Descriptive Specifications", "alvarado/su3000-Descriptive-Specifications-PSD1102R4-0_SEC_OPT_SU3000_DESC.pdf")]))

PAGES["products/optical-turnstiles/su2000/index.html"] = page(
"SU2000 Barrier-Free Optical Turnstile",
"Alvarado SU2000 barrier-free optical turnstile — sensor-only passage control for supervised entrances. No barriers, just detection. Spec sheets and drawings.",
product_page("Optical Turnstiles", "/products/optical-turnstiles/", "SU2000 Barrier-Free Optical Turnstile",
"/assets/img/alvarado/su2000-1.jpg",
["Sometimes you don't want a physical barrier &mdash; you want to know who's coming through and stop the ones who shouldn't be there. The SU2000 is a barrier-free optical turnstile: no arms, no glass, just a compact cabinet with sensors that track every passage and flag tailgating, wrong-way entry, and unauthorized presence.",
"It's designed for supervised entrances &mdash; places with a receptionist or guard nearby who can respond when the system raises an alarm. Think office lobbies with a front desk, museums, and corporate campuses where you want throughput to stay high and the entrance to stay open and welcoming.",
"The cabinet is compact enough for tight spots, standard and ADA lanes match, and the lid carries the same intuitive LED graphics as the rest of the SU family so users know exactly what to do."],
["No physical barrier &mdash; sensor-only detection keeps traffic flowing",
"Flags tailgating, wrong-way passage, and unauthorized presence",
"Built for supervised entrances with staff nearby",
"Compact cabinet fits tight lobbies and corridors",
"Standard and handicapped lanes share cabinet dimensions",
"LED user graphics embedded in the lid",
"Multiple cabinet finishes and lid colors",
"High throughput for busy entry points"],
[("Datasheet", "alvarado/su2000-Datasheet-PDS1038R5-0_SEC_OPT_SU2000_DATA.pdf"),
 ("Descriptive Specifications", "alvarado/su2000-Descriptive-Specifications-PSD1540R2-0_SEC_OPT_SU2000_DESC.pdf"),
 ("Plan & Elevation Drawings", "alvarado/su2000-Plan-and-Elevation-SEC_OPT_SU2000-STD_DRAW_PEF-467_REV-B.pdf")]))

# ================= detail pages: waist-high turnstiles =================

PAGES["products/waist-high-turnstiles/edm/index.html"] = page(
"EDM Series Waist-High Turnstile",
"Alvarado EDM motorized waist-high turnstile — smooth, quiet, motor-driven arm rotation for lobbies and interior control points. Spec sheets and drawings.",
product_page("Waist-High Turnstiles", "/products/waist-high-turnstiles/", "EDM Series Motorized Waist-High Turnstile",
"/assets/img/alvarado/edm-0.png",
["The EDM is the motorized member of Alvarado's waist-high family. Instead of the user pushing the arms, a motor drives the rotation &mdash; the result is smoother, quieter operation and a more premium feel at the entrance. For high-traffic lobbies, that difference adds up over thousands of passages a day.",
"Like every Alvarado waist-high, it's built for continuous duty: the mechanism self-centers after each passage, and the cabinet can be field-configured for one-way or two-way operation as the facility's needs change. Anchoring hardware is hidden, so there are no exposed bolts to collect dirt or tampering.",
"We install EDMs in office buildings, recreation centers, and transit-adjacent facilities where the classic tripod turnstile is the right answer but the client wants it to feel a step up from the mechanical units of the past."],
["Motor-driven arm rotation &mdash; smoother and quieter than mechanical units",
"Automatic arm self-centering after each passage",
"Field-configurable for single-direction or bi-directional use",
"Hidden anchoring &mdash; no exposed bolts or fasteners",
"Built for long-term continuous operation",
"One person per passage &mdash; reliable tailgate deterrence",
"Straightforward installation and maintenance",
"Clean appearance in any finish"],
[("Datasheet", "alvarado/edm-Datasheet-PDS4273R2-0_SEC_WTS_EDM_DATA.pdf"),
 ("Descriptive Specifications", "alvarado/edm-Descriptive-Specifications-PSD4028R2-0_SEC_WTS_EDM-SERIES_DESC.pdf"),
 ("Plan & Elevation Drawings", "alvarado/edm-Plan-and-Elevation-SEC_WTS_EDMS_DRAW_PEF-717_REV-B.pdf")]))

PAGES["products/waist-high-turnstiles/edc/index.html"] = page(
"EDC Series Waist-High Turnstile",
"Alvarado EDC waist-high turnstile — stainless steel tripod turnstiles in four configurations for reliable indoor crowd control. Spec sheets and drawings.",
product_page("Waist-High Turnstiles", "/products/waist-high-turnstiles/", "EDC Series Waist-High Turnstile",
"/assets/img/alvarado/edc-1.jpg",
["The EDC is the classic tripod turnstile done right. Stainless steel cabinet, investment-cast internal components, and a rotation mechanism that's smooth enough that users barely notice it &mdash; this is the unit you'll find in thousands of facilities worldwide because it simply keeps working.",
"Alvarado offers the EDC in four versions: standard or bullnose cabinet ends, and standard or extended-length cabinets with longer arms for wider passages. Every version can be field-set for one-way or two-way traffic, and the arms self-center after each rotation. No exposed fasteners anywhere on the cabinet.",
"For gyms, stadiums, offices, and industrial sites that need dependable one-at-a-time passage control without overthinking it, the EDC is our default recommendation. It integrates with any access control system via dry contact, and readers mount cleanly on the cabinet."],
["Stainless steel cabinet with investment-cast internal components",
"Smooth rotation with automatic self-centering",
"Four versions: square or bullnose ends, standard or extended cabinets",
"Field-configurable for single-direction or bi-directional operation",
"No exposed bolts or fasteners",
"Designed for continuous, long-term duty",
"One passage per authorization",
"Simple to install and service"],
[("Datasheet", "alvarado/edc-Datasheet-PDS1024R4-0_SEC_WTS_EDC_DATA.pdf"),
 ("Descriptive Specifications", "alvarado/edc-Descriptive-Specifications-SEC_WTS_EDC-SERIES_DESC_PSD4033R2-1.pdf"),
 ("Plan & Elevation Drawings", "alvarado/edc-Plan-and-Elevation-SEC_WTS_EDC_DRAW_PEF-096_REV-B.pdf")]))

# ================= detail pages: full-height turnstiles =================

PAGES["products/full-height-turnstiles/mst/index.html"] = page(
"MST & MSTT Full-Height Turnstiles",
"Alvarado MST full-height turnstile — fully welded perimeter security trusted worldwide, plus the space-saving MSTT tandem. Spec sheets and drawings.",
product_page("Full-Height Turnstiles", "/products/full-height-turnstiles/", "MST &amp; MSTT Full-Height Turnstiles",
"/assets/img/alvarado/mst-0.png",
["If you've seen a full-height turnstile at a construction site, stadium, or industrial plant, there's a good chance it was an MST. It's the benchmark of the category: fully welded steel construction, a splined rotation assembly with almost no play, and sealed bearings that keep it turning smoothly for decades outdoors.",
"The controller is built for the real world &mdash; surge protection and coated circuitry shrug off weather and power events. Each direction can be set independently: free passage, controlled by your access system, or locked down, with separate fail-safe/fail-secure behavior on power loss. It talks to any access control panel via dry contact.",
"Where two lanes are needed but space is tight, the MSTT tandem puts two full-height turnstiles in a single footprint about 30 percent smaller than two separate units. We install MSTs at fence lines, parking areas, and unmanned entry points where the requirement is simple: one authorized person per rotation, around the clock."],
["Fully welded steel &mdash; no exposed bolts or fasteners to attack",
"Splined rotation assembly for minimal play and long life",
"Sealed bearings and stainless components stand up to weather",
"Surge-protected controller with coated circuitry",
"Independent per-direction settings: free, controlled, or locked",
"Separate fail-safe / fail-secure behavior on power failure",
"Manual or electric lock control versions",
"MSTT tandem: two lanes in ~30% less space than two singles"],
[("Datasheet (MST)", "alvarado/mst-Datasheet-PDS1027R4-0_SEC_FHT_MST_DATA.pdf"),
 ("Descriptive Specifications (MST)", "alvarado/mst-Descriptive-Specifications-PSD1561R6-0_SEC_FHT_MST_DESC.pdf"),
 ("Plan & Elevation (MST)", "alvarado/mst-Plan-and-Elevation-SEC_FTS_MST_DRAW_PEF-012_REV-D.pdf"),
 ("Datasheet (MSTT)", "alvarado/mstt-Datasheet-PDS1027R3-0_SEC_FHT_MSTT_DATA.pdf"),
 ("Descriptive Specifications (MSTT)", "alvarado/mstt-Descriptive-Specifications-PSD1528R5-0_SEC_FHT_MSTT_DESC.pdf"),
 ("Plan & Elevation (MSTT)", "alvarado/mstt-Plan-and-Elevation-SEC_FTS_MSTT_DRAW_PEF-013_REV-F.pdf")]))

PAGES["products/full-height-turnstiles/clst/index.html"] = page(
"CLST Full-Height Turnstile",
"Alvarado CLST transitional full-height turnstile — MST-grade security with clear side panels for semi-enclosed entrances. Spec sheets and drawings.",
product_page("Full-Height Turnstiles", "/products/full-height-turnstiles/", "CLST Transitional Full-Height Turnstile",
"/assets/img/alvarado/clst-0.jpg",
["The CLST is for the in-between spaces: vestibules, covered walkways, canopies, and interior areas that need full-height security without the industrial look of a perimeter turnstile. Mechanically it's MST-grade &mdash; fully welded, splined rotation, sealed bearings &mdash; but the solid side panels are replaced with crystal-clear panels in aluminum frames.",
"The result lets light through and keeps sight lines open, so a lobby or break-room entrance doesn't feel like a checkpoint. Like the MST, each direction configures independently for free, controlled, or locked passage, with separate fail-safe/fail-secure behavior if power drops.",
"We often pair CLSTs with the matching clear-panel aesthetic at corporate campuses, distribution break areas, and transit facilities where the turnstile sits under a roof and the client wants security that doesn't shout."],
["Clear side panels in aluminum frames &mdash; open sight lines, less industrial",
"Same welded construction and rotation hardware as the MST",
"Built for vestibules, canopies, and semi-enclosed entrances",
"Bi-directional control with electric lock or manual override",
"Independently configurable fail-safe / fail-lock per direction",
"No exposed bolts or fasteners",
"Stainless top channel cover; sealed internal bearings",
"Integrates with any access control system"],
[("Datasheet", "alvarado/clst-Datasheet-PDS4259R4-0_SEC_FHT_CLST_DATA.pdf"),
 ("Descriptive Specifications", "alvarado/clst-Descriptive-Specifications-PSD1532R6-0_SEC_FHT_CLST_DESC.pdf"),
 ("Plan & Elevation Drawings", "alvarado/clst-Plan-and-Elevation-SEC_FTS_CLST_DRAW_PEF-010_REV-C.pdf")]))

PAGES["products/full-height-turnstiles/cpst/index.html"] = page(
"CPST Interior Full-Height Turnstile",
"Alvarado CPST interior full-height turnstile — high-security access control with clear panels for lobbies and secure interiors. Spec sheets and drawings.",
product_page("Full-Height Turnstiles", "/products/full-height-turnstiles/", "CPST Interior Full-Height Turnstile",
"/assets/img/alvarado/cpst-0.png",
["The CPST brings full-height security indoors without making the lobby feel like a loading dock. Clear rotating arms and clear side panels set in aluminum frames give it a light, modern presence &mdash; while the welded construction underneath delivers the same one-person-per-rotation control as the outdoor models.",
"It's aimed at lobbies, employee vestibules, data halls, and other interior zones where the threat model calls for more than a waist-high tripod but the architecture won't tolerate an industrial cage. Standard, motorized, and touch-free versions cover different throughput and hygiene requirements.",
"Operation mirrors the rest of the full-height line: credential in, single controlled rotation, with per-direction settings for free, controlled, or locked passage. Card readers mount cleanly on the frames, and the whole unit ties into the building's access control system."],
["Clear rotating arms and side panels &mdash; security with a light footprint",
"Designed for lobbies, vestibules, and high-security interiors",
"Available in standard, motorized, and touch-free versions",
"Fully welded construction &mdash; no exposed bolts or fasteners",
"Bi-directional control with electric lock or manual override",
"Independently configurable fail-safe / fail-lock per direction",
"Stainless top channel cover; sealed bearings for smooth rotation",
"Clean card-reader mounting; works with any access control panel"],
[("Datasheet", "alvarado/cpst-Datasheet-PDS4258R4-0_SEC_FHT_CPST_DATA.pdf"),
 ("Descriptive Specifications", "alvarado/cpst-Descriptive-Specifications-PSD1530R5-0SEC_FHT_CPST_DESC.pdf"),
 ("Plan & Elevation Drawings", "alvarado/cpst-Plan-and-Elevation-SEC_FTS_CPST_DRAW_PEF-011_REV-D.pdf")]))

# ================= detail pages: pedestrian security gates =================

PAGES["products/pedestrian-gates/msg/index.html"] = page(
"MSG Full-Height Pedestrian Security Gate",
"Alvarado MSG full-height pedestrian gate — a 48-inch pre-hung security gate that beats chain link, for fence lines and turnstile arrays. Spec sheets and drawings.",
product_page("Pedestrian Security Gates", "/products/pedestrian-gates/", "MSG Full-Height Pedestrian Security Gate",
"/assets/img/alvarado/msg-0.png",
["Every full-height turnstile installation eventually needs the same thing: a matching gate for deliveries, equipment, and accessible passage. The MSG is built for exactly that &mdash; a full-height pedestrian security gate that looks and performs like it was engineered for the job, because it was. No more chain-link afterthoughts bolted next to a nice turnstile.",
"It arrives framed, pre-hung, and fully assembled, which keeps installation straightforward: set it, anchor it, done. The 48-inch opening clears wheelchairs and carts, the hydraulic closer shuts it reliably every time, and stainless hinges stand up to outdoor duty. Welded steel construction throughout.",
"We install MSGs alongside MST arrays at industrial sites, stadiums, and campuses &mdash; anywhere the fence line needs a personnel gate that matches the security level of the turnstiles next to it. Multiple models and finishes cover different heights and latch configurations."],
["48-inch clear opening &mdash; accessible for wheelchairs and carts",
"Arrives framed, pre-hung, and fully assembled",
"Welded steel construction with stainless steel hinges",
"Heavy-duty hydraulic self-closing on every model",
"Built for outdoor fence-line duty",
"Installs standalone or alongside full-height turnstiles",
"Multiple models, options, and finishes",
"A finished look &mdash; not a chain-link afterthought"],
[("Datasheet", "alvarado/msg-Datasheet-PDS1036R6-0_SEC_PSG_MSG_DATA.pdf"),
 ("Descriptive Specifications", "alvarado/msg-Descriptive-Specifications-PSD1393R4-1_SEC_PSG_MSG_DESC.pdf"),
 ("Plan & Elevation Drawings", "alvarado/msg-Plan-and-Elevation-SEC_PSG_MSG-48_DRAW_PEF-90.pdf")]))

PAGES["products/pedestrian-gates/sw1000/index.html"] = page(
"SW1000 Motorized Pedestrian Gate",
"Alvarado SW1000 motorized pedestrian gate — a clear-panel ADA gate that matches Alvarado optical turnstiles. Spec sheets and drawings.",
product_page("Pedestrian Security Gates", "/products/pedestrian-gates/", "SW1000 Motorized Pedestrian Gate",
"/assets/img/alvarado/sw1000-1.jpg",
["Optical turnstile lanes handle standard foot traffic beautifully, but every array needs an accessible lane &mdash; and it should look like it belongs. The SW1000 is a motorized pedestrian gate with a crystal-clear moving panel, styled to match Alvarado's optical turnstiles down to the finish and panel heights.",
"The clear opening is 36 inches minimum, wider in tandem configurations, which comfortably clears wheelchairs, strollers, and delivery carts. Panels come in two heights matching the SU5000's low and mid options, and the panel itself can be etched with the client's logo or artwork. An optional motion detector can trigger free entry or free exit without a credential presentation.",
"We spec the SW1000 on nearly every optical lane project &mdash; it's the accessible companion the array needs, and because it shares the optical line's design language, the entrance reads as one intentional installation instead of a turnstile plus an afterthought."],
["36-inch-plus clear opening for accessible and cart passage",
"Crystal-clear moving panel in two heights",
"Panel heights match SU5000 optical turnstile options",
"Finish matched to Alvarado optical turnstiles",
"Panel can be etched with customer logo or artwork",
"Motorized operation &mdash; smooth, controlled swing",
"Optional motion detector for free entry or free exit",
"Installs solo or in tandem for wider openings"],
[("Datasheet", "alvarado/sw1000-Datasheet-PDS3497R4-0_SEC_PSG__SW1000_DATA.pdf"),
 ("Descriptive Specifications", "alvarado/sw1000-Descriptive-Specifications-PSD3498R3-0_SEC_PSG_SW1000_DESC.pdf"),
 ("Plan & Elevation Drawings", "alvarado/sw1000-Plan-and-Elevation-SW1000-Drawings.zip")]))

PAGES["products/pedestrian-gates/vsg/index.html"] = page(
"VSG-X Pedestrian Gate",
"Alvarado VSG-X self-closing pedestrian gate — the companion gate for waist-high and optical turnstile lanes. Spec sheets and drawings.",
product_page("Pedestrian Security Gates", "/products/pedestrian-gates/", "VSG-X Pedestrian Gate",
"/assets/img/alvarado/vsgx-1.jpg",
["The VSG-X is the gate we pair with waist-high and optical turnstile installations when the job calls for a simple, dependable self-closing pedestrian gate. It handles the accessible lane, the delivery pass-through, or the exit-only path &mdash; wherever a turnstile lane isn't the right tool.",
"Operation is mechanical and fuss-free: an adjustable hydraulic closer shuts the gate behind each user, and it can be ordered non-locking or with electric lock control tied into the access system. Infill comes as bars or an acrylic panel depending on the look and security level the site needs, and a kick plate protects the lower section from wheelchair and cart traffic.",
"It's the kind of product that disappears into the installation &mdash; which is exactly what a companion gate should do. Same quality fabrication and finish as the turnstiles it sits next to, sized to give a genuinely wider passage where accessibility matters."],
["Self-closing with adjustable hydraulic closer",
"Companion gate for waist-high and optical turnstile lanes",
"Wider passage for accessible entry and carts",
"Kick plate stands up to wheelchair and cart contact",
"Non-locking or electric lock control models",
"Infill bars or acrylic panel options",
"Single-direction operation",
"Finish and fabrication matched to Alvarado turnstiles"],
[("Datasheet", "alvarado/vsg-Datasheet-SEC_PSG_-VSG_DATA_PDS1031R4-0.pdf"),
 ("Descriptive Specifications", "alvarado/vsg-Descriptive-Specifications-PSD3008R2-0_SEC_PSG_VSG_DESC.pdf"),
 ("Plan & Elevation Drawings", "alvarado/vsg-Plan-and-Elevation-VSG-Drawings-1.zip")]))

# ================= detail pages: revolving doors =================

PAGES["products/data-center-high-security/srd/index.html"] = page(
"SRD Secured Revolving Door",
"Alvarado SRD secured revolving door — automatic anti-tailgating revolving entry with piggybacking detection. Spec sheets.",
product_page("Data Center & High Security", "/products/data-center-high-security/", "SRD Secured Revolving Door",
"/assets/img/alvarado/srd-0.jpg",
["The SRD is a different animal from a conventional revolving door. It's a secured revolving door: the rotation, the sensors, and the access control work together so that exactly one authorized person passes per cycle &mdash; no tailgating, no piggybacking, no propped doors. For lobbies that need real entrance security without posting a guard, it's one of the most effective options available.",
"Three models scale the protection: the S2 covers bidirectional tailgate prevention and exit-side unauthorized entry, while the S3 and S4 add sensors that catch piggybacking &mdash; two people trying to enter as one. Four standard sensors watch each compartment, voice prompts tell users what to do, and the door can run entry, exit, or bidirectional authentication while tracking occupancy in real time.",
"As a bonus over a standard revolving door, weather sweeps cut air transfer dramatically, which helps with energy costs and lobby comfort. Installation is handled by certified technicians, and lead times are shorter than you'd expect for this class of equipment. We've seen SRDs go into corporate headquarters, data centers, and government buildings where the entrance has to enforce the access policy by itself."],
["One authorized person per cycle &mdash; true anti-tailgating entry",
"Three models: S2 tailgate prevention; S3/S4 add piggybacking detection",
"Four sensors per compartment; two more on S3/S4 models",
"Configurable voice alarms guide and instruct users",
"Entry, exit, or bidirectional authentication with live occupancy count",
"Weather sweeps cut air transfer for energy savings and comfort",
"Hand-welded construction",
"Installed by certified technicians; no dedicated guard needed"],
[("Datasheet", "alvarado/srd-Datasheet-SEC_SRD_S2-S3-S4_DATA_PDS4762R1-1.pdf"),
 ("Architectural Specifications", "alvarado/srd-Architectural-Specifications-CSI4763R1-1_SEC_SRD_S2-S3-S4_ARCH.pdf")]))

# ================= detail pages: specialty =================

PAGES["products/specialty/intraq-x/index.html"] = page(
"IntraQ-X Suite Access Terminal",
"Alvarado IntraQ-X suite access scanner — wall-mounted validation of mobile and printed credentials for suites and clubs. Spec sheets.",
product_page("Specialty", "/products/specialty/", "IntraQ-X Suite Access Terminal",
"/assets/img/alvarado/intraqx-0.jpg",
["Luxury suites, club levels, and VIP areas have an access problem: the credentials are tickets, often on phones, and the door needs to read them fast without a staff member standing there. The IntraQ-X is a compact wall-mounted scanner built for exactly that &mdash; guests hold up a printed ticket or a phone screen, the unit validates it, and the suite door unlocks.",
"It reads practically everything: 1D and 2D printed barcodes, mobile phone barcodes, and RFID/NFC passes. A bright touchscreen walks guests through it, and the venue can load custom graphics and audio so a valid ticket gets the team's branding and sound. Power and data run over a single Ethernet cable (PoE+), which keeps installation clean.",
"We install IntraQ-X units at arena suite entries, club doors, and back-of-house restricted areas anywhere in the venue footprint. It speaks TCP/IP to the venue's systems, so it drops into the existing network without special infrastructure."],
["Validates printed and mobile 1D/2D barcodes plus RFID/NFC passes",
"Compact wall-mounted design for suite and club entries",
"Bright TFT touchscreen with guest instructions",
"Custom graphics, sounds, and LED accent lighting",
"Power over Ethernet (PoE+) &mdash; one cable for power and data",
"Unlocks suite doors, re-locking after passage",
"TCP/IP communication with venue systems",
"Built for stadiums, arenas, and entertainment venues"],
[("Datasheet", "alvarado/intraq-x-Datasheet-SNE_GAS_IntraQ-X-Suite_Scanner_DATA_PDS4266R1-0.pdf"),
 ("Descriptive Specifications", "alvarado/intraq-x-Descriptive-Specifications-SNE_GAS_IntraQ-X-SUITE_DESC_PSD4267R2-0.pdf")]))

PAGES["products/specialty/su500/index.html"] = page(
"SU500 Optical Counting Turnstile",
"Alvarado SU500 barrier-free optical counting turnstile — accurate patron counting for entries, exits, and occupancy tracking. Spec sheets and drawings.",
product_page("Specialty", "/products/specialty/", "SU500 Optical Counting Turnstile",
"/assets/img/alvarado/su500-1.jpg",
["The SU500 isn't an access control turnstile &mdash; it's a counting turnstile. No barriers, no credentials: people walk through and the optical sensor array counts each passage with high accuracy. If you need to know how many people entered, exited, or are currently in the building, this is the tool.",
"Common installs put SU500 lanes at facility entries and exits, sometimes paired: one lane counts people in, another counts them out, and the difference is your live occupancy number. It counts in one direction or both, and a configurable audible alarm can flag wrong-way movement. The cabinet is compact, lanes can be spaced for standard or ADA-width passages, and it works indoors plus in select outdoor applications.",
"We've used SU500s for occupancy compliance, staffing decisions, and traffic analysis at venues, campuses, and retail-adjacent facilities. It's a simple product that answers a question every facility manager asks: how many people are in my building right now?"],
["Barrier-free optical counting &mdash; no credentials, just accurate counts",
"Single-direction or bi-directional patron counting",
"High counting accuracy with high throughput",
"Configurable wrong-way passage alarm",
"Live occupancy tracking when paired at entries and exits",
"Compact cabinet; standard and ADA-width lane spacing",
"Stainless steel or powder-coated finishes",
"Suitable for indoor and select outdoor use"],
[("Datasheet", "alvarado/su500-Datasheet-SNE_PAC_SU500_DATA_PDS1039R1-0.pdf"),
 ("Descriptive Specifications", "alvarado/su500-Descriptive-Specifications-SNE_PAC_SU500_DESC_PSD1568R2-0.pdf"),
 ("Plan & Elevation Drawings", "alvarado/su500-Plan-and-Elevation-SEC_OPT_SU500-STD_DRAW_PEF-513_REV-A.pdf")]))

# ================= category index pages =================

PAGES["products/optical-turnstiles/index.html"] = page(
"Optical Turnstiles",
"Turnwell LLC optical turnstiles: Argus, Argus V60, SU5000, SU4500, SU3000, SU2000 — elegant lobby security with high throughput.",
"""<section class="page-hero"><div class="hero-inner wrap">
  <h1>Optical Turnstiles</h1>
  <p>Elegant, high-throughput pedestrian control for lobbies, offices, and interiors &mdash; security that complements the space instead of fighting it.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="eyebrow">Models</div>
  <h2 class="section-title">Beautiful security for supervised entrances</h2>
  <div class="grid-3">
    <div class="card"><div class="card-img"><img src="/assets/img/alvarado/argus-1.jpg" alt="Argus sensor barriers"></div><div class="card-body"><h3>Argus 40 / 60 / 80</h3><p>Glass swinging-barrier sensor lanes with European styling &mdash; security that reads as architecture.</p><a class="card-link" href="/products/optical-turnstiles/argus/">Find Out More &rarr;</a></div></div>
    <div class="card"><div class="card-img"><img src="/assets/img/alvarado/argus-v60-0.jpg" alt="Argus V60"></div><div class="card-body"><h3>Argus V60</h3><p>Compact optical lane with a 9.5-inch cabinet &mdash; full tailgate detection where space is tight.</p><a class="card-link" href="/products/optical-turnstiles/argus-v60/">Find Out More &rarr;</a></div></div>
    <div class="card"><div class="card-img"><img src="/assets/img/alvarado/su5000-0.png" alt="SU5000"></div><div class="card-body"><h3>SU5000</h3><p>The swinging-barrier workhorse &mdash; slimmest cabinet in its class, motorized barriers, multi-lane arrays.</p><a class="card-link" href="/products/optical-turnstiles/su5000/">Find Out More &rarr;</a></div></div>
    <div class="card"><div class="card-img"><img src="/assets/img/alvarado/su4500-0.png" alt="SU4500"></div><div class="card-body"><h3>SU4500</h3><p>The most compact barrier optical &mdash; full features in a 38-inch cabinet for smaller lobbies.</p><a class="card-link" href="/products/optical-turnstiles/su4500/">Find Out More &rarr;</a></div></div>
    <div class="card"><div class="card-img"><img src="/assets/img/alvarado/su3000-1.jpg" alt="SU3000"></div><div class="card-body"><h3>SU3000</h3><p>Drop-arm optical with a slim profile &mdash; visible access control without the glass.</p><a class="card-link" href="/products/optical-turnstiles/su3000/">Find Out More &rarr;</a></div></div>
    <div class="card"><div class="card-img"><img src="/assets/img/alvarado/su2000-1.jpg" alt="SU2000"></div><div class="card-body"><h3>SU2000</h3><p>Barrier-free optical &mdash; sensor-only detection for supervised entrances that stay open.</p><a class="card-link" href="/products/optical-turnstiles/su2000/">Find Out More &rarr;</a></div></div>
  </div>
</div></section>
""" + CTA_BAND)

PAGES["products/waist-high-turnstiles/index.html"] = page(
"Waist-High Turnstiles",
"Turnwell LLC waist-high turnstiles: Alvarado EDM motorized and EDC tripod turnstiles for reliable one-at-a-time passage control.",
"""<section class="page-hero"><div class="hero-inner wrap">
  <h1>Waist-High Turnstiles</h1>
  <p>The classic tripod turnstile, built for continuous duty &mdash; dependable one-person-per-passage control for gyms, offices, stadiums, and industrial sites.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="eyebrow">Models</div>
  <h2 class="section-title">Proven passage control, indoors and out</h2>
  <div class="grid-3">
    <div class="card"><div class="card-img"><img src="/assets/img/alvarado/edm-0.png" alt="EDM turnstile"></div><div class="card-body"><h3>EDM Series</h3><p>Motorized waist-high turnstile &mdash; smooth, quiet, motor-driven rotation with a premium feel.</p><a class="card-link" href="/products/waist-high-turnstiles/edm/">Find Out More &rarr;</a></div></div>
    <div class="card"><div class="card-img"><img src="/assets/img/alvarado/edc-1.jpg" alt="EDC turnstile"></div><div class="card-body"><h3>EDC Series</h3><p>Stainless tripod turnstiles in four configurations &mdash; the reliable default for crowd control.</p><a class="card-link" href="/products/waist-high-turnstiles/edc/">Find Out More &rarr;</a></div></div>
  </div>
  <div style="margin-top:48px">
    <div class="eyebrow">Typical applications</div>
    <ul class="feature-list">
      <li><span class="check">&#10003;</span> Employee and visitor entrances</li>
      <li><span class="check">&#10003;</span> Gyms, fitness centers, and recreation facilities</li>
      <li><span class="check">&#10003;</span> Stadiums and event venues</li>
      <li><span class="check">&#10003;</span> Time and attendance points</li>
      <li><span class="check">&#10003;</span> One-way exit control</li>
    </ul>
  </div>
</div></section>
""" + CTA_BAND)

PAGES["products/full-height-turnstiles/index.html"] = page(
"Full-Height Turnstiles",
"Turnwell LLC full-height turnstiles: Alvarado MST, MSTT tandem, CLST, and CPST — welded perimeter security for unmanned entry points.",
"""<section class="page-hero"><div class="hero-inner wrap">
  <h1>Full-Height Turnstiles</h1>
  <p>Full-height turnstiles secure perimeters, fence lines, and large venues &mdash; one authorized person per rotation, around the clock, no guard required.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="eyebrow">Models</div>
  <h2 class="section-title">Welded security for the toughest posts</h2>
  <div class="grid-3">
    <div class="card"><div class="card-img"><img src="/assets/img/alvarado/mst-0.png" alt="MST full-height turnstile"></div><div class="card-body"><h3>MST &amp; MSTT</h3><p>The benchmark full-height turnstile &mdash; fully welded for outdoor perimeter duty; tandem MSTT saves space.</p><a class="card-link" href="/products/full-height-turnstiles/mst/">Find Out More &rarr;</a></div></div>
    <div class="card"><div class="card-img"><img src="/assets/img/alvarado/clst-0.jpg" alt="CLST turnstile"></div><div class="card-body"><h3>CLST</h3><p>MST-grade security with clear side panels &mdash; for vestibules, canopies, and semi-enclosed entrances.</p><a class="card-link" href="/products/full-height-turnstiles/clst/">Find Out More &rarr;</a></div></div>
    <div class="card"><div class="card-img"><img src="/assets/img/alvarado/cpst-0.png" alt="CPST turnstile"></div><div class="card-body"><h3>CPST</h3><p>Interior full-height security with clear panels &mdash; high protection that suits the lobby.</p><a class="card-link" href="/products/full-height-turnstiles/cpst/">Find Out More &rarr;</a></div></div>
    <div class="card"><div class="card-img"><img src="/assets/img/products/full-height-turnstiles/fts.jpg" alt="FTS full-height turnstile"></div><div class="card-body"><h3>FTS</h3><p>Full-height turnstile for demanding perimeter applications.</p><a class="card-link" href="/products/full-height-turnstiles/fts/">Find Out More &rarr;</a></div></div>
  </div>
  <div style="margin-top:48px">
    <div class="eyebrow">Secured entry-control applications</div>
    <ul class="feature-list">
      <li><span class="check">&#10003;</span> Perimeter control &amp; fence-line security</li>
      <li><span class="check">&#10003;</span> Employee and visitor access control</li>
      <li><span class="check">&#10003;</span> Time and attendance integration</li>
      <li><span class="check">&#10003;</span> Parking lot access &amp; one-way exit control</li>
      <li><span class="check">&#10003;</span> Unattended entry points</li>
    </ul>
  </div>
</div></section>
""" + CTA_BAND)

PAGES["products/pedestrian-gates/index.html"] = page(
"Pedestrian Security Gates",
"Turnwell LLC pedestrian security gates: Alvarado MSG full-height gate, SW1000 motorized ADA gate, and VSG-X self-closing gate.",
"""<section class="page-hero"><div class="hero-inner wrap">
  <h1>Pedestrian Security Gates</h1>
  <p>Every turnstile array needs its gates &mdash; accessible lanes, delivery passage, and exit paths that match the security level of the installation.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="eyebrow">Models</div>
  <h2 class="section-title">The right gate for every opening</h2>
  <div class="grid-3">
    <div class="card"><div class="card-img"><img src="/assets/img/alvarado/msg-0.png" alt="MSG gate"></div><div class="card-body"><h3>MSG</h3><p>Full-height pedestrian security gate &mdash; a 48-inch pre-hung gate for fence lines and turnstile arrays.</p><a class="card-link" href="/products/pedestrian-gates/msg/">Find Out More &rarr;</a></div></div>
    <div class="card"><div class="card-img"><img src="/assets/img/alvarado/sw1000-1.jpg" alt="SW1000 gate"></div><div class="card-body"><h3>SW1000</h3><p>Motorized clear-panel gate styled to match optical turnstiles &mdash; the accessible lane, done right.</p><a class="card-link" href="/products/pedestrian-gates/sw1000/">Find Out More &rarr;</a></div></div>
    <div class="card"><div class="card-img"><img src="/assets/img/alvarado/vsgx-1.jpg" alt="VSG-X gate"></div><div class="card-body"><h3>VSG-X</h3><p>Self-closing pedestrian gate &mdash; the dependable companion for waist-high and optical lanes.</p><a class="card-link" href="/products/pedestrian-gates/vsg/">Find Out More &rarr;</a></div></div>
  </div>
</div></section>
""" + CTA_BAND)

PAGES["products/data-center-high-security/index.html"] = page(
"Data Center & High Security",
"Turnwell LLC data center entrance security: Alvarado SRD secured revolving doors and dormakaba Orthos personal interlocks — anti-tailgating, anti-piggybacking entry for data centers and high-security facilities.",
"""<section class="page-hero"><div class="hero-inner wrap">
  <h1>Data Center & High Security</h1>
  <p>One tailgater through a lobby door can compromise an entire facility. We install the entrance systems that make that impossible.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="eyebrow">Why Turnwell for data centers</div>
  <h2 class="section-title">Physical security your auditors can verify</h2>
  <p style="max-width:760px;font-size:17px">Data centers live or die on physical security. The compliance frameworks your customers answer to &mdash; SOC 2, HIPAA, PCI DSS &mdash; demand provable, auditable control of every entry point. Turnwell designs and installs entrance systems that enforce those policies without posting a guard at every door: secured revolving doors that admit exactly one authorized person per cycle, and personal interlocks that verify identity mid-passage with anti-piggybacking detection.</p>
  <p style="max-width:760px;font-size:17px">At Turnwell, we handle the complete installation &mdash; equipment, integration with your access control system, and commissioning. As a licensed General Contractor, we&rsquo;re your one point of accountability from delivery to go-live.</p>
  <div style="margin-top:36px">
  <div class="eyebrow">Models</div>
  <h2 class="section-title">High-security entrance systems</h2>
  <div class="grid-3">
    <div class="card"><div class="card-img"><img src="/assets/img/alvarado/srd-0.jpg" alt="SRD secured revolving door"></div><div class="card-body"><h3>SRD</h3><p>Secured revolving door with anti-tailgating and piggybacking detection &mdash; unmanned high-security entry.</p><a class="card-link" href="/products/data-center-high-security/srd/">Find Out More &rarr;</a></div></div>
    <div class="card"><div class="card-img"><img src="/assets/img/products/interlocks-revolving-doors/orthos.jpg" alt="Orthos personal interlock"></div><div class="card-body"><h3>Orthos</h3><p>Electronically monitored personal interlocks for the highest security demands.</p><a class="card-link" href="/products/data-center-high-security/orthos/">Find Out More &rarr;</a></div></div>
    <div class="card"><div class="card-img"><img src="/assets/img/products/interlocks-revolving-doors/geryon.jpg" alt="Geryon security revolving door"></div><div class="card-body"><h3>Geryon</h3><p>Security revolving doors that blend elegantly into their surroundings &mdash; inside or at the entrance.</p><a class="card-link" href="/products/data-center-high-security/geryon/">Find Out More &rarr;</a></div></div>
  </div>
  </div>
  <div style="margin-top:48px">
    <div class="eyebrow">Typical applications</div>
    <ul class="feature-list">
      <li><span class="check">&#10003;</span> Data centers and colocation facilities</li>
      <li><span class="check">&#10003;</span> Personal interlocks at data halls</li>
      <li><span class="check">&#10003;</span> Corporate headquarters lobbies</li>
      <li><span class="check">&#10003;</span> Government and defense facilities</li>
      <li><span class="check">&#10003;</span> Any entrance that must enforce access without staffing</li>
    </ul>
  </div>
</div></section>
""" + CTA_BAND)

PAGES["products/specialty/index.html"] = page(
"Specialty Entry Products",
"Turnwell LLC specialty entry products: IntraQ-X suite access terminals and SU500 optical people-counting turnstiles.",
"""<section class="page-hero"><div class="hero-inner wrap">
  <h1>Specialty Entry Products</h1>
  <p>Beyond turnstiles and gates &mdash; credential validation for suites and accurate people-counting for entries and exits.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="eyebrow">Models</div>
  <h2 class="section-title">Solve the unusual problems</h2>
  <div class="grid-3">
    <div class="card"><div class="card-img"><img src="/assets/img/alvarado/intraqx-0.jpg" alt="IntraQ-X"></div><div class="card-body"><h3>IntraQ-X</h3><p>Wall-mounted suite access scanner &mdash; validates mobile and printed tickets at suite and club doors.</p><a class="card-link" href="/products/specialty/intraq-x/">Find Out More &rarr;</a></div></div>
    <div class="card"><div class="card-img"><img src="/assets/img/alvarado/su500-1.jpg" alt="SU500"></div><div class="card-body"><h3>SU500</h3><p>Barrier-free optical counting turnstile &mdash; know exactly how many people are in the building.</p><a class="card-link" href="/products/specialty/su500/">Find Out More &rarr;</a></div></div>
  </div>
</div></section>
""" + CTA_BAND)

# ---------------------------------------------------------------- build
if __name__ == "__main__":
    for relpath, html in PAGES.items():
        dest = os.path.join(OUT, relpath)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w") as f:
            f.write(html)
    print(f"built {len(PAGES)} pages")
