# Shared templates for the Blossom static site generator.
# COPY DECK V2 (01 Sep 2026): Complete Garden Management positioning.

DOMAIN = "https://blossomgarden.design"

NAV_ITEMS = [
    ("garden-management.html", "Garden Management"),
    ("garden-projects.html", "Garden Projects"),
    ("garden-design.html", "Garden Design"),
    ("complete-garden-transformation.html", "Transformation"),
    ("how-it-works.html", "How It Works"),
    ("about.html", "About"),
]

MOBILE_ITEMS = [
    ("garden-management.html", "Garden Management"),
    ("garden-projects.html", "Garden Projects"),
    ("garden-design.html", "Garden Design"),
    ("complete-garden-transformation.html", "Complete Garden Transformation"),
    ("your-garden-manager.html", "Your Garden Manager"),
    ("garden-review.html", "Garden Review"),
    ("how-it-works.html", "How It Works"),
    ("garden-services.html", "Services A to Z"),
    ("projects.html", "Projects"),
    ("areas.html", "Areas We Cover"),
    ("journal.html", "Garden Journal"),
    ("faq.html", "FAQ"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]

LOCAL_BUSINESS_SCHEMA = """{
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "Blossom",
    "url": "%s/",
    "slogan": "One trusted point of contact for everything your garden needs.",
    "description": "Complete garden management for homeowners across Surrey, Hampshire and Sussex. Garden reviews, design, done-for-you projects, complete transformations and ongoing garden management.",
    "areaServed": [
      { "@type": "AdministrativeArea", "name": "Surrey" },
      { "@type": "AdministrativeArea", "name": "Hampshire" },
      { "@type": "AdministrativeArea", "name": "West Sussex" },
      { "@type": "AdministrativeArea", "name": "East Sussex" }
    ],
    "founder": { "@type": "Person", "name": "Damian Hickey" },
    "knowsAbout": ["Complete garden management", "Garden design", "Garden projects", "Garden buildings", "Outdoor living", "Garden maintenance coordination"]
  }""" % DOMAIN


def head(title, desc, path, extra_schema="", noindex=False):
    robots = '\n  <meta name="robots" content="noindex, nofollow">' if noindex else ""
    schema_blocks = '<script type="application/ld+json">\n  %s\n  </script>' % LOCAL_BUSINESS_SCHEMA
    if extra_schema:
        schema_blocks += '\n  <script type="application/ld+json">\n  %s\n  </script>' % extra_schema
    return """<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>%s</title>
  <meta name="description" content="%s">
  <link rel="canonical" href="%s/%s">%s
  <link rel="icon" type="image/png" href="assets/img/logo-lockup.png">
  <meta property="og:title" content="%s">
  <meta property="og:description" content="%s">
  <meta property="og:type" content="website">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;1,9..144,400&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css?v=22">
  %s
</head>
<body>
""" % (title, desc, DOMAIN, path, robots, title, desc, schema_blocks)


def header(active=""):
    links = []
    for href, label in NAV_ITEMS:
        current = ' aria-current="page"' if href == active else ""
        links.append('          <li><a href="%s"%s>%s</a></li>' % (href, current, label))
    mobile = []
    for href, label in MOBILE_ITEMS:
        mobile.append('        <li><a href="%s">%s</a></li>' % (href, label))
    return """  <a class="skip-link" href="#main">Skip to content</a>

  <header class="site-header">
    <div class="nav-bar">
      <a class="brand" href="index.html" aria-label="Blossom, home">
        <img src="assets/img/logo-lockup.png" alt="Blossom" height="78">
      </a>
      <nav aria-label="Main">
        <ul class="nav-links">
%s
        </ul>
      </nav>
      <a class="btn btn-primary nav-cta" data-event="book_review_click" href="contact.html">Book a Garden Review</a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="mobile-menu">Menu</button>
    </div>
    <div class="mobile-menu" id="mobile-menu">
      <ul>
%s
      </ul>
      <a class="btn btn-primary" data-event="book_review_click" href="contact.html">Book a Garden Review</a>
    </div>
  </header>
""" % ("\n".join(links), "\n".join(mobile))


FOOTER = """  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="footer-logo"><img src="assets/img/logo-lockup.png" alt="Blossom logo"></div>
          <p>Complete garden management for homeowners across Surrey, Hampshire and Sussex. One trusted point of contact for design, projects, maintenance and everything in between.</p>
        </div>
        <div>
          <h4>Services</h4>
          <ul>
            <li><a href="garden-review.html">Garden Review</a></li>
            <li><a href="garden-design.html">Garden Design</a></li>
            <li><a href="garden-projects.html">Garden Projects</a></li>
            <li><a href="complete-garden-transformation.html">Complete Transformation</a></li>
            <li><a href="your-garden-manager.html">Your Garden Manager</a></li>
          </ul>
        </div>
        <div>
          <h4>Explore</h4>
          <ul>
            <li><a href="how-it-works.html">How It Works</a></li>
            <li><a href="garden-services.html">Services A to Z</a></li>
            <li><a href="projects.html">Projects</a></li>
            <li><a href="areas.html">Areas We Cover</a></li>
            <li><a href="journal.html">Garden Journal</a></li>
            <li><a href="faq.html">FAQ</a></li>
            <li><a href="about.html">About Blossom</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <ul>
            <li><a href="mailto:hello@blossomgarden.design">hello@blossomgarden.design</a></li>
            <li>Surrey, Hampshire and Sussex</li>
          </ul>
        </div>
      </div>
      <div class="footer-legal">
        <span>© 2026 Blossom</span>
        <a href="privacy.html">Privacy</a>
        <a href="cookies.html">Cookie policy</a>
        <a href="terms.html">Website terms</a>
      </div>
    </div>
  </footer>

  <div class="cookie-banner" role="dialog" aria-modal="false" aria-label="Cookie preferences">
    <p><strong>A quiet word about cookies.</strong> We would like to use optional analytics to understand which pages help visitors most. No advertising and no data sold. The site works fully either way.</p>
    <div class="cookie-actions">
      <button class="btn btn-primary" data-consent-accept>Accept analytics</button>
      <button class="btn btn-outline" data-consent-decline>Essential only</button>
    </div>
  </div>

  <script src="assets/js/main.js?v=22"></script>
</body>
</html>
"""


def page(title, desc, path, active, body, extra_schema="", noindex=False, cta=True):
    return (
        head(title, desc, path, extra_schema, noindex)
        + header(active)
        + '\n  <main id="main">\n\n'
        + body
        + "\n  </main>\n\n"
        + FOOTER
    )
