from flask import Flask, render_template_string


app = Flask(__name__)


PAGE = r'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="FlowForge Web builds professional, mobile-friendly websites for local and small businesses.">
  <title>FlowForge Web | Custom Websites for Local Business</title>
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%2307142d'/%3E%3Cpath d='M12 21h24l-9 9 9 9H12l9-9z' fill='%231e8bff'/%3E%3Cpath d='M52 43H28l9-9-9-9h24l-9 9z' fill='%23ffc629'/%3E%3C/svg%3E">
  <style>
    :root {
      --navy: #06142f;
      --navy-2: #0a2145;
      --blue: #1688f8;
      --blue-light: #54adff;
      --yellow: #ffc629;
      --yellow-light: #ffe178;
      --white: #f7fbff;
      --muted: #b7c8df;
      --card: rgba(10, 33, 69, .78);
      --border: rgba(102, 171, 255, .2);
      --shadow: 0 22px 60px rgba(0, 0, 0, .28);
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      color: var(--white);
      background:
        radial-gradient(circle at 80% 8%, rgba(22, 136, 248, .19), transparent 28rem),
        radial-gradient(circle at 8% 78%, rgba(255, 198, 41, .08), transparent 24rem),
        var(--navy);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.6;
    }

    a { color: inherit; }
    img { max-width: 100%; display: block; }
    .container { width: min(1120px, calc(100% - 2rem)); margin: 0 auto; }

    .nav {
      position: sticky;
      top: 0;
      z-index: 20;
      border-bottom: 1px solid var(--border);
      background: rgba(6, 20, 47, .86);
      backdrop-filter: blur(16px);
    }
    .nav-inner {
      min-height: 72px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }
    .brand { font-weight: 900; font-size: 1.35rem; text-decoration: none; letter-spacing: -.03em; }
    .brand span:first-child { color: var(--blue-light); }
    .brand span:last-child { color: var(--yellow); }
    .nav-links { display: flex; align-items: center; gap: 1.4rem; }
    .nav-links a { color: var(--muted); text-decoration: none; font-weight: 700; font-size: .94rem; }
    .nav-links a:hover, .nav-links a:focus-visible { color: var(--white); }

    .button {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 48px;
      padding: .78rem 1.25rem;
      border: 1px solid transparent;
      border-radius: 999px;
      background: linear-gradient(135deg, var(--yellow), #ffad16);
      color: #101827;
      font-weight: 900;
      text-decoration: none;
      box-shadow: 0 12px 30px rgba(255, 198, 41, .18);
      transition: transform .2s ease, box-shadow .2s ease;
    }
    .button:hover { transform: translateY(-2px); box-shadow: 0 16px 34px rgba(255, 198, 41, .28); }
    .button.secondary { background: transparent; color: var(--white); border-color: rgba(255,255,255,.24); box-shadow: none; }
    .button.secondary:hover { border-color: var(--blue-light); }

    .hero {
      min-height: 720px;
      display: grid;
      align-items: center;
      padding: 5.5rem 0 4rem;
      position: relative;
      overflow: hidden;
    }
    .hero::after {
      content: "</>";
      position: absolute;
      right: -2rem;
      bottom: -8rem;
      font-size: clamp(12rem, 26vw, 26rem);
      font-weight: 950;
      line-height: 1;
      color: rgba(22, 136, 248, .035);
      pointer-events: none;
    }
    .hero-grid { display: grid; grid-template-columns: 1.05fr .95fr; align-items: center; gap: 3.5rem; }
    .eyebrow { display: inline-flex; gap: .55rem; align-items: center; color: var(--yellow-light); font-weight: 900; letter-spacing: .12em; text-transform: uppercase; font-size: .78rem; }
    .eyebrow::before { content: ""; width: 34px; height: 3px; border-radius: 99px; background: var(--yellow); }
    h1, h2, h3 { line-height: 1.08; margin-top: 0; }
    h1 { font-size: clamp(3.25rem, 7vw, 6.5rem); letter-spacing: -.07em; margin: 1rem 0 1.2rem; }
    h1 .flow { color: var(--blue-light); }
    h1 .forge { color: var(--yellow); }
    .hero p { color: var(--muted); max-width: 650px; font-size: clamp(1.05rem, 2vw, 1.25rem); margin-bottom: 2rem; }
    .hero-actions { display: flex; flex-wrap: wrap; gap: .85rem; }
    .hero-art {
      border: 1px solid var(--border);
      border-radius: 32px;
      overflow: hidden;
      background: #07152f;
      box-shadow: var(--shadow);
      transform: rotate(1deg);
    }
    .hero-art img { width: 100%; aspect-ratio: 16/9; object-fit: cover; }

    section { padding: 6rem 0; }
    .section-kicker { color: var(--yellow); font-weight: 900; text-transform: uppercase; letter-spacing: .14em; font-size: .78rem; }
    .section-title { font-size: clamp(2.25rem, 4vw, 4rem); letter-spacing: -.055em; max-width: 780px; margin: .7rem 0 1.25rem; }
    .section-lead { color: var(--muted); font-size: 1.1rem; max-width: 720px; }

    .about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2.5rem; align-items: start; }
    .feature-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; }
    .feature, .price-card, .referral-card, .contact-card {
      border: 1px solid var(--border);
      background: var(--card);
      border-radius: 24px;
      box-shadow: var(--shadow);
    }
    .feature { padding: 1.5rem; }
    .feature .icon { color: var(--yellow); font-size: 1.35rem; font-weight: 950; }
    .feature h3 { margin: .75rem 0 .5rem; font-size: 1.1rem; }
    .feature p { margin: 0; color: var(--muted); font-size: .95rem; }

    .pricing { border-block: 1px solid var(--border); background: rgba(4, 15, 36, .44); }
    .price-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.25rem; margin-top: 2.5rem; }
    .price-card { padding: 2rem; position: relative; overflow: hidden; }
    .price-card.featured { border-color: rgba(255, 198, 41, .6); transform: translateY(-10px); }
    .price-card.featured::before { content: "Popular"; position: absolute; top: 16px; right: -34px; transform: rotate(42deg); width: 130px; text-align: center; background: var(--yellow); color: #111827; font-weight: 900; font-size: .75rem; }
    .price-card h3 { color: var(--white); font-size: 1.2rem; margin-bottom: 1rem; }
    .price { font-size: 3.2rem; font-weight: 950; letter-spacing: -.06em; color: var(--yellow); }
    .price small { font-size: 1rem; color: var(--muted); letter-spacing: normal; }
    .price-card p { color: var(--muted); min-height: 78px; }
    .price-card ul { list-style: none; padding: 0; margin: 1.5rem 0 0; display: grid; gap: .7rem; }
    .price-card li::before { content: "✓"; color: var(--blue-light); font-weight: 950; margin-right: .65rem; }

    .referral-wrap { display: grid; grid-template-columns: .9fr 1.1fr; gap: 2rem; align-items: center; }
    .referral-card { padding: clamp(2rem, 4vw, 3.5rem); border-color: rgba(255, 198, 41, .45); background: linear-gradient(145deg, rgba(255, 198, 41, .11), rgba(10, 33, 69, .8)); }
    .commission { font-size: clamp(5rem, 12vw, 9rem); font-weight: 950; letter-spacing: -.09em; line-height: .9; color: var(--yellow); }
    .commission-label { color: var(--yellow-light); text-transform: uppercase; font-weight: 900; letter-spacing: .14em; margin-top: .75rem; }

    .contact-card { padding: clamp(2rem, 5vw, 4rem); text-align: center; background: linear-gradient(145deg, rgba(22,136,248,.13), rgba(10,33,69,.9)); }
    .contact-actions { display: flex; justify-content: center; flex-wrap: wrap; gap: 1rem; margin-top: 2rem; }
    .contact-note { color: var(--muted); margin: 1.5rem 0 0; }

    footer { border-top: 1px solid var(--border); padding: 2rem 0; color: var(--muted); }
    .footer-inner { display: flex; justify-content: space-between; gap: 1rem; flex-wrap: wrap; }

    @media (max-width: 850px) {
      .nav-links a:not(.button) { display: none; }
      .hero { min-height: auto; padding-top: 4rem; }
      .hero-grid, .about-grid, .referral-wrap { grid-template-columns: 1fr; }
      .hero-art { order: -1; transform: none; }
      .price-grid { grid-template-columns: 1fr; }
      .price-card.featured { transform: none; }
    }
    @media (max-width: 560px) {
      .container { width: min(100% - 1.25rem, 1120px); }
      .nav-inner { min-height: 64px; }
      .nav .button { min-height: 42px; padding: .62rem .9rem; font-size: .85rem; }
      section { padding: 4.5rem 0; }
      .feature-grid { grid-template-columns: 1fr; }
      .hero-actions .button, .contact-actions .button { width: 100%; }
    }
    @media (prefers-reduced-motion: reduce) {
      html { scroll-behavior: auto; }
      * { transition: none !important; }
    }
  </style>
</head>
<body>
  <header class="nav">
    <div class="container nav-inner">
      <a class="brand" href="#top" aria-label="FlowForge Web home"><span>Flow</span><span>Forge</span> Web</a>
      <nav class="nav-links" aria-label="Primary navigation">
        <a href="#about">About</a>
        <a href="#pricing">Pricing</a>
        <a href="#referrals">Referral Program</a>
        <a class="button" href="#contact">Contact Us</a>
      </nav>
    </div>
  </header>

  <main id="top">
    <section class="hero">
      <div class="container hero-grid">
        <div>
          <div class="eyebrow">Custom web development</div>
          <h1><span class="flow">Flow</span><span class="forge">Forge</span> Web</h1>
          <p>Professional, mobile-friendly websites built for local and small businesses that want to look credible, reach more customers, and grow online.</p>
          <div class="hero-actions">
            <a class="button" href="mailto:braylonsutton3@gmail.com?subject=FlowForge%20Website%20Inquiry">Start Your Website</a>
            <a class="button secondary" href="#pricing">See Pricing</a>
          </div>
        </div>
        <div class="hero-art">
          <img src="{{ url_for('static', filename='flowforge-cover.png') }}" alt="FlowForge blue and gold snake coding logo">
        </div>
      </div>
    </section>

    <section id="about">
      <div class="container about-grid">
        <div>
          <div class="section-kicker">About us</div>
          <h2 class="section-title">Custom websites without the agency-sized price.</h2>
          <p class="section-lead">FlowForge Web creates personalized websites for local and small businesses. We turn your services, branding, and goals into a clean online presence that works smoothly across phones, tablets, and computers.</p>
          <p class="section-lead">Our focus is straightforward: learn what makes your business different, build a site that represents it professionally, and remain available when your information needs to change.</p>
        </div>
        <div class="feature-grid">
          <article class="feature"><div class="icon">01</div><h3>Custom Design</h3><p>A website tailored to your business, services, colors, and customers.</p></article>
          <article class="feature"><div class="icon">02</div><h3>Mobile Friendly</h3><p>A responsive experience that looks polished on every screen size.</p></article>
          <article class="feature"><div class="icon">03</div><h3>Clear Information</h3><p>Simple navigation that helps visitors understand and contact your business.</p></article>
          <article class="feature"><div class="icon">04</div><h3>Ongoing Support</h3><p>Optional monthly updates keep your website accurate and current.</p></article>
        </div>
      </div>
    </section>

    <section class="pricing" id="pricing">
      <div class="container">
        <div class="section-kicker">Simple pricing</div>
        <h2 class="section-title">Professional web presence. Clear costs.</h2>
        <p class="section-lead">Choose the services your business needs without complicated packages.</p>
        <div class="price-grid">
          <article class="price-card featured">
            <h3>Custom Website</h3>
            <div class="price">$300 <small>upfront</small></div>
            <p>A personalized business website designed around your brand and services.</p>
            <ul><li>Custom design</li><li>Mobile-friendly layout</li><li>Business contact information</li></ul>
          </article>
          <article class="price-card">
            <h3>Website Updates</h3>
            <div class="price">$50 <small>/ month</small></div>
            <p>Ongoing help keeping your website's content and business details current.</p>
            <ul><li>Content changes</li><li>Price and service updates</li><li>Ongoing assistance</li></ul>
          </article>
          <article class="price-card">
            <h3>Translated Version</h3>
            <div class="price">$100 <small>upfront</small></div>
            <p>Add a translated version of your website in the language your customers need.</p>
            <ul><li>Any language</li><li>Consistent page design</li><li>Reach more customers</li></ul>
          </article>
        </div>
      </div>
    </section>

    <section id="referrals">
      <div class="container referral-wrap">
        <div>
          <div class="section-kicker">Work with FlowForge</div>
          <h2 class="section-title">Know a business that needs a better website?</h2>
          <p class="section-lead">Refer the business to FlowForge Web. If your referral becomes a paying client and FlowForge earns money from the project, you receive a 40% commission from that referral.</p>
          <div class="hero-actions" style="margin-top: 2rem;">
            <a class="button" href="mailto:braylonsutton3@gmail.com?subject=FlowForge%20Business%20Referral&body=Business%20name%3A%0AContact%20person%3A%0APhone%20or%20email%3A%0AWhy%20they%20may%20need%20a%20website%3A">Refer a Business</a>
            <a class="button secondary" href="tel:+15026427649">Call About Referrals</a>
          </div>
        </div>
        <aside class="referral-card" aria-label="Referral commission">
          <div class="commission">40%</div>
          <div class="commission-label">Referral commission</div>
          <p>Connect FlowForge with a business. When the referral becomes a paying customer, you earn commission.</p>
        </aside>
      </div>
    </section>

    <section id="contact">
      <div class="container">
        <div class="contact-card">
          <div class="section-kicker">Contact FlowForge</div>
          <h2 class="section-title" style="margin-inline:auto;">Ready to build your business website?</h2>
          <p class="section-lead" style="margin-inline:auto;">Tell us about your business, what you offer, and what you want your website to accomplish.</p>
          <div class="contact-actions">
            <a class="button" href="mailto:braylonsutton3@gmail.com?subject=FlowForge%20Website%20Inquiry">braylonsutton3@gmail.com</a>
            <a class="button secondary" href="tel:+15026427649">(502) 642-7649</a>
          </div>
          <p class="contact-note">Website inquiries, monthly updates, translations, and business referrals are welcome.</p>
        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="container footer-inner">
      <div>© {{ year }} FlowForge Web</div>
      <div>Custom websites built for local business.</div>
    </div>
  </footer>
</body>
</html>'''


@app.route("/")
def home():
    from datetime import datetime
    return render_template_string(PAGE, year=datetime.now().year)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
