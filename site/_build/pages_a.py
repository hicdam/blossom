# Core service pages. COPY DECK V2 verbatim. Bodies only; templates.py wraps them.

def hero(photo, alt, eyebrow, h1, stand, cta_label="Book a Garden Review", cta_href="contact.html"):
    cta = ''
    if cta_label:
        cta = '\n          <div class="btn-row on-dark"><a class="cta-link big" data-event="book_review_click" href="%s">%s</a></div>' % (cta_href, cta_label)
    return '''    <section class="page-hero">
      <div class="plx-bg"><img src="assets/img/photos/%s" alt="%s"></div>
      <div class="shade"></div>
      <div class="inner wrap">
        <span class="eyebrow">%s</span>
        <h1>%s</h1>
        <p class="standfirst">%s</p>%s
      </div>
    </section>''' % (photo, alt, eyebrow, h1, stand, cta)


GARDEN_MANAGEMENT = {
    "path": "garden-management.html",
    "title": "Complete Garden Management for Homeowners | Blossom",
    "desc": "Blossom manages every aspect of your garden, from maintenance and supplier coordination to improvements, garden buildings and major projects across Surrey, Hampshire and Sussex.",
    "active": "garden-management.html",
    "schema": """{
    "@context": "https://schema.org",
    "@type": "Service",
    "serviceType": "Complete garden management",
    "name": "Complete Garden Management",
    "provider": { "@type": "ProfessionalService", "name": "Blossom" },
    "areaServed": ["Surrey", "Hampshire", "West Sussex", "East Sussex"],
    "description": "One accountable relationship for the condition, operation and continuing improvement of your garden."
  }""",
    "body": hero("country-garden.jpg", "A country garden in evening light with mature trees and a treehouse",
        "Complete Garden Management", "Everything your garden needs, managed in one place.",
        "One accountable relationship for the condition, operation and continuing improvement of your garden.",
        "Discuss garden management") + '''

    <section class="split">
      <div class="split-copy reveal">
        <span class="eyebrow">More than maintenance</span>
        <h2>A gardener cares for the plants. Blossom manages the garden.</h2>
        <p>Gardens contain living systems, built structures, utilities, equipment, suppliers and continual decisions. Mowing and pruning matter, but they do not manage drainage, lighting, irrigation, contractors, repairs, budgets, warranties or improvement projects.</p>
        <p>Blossom oversees the whole environment. We can work with the people you already trust, replace missing or unsuitable suppliers and bring in specialists whenever the garden needs them.</p>
      </div>
      <div class="split-photo"><img src="assets/img/photos/courtyard-reading.jpg" alt="A walled courtyard garden with someone reading beside a sleeping dog"></div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="center reveal">
          <span class="eyebrow">What we manage</span>
          <h2>The people, the place and the plan.</h2>
        </div>
        <div class="grid-4" style="margin-top: 40px;">
          <article class="card reveal">
            <p class="card-meta">The garden itself</p>
            <ul class="check-list" style="font-size: 15px;">
              <li>Planting, trees, hedges and lawns</li>
              <li>Soil, drainage and water management</li>
              <li>Seasonal development and replacement planting</li>
              <li>Wildlife, biodiversity and sustainability</li>
              <li>Kitchen gardens, orchards and productive areas</li>
            </ul>
          </article>
          <article class="card reveal">
            <p class="card-meta">Built assets and systems</p>
            <ul class="check-list" style="font-size: 15px;">
              <li>Garden buildings and outdoor rooms</li>
              <li>Terraces, paths, walls, fences and gates</li>
              <li>Lighting, power, irrigation and smart controls</li>
              <li>Ponds, pools, spas and water features</li>
              <li>Outdoor kitchens, furniture and equipment</li>
            </ul>
          </article>
          <article class="card reveal">
            <p class="card-meta">People and suppliers</p>
            <ul class="check-list" style="font-size: 15px;">
              <li>Maintenance gardeners</li>
              <li>Landscape contractors</li>
              <li>Arborists and horticultural specialists</li>
              <li>Electricians, plumbers and irrigation engineers</li>
              <li>Pool, pond, gate, security and building specialists</li>
            </ul>
          </article>
          <article class="card reveal">
            <p class="card-meta">Commercial control</p>
            <ul class="check-list" style="font-size: 15px;">
              <li>Annual budget and priorities</li>
              <li>Quotations and supplier comparison</li>
              <li>Work orders and scheduling</li>
              <li>Invoice review</li>
              <li>Warranty and defect management</li>
              <li>Planned replacement and improvement</li>
            </ul>
          </article>
        </div>
      </div>
    </section>

    <section class="split flip">
      <div class="split-copy reveal">
        <span class="eyebrow">The garden management plan</span>
        <h2>A clear record of what you own, what it needs and what happens next.</h2>
        <p>Every ongoing relationship begins with a Garden Management Review. We establish the condition of the garden, record its important assets and systems, review existing suppliers and build the first annual plan.</p>
        <div class="receive tint-lilac" style="margin-top: 10px;">
          <h4>You receive</h4>
          <ul>
            <li>A garden condition and priorities report</li>
            <li>A garden asset and supplier register</li>
            <li>A seasonal maintenance programme</li>
            <li>Known risks and outstanding repairs</li>
            <li>Recommended improvement projects</li>
            <li>An initial annual budget and decision calendar</li>
          </ul>
        </div>
      </div>
      <div class="split-photo"><img src="assets/img/photos/greenhouse-tools.jpg" alt="Garden hand tools and seedling trays behind a weathered greenhouse window"></div>
    </section>

    <section class="section section-deep">
      <div class="wrap">
        <div class="grid-3">
          <div class="reveal">
            <span class="eyebrow">Ongoing management</span>
            <h3>Planned care and responsive help.</h3>
            <p style="font-size: 15px;">The exact service is shaped around the garden and the level of responsibility you want Blossom to take. It can include scheduled inspections, supplier management, seasonal planning, project delivery and a priority route for anything unexpected.</p>
            <p style="font-size: 15px;">You receive a concise update at an agreed frequency, with completed work, upcoming decisions, current expenditure and anything requiring your approval.</p>
          </div>
          <div class="reveal">
            <span class="eyebrow">Your existing team</span>
            <h3>Good suppliers stay. Missing capabilities are added.</h3>
            <p style="font-size: 15px;">Blossom does not replace people for the sake of it. We review the gardeners and specialists already involved, clarify responsibilities and make sure their work supports the same garden plan. Where a gap exists, we source and manage the right person to fill it.</p>
          </div>
          <div class="reveal">
            <span class="eyebrow">Commercial clarity</span>
            <h3>You know what Blossom costs and what everyone else is charging.</h3>
            <p style="font-size: 15px;">Ongoing management uses an agreed onboarding fee and management retainer. Project work and specialist services are scoped separately. Any supplier commission, procurement fee or product margin relevant to your appointment is disclosed before you approve it.</p>
            <p class="smallprint">As a guide: Garden Review £295, design fees typically 10 to 15 percent of the build budget, project management from £950 a month, retained management from £650 a year. Exact fees depend on the size, complexity and level of responsibility involved and are confirmed in writing before the service begins.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap-narrow center reveal">
        <h2>Give the whole garden one point of responsibility.</h2>
        <div class="btn-row" style="justify-content: center;">
          <a class="cta-link big" data-event="book_review_click" href="contact.html">Book a Garden Management Review</a>
        </div>
      </div>
    </section>
''',
}

GARDEN_PROJECTS = {
    "path": "garden-projects.html",
    "title": "Done-for-You Garden Projects | Surrey, Hampshire & Sussex | Blossom",
    "desc": "Garden offices, gyms, pergolas, outdoor kitchens, pools, landscaping, lighting and more. Blossom scopes, sources and manages any garden project for you.",
    "active": "garden-projects.html",
    "schema": """{
    "@context": "https://schema.org",
    "@type": "Service",
    "serviceType": "Garden project management",
    "name": "Garden Projects",
    "provider": { "@type": "ProfessionalService", "name": "Blossom" },
    "areaServed": ["Surrey", "Hampshire", "West Sussex", "East Sussex"],
    "description": "A done-for-you service for any garden improvement, installation or problem: scoped, sourced and managed through to completion."
  }""",
    "body": hero("timber-courtyard.jpg", "A contemporary timber courtyard garden with layered planting and decking",
        "Done-for-you Garden Projects", "Tell us what you want. We will organise everything it takes.",
        "One defined improvement or a connected series of works. Blossom turns the requirement into a plan, finds the right specialists and manages the project through to completion.",
        "Tell us about your project") + '''

    <section class="section">
      <div class="wrap-narrow reveal">
        <span class="eyebrow">Any scale, any starting point</span>
        <h2>The project does not need to begin with a garden design.</h2>
        <p>You might want a garden office, a pergola, better lighting, a new terrace or someone to fix a project that has gone wrong. Blossom starts with the outcome, then works out the design, technical and delivery support needed to achieve it.</p>
      </div>
    </section>

    <section>
      <div class="check-grid">
        <div class="check-cell reveal">
          <span class="eyebrow">Outdoor rooms and buildings</span>
          <h2>Useful space, properly integrated into the garden.</h2>
          <ul class="check-list" style="font-size: 15px; columns: 1;">
            <li>Garden offices and meeting rooms</li>
            <li>Gyms, yoga and wellness studios</li>
            <li>Art, music, photography and maker studios</li>
            <li>Therapy and treatment rooms</li>
            <li>Guest rooms and annexes, subject to consent</li>
            <li>Summerhouses and entertainment rooms</li>
            <li>Workshops, potting sheds and storage buildings</li>
            <li>Greenhouses, glasshouses and polytunnels</li>
            <li>Pool houses, changing rooms and sauna buildings</li>
            <li>Garages, carports, bike and equipment stores</li>
          </ul>
          <p style="font-size: 15px;">Blossom can manage feasibility, design, planning advice, supplier selection, groundworks, utilities, fit-out and the surrounding landscape.</p>
        </div>
        <div class="check-cell photo-cell"><img src="assets/img/photos/garden-room.jpg" alt="A vintage garden room with an armchair, sunlight and climbing plants"></div>
        <div class="check-cell photo-cell"><img src="assets/img/photos/pergola-evening.jpg" alt="A timber pergola at dusk with curtains, string lights and cushioned seating"></div>
        <div class="check-cell tint-cell reveal">
          <span class="eyebrow">Outdoor living</span>
          <h2>Make the garden a place you use, not simply look at.</h2>
          <ul class="check-list" style="font-size: 15px;">
            <li>Pergolas, pavilions and covered terraces</li>
            <li>Outdoor kitchens and barbecue stations</li>
            <li>Garden bars and entertaining spaces</li>
            <li>Dining terraces and built-in seating</li>
            <li>Fireplaces, firepits and heating</li>
            <li>Outdoor cinemas, audio and lighting</li>
            <li>Pools, spas, hot tubs and cold plunges</li>
            <li>Saunas, outdoor showers and wellness areas</li>
            <li>Play areas, sports courts and exercise spaces</li>
          </ul>
        </div>
        <div class="check-cell tint-cell tint-butter reveal">
          <span class="eyebrow">Landscape and infrastructure</span>
          <h2>The work beneath and around the finished garden.</h2>
          <ul class="check-list" style="font-size: 15px;">
            <li>Patios, paths, steps and driveways</li>
            <li>Walls, retaining structures and level changes</li>
            <li>Fencing, gates, screens and access control</li>
            <li>Drainage, rainwater management and irrigation</li>
            <li>Garden lighting, exterior power and connectivity</li>
            <li>Ponds, streams, fountains and water features</li>
            <li>Planting, lawns, meadows, orchards and kitchen gardens</li>
            <li>Privacy, screening and acoustic improvements</li>
            <li>Security, CCTV and smart garden technology</li>
          </ul>
        </div>
        <div class="check-cell photo-cell"><img src="assets/img/photos/tiled-steps.jpg" alt="Patterned tiled garden steps between stone walls, urns and clipped hedges"></div>
        <div class="check-cell photo-cell"><img src="assets/img/photos/light-arches.jpg" alt="Arches of warm lights over a hedged garden path in the evening"></div>
        <div class="check-cell reveal">
          <span class="eyebrow">Bespoke details</span>
          <h2>Designed for the place rather than selected as an afterthought.</h2>
          <ul class="check-list" style="font-size: 15px;">
            <li>Bespoke furniture and built-in seating</li>
            <li>Planters, screens and trellis</li>
            <li>Outdoor cabinetry and storage</li>
            <li>Fire features and water features</li>
            <li>Stone, metal and timber commissions</li>
            <li>Sculpture, mirrors and garden art</li>
            <li>Antiques, architectural salvage and reclaimed materials</li>
            <li>Seasonal styling and event preparation</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap grid-2" style="align-items: start;">
        <div class="reveal">
          <span class="eyebrow">What Blossom does</span>
          <h2>The client-side work that turns an idea into a finished result.</h2>
          <p>You retain the important decisions. Blossom takes away the chasing, comparing, coordinating and problem solving.</p>
          <h3 style="margin-top: 28px;">Specialist work</h3>
          <p>Planning consultants, architects, structural engineers, arborists, ecologists, electricians, gas engineers and other regulated specialists are appointed when the project requires them. Blossom coordinates their contribution and keeps it connected to the wider garden.</p>
          <h3 style="margin-top: 28px;">Fees</h3>
          <p>As a guide, project management is from £950 a month while work is on site, or 10 percent of the build cost for full management from tender to handover. The basis is agreed and confirmed in writing before the project starts.</p>
        </div>
        <ol class="process reveal">
          <li><p>Define the requirement and success criteria</p></li>
          <li><p>Inspect the garden and identify constraints</p></li>
          <li><p>Establish the likely route, budget and programme</p></li>
          <li><p>Coordinate any design or technical advice</p></li>
          <li><p>Source and assess suitable suppliers</p></li>
          <li><p>Compare proposals on a consistent basis</p></li>
          <li><p>Agree scope, responsibilities and payment stages</p></li>
          <li><p>Coordinate access, logistics and dependencies</p></li>
          <li><p>Monitor delivery, cost, quality and changes</p></li>
          <li><p>Manage defects, handover, warranties and aftercare</p></li>
        </ol>
      </div>
    </section>

    <section class="section section-deep tint-rose">
      <div class="wrap-narrow center reveal">
        <h2>What would you like the garden to do next?</h2>
        <div class="btn-row" style="justify-content: center;">
          <a class="cta-link big" href="contact.html">Discuss a Garden Project</a>
        </div>
      </div>
    </section>
''',
}

GARDEN_DESIGN = {
    "path": "garden-design.html",
    "title": "Garden Design in Surrey, Hampshire & Sussex | Blossom",
    "desc": "Whole-garden and individual-area design grounded in your property, budget and lifestyle, with optional complete project delivery and ongoing garden management.",
    "active": "garden-design.html",
    "schema": """{
    "@context": "https://schema.org",
    "@type": "Service",
    "serviceType": "Garden design",
    "name": "Garden Design",
    "provider": { "@type": "ProfessionalService", "name": "Blossom" },
    "areaServed": ["Surrey", "Hampshire", "West Sussex", "East Sussex"],
    "description": "Whole-garden and individual-area design grounded in the property, the ground and the way you want to live."
  }""",
    "body": hero("lavender-path.jpg", "Lavender leaning over stone stepping slabs on a gravel garden path",
        "Garden Design", "Designed for the property, the ground and the way you want to live.",
        "A complete new garden, a better use for one part of it or a considered improvement that works with what is already there.") + '''

    <section class="split">
      <div class="split-copy reveal">
        <span class="eyebrow">Design at the right scale</span>
        <h2>Start again, work in phases or improve what deserves to stay.</h2>
        <p>Not every garden needs a complete redesign. Blossom can create a masterplan for the whole property, redesign a specific area, resolve a difficult problem or develop one feature such as an outdoor room, entertaining terrace or planting scheme.</p>
        <h3 style="margin-top: 28px;">Whole-garden masterplanning</h3>
        <p>A masterplan establishes the long-term shape of the garden even when delivery will happen over several years. Individual projects can then be completed in the right order without creating conflicts, wasted work or disconnected results.</p>
      </div>
      <div class="split-photo"><img src="assets/img/photos/sketch-plans.jpg" alt="Concept layouts being sketched in pen on paper"></div>
    </section>

    <section class="section section-deep tint-lilac">
      <div class="wrap">
        <div class="center reveal">
          <span class="eyebrow">What design can include</span>
        </div>
        <div class="grid-3" style="margin-top: 26px;">
          <ul class="check-list reveal" style="font-size: 15px;">
            <li>Garden strategy and client brief</li>
            <li>Measured survey and site analysis</li>
            <li>Concept and masterplan</li>
            <li>Levels, layout and circulation</li>
            <li>Materials and hard-landscape design</li>
          </ul>
          <ul class="check-list reveal" style="font-size: 15px;">
            <li>Planting design and plant schedules</li>
            <li>Lighting and irrigation coordination</li>
            <li>Drainage and water-management strategy</li>
            <li>Garden buildings and outdoor-living integration</li>
            <li>Furniture, features and styling</li>
          </ul>
          <ul class="check-list reveal" style="font-size: 15px;">
            <li>3D visualisation and design presentations</li>
            <li>Construction drawings and specifications</li>
            <li>Tender and contractor information</li>
            <li>Phasing and implementation plan</li>
            <li>Maintenance and long-term development plan</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="split flip">
      <div class="split-copy reveal">
        <span class="eyebrow">Planting</span>
        <h2>Right plant, right place, right level of care.</h2>
        <p>Planting is developed around soil, aspect, exposure, drainage, seasonal structure and the amount of gardening you want to do. Schemes can be formal, naturalistic, productive, wildlife-focused, drought resilient or any considered combination that belongs to the property.</p>
      </div>
      <div class="split-photo"><img src="assets/img/photos/planting-plan.jpg" alt="A hand-coloured planting plan drawing full of plant symbols and labels"></div>
    </section>

    <section class="section section-deep">
      <div class="wrap">
        <div class="grid-2" style="align-items: start;">
          <div class="reveal">
            <span class="eyebrow">Designed to be delivered</span>
            <h2>The drawings are only useful if the garden can be built and cared for.</h2>
            <p>Budget, access, construction, maintenance and procurement are considered as the design develops. You can take the completed information to your own contractor, ask Blossom to manage the project or continue into a complete transformation.</p>
          </div>
          <div class="reveal">
            <span class="eyebrow">Design fees</span>
            <h2>Defined by the work, agreed before it starts.</h2>
            <p>Design is proposed in clear stages with an output and fee for each. Surveys and specialist advice are identified separately, so you know what is included and what decisions sit ahead.</p>
            <p>As a guide, design fees are typically 10 to 15 percent of the build budget, agreed as a fixed fee before work starts. Most full garden designs start from around £3,500. Every figure is confirmed in writing before the work begins.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap-narrow center reveal">
        <h2>Begin with a clear view of what the garden could become.</h2>
        <div class="btn-row" style="justify-content: center;">
          <a class="cta-link big" data-event="book_review_click" href="contact.html">Book a Garden Review</a>
        </div>
      </div>
    </section>
''',
}

TRANSFORMATION = {
    "path": "complete-garden-transformation.html",
    "title": "Complete Garden Transformation | Design to Delivery | Blossom",
    "desc": "One accountable lead for garden design, permissions, procurement, contractors, construction, planting and handover across Surrey, Hampshire and Sussex.",
    "active": "complete-garden-transformation.html",
    "schema": """{
    "@context": "https://schema.org",
    "@type": "Service",
    "serviceType": "Complete garden transformation",
    "name": "Complete Garden Transformation",
    "provider": { "@type": "ProfessionalService", "name": "Blossom" },
    "areaServed": ["Surrey", "Hampshire", "West Sussex", "East Sussex"],
    "description": "One accountable lead for garden design, permissions, procurement, contractors, construction, planting and handover."
  }""",
    "body": hero("pergola-path.jpg", "A brick path leading through a leafy pergola into an established garden",
        "The complete service", "One lead, from the first idea to the finished garden.",
        "You make the important decisions. Blossom does the planning, sourcing, coordinating, checking and chasing required to deliver them.",
        "Discuss a transformation") + '''

    <section class="section">
      <div class="wrap-narrow reveal">
        <span class="eyebrow">Why one lead</span>
        <h2>Coordinating a garden transformation is a job. It should not become yours.</h2>
        <p>A substantial garden can involve surveyors, designers, planning advisers, landscape contractors, electricians, arborists, nurseries, building suppliers and specialist installers. Managed separately, each becomes another relationship, quotation, diary and risk for the homeowner.</p>
        <p>Blossom provides a single point of accountability across the entire journey. Information, decisions and quality are carried from the original brief through to completion and aftercare.</p>
      </div>
    </section>

    <section class="section section-deep" style="padding-top: 44px;">
      <div class="wrap">
        <div class="center reveal">
          <span class="eyebrow">The journey</span>
          <h2>Clear stages with a decision at each point.</h2>
        </div>
        <div class="grid-2" style="margin-top: 40px; align-items: start;">
          <ol class="process reveal">
            <li><h3>Garden Review</h3><p>We understand the property, the problems, the ambition, the likely constraints and the level of investment involved.</p></li>
            <li><h3>Survey and brief</h3><p>We establish what exists, what must change and what the completed garden needs to achieve.</p></li>
            <li><h3>Concept and masterplan</h3><p>The overall design, structure, materials, planting and major features are developed as one coherent garden.</p></li>
            <li><h3>Technical development</h3><p>Drawings, specifications, permissions and specialist input turn the approved concept into information that can be priced and delivered.</p></li>
          </ol>
          <ol class="process reveal" style="counter-reset: step 4;">
            <li><h3>Procurement</h3><p>Suitable contractors and suppliers are identified, proposals are compared and appointments are made against a clear scope and programme.</p></li>
            <li><h3>Delivery</h3><p>Blossom coordinates the work, communication, decisions, progress, costs, changes and quality on the client's behalf.</p></li>
            <li><h3>Completion and establishment</h3><p>Defects are recorded and managed, warranties and care information are assembled and the garden moves into its establishment period.</p></li>
            <li><h3>Ongoing management</h3><p>If you want Blossom to retain responsibility, Your Garden Manager continues the plan, supplier coordination and future improvement.</p></li>
          </ol>
        </div>
      </div>
    </section>

    <section class="split">
      <div class="split-copy reveal">
        <span class="eyebrow">Budget and programme</span>
        <h2>Ambition, money and time kept in the same conversation.</h2>
        <p>The working budget and desired completion are discussed from the outset. Estimates become firmer as the design, specification and supplier proposals develop. Changes are recorded and their implications explained before they are approved.</p>
        <p>As a guide, complete garden transformations of this kind typically sit between £30,000 and £80,000 all in, and we design to an agreed budget from day one. No website range can price a particular garden without understanding its size, access, levels, ground, structures and specification. The Garden Review exists to establish a realistic starting position.</p>
      </div>
      <div class="split-photo"><img src="assets/img/photos/patio-dining.jpg" alt="A finished modern garden with dining terrace, raised beds and granite steps"></div>
    </section>

    <section class="section section-yew">
      <div class="wrap-narrow center reveal">
        <h2>One garden. One plan. One accountable lead.</h2>
        <div class="btn-row on-dark" style="justify-content: center;">
          <a class="cta-link big" data-event="book_review_click" href="contact.html">Book a Garden Review</a>
        </div>
      </div>
    </section>
''',
}

YOUR_GARDEN_MANAGER = {
    "path": "your-garden-manager.html",
    "title": "Ongoing Garden Management | Your Garden Manager | Blossom",
    "desc": "Ongoing garden management for homeowners across Surrey, Hampshire and Sussex. Blossom coordinates maintenance, suppliers, systems, repairs and future improvements.",
    "active": "",
    "schema": """{
    "@context": "https://schema.org",
    "@type": "Service",
    "serviceType": "Ongoing garden management",
    "name": "Your Garden Manager",
    "provider": { "@type": "ProfessionalService", "name": "Blossom" },
    "areaServed": ["Surrey", "Hampshire", "West Sussex", "East Sussex"],
    "description": "Ongoing responsibility for maintenance, suppliers, problems and improvement, with one number to call whenever the garden needs attention."
  }""",
    "body": hero("garden-lighting.jpg", "Warm bollard lighting glowing among shrubs and mulched beds at dusk",
        "Your Garden Manager", "One number to call whenever the garden needs attention.",
        "Planned care, reliable suppliers, responsive problem solving and a garden that continues to improve rather than gradually getting away from you.",
        "Discuss ongoing management") + '''

    <section class="section">
      <div class="wrap-narrow reveal">
        <span class="eyebrow">The retained service</span>
        <h2>We keep hold of the detail so you do not have to.</h2>
        <p>Your Garden Manager is for homeowners who want the garden looked after as an important part of the property. Blossom understands the plan, knows the suppliers, tracks what is due and becomes the first call for anything new or unexpected.</p>
      </div>
    </section>

    <section class="section section-deep" style="padding-top: 44px;">
      <div class="wrap grid-3">
        <div class="reveal">
          <span class="eyebrow">Planned garden management</span>
          <ul class="check-list" style="font-size: 15px;">
            <li>Annual condition and priorities review</li>
            <li>Garden asset and supplier register</li>
            <li>Seasonal maintenance programme</li>
            <li>Planting, lawn, tree and hedge planning</li>
            <li>Irrigation and water-management checks</li>
            <li>Lighting, power and equipment servicing</li>
            <li>Pond, pool, spa and water-feature coordination</li>
            <li>Garden-building and structure maintenance</li>
            <li>Furniture and surface care</li>
            <li>Budget and improvement planning</li>
          </ul>
        </div>
        <div class="reveal">
          <span class="eyebrow">People and performance</span>
          <ul class="check-list" style="font-size: 15px;">
            <li>Gardener and contractor briefing</li>
            <li>Supplier scheduling and access</li>
            <li>Quotation comparison</li>
            <li>Work-quality checks</li>
            <li>Invoice review</li>
            <li>Issue escalation and resolution</li>
            <li>Warranty and defect tracking</li>
            <li>Replacement supplier sourcing</li>
          </ul>
        </div>
        <div class="reveal">
          <span class="eyebrow">Reactive support</span>
          <ul class="check-list" style="font-size: 15px;">
            <li>Storm and tree damage</li>
            <li>Flooding and drainage failure</li>
            <li>Irrigation, lighting and gate faults</li>
            <li>Plant losses, pests and disease</li>
            <li>Pond, pool and equipment problems</li>
            <li>Contractor and supplier failures</li>
            <li>Urgent preparation for guests, events or sale</li>
          </ul>
          <p class="smallprint">Response times and emergency arrangements depend on the service level and specialist availability. They are agreed as part of the management plan.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap grid-2" style="align-items: start;">
        <div class="reveal">
          <span class="eyebrow">Continuous improvement</span>
          <h2>Care for today, decisions for what comes next.</h2>
          <p>The retained relationship makes future projects easier. Blossom already understands the property, the budget, the existing systems and the way you use the garden. Improvements can be identified early, planned in the right season and delivered without starting from zero each time.</p>
        </div>
        <div class="reveal">
          <span class="eyebrow">Management fees</span>
          <h2>An onboarding stage and an agreed monthly service.</h2>
          <p>The Garden Management Review establishes the starting point. As a guide, the ongoing retainer starts from £650 a year and reflects the garden's scale, complexity, supplier network, inspection frequency and the level of responsibility you want Blossom to take.</p>
          <p>Projects and significant specialist works are scoped separately. There are no hidden charges or undisclosed commercial arrangements.</p>
        </div>
      </div>
    </section>

    <section class="section section-deep tint-rose">
      <div class="wrap-narrow center reveal">
        <h2>Give the garden a manager, not another list of jobs.</h2>
        <div class="btn-row" style="justify-content: center;">
          <a class="cta-link big" data-event="book_review_click" href="contact.html">Book a Garden Management Review</a>
        </div>
      </div>
    </section>
''',
}

GARDEN_REVIEW = {
    "path": "garden-review.html",
    "title": "Garden Review and Management Plan | Blossom",
    "desc": "An expert review of your garden, its condition, problems, potential and priorities, followed by a clear recommended plan.",
    "active": "",
    "schema": """{
    "@context": "https://schema.org",
    "@type": "Service",
    "serviceType": "Garden review",
    "name": "Garden Review",
    "provider": { "@type": "ProfessionalService", "name": "Blossom" },
    "areaServed": ["Surrey", "Hampshire", "West Sussex", "East Sussex"],
    "description": "A structured on-site review of the garden as it is today, what you want from it and the most sensible route forward."
  }""",
    "body": hero("walled-garden.jpg", "A wrought iron gate in a walled garden framed by catmint borders",
        "The starting point", "Understand what the garden needs before deciding what to buy.",
        "A structured on-site review of the garden as it is today, what you want from it and the most sensible route forward.") + '''

    <section class="section">
      <div class="wrap grid-2" style="align-items: start;">
        <div class="reveal">
          <span class="eyebrow">Who it is for</span>
          <h2>Useful when you know something needs to change, but not necessarily what.</h2>
          <ul class="check-list">
            <li>You have inherited a garden and need a plan</li>
            <li>The garden has several unrelated problems</li>
            <li>You want to improve it without starting again</li>
            <li>You are considering a building, pool or major feature</li>
            <li>You need help prioritising expenditure</li>
            <li>Maintenance is inconsistent or difficult to manage</li>
            <li>A project has stalled or gone wrong</li>
            <li>You want Blossom to manage the garden ongoing</li>
          </ul>
        </div>
        <div class="reveal">
          <span class="eyebrow">What we examine</span>
          <ul class="check-list" style="font-size: 15px;">
            <li>How the garden is used</li>
            <li>Condition and performance</li>
            <li>Planting, trees and lawns</li>
            <li>Levels, surfaces and boundaries</li>
            <li>Drainage, irrigation and water</li>
            <li>Buildings, structures and equipment</li>
            <li>Lighting, power and security</li>
            <li>Maintenance and existing suppliers</li>
            <li>Immediate risks and repairs</li>
            <li>Future opportunities</li>
            <li>Likely dependencies, permissions and specialist input</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section section-deep tint-lilac">
      <div class="wrap grid-2" style="align-items: start;">
        <div class="reveal">
          <span class="eyebrow">What you receive</span>
          <h2>A practical route, not a generic inspiration board.</h2>
          <p>As a guide, a Garden Review is £295, confirmed in writing before booking, and is taken off any later design or management fee. If more technical investigation is required, it is recommended rather than guessed at.</p>
        </div>
        <div class="reveal">
          <div class="receive" style="background: var(--surface);">
            <h4>You receive</h4>
            <ul>
              <li>Summary of what we found</li>
              <li>Immediate priorities</li>
              <li>Recommended projects or interventions</li>
              <li>Suggested sequence</li>
              <li>Budget considerations and unknowns</li>
              <li>Specialists or surveys likely to be required</li>
              <li>Recommended next service</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap-narrow center reveal">
        <h2>Start with clarity.</h2>
        <div class="btn-row" style="justify-content: center;">
          <a class="cta-link big" data-event="book_review_click" href="contact.html">Request a Garden Review</a>
        </div>
      </div>
    </section>
''',
}

HOW_IT_WORKS = {
    "path": "how-it-works.html",
    "title": "How Complete Garden Management Works | Blossom",
    "desc": "How Blossom reviews, plans, sources, delivers and manages garden work for homeowners across Surrey, Hampshire and Sussex.",
    "active": "how-it-works.html",
    "schema": "",
    "body": hero("grass-light.jpg", "Low evening sun catching long garden grass",
        "How Blossom works", "You keep the decisions. We take away the management burden.",
        "The process adapts to the job, but the discipline stays the same: understand, define, source, deliver and manage.", "") + '''

    <section class="section" style="padding-top: 40px;">
      <div class="wrap">

        <div class="stage reveal">
          <div>
            <span class="stage-num">01</span>
            <h3>Understand</h3>
            <p>We listen to what you want, inspect the garden and establish the real problem or opportunity. Where necessary, we coordinate surveys or specialist advice before recommending a solution.</p>
            <div class="receive tint-lilac">
              <h4>You receive</h4>
              <ul>
                <li>A shared understanding of the requirement</li>
                <li>Known constraints and important unknowns</li>
                <li>A recommended route forward</li>
              </ul>
            </div>
          </div>
          <div class="stage-photo photo-block photo-wide"><img src="assets/img/photos/formal-garden.jpg" alt="A formal garden with clipped box balls, terracotta pots and a paved path" width="1800" height="1192"></div>
        </div>

        <div class="stage flip reveal">
          <div>
            <span class="stage-num">02</span>
            <h3>Define</h3>
            <p>We turn the requirement into a clear scope, desired result, working budget, responsibilities and programme. For design work, this includes the agreed design brief.</p>
            <div class="receive tint-lilac">
              <h4>You receive</h4>
              <ul>
                <li>A written scope or brief</li>
                <li>An agreed decision and approval process</li>
                <li>A clear explanation of Blossom's fees</li>
              </ul>
            </div>
          </div>
          <div class="stage-photo photo-block photo-wide"><img src="assets/img/photos/olive-steps.jpg" alt="Stone steps set into a white rendered wall beneath an old olive tree" width="1440" height="1800"></div>
        </div>

        <div class="stage reveal">
          <div>
            <span class="stage-num">03</span>
            <h3>Design and plan</h3>
            <p>The solution is designed and developed to the level the project requires. Products, materials, specialists, permissions, buildability, maintenance and dependencies are resolved before commitments are made.</p>
            <div class="receive tint-lilac">
              <h4>You receive</h4>
              <ul>
                <li>The design or proposed solution</li>
                <li>Specifications and supporting information</li>
                <li>Updated budget and programme</li>
              </ul>
            </div>
          </div>
          <div class="stage-photo photo-block photo-wide"><img src="assets/img/photos/sketch-plans.jpg" alt="Concept layouts being sketched in pen on paper" width="1800" height="1200"></div>
        </div>

        <div class="stage flip reveal">
          <div>
            <span class="stage-num">04</span>
            <h3>Source</h3>
            <p>We identify suitable suppliers and contractors, issue consistent information, clarify proposals and help you choose on capability, value and fit rather than headline price alone.</p>
            <div class="receive tint-lilac">
              <h4>You receive</h4>
              <ul>
                <li>Comparable proposals</li>
                <li>Clear recommendations</li>
                <li>Agreed appointments and responsibilities</li>
              </ul>
            </div>
          </div>
          <div class="stage-photo photo-block photo-wide"><img src="assets/img/photos/courtyard-bench.jpg" alt="A calm courtyard garden with soft planting and a curved bench" width="1193" height="1800"></div>
        </div>

        <div class="stage reveal">
          <div>
            <span class="stage-num">05</span>
            <h3>Deliver</h3>
            <p>Blossom becomes the coordinating point for the client, design team, suppliers and contractors. We manage information, decisions, programme, expenditure, issues and quality at the frequency agreed for the project.</p>
            <div class="receive tint-lilac">
              <h4>You receive</h4>
              <ul>
                <li>Progress updates</li>
                <li>Visible decisions and changes</li>
                <li>Quality observations and issue management</li>
              </ul>
            </div>
          </div>
          <div class="stage-photo photo-block photo-wide"><img src="assets/img/photos/modern-pergola.jpg" alt="A modern louvred pergola over rattan garden seating, cleanly built and finished" width="1200" height="1800"></div>
        </div>

        <div class="stage flip reveal">
          <div>
            <span class="stage-num">06</span>
            <h3>Complete</h3>
            <p>We record incomplete or defective work, coordinate its resolution, gather relevant care and warranty information and establish what the garden needs next.</p>
            <div class="receive tint-lilac">
              <h4>You receive</h4>
              <ul>
                <li>Completion and defect record</li>
                <li>Care and warranty information</li>
                <li>Recommended establishment or management plan</li>
              </ul>
            </div>
          </div>
          <div class="stage-photo photo-block photo-wide"><img src="assets/img/photos/daisies.jpg" alt="Daisies in long meadow grass lit by low evening sun" width="1800" height="1200"></div>
        </div>

        <div class="stage reveal">
          <div>
            <span class="stage-num">07</span>
            <h3>Manage</h3>
            <p>Where Blossom remains as Your Garden Manager, the project becomes part of the garden's ongoing operating plan rather than a disconnected one-off intervention.</p>
          </div>
          <div class="stage-photo photo-block photo-wide"><img src="assets/img/photos/urns-terrace.jpg" alt="A lush established garden with aged stone urns, woven chairs and layered planting" width="1800" height="1186"></div>
        </div>

      </div>
    </section>

    <section class="section section-deep">
      <div class="wrap grid-2" style="align-items: start;">
        <div class="reveal">
          <span class="eyebrow">Approvals and authority</span>
          <h2>We act for you, but we do not make unapproved commitments with your money.</h2>
          <p>The appointment sets out what Blossom can decide, what requires approval and any financial thresholds. You can delegate routine decisions while retaining control over scope, budget and significant changes.</p>
        </div>
        <div class="reveal">
          <span class="eyebrow">Transparency</span>
          <h2>The commercial arrangement is stated before the work starts.</h2>
          <p>Blossom may be paid through fixed fees, staged design fees, project-management fees, retainers, procurement fees or disclosed supplier arrangements, depending on the service. The basis is confirmed in writing so you understand who is being paid, by whom and for what.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap-narrow center reveal">
        <h2>One process, shaped around what the garden needs.</h2>
        <div class="btn-row" style="justify-content: center;">
          <a class="cta-link big" href="contact.html">Start the conversation</a>
        </div>
      </div>
    </section>
''',
}

GARDEN_SERVICES = {
    "path": "garden-services.html",
    "title": "Garden Services A to Z | Complete Garden Management | Blossom",
    "desc": "The complete range of garden design, outdoor living, garden buildings, landscaping, project management and ongoing garden services Blossom can coordinate.",
    "active": "",
    "schema": "",
    "body": hero("courtyard-dusk.jpg", "A courtyard garden at dusk with stone path, boulders and warm lighting",
        "Services A to Z", "If it belongs outside the house, ask Blossom.",
        "The list is intentionally broad. Blossom manages the whole garden and assembles the specialist team each requirement needs.",
        "Tell us what your garden needs") + '''

    <section class="section" style="padding-top: 40px;">
      <div class="wrap">
        <div class="grid-4" style="align-items: start;">
          <div class="card reveal">
            <p class="card-meta">Advice, assessment and planning</p>
            <ul class="check-list" style="font-size: 14.5px;">
              <li>Garden consultations and reviews</li>
              <li>Condition and potential assessments</li>
              <li>Maintenance and supplier reviews</li>
              <li>Budget and priority planning</li>
              <li>Pre-purchase and pre-sale garden advice</li>
              <li>Project rescue and second opinions</li>
              <li>Masterplans and phased development plans</li>
              <li>Planning and specialist coordination</li>
            </ul>
          </div>
          <div class="card reveal">
            <p class="card-meta">Garden and planting design</p>
            <ul class="check-list" style="font-size: 14.5px;">
              <li>Complete garden design</li>
              <li>Garden renovation</li>
              <li>Individual-area design</li>
              <li>Planting and border design</li>
              <li>Trees, hedges, orchards and productive gardens</li>
              <li>Wildlife, sensory and climate-resilient gardens</li>
              <li>Lighting, irrigation and drainage coordination</li>
              <li>Technical drawings and specifications</li>
            </ul>
          </div>
          <div class="card reveal">
            <p class="card-meta">Garden buildings and structures</p>
            <ul class="check-list" style="font-size: 14.5px;">
              <li>Offices, gyms and studios</li>
              <li>Guest rooms and annexes</li>
              <li>Summerhouses and entertainment rooms</li>
              <li>Sheds, workshops and storage</li>
              <li>Greenhouses and glasshouses</li>
              <li>Pergolas, pavilions and covered terraces</li>
              <li>Pool houses, saunas and changing rooms</li>
              <li>Garages, carports and equipment stores</li>
            </ul>
          </div>
          <div class="card reveal">
            <p class="card-meta">Outdoor living and recreation</p>
            <ul class="check-list" style="font-size: 14.5px;">
              <li>Outdoor kitchens and bars</li>
              <li>Dining and entertaining terraces</li>
              <li>Fireplaces, firepits and heating</li>
              <li>Outdoor cinemas, sound and lighting</li>
              <li>Pools, spas, hot tubs and cold plunges</li>
              <li>Sports, exercise and play spaces</li>
              <li>Pet areas and animal structures</li>
              <li>Bespoke furniture, art and styling</li>
            </ul>
          </div>
          <div class="card reveal">
            <p class="card-meta">Landscape, water and infrastructure</p>
            <ul class="check-list" style="font-size: 14.5px;">
              <li>Patios, paths, steps and driveways</li>
              <li>Walls, terraces, fencing and gates</li>
              <li>Drainage, rain gardens and water harvesting</li>
              <li>Irrigation and water management</li>
              <li>Ponds, streams, fountains and water features</li>
              <li>Garden lighting, exterior power and connectivity</li>
              <li>Security, access and smart technology</li>
              <li>Groundworks, levels and site access</li>
            </ul>
          </div>
          <div class="card reveal">
            <p class="card-meta">Project delivery</p>
            <ul class="check-list" style="font-size: 14.5px;">
              <li>Feasibility and scope definition</li>
              <li>Budget and programme development</li>
              <li>Designer and specialist coordination</li>
              <li>Planning and technical-adviser coordination</li>
              <li>Contractor and supplier sourcing</li>
              <li>Tendering and proposal comparison</li>
              <li>Procurement and delivery coordination</li>
              <li>Project, cost, change and quality management</li>
              <li>Defects, warranties and handover</li>
            </ul>
          </div>
          <div class="card reveal">
            <p class="card-meta">Ongoing garden management</p>
            <ul class="check-list" style="font-size: 14.5px;">
              <li>Annual garden management plans</li>
              <li>Gardener and supplier coordination</li>
              <li>Seasonal schedules and inspections</li>
              <li>Tree, lawn and planting programmes</li>
              <li>Building, lighting, irrigation and equipment servicing</li>
              <li>Quote, invoice and warranty management</li>
              <li>Reactive issue resolution</li>
              <li>Continuous improvement planning</li>
            </ul>
          </div>
          <div class="card tint-cell reveal" style="background: var(--parchment-deep);">
            <p class="card-meta">How services are delivered</p>
            <p style="font-size: 15px;">Some services are delivered directly by Blossom. Others are designed, supplied or installed by specialist partners under Blossom's coordination. The route is explained before you proceed.</p>
            <a class="card-link" href="contact.html">Tell us what your garden needs</a>
          </div>
        </div>
      </div>
    </section>
''',
}

PAGES = [GARDEN_MANAGEMENT, GARDEN_PROJECTS, GARDEN_DESIGN, TRANSFORMATION, YOUR_GARDEN_MANAGER, GARDEN_REVIEW, HOW_IT_WORKS, GARDEN_SERVICES]
