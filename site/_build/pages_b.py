# Content and utility pages. COPY DECK V2 verbatim.
from pages_a import hero

FAQ_ITEMS = [
    ("Is Blossom a garden designer, project manager or maintenance company?",
     "Blossom is a complete garden management service. Garden design and project management are core capabilities, but the responsibility is broader: understanding what the garden needs, finding and coordinating the right people, managing work and helping the garden improve over time. Maintenance can be included and managed through suitable gardening partners."),
    ("What can Blossom help with?",
     "Anything connected to the garden or outdoor property. That includes planting, landscaping and maintenance, but also garden offices, gyms, sheds, pergolas, outdoor kitchens, pools, spas, lighting, irrigation, security, furniture, play, sport and bespoke projects. If specialist expertise is required, Blossom sources and coordinates it."),
    ("Does Blossom carry out all the work itself?",
     "No single business should claim to be expert in every trade involved in a substantial garden. Blossom owns the brief, design where appointed, commercial process, coordination and client experience. Appropriately competent specialists carry out regulated and trade-specific work."),
    ("Can you manage the gardener or contractors we already use?",
     "Yes. Good existing suppliers do not need to be replaced. Blossom reviews the current arrangement, clarifies responsibilities and coordinates everyone against the same garden plan. Where a capability or service standard is missing, we help fill the gap."),
    ("Can you take over a project that has already started?",
     "Yes, subject to an initial review. We establish the current scope, appointments, expenditure, progress, defects and outstanding decisions before proposing a recovery or completion plan."),
    ("Can you manage a design created by somebody else?",
     "Yes. We first review whether the information is sufficiently complete, buildable and consistent with the working budget. Any gaps are resolved with the original designer or another suitable specialist before delivery continues."),
    ("Can Blossom manage just one project?",
     "Yes. Garden Projects is a done-for-you service for one defined improvement, installation, repair or problem. You do not need an ongoing management agreement or a complete garden redesign."),
    ("Do I have to start with a Garden Review?",
     "It is the best starting point when the requirement is broad, unclear or connected to several parts of the garden. A well-defined project may begin with a shorter scoping conversation before we confirm the appropriate next step."),
    ("How does ongoing garden management work?",
     "It begins with an onboarding review and management plan. We then agree the inspections, supplier coordination, reporting, reactive support and decision authority required. The service operates under an agreed retainer, while significant projects are scoped separately."),
    ("How are Blossom's fees calculated?",
     "The basis depends on the work. It may be a fixed consultation fee, staged design fee, fixed project fee, monthly project-management fee, percentage fee, ongoing retainer or a disclosed procurement arrangement. The basis and inclusions are confirmed in writing before appointment."),
    ("Does Blossom receive supplier commissions?",
     "Blossom does not use hidden commercial arrangements. If a relevant supplier commission, procurement fee or product margin applies, it is disclosed as part of the proposal before you approve the appointment or purchase."),
    ("Will Blossom control payments to contractors?",
     "The appointment defines Blossom's authority. We can review applications for payment, compare them with progress and make recommendations. Payments remain subject to the contract and the approval process agreed with you."),
    ("Do you guarantee a contractor's work?",
     "The contractor or supplier remains responsible for its work and warranties. Blossom manages scope, information, observation, defects and escalation within its appointment, but does not replace the legal responsibilities of the appointed specialist."),
    ("Do garden buildings require planning permission?",
     "Some can be built under permitted-development rights, while others require planning permission, Building Regulations approval or specialist advice. Location, height, use, boundary position, listed status and designated land can all affect the route. Blossom identifies the likely requirements and coordinates qualified advice where needed."),
    ("Can the garden be improved in phases?",
     "Yes. A whole-garden masterplan can establish the long-term direction, then projects can be prioritised and delivered in a sequence that avoids abortive work and keeps each phase useful."),
    ("Which areas do you cover?",
     "The core service area is Surrey, Hampshire and Sussex. Travel depends on the work and the frequency of visits required. Design-only and specialist commissions may be possible further away."),
    ("What if Blossom is not the right business for the job?",
     "We will say so. If the requirement is better handled directly by a specialist, we can recommend the right route rather than create unnecessary management around a simple task."),
]


def _faq_schema():
    import json
    entities = [{"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ_ITEMS]
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities},
                      indent=2, ensure_ascii=False)


def _faq_body():
    blocks = []
    for q, a in FAQ_ITEMS:
        blocks.append('          <details>\n            <summary>%s</summary>\n            <div class="faq-body"><p>%s</p></div>\n          </details>' % (q, a))
    return hero("tiled-steps.jpg", "Patterned tiled garden steps between stone walls and clipped hedges",
        "Questions, answered clearly", "What does complete garden management actually mean?",
        "Straight answers about garden management, design, projects, maintenance, suppliers, fees and how Blossom works.", "") + '''

    <section class="section" style="padding-top: 32px;">
      <div class="wrap">
        <div class="faq" style="margin: 0 auto;">
''' + "\n".join(blocks) + '''
        </div>
      </div>
    </section>
'''


FAQ = {
    "path": "faq.html",
    "title": "Complete Garden Management FAQ | Blossom",
    "desc": "Straight answers about garden management, design, projects, maintenance, suppliers, fees and how Blossom works.",
    "active": "",
    "schema": _faq_schema(),
    "body": _faq_body(),
}

PROJECTS = {
    "path": "projects.html",
    "title": "Garden Projects and Case Studies | Blossom",
    "desc": "Real Blossom garden reviews, designs, managed projects, transformations and ongoing garden-management case studies.",
    "active": "projects.html",
    "schema": "",
    "body": hero("patio-dining.jpg", "A finished modern garden with dining terrace, raised beds and granite steps",
        "Projects", "The problem, the plan and what changed.",
        "Blossom case studies document more than the finished photograph. They show what the client needed, how the work was organised and the difference the completed result made.", "") + '''

    <section class="split flip">
      <div class="split-copy reveal">
        <span class="eyebrow">Case study structure</span>
        <h2>What every case study will record</h2>
        <ul class="check-list" style="font-size: 15px;">
          <li>The property and garden</li>
          <li>What the client needed</li>
          <li>Why the existing position was not working</li>
          <li>The scope Blossom accepted</li>
          <li>The plan and design decisions</li>
          <li>The specialists involved</li>
          <li>The budget band, where the client permits publication</li>
          <li>The delivery programme</li>
          <li>Issues encountered and how they were resolved</li>
          <li>The completed result</li>
          <li>The ongoing management plan</li>
          <li>The client's view, published only with permission</li>
        </ul>
        <p>The first case studies will be added when real Blossom work can be documented honestly. No stock project will be presented as client evidence.</p>
      </div>
      <div class="split-photo"><img src="assets/img/photos/sketch-plans.jpg" alt="Concept layouts being sketched in pen on paper"></div>
    </section>

    <section class="section section-deep">
      <div class="wrap">
        <div class="grid-3">
          <div class="placeholder-slot"><span class="tag">Required input</span><p>First case study slot, following the structure opposite.</p></div>
          <div class="placeholder-slot"><span class="tag">Required input</span><p>Second case study slot, same structure.</p></div>
          <div class="placeholder-slot"><span class="tag">Required input</span><p>Third case study slot, same structure.</p></div>
        </div>
      </div>
    </section>
''',
}

ABOUT = {
    "path": "about.html",
    "title": "About Blossom | Design and Complete Garden Management",
    "desc": "Blossom combines design judgement with more than 30 years of project and commercial leadership to manage gardens properly from idea through delivery and ongoing care.",
    "active": "about.html",
    "schema": "",
    "body": hero("olive-steps.jpg", "Stone steps built into a white wall beneath an old olive tree",
        "About Blossom", "Design judgement. Project discipline. One person accountable.",
        "Blossom was created for homeowners who want the garden taken seriously as part of the property, without having to manage every specialist, supplier and decision themselves.", "") + '''

    <section class="section">
      <div class="wrap-narrow reveal">
        <span class="eyebrow">Why Blossom exists</span>
        <h2>The garden industry is full of capable specialists. The homeowner is still expected to manage the whole.</h2>
        <p>Designers design. Gardeners maintain. Landscapers build. Arborists, electricians, pool companies and building suppliers solve their own specialist part. The gaps between them are where decisions drift, costs hide and responsibility becomes unclear.</p>
        <p>Blossom closes those gaps. It gives the garden a single point of responsibility that can see the whole property, organise the right expertise and stay involved from the first requirement through to long-term care.</p>
      </div>
    </section>

    <section class="section section-deep">
      <div class="wrap">
        <div class="reveal">
          <span class="eyebrow">Meet the founder</span>
          <h2>Damian Hickey</h2>
        </div>
        <div class="grid-2" style="align-items: start; margin-top: 18px;">
          <div class="reveal">
            <p>Damian is a designer and project leader with more than 30 years of experience turning complex ideas into delivered outcomes for large organisations and global real-estate environments.</p>
            <p>His background spans industrial design, product and service development, materials, technology, property and the leadership of substantial, multi-disciplinary programmes. The common thread is making many moving parts work as one: understanding the real requirement, establishing a strong design direction and then managing people, money, decisions and quality through to completion.</p>
          </div>
          <div class="reveal">
            <p>Blossom brings that experience into the garden. It combines Damian's lifelong interest in design, materials and nature with the commercial discipline required to run projects on time, keep budgets visible and hold quality at the centre of every decision.</p>
            <p><strong>The ambition is simple: homeowners should be able to improve and manage the garden without becoming its unpaid project manager.</strong></p>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="center reveal">
          <span class="eyebrow">How we behave</span>
        </div>
        <div class="grid-5" style="margin-top: 32px;">
          <article class="card reveal"><h3>Accountable</h3><p>One named lead, clear responsibilities and no disappearing between stages.</p></article>
          <article class="card reveal"><h3>Considered</h3><p>The right intervention for the property, rather than selling the largest available project.</p></article>
          <article class="card reveal"><h3>Commercially clear</h3><p>Defined fees, visible decisions and disclosed commercial arrangements.</p></article>
          <article class="card reveal"><h3>Independent in judgement</h3><p>Recommendations based on the client's requirement, quality, value and fit.</p></article>
          <article class="card reveal"><h3>Practical</h3><p>Beautiful ideas resolved against maintenance, access, programme, budget and delivery.</p></article>
        </div>
      </div>
    </section>

    <section class="split flip">
      <div class="split-copy tint reveal">
        <span class="eyebrow">The specialist network</span>
        <h2>The right people for the garden, coordinated as one team.</h2>
        <p>Blossom builds relationships with garden designers, landscape contractors, gardeners, arborists, surveyors, engineers, planning advisers, building suppliers, craftspeople and technical specialists across the region.</p>
        <p>Partners remain responsible for their professional and trade-specific work. Blossom makes sure their contribution answers the same brief and supports the same finished result.</p>
      </div>
      <div class="split-photo"><img src="assets/img/photos/courtyard-reading.jpg" alt="A walled courtyard garden with someone reading beside a sleeping dog"></div>
    </section>

    <section class="section section-yew">
      <div class="wrap-narrow center reveal">
        <h2>The garden deserves the same quality of management as the home.</h2>
        <div class="btn-row on-dark" style="justify-content: center;">
          <a class="cta-link big" href="contact.html">Start a conversation</a>
        </div>
      </div>
    </section>
''',
}

AREAS = {
    "path": "areas.html",
    "title": "Complete Garden Management in Surrey, Hampshire and Sussex | Blossom",
    "desc": "Garden design, done-for-you projects and ongoing garden management across Surrey, Hampshire and Sussex.",
    "active": "",
    "schema": "",
    "body": hero("sunbeams-path.jpg", "Morning sun breaking through mature trees over a stone garden path",
        "Areas we cover", "Close enough to know the garden and manage it properly.",
        "The core service area covers Surrey, Hampshire and Sussex. The practical radius depends on the type of work and how often Blossom needs to be present.", "") + '''

    <section class="section">
      <div class="wrap">
        <div class="grid-3">
          <article class="card reveal">
            <p class="card-meta">Surrey</p>
            <h3>Guildford, Farnham, Godalming, Haslemere, Cranleigh, Dorking, Cobham, Esher, Weybridge, Woking and surrounding villages.</h3>
            <p>Services include Garden Reviews, design, individual projects, complete transformations and ongoing management. Properties within the Surrey Hills National Landscape, conservation areas or with protected trees may require additional advice and permissions.</p>
          </article>
          <article class="card reveal">
            <p class="card-meta">Hampshire</p>
            <h3>Bordon, Alton, Petersfield, Winchester, Alresford, Stockbridge, Romsey and surrounding villages.</h3>
            <p>The area includes town gardens, new-build plots, downland properties and rural gardens with very different soil, access and maintenance requirements. South Downs National Park and conservation constraints are identified at the appropriate stage.</p>
          </article>
          <article class="card reveal">
            <p class="card-meta">Sussex</p>
            <h3>Chichester, Midhurst, Petworth, Horsham, Haywards Heath, Cuckfield, Lewes and surrounding areas.</h3>
            <p>Blossom can coordinate design, maintenance and specialist projects across West and East Sussex, subject to the level of site presence each appointment requires.</p>
          </article>
        </div>
      </div>
    </section>

    <section style="height: 42vh; overflow: hidden; position: relative;">
      <div class="plx-bg"><img src="assets/img/photos/urns-terrace.jpg" alt="A lush established garden with aged stone urns, woven chairs and layered planting"></div>
    </section>

    <section class="section-deep tint-butter" style="padding: 26px 0;">
      <div class="wrap" style="display: flex; gap: 8px 36px; flex-wrap: wrap; align-items: baseline;">
        <h4 style="margin: 0; white-space: nowrap;">Outside the core area?</h4>
        <p style="margin: 0; font-size: 15px; color: #47555F; max-width: 78ch;">Ask. Design, remote advisory work and defined specialist projects may be practical further away. If Blossom cannot manage the requirement properly, we will say so before taking it on.</p>
      </div>
    </section>
''',
}

JOURNAL_TOPICS = [
    "What complete garden management means",
    "What a garden manager does that a gardener does not",
    "How to create an annual garden operating plan",
    "When a garden office needs planning permission",
    "How to brief and compare garden-room suppliers",
    "What to include in a landscaping quotation",
    "Who should manage a garden transformation",
    "How to phase a large garden over several years",
    "How to choose and manage a maintenance gardener",
    "Garden drainage problems and who solves them",
    "Planning a garden for year-round use",
    "The real running costs of pools, ponds and outdoor buildings",
    "How to build a reliable garden supplier network",
    "What to inspect before paying a landscape contractor",
    "How to prepare the garden for sale",
    "Why autumn and winter are planning seasons",
]

JOURNAL = {
    "path": "journal.html",
    "title": "Garden Management Journal | Blossom",
    "desc": "Practical guidance for homeowners on garden design, maintenance, garden buildings, outdoor projects, suppliers, budgets and year-round garden management.",
    "active": "",
    "schema": "",
    "body": hero("botanical-desk.jpg", "A desk of marigolds, botanical prints, a compass and garden ephemera",
        "The Garden Journal", "Practical guidance for people responsible for a garden.",
        "Design, delivery, maintenance and the decisions that sit between them, explained without trade language or sales theatre.", "") + '''

    <section class="section">
      <div class="wrap">
        <div class="grid-4">
''' + "\n".join('          <article class="card reveal"><p class="card-meta">In preparation</p><h3 style="font-size: 19px;">%s</h3></article>' % t for t in JOURNAL_TOPICS) + '''
        </div>
      </div>
    </section>
''',
}

CONTACT = {
    "path": "contact.html",
    "title": "Contact Blossom | Complete Garden Management",
    "desc": "Tell Blossom what your garden needs. Garden reviews, design, done-for-you projects, complete transformations and ongoing management across Surrey, Hampshire and Sussex.",
    "active": "",
    "schema": "",
    "body": hero("wall-pots.jpg", "A whitewashed wall of blue pots planted with geraniums in full sun",
        "Start the conversation", "Tell us what your garden needs.",
        "You do not need to identify the correct service or specialist. Describe the outcome, problem or idea and Blossom will help establish the right route.", "") + '''

    <section class="section" style="padding-top: 40px;">
      <div class="wrap">
        <div class="grid-2" style="align-items: start; gap: clamp(32px, 4vw, 56px);">
          <div class="form-panel reveal">
            <form data-enquiry id="enquiry-form" method="POST" action="https://REPLACE_WITH_FORM_ENDPOINT.example/f/blossom" data-thanks="thanks.html">
              <div class="form-grid">
                <div>
                  <label for="name">Your name</label>
                  <input type="text" id="name" name="name" autocomplete="name" required>
                </div>
                <div>
                  <label for="email">Email</label>
                  <input type="email" id="email" name="email" autocomplete="email" required>
                </div>
                <div>
                  <label for="phone">Telephone</label>
                  <input type="tel" id="phone" name="phone" autocomplete="tel">
                </div>
                <div>
                  <label for="location">Town, village or postcode</label>
                  <input type="text" id="location" name="location" required>
                </div>
                <div class="span-2">
                  <label for="help_with">What would you like help with?</label>
                  <select id="help_with" name="help_with" required>
                    <option value="">Please choose</option>
                    <option>Understanding what the garden needs</option>
                    <option>Garden design or planting design</option>
                    <option>A garden office, gym or other building</option>
                    <option>Landscaping or an outdoor-living project</option>
                    <option>Help managing an existing project</option>
                    <option>A complete garden transformation</option>
                    <option>Ongoing garden management</option>
                    <option>An urgent garden problem</option>
                    <option>Something else</option>
                    <option>Not sure yet</option>
                  </select>
                </div>
                <div class="span-2">
                  <label for="message">What would you like to achieve?</label>
                  <textarea id="message" name="message" placeholder="Tell us what you would like to change, add, solve or stop having to manage yourself."></textarea>
                </div>
                <div>
                  <label for="timing">When would you like something to happen?</label>
                  <select id="timing" name="timing">
                    <option value="">Not sure yet</option>
                    <option>As soon as practical</option>
                    <option>Within three months</option>
                    <option>Within six months</option>
                    <option>Within twelve months</option>
                    <option>Planning further ahead</option>
                  </select>
                </div>
                <div>
                  <label for="budget">Do you have a working budget or approval range?</label>
                  <select id="budget" name="budget">
                    <option value="">Prefer to discuss it</option>
                    <option>Under £10,000</option>
                    <option>£10,000 to £25,000</option>
                    <option>£25,000 to £50,000</option>
                    <option>£50,000 to £100,000</option>
                    <option>Over £100,000</option>
                    <option>Not established yet</option>
                  </select>
                </div>
                <div class="span-2 consent-row">
                  <input type="checkbox" id="consent" name="consent" required>
                  <label for="consent">I am happy for Blossom to use these details to respond to my enquiry and, where necessary, discuss the requirement with me. See the <a href="privacy.html">privacy policy</a>.</label>
                </div>
                <input type="hidden" name="utm_source"><input type="hidden" name="utm_medium">
                <input type="hidden" name="utm_campaign"><input type="hidden" name="utm_content">
                <input type="hidden" name="landing_page"><input type="hidden" name="referrer">
                <div class="span-2">
                  <button class="btn btn-primary" type="submit" style="width: 100%;">Send my enquiry</button>
                </div>
              </div>
              <p class="form-note">Your details are used to respond to this enquiry. They are not added to a marketing list without separate permission.</p>
            </form>
          </div>
          <div class="reveal">
            <span class="eyebrow">What happens next</span>
            <ol class="process">
              <li><h3>We review what you have sent</h3><p>We consider the location, requirement and likely route, then come back with any important first questions.</p></li>
              <li><h3>We arrange a short call</h3><p>The call establishes whether Blossom is the right fit and whether the next step should be a Garden Review, a defined proposal or a direct specialist route.</p></li>
              <li><h3>You receive a clear next step</h3><p>If Blossom can help, we explain the proposed service, output, fee and what information is needed to begin.</p></li>
            </ol>
          </div>
        </div>
      </div>
    </section>
''',
}

THANKS = {
    "path": "thanks.html",
    "title": "Thank You | Blossom",
    "desc": "Your enquiry has been received.",
    "active": "",
    "schema": "",
    "noindex": True,
    "body": '''    <section class="hero">
      <div class="wrap-narrow center">
        <span class="eyebrow">Enquiry received</span>
        <h1>Thank you. We will look at what your garden needs.</h1>
        <p class="standfirst" style="margin-left: auto; margin-right: auto;">You will receive a personal response with any first questions and the clearest next step.</p>
        <div class="btn-row" style="justify-content: center;">
          <a class="cta-link" href="garden-management.html">Explore complete garden management</a>
          <a class="cta-link" href="garden-services.html">See the services A to Z</a>
        </div>
      </div>
    </section>
''',
}

PRIVACY = {
    "path": "privacy.html",
    "title": "Privacy Policy | Blossom",
    "desc": "How Blossom collects, uses and protects your personal information.",
    "active": "",
    "schema": "",
    "body": '''    <section class="hero">
      <div class="wrap-narrow">
        <span class="eyebrow">Legal</span>
        <h1>Privacy policy</h1>
        <p class="standfirst">We collect only the information needed to respond to enquiries, manage appointments and deliver garden services. We do not sell personal information.</p>
        <p class="smallprint">Last updated: <span class="req-input">date on launch</span></p>
      </div>
    </section>
    <section class="section prose" style="padding-top: 0;">
      <div class="wrap-narrow">
        <h2>What we collect</h2>
        <p>When you make an enquiry, we collect your name, contact information, location and the information you provide about the garden or property. During an appointment, project or ongoing management service, we may also hold plans, photographs, access information, supplier details, project records, approvals, budgets and invoices relevant to the work.</p>
        <h2>Why we use it</h2>
        <p>We use this information to respond to enquiries, prepare proposals, perform contracts, manage garden work, coordinate approved suppliers and meet legal, tax and insurance obligations. Optional website analytics are used only where you have consented.</p>
        <h2>Who we share it with</h2>
        <p>Information is shared with contractors, consultants, suppliers and service providers only where needed to assess or deliver approved work. We explain significant project-related sharing as part of the appointment. Website and business-service providers may process data under their own contractual obligations.</p>
        <h2>How long we keep it</h2>
        <p>Unsuccessful enquiries are normally deleted within 12 months. Client, project and financial records may be retained for at least six years after completion where required for contractual, tax, insurance or legal purposes.</p>
        <h2>Your rights</h2>
        <p>You may request access to, correction of or deletion of your personal information, object to certain processing and withdraw consent where consent is the basis used. You also have the right to complain to the Information Commissioner's Office.</p>
        <h2>Contact</h2>
        <p>Privacy questions: <a href="mailto:hello@blossomgarden.design">hello@blossomgarden.design</a>. <span class="req-input">Legal entity to be confirmed before launch.</span></p>
      </div>
    </section>
''',
}

COOKIES = {
    "path": "cookies.html",
    "title": "Cookie Policy | Blossom",
    "desc": "The cookies and optional analytics this website uses, and how to change your choice.",
    "active": "",
    "schema": "",
    "body": '''    <section class="hero">
      <div class="wrap-narrow">
        <span class="eyebrow">Legal</span>
        <h1>Cookie policy</h1>
        <p class="standfirst">The website works without optional analytics. Analytics load only if you choose to allow them.</p>
      </div>
    </section>
    <section class="section prose" style="padding-top: 0;">
      <div class="wrap-narrow">
        <h2>Essential storage</h2>
        <p>The site may store your cookie choice and short-lived campaign attribution needed to understand which advert or QR code brought you to the enquiry page.</p>
        <h2>Optional analytics</h2>
        <p>If analytics are enabled, the service and exact cookies used must be named here before launch. Analytics must not load until consent has been given where consent is required.</p>
        <h2>Changing your choice</h2>
        <p>Cookie controls must provide a way to change or withdraw the choice after it has been made.</p>
      </div>
    </section>
''',
}

TERMS = {
    "path": "terms.html",
    "title": "Website Terms | Blossom",
    "desc": "Terms of use for the Blossom website.",
    "active": "",
    "schema": "",
    "body": '''    <section class="hero">
      <div class="wrap-narrow">
        <span class="eyebrow">Legal</span>
        <h1>Website terms</h1>
        <p class="standfirst">These terms apply to use of the website. Garden reviews, designs, projects and management appointments are governed by their own written agreements.</p>
        <p class="smallprint"><span class="req-input">Operator, legal entity, company number, registered address and contact details to be confirmed before launch.</span></p>
      </div>
    </section>
    <section class="section prose" style="padding-top: 0;">
      <div class="wrap-narrow">
        <h2>General information</h2>
        <p>Website content explains Blossom's general services. It is not design, planning, engineering, horticultural, safety or legal advice for a particular property.</p>
        <h2>Services and pricing</h2>
        <p>Service descriptions and any guide prices do not constitute an offer. Scope, responsibility, authority, exclusions, fees and payment terms are confirmed in a written proposal or agreement before work begins.</p>
        <h2>Specialist appointments</h2>
        <p>Some work is undertaken by independent contractors, consultants and suppliers. Their responsibility, appointment route and relationship with Blossom are defined for each engagement.</p>
        <h2>Permissions and approvals</h2>
        <p>Planning permission, Building Regulations approval, listed-building consent, tree consent, Party Wall procedures and other requirements depend on the property and proposed work. No website statement confirms that a particular project is exempt.</p>
        <h2>Intellectual property</h2>
        <p>The Blossom name, visual identity, illustrations, plans and written website content may not be reproduced commercially without permission. Project-specific intellectual-property terms are contained in the relevant appointment.</p>
        <h2>Liability</h2>
        <p>We take care to keep the website accurate, but accept no liability for decisions made solely in reliance on its general content. Nothing excludes liability that cannot lawfully be excluded.</p>
        <h2>Law</h2>
        <p>These terms are governed by the law of England and Wales.</p>
      </div>
    </section>
''',
}

PAGES = [FAQ, PROJECTS, ABOUT, AREAS, JOURNAL, CONTACT, THANKS, PRIVACY, COOKIES, TERMS]
