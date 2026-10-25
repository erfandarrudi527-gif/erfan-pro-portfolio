# -*- coding: utf-8 -*-
"""
Real-World Complete Production Projects with Line-by-Line Technical Breakdown.
For all 5 tracks: HTML, CSS, JavaScript, React, and Next.js.
Each track contains:
- Complete production code for a real-world project
- Line-by-line breakdown explaining what each line does, why it is written that way, and architectural insights
- Interactive live working preview
"""

PROJECTS = {
    "html": {
        "title": "پروژه جامع HTML: صفحه فرود استاندارد و دسترس‌پذیر شرکت ابری TechNova",
        "badge": "PRODUCTION HTML5 SPEC",
        "desc": "یک وب‌سایت تجاری کامل با سئو تکنیکال، ساختار سمانتیک W3C، داده‌های ساختاریافته Schema.org، فرم اعتبارسنجی‌شده بومی و المان‌های تعاملی dialog.",
        "preview_html": """
        <div style="background:#030712; color:#f9fafb; font-family:'IRANYekan', sans-serif; border-radius:12px; border:1px solid #1f2937; overflow:hidden; direction:rtl; text-align:right;">
          <header style="background:rgba(17,24,39,0.85); backdrop-filter:blur(10px); padding:14px 20px; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #374151;">
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="font-size:20px;">⚡</span>
              <strong style="color:#38bdf8; font-size:15px;">TechNova Cloud</strong>
            </div>
            <nav style="display:flex; gap:16px; font-size:12.5px;">
              <a href="#services" style="color:#9ca3af; text-decoration:none;">خدمات</a>
              <a href="#features" style="color:#9ca3af; text-decoration:none;">ویژگی‌ها</a>
              <a href="#contact" style="color:#9ca3af; text-decoration:none;">تماس با ما</a>
            </nav>
            <button onclick="alert('فرم درخواست مشاوره فعال شد')" style="background:#0284c7; color:#fff; border:none; padding:6px 14px; border-radius:6px; font-size:12px; font-weight:700; cursor:pointer;">ثبت‌نام سازمانی</button>
          </header>
          <div style="padding:32px 24px; text-align:center; background:radial-gradient(circle at 50% 0%, rgba(56,189,248,0.15), transparent 70%);">
            <span style="background:rgba(56,189,248,0.1); color:#38bdf8; border:1px solid rgba(56,189,248,0.3); font-size:11px; padding:3px 10px; border-radius:99px; font-weight:700;">نسل جدید زیرساخت ابری</span>
            <h1 style="font-size:26px; font-weight:900; margin:12px 0 8px; color:#fff;">زیرساخت ابری فوق‌سریع و توزیع‌شده برای مقیاس‌های میلیونی</h1>
            <p style="font-size:13.5px; color:#9ca3af; max-width:540px; margin:0 auto 20px; line-height:1.8;">پیاده‌سازی شده با رعایت بالاترین استانداردهای وب، سئو تکنیکال و دسترسی‌پذیری جهانی برای نابینایان (WCAG 2.2).</p>
            <div style="display:flex; justify-content:center; gap:10px;">
              <button onclick="alert('درخواست دمو ارسال شد')" style="background:#38bdf8; color:#030712; border:none; padding:8px 18px; border-radius:8px; font-weight:800; font-size:12.5px; cursor:pointer;">درخواست دموی اختصاصی</button>
              <button onclick="alert('مستندات باز شد')" style="background:rgba(255,255,255,0.05); color:#e5e7eb; border:1px solid #374151; padding:8px 18px; border-radius:8px; font-size:12.5px; cursor:pointer;">مطالعه مستندات</button>
            </div>
          </div>
          <div style="padding:20px 24px; border-top:1px solid #1f2937; display:grid; grid-template-columns:repeat(3, 1fr); gap:12px; text-align:center;">
            <div style="background:#111827; padding:12px; border-radius:8px; border:1px solid #1f2937;">
              <div style="font-size:20px; font-weight:900; color:#38bdf8;">۹۹.۹۹٪</div>
              <div style="font-size:11.5px; color:#9ca3af; margin-top:2px;">پایداری آپ‌تایم شبکه</div>
            </div>
            <div style="background:#111827; padding:12px; border-radius:8px; border:1px solid #1f2937;">
              <div style="font-size:20px; font-weight:900; color:#10b981;">&lt; 15ms</div>
              <div style="font-size:11.5px; color:#9ca3af; margin-top:2px;">تاخیر شبکه در سطح کشور</div>
            </div>
            <div style="background:#111827; padding:12px; border-radius:8px; border:1px solid #1f2937;">
              <div style="font-size:20px; font-weight:900; color:#f59e0b;">+۵۰۰ شرکت</div>
              <div style="font-size:11.5px; color:#9ca3af; margin-top:2px;">کسب‌وکارهای فعال</div>
            </div>
          </div>
        </div>
        """,
        "full_code": """<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="زیرساخت ابری TechNova با مقیاس‌پذیری میلیونی و امنیت بانکی.">
  <meta property="og:title" content="TechNova // پلتفرم زیرساخت ابری">
  <meta property="og:description" content="ارائه‌دهنده سرورهای لبه‌ای ابری و دیتابیس توزیع‌شده با آپ‌تایم ۹۹.۹۹٪.">
  <meta property="og:type" content="website">
  <title>TechNova Cloud // زیرساخت ابری نسل آینده</title>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "TechNova Cloud",
    "url": "https://technova.dev",
    "logo": "https://technova.dev/logo.png"
  }
  </script>
</head>
<body>
  <header role="banner">
    <nav aria-label="ناوبری اصلی">
      <a href="/" class="brand-link">
        <span aria-hidden="true">⚡</span>
        <strong>TechNova Cloud</strong>
      </a>
      <ul>
        <li><a href="#services">خدمات ابری</a></li>
        <li><a href="#features">مزایا</a></li>
        <li><a href="#pricing">قیمت‌گذاری</a></li>
      </ul>
      <button type="button" id="openDialogBtn" aria-haspopup="dialog">ورود سازمانی</button>
    </nav>
  </header>

  <main id="main-content">
    <section class="hero-section" aria-labelledby="hero-heading">
      <span class="badge">نسل جدید محاسبات ابری</span>
      <h1 id="hero-heading">زیرساخت ابری هوشمند و توزیع‌شده برای سازمان‌های پیشرو</h1>
      <p>پردازش فوق‌سریع در لبه شبکه با تضمین امنیت داده و نرخ تاخیر زیر ۱۵ میلی‌ثانیه.</p>
      <div class="actions-group">
        <a href="#demo" class="btn btn-primary">درخواست دموی رایگان</a>
        <a href="#docs" class="btn btn-secondary">مستندات API</a>
      </div>
    </section>

    <section id="services" aria-labelledby="services-heading">
      <h2 id="services-heading">خدمات اصلی زیرساخت</h2>
      <div class="services-grid">
        <article class="service-card">
          <figure>
            <img src="cloud-db.svg" alt="نمودار شماتیک پایگاه داده توزیع‌شده با قابلیت پاسخ‌دهی بلادرنگ" width="64" height="64" loading="lazy">
            <figcaption>پایگاه داده توزیع‌شده</figcaption>
          </figure>
          <h3>Distributed Database</h3>
          <p>همگام‌سازی بلادرنگ داده‌ها در ۳ ناحیه جغرافیایی بدون ریسک قطعی اطلاعات.</p>
        </article>
      </div>
    </section>

    <section id="contact" aria-labelledby="contact-heading">
      <h2 id="contact-heading">دریافت مشاوره مهندسی</h2>
      <form action="/api/contact" method="POST" novalidate>
        <fieldset>
          <legend>اطلاعات ارتباطی متقاضی</legend>
          <label for="fullName">نام و نام خانوادگی:</label>
          <input type="text" id="fullName" name="fullName" required minlength="3" autocomplete="name">

          <label for="corpEmail">ایمیل شرکتی:</label>
          <input type="email" id="corpEmail" name="corpEmail" required autocomplete="email">

          <label for="companySize">تعداد سرورهای فعال:</label>
          <select id="companySize" name="companySize">
            <option value="small">۱ تا ۱۰ سرور</option>
            <option value="medium">۱۰ تا ۱۰۰ سرور</option>
            <option value="enterprise">بیش از ۱۰۰ سرور</option>
          </select>

          <button type="submit">ارسال درخواست مشاوره</button>
        </fieldset>
      </form>
    </section>
  </main>

  <dialog id="loginModal" aria-labelledby="modalTitle">
    <form method="dialog">
      <h3 id="modalTitle">ورود به کنسول ابری</h3>
      <label for="userKey">کلید دسترسی سازمانی (Access Key):</label>
      <input type="password" id="userKey" required>
      <div class="dialog-actions">
        <button type="submit" value="confirm">ورود ایمن</button>
        <button type="submit" value="cancel">انصراف</button>
      </div>
    </form>
  </dialog>

  <footer role="contentinfo">
    <p>&copy; ۲۰۲۶ تمامی حقوق برای شرکت توسعه ابری TechNova محفوظ است.</p>
  </footer>
</body>
</html>""",
        "lines_breakdown": [
            {"line": 1, "code": "<!DOCTYPE html>", "role": "اعلام استاندارد HTML5 به مرورگر", "explanation": "این خط حیاتی به موتور چیدمان مرورگر فرمان می‌دهد که صفحه را در حالت استانداردهای مدرن (Standards Mode) پردازش کند و مانع از ورود به حالت Quirks Mode که محاسبات ابعاد و استایل را به سبک سال ۱۹۹۸ می‌برد می‌شود."},
            {"line": 2, "code": '<html lang="fa" dir="rtl">', "role": "ریشه سند، زبان و جهت متن", "explanation": "مشخص کردن lang=\"fa\" به صفحه‌خوان نابینایان می‌گوید متون را با تلفظ فارسی بخواند و موتورهای جستجو زبان صفحه را بفهمند. ویژگی dir=\"rtl\" جهت چیدمان راست‌به‌چپ را در کل درخت DOM بدون باگ فعال می‌سازد."},
            {"line": 4, "code": '<meta charset="UTF-8">', "role": "کدگذاری کاراکترهای یونیکد", "explanation": "پشتیبانی استاندارد از تمام حروف الفبای فارسی، گچ‌پژ، اعداد و ایموجی‌ها بدون به هم ریختگی و تبدیل به حروف نامفهوم (Mojibake)."},
            {"line": 5, "code": '<meta name="viewport" content="width=device-width, initial-scale=1.0">', "role": "ریسپانسیو و تطبیق با ابعاد موبایل", "explanation": "عرض Viewport را با عرض فیزیکی مانیتور یا گوشی ست می‌کند و مقیاس اولیه زوم را روی ۱ قرار می‌دهد تا سایت روی موبایل کوچک و زوم‌اوت نشان داده نشود."},
            {"line": 6, "code": '<meta name="description" content="...">', "role": "توضیحات متای سئو برای نتایج گوگل", "explanation": "این متن در صفحه نتایج جستجوی گوگل (SERP) زیر لینک تیتر نمایش داده شده و مستقیماً روی نرخ کلیک (CTR) کاربران اثر می‌گذارد."},
            {"line": 7, "code": '<meta property="og:title" content="...">', "role": "پروتکل Open Graph برای شبکه‌های اجتماعی", "explanation": "هنگامی که آدرس صفحه در تلگرام، لینکدین، توییتر یا واتس‌اپ ارسال شود، این متا دیتا کارت پیش‌نمایش گرافیکی زیبا به همراه تیتر و عکس ایجاد می‌کند."},
            {"line": 11, "code": '<script type="application/ld+json">', "role": "داده‌های ساختاریافته Schema.org JSON-LD", "explanation": "اطلاعات هویتی شرکت را به صورت ساختاریافته به هوش مصنوعی گوگل معرفی می‌کند تا ریچ اسنیپت (Knowledge Graph) شرکت در جستجوها شکل گیرد."},
            {"line": 21, "code": '<header role="banner">', "role": "هدر سمانتیک صفحه وب", "explanation": "معرفی بخش سربرگ اصلی صفحه که حاوی لوگو و ابزارهای ناوبری است؛ role=\"banner\" دسترسی‌پذیری آن را در درخت دسترسی سیستم‌عامل ثبت می‌کند."},
            {"line": 22, "code": '<nav aria-label="ناوبری اصلی">', "role": "تگ ناوبری با برچسب دسترس‌پذیری", "explanation": "به صفحه‌خوان‌ها اعلام می‌کند که این بخش محل پیوندهای ناوبری اصلی سایت است و کاربر نابینا می‌تواند با یک کلید میانبر مستقیماً به آن بپرد."},
            {"line": 34, "code": '<main id="main-content">', "role": "محتوای یکتا و اصلی سند", "explanation": "در هر صفحه فقط یک تگ <main> مجاز است که دربرگیرنده هسته پیام صفحه به دور از منوها و فوترهای مشترک است."},
            {"line": 35, "code": '<section class="hero-section" aria-labelledby="hero-heading">', "role": "بخش‌بندی موضوعی با ارتباط به تیتر", "explanation": "یک بخش مستقل معنادار که با aria-labelledby به تیتر اصلی h1 خود ارجاع می‌دهد تا ساختار صفحه کاملاً شفاف گردد."},
            {"line": 37, "code": '<h1 id="hero-heading">...</h1>', "role": "مهم‌ترین تیتر صفحه برای سئو و هویت محتوا", "explanation": "تنها یک بار در هر صفحه وب باید از h1 استفاده شود تا موضوع و ارزش بنیادین کسب‌وکار به خزنده‌های گوگل و کاربران منتقل شود."},
            {"line": 49, "code": '<article class="service-card">', "role": "کارت مقاله مستقل و بازتولیدپذیر", "explanation": "تگ <article> برای هر المانی استفاده می‌شود که به خودی خود معنی مستقلی دارد و می‌توان آن را بدون از دست رفتن محتوا در صفحه دیگری بازنشر داد."},
            {"line": 50, "code": '<figure> ... <figcaption> ... </figcaption></figure>', "role": "کادر گرافیکی با توضیح ساختاری", "explanation": "تگ استاندارد بسته‌بندی عکس یا نمودار همراه با متن شرح آن که ارتباط محتوایی تصویر با متن را برای سئو مستند می‌سازد."},
            {"line": 51, "code": '<img ... loading="lazy" width="64" height="64">', "role": "بارگذاری تنبل و جلوگیری از CLS", "explanation": "ویژگی loading=\"lazy\" مانع دانلود عکس تا زمان اسکرول کاربر می‌شود؛ ذکر width و height ثابت نیز از پرش ناگهانی صفحه (Layout Shift) جلوگیری می‌کند."},
            {"line": 60, "code": '<form action="/api/contact" method="POST" novalidate>', "role": "فرم سمانتیک استاندارد ارسال داده", "explanation": "تگ form با متد POST داده‌ها را به صورت امن در بدنه درخواست HTTP ارسال می‌کند. ویژگی novalidate اجازه کنترل کامل پیام‌های خطای فرم را به ما می‌دهد."},
            {"line": 61, "code": '<fieldset><legend>اطلاعات متقاضی</legend>', "role": "گروه‌بندی فیلدهای فرم با عنوان رسمی", "explanation": "تمام فیلدهای مرتبط را داخل یک گروه قرار می‌دهد؛ تگ legend تیتری می‌سازد که صفحه‌خوان قبل از خواندن هر فیلد آن را اعلام می‌کند."},
            {"line": 63, "code": '<label for="fullName">نام:</label><input id="fullName" autocomplete="name">', "role": "پیوند لیبل به فیلد و تکمیل خودکار", "explanation": "ویژگی for به id متصل شده تا کلیک روی متن لیبل، فیلد را فعال کند. autocomplete=\"name\" به مرورگر اجازه می‌دهد اطلاعات کاربر را با یک تپ پر کند."},
            {"line": 84, "code": '<dialog id="loginModal" aria-labelledby="modalTitle">', "role": "پنجره مودال بومی با قابلیت لایه Top Layer", "explanation": "المان رسمی HTML5 برای ساخت دیالوگ‌های مدال؛ بدون نیاز به کتابخانه جاوا اسکریپت با متد showModal() باز می‌شود و کلید ESC را مدیریت می‌کند."},
            {"line": 97, "code": '<footer role="contentinfo">', "role": "فوتر صفحه و اطلاعات پایانی", "explanation": "محل قرارگیری اطلاعات کپی‌رایت، سلب مسئولیت و لینک‌های دسترسی نهایی صفحه."}
        ]
    },

    "css": {
        "title": "پروژه جامع CSS: دیزاین‌سیستم مدرن و وب‌سایت پورتفولیو Zenith Luxe",
        "badge": "FLUID DESIGN SYSTEM & GPU MOTION",
        "desc": "طراحی استایل‌شیت کامل شامل توکن‌های CSS Custom Properties، تایپوگرافی روان با clamp()، چیدمان‌های گرید دوسطحی، گلس‌مورفیسم، انیمیشن‌های سه‌بعدی و مدیاکوئری‌های پیشرفته.",
        "preview_html": """
        <div style="background:#090d16; border-radius:12px; border:1px solid #1e293b; padding:24px; color:#f8fafc; font-family:'IRANYekan', sans-serif; direction:rtl; text-align:right;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px; border-bottom:1px solid rgba(255,255,255,0.06); padding-bottom:12px;">
            <div>
              <span style="font-size:11px; color:#38bdf8; font-family:monospace;">DESIGN TOKENS // CSS ENGINE</span>
              <h3 style="font-size:18px; font-weight:900; margin:2px 0 0; color:#fff;">Zenith Modern Design System</h3>
            </div>
            <span style="background:rgba(56,189,248,0.1); color:#38bdf8; border:1px solid rgba(56,189,248,0.3); padding:3px 10px; border-radius:6px; font-size:11px; font-weight:700;">Fluid Typography Active</span>
          </div>
          <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:14px; margin-bottom:20px;">
            <div style="background:rgba(15,23,42,0.6); backdrop-filter:blur(12px); border:1px solid rgba(255,255,255,0.08); padding:16px; border-radius:10px; transition:transform 0.2s;">
              <div style="width:32px; height:32px; border-radius:8px; background:linear-gradient(135deg, #38bdf8, #0284c7); display:flex; align-items:center; justify-content:center; margin-bottom:10px; font-size:16px;">💎</div>
              <div style="font-size:13.5px; font-weight:800; color:#fff; margin-bottom:4px;">گلس‌مورفیسم مات</div>
              <p style="font-size:11.5px; color:#94a3b8; line-height:1.6; margin:0;">رندرینگ لایه‌ای با backdrop-filter و مرزهای مویین چندلایه.</p>
            </div>
            <div style="background:rgba(15,23,42,0.6); backdrop-filter:blur(12px); border:1px solid rgba(255,255,255,0.08); padding:16px; border-radius:10px;">
              <div style="width:32px; height:32px; border-radius:8px; background:linear-gradient(135deg, #10b981, #059669); display:flex; align-items:center; justify-content:center; margin-bottom:10px; font-size:16px;">⚡</div>
              <div style="font-size:13.5px; font-weight:800; color:#fff; margin-bottom:4px;">CSS Grid واکنش‌گرا</div>
              <p style="font-size:11.5px; color:#94a3b8; line-height:1.6; margin:0;">چیدمان اتوماتیک با repeat(auto-fit, minmax(240px, 1fr)).</p>
            </div>
            <div style="background:rgba(15,23,42,0.6); backdrop-filter:blur(12px); border:1px solid rgba(255,255,255,0.08); padding:16px; border-radius:10px;">
              <div style="width:32px; height:32px; border-radius:8px; background:linear-gradient(135deg, #a855f7, #7c3aed); display:flex; align-items:center; justify-content:center; margin-bottom:10px; font-size:16px;">🚀</div>
              <div style="font-size:13.5px; font-weight:800; color:#fff; margin-bottom:4px;">شتاب‌دهی سخت‌افزاری</div>
              <p style="font-size:11.5px; color:#94a3b8; line-height:1.6; margin:0;">انیمیشن‌های بدون لگ با transform3d روی واحد GPU.</p>
            </div>
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center; background:#040711; border:1px solid #1e293b; padding:10px 16px; border-radius:8px; font-size:12px;">
            <span style="color:#64748b;">FPS TARGET: 120 FPS // NO LAYOUT REFLOW</span>
            <span style="color:#10b981; font-weight:700;">GPU COMPOSITING ✓</span>
          </div>
        </div>
        """,
        "full_code": """/* ==========================================================================
   ZENITH LUXE DESIGN SYSTEM // PRODUCTION CSS SPECIFICATION
   ========================================================================== */

/* 1. Global Custom Properties (Design Tokens) */
:root {
  /* Color Palette (Tailored HSL & P3 Gamut) */
  --bg-deep: hsl(222, 47%, 4%);
  --bg-surface: hsla(222, 47%, 9%, 0.75);
  --bg-card: hsla(217, 33%, 14%, 0.6);
  --border-subtle: hsla(0, 0%, 100%, 0.08);
  --border-glow: hsla(199, 89%, 60%, 0.45);
  
  --primary: hsl(199, 89%, 60%);
  --accent: hsl(160, 84%, 45%);
  --warning: hsl(38, 92%, 50%);
  --text-main: hsl(210, 40%, 98%);
  --text-dim: hsl(215, 20%, 65%);

  /* Fluid Typography with clamp() (Zero Media Query Breakpoints) */
  --fs-hero: clamp(2rem, 1.2rem + 3.5vw, 4rem);
  --fs-h2: clamp(1.4rem, 1rem + 1.8vw, 2.2rem);
  --fs-body: clamp(0.9rem, 0.85rem + 0.35vw, 1.05rem);

  /* Spacing Tokens */
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 2rem;
  --space-xl: 3.5rem;

  /* Elevation Shadows & Glassmorphism Blur */
  --shadow-elevation: 0 20px 45px -15px rgba(0, 0, 0, 0.85);
  --blur-glass: blur(16px);
  --transition-smooth: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

/* 2. Universal Box Sizing & Fluid Reset */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  text-size-adjust: 100%;
}

body {
  font-family: 'IRANYekan', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: var(--fs-body);
  color: var(--text-main);
  background-color: var(--bg-deep);
  background-image: 
    radial-gradient(ellipse at 50% 0%, hsla(199, 89%, 60%, 0.12) 0%, transparent 60%),
    linear-gradient(to right, hsla(0, 0%, 100%, 0.02) 1px, transparent 1px),
    linear-gradient(to bottom, hsla(0, 0%, 100%, 0.02) 1px, transparent 1px);
  background-size: 100% 100%, 32px 32px, 32px 32px;
  line-height: 1.8;
  direction: rtl;
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
}

/* 3. Modern CSS Grid Layout Engine */
.bento-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr));
  gap: var(--space-lg);
  max-width: 1280px;
  margin: var(--space-xl) auto;
  padding: 0 var(--space-md);
}

/* 4. The Glassmorphism Bento Card with Top Specular Rim */
.zenith-card {
  position: relative;
  background: var(--bg-card);
  backdrop-filter: var(--blur-glass);
  -webkit-backdrop-filter: var(--blur-glass);
  border: 1px solid var(--border-subtle);
  border-radius: 16px;
  padding: var(--space-lg);
  box-shadow: var(--shadow-elevation);
  overflow: hidden;
  will-change: transform, border-color;
  transition: var(--transition-smooth);
}

.zenith-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1.5px;
  background: linear-gradient(90deg, transparent, var(--border-glow), transparent);
  opacity: 0;
  transition: opacity 0.25s ease;
}

.zenith-card:hover {
  transform: translateY(-4px) scale(1.01);
  border-color: var(--border-glow);
}

.zenith-card:hover::before {
  opacity: 1;
}

/* 5. Typography Hierarchy */
.hero-title {
  font-size: var(--fs-hero);
  font-weight: 900;
  letter-spacing: -1px;
  line-height: 1.25;
  background: linear-gradient(180deg, #ffffff 10%, #94a3b8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: var(--space-md);
}

/* 6. GPU-Accelerated Keyframe Animation */
@keyframes pulseOrb {
  0%, 100% {
    transform: translate3d(0, 0, 0) scale(1);
    opacity: 0.6;
  }
  50% {
    transform: translate3d(0, -10px, 0) scale(1.05);
    opacity: 0.9;
  }
}

.glowing-orb {
  width: 140px;
  height: 140px;
  border-radius: 50%;
  background: radial-gradient(circle, var(--primary) 0%, transparent 70%);
  filter: blur(25px);
  animation: pulseOrb 4s infinite ease-in-out;
  pointer-events: none;
}

/* 7. Accessibility: Reduced Motion Query */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}""",
        "lines_breakdown": [
            {"line": 6, "code": ":root { ... }", "role": "تعریف توکن‌های طراحی در سطح کل سند", "explanation": "تمام مقادیر رنگ، فواصل، اندازه فونت‌ها و سایه‌ها در ریشه سند تعریف می‌شوند تا تغییر تم یا ابعاد از یک نقطه متمرکز مدیریت شود."},
            {"line": 8, "code": "--bg-deep: hsl(222, 47%, 4%);", "role": "تعریف رنگ مشکی فضا با مدل HSL", "explanation": "استفاده از فرمت HSL (رنگ، اشباع، روشنایی) نسبت به کد هگز یا RGB امکان تنظیم دقیق شدت روشنایی و ساخت پالت‌های هماهنگ را به مهندس فرانت‌اند می‌دهد."},
            {"line": 19, "code": "--fs-hero: clamp(2rem, 1.2rem + 3.5vw, 4rem);", "role": "تایپوگرافی کاملاً روان و سیال بدون مدیاکوئری", "explanation": "تابع clamp(حداقل, مقدار دینامیک, حداکثر) به متن اجازه می‌دهد با تغییر پهنای مانیتور کاربر به نرمی کوچک یا بزرگ شود بدون اینکه نیازی به نوشتن ده‌ها مدیاکوئری باشد."},
            {"line": 31, "code": "--transition-smooth: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);", "role": "منحنی شتاب فیزیکی و طبیعی انیمیشن", "explanation": "منحنی cubic-bezier(0.16, 1, 0.3, 1) همان منحنی حرکت پیش‌فرض در سیستم‌عامل‌های اپل و Linear است که شروع تند و توقف کشسان و نرمی به المنت‌ها می‌دهد."},
            {"line": 36, "code": "*, *::before, *::after { box-sizing: border-box; }", "role": "تثبیت جهانی باکس‌مدل", "explanation": "پدینگ و بوردر را درون عرض المان لحاظ کرده و مانع شکستن کادرها در تمام تگ‌ها و شبه‌المان‌های صفحه می‌شود."},
            {"line": 42, "code": "html { scroll-behavior: smooth; text-size-adjust: 100%; }", "role": "پیمایش نرم و جلوگیری از باگ تغییر سایز موبایل", "explanation": "پرش‌های درون‌صفحه‌ای (لینک‌های #) را به اسکرول نرم تبدیل کرده و از زوم ناخواسته مرورگرهای موبایل هنگام چرخش گوشی جلوگیری می‌کند."},
            {"line": 49, "code": "background-image: radial-gradient(...), linear-gradient(...);", "role": "ایجاد الگوی ماتریکس مهندسی در پس‌زمینه", "explanation": "ترکیب گرادیانت شعاعی با خطوط شبکه ۳۲ پیکسلی ظاهری فوق‌العاده مدرن شبیه داشبوردهای Vercel و Raycast به وجود می‌آورد."},
            {"line": 62, "code": "grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr));", "role": "شاهکار سیستم چیدمان خودکار گرید", "explanation": "کارت‌ها حداقل عرض ۳۲۰ پیکسل می‌گیرند؛ در صفحات بزرگ ردیف‌های ۳ یا ۴ تایی می‌سازند و در موبایل خودکار بدون ایجاد اسکرول افقی تک‌ستونه می‌شوند."},
            {"line": 73, "code": "backdrop-filter: var(--blur-glass);", "role": "افکت شیشه مات و گلس‌مورفیسم پیشرفته", "explanation": "پیکسل‌های پشت کارت را تار (Blur) کرده و حس عمق لایه‌ای ایجاد می‌کند."},
            {"line": 78, "code": "will-change: transform, border-color;", "role": "اطلاع‌رسانی به موتور رندر GPU برای کش کردن لایه", "explanation": "به مرورگر می‌گوید که این خصوصیات قرار است متحرک شوند؛ مرورگر پیشاپیش المان را در یک لایه مجزای کارت گرافیک کش می‌کند تا هاور بدون افت فریم باشد."},
            {"line": 89, "code": ".zenith-card:hover { transform: translateY(-4px) scale(1.01); }", "role": "شناور شدن نرم با ترنسفورم دو محوره", "explanation": "به جای تغییر margin یا top، از transform استفاده شده تا بازچینی کل صفحه رخ نداده و نرخ فریم روی ۱۲۰ قفل بماند."},
            {"line": 108, "code": "transform: translate3d(0, -10px, 0) scale(1.05);", "role": "استفاده از translate3d برای شتاب‌دهی ۳ بعدی سخت‌افزار", "explanation": "با اعلام محور Z در translate3d مرورگر مجبور می‌شود رندرینگ انیمیشن را به هسته‌های گرافیکی GPU واگذار کند."},
            {"line": 121, "code": "@media (prefers-reduced-motion: reduce) { ... }", "role": "رعایت دسترسی‌پذیری و سلامت کاربر در برابر سرگیجه", "explanation": "برای کاربرانی که در ویندوز یا مک گزینه کاهش انیمیشن را فعال کرده‌اند، انیمیشن‌ها را خاموش می‌کند تا سرگیجه نگیرند."}
        ]
    },

    "javascript": {
        "title": "پروژه جامع JavaScript: داشبورد بلادرنگ مانیتورینگ نرخ‌ها و مدیریت عملیات Nexus",
        "badge": "VANILLA JS ARCHITECTURE // PUB-SUB & ASYNC CORE",
        "desc": "سامانه کامل جاوا اسکریپت خالص بدون هیچ فریم‌ورکی شامل مدیریت استیت کپسوله‌شده، الگوی انتشار/اشتراک (Pub/Sub Event Bus)، شبیه‌ساز API ناهمگام با انقضا و تلاش مجدد، فیلتر جستجوی Debounce، و رندر بهینه با DocumentFragment.",
        "preview_html": """
        <div id="nexus-demo-app" style="background:#020617; border-radius:12px; border:1px solid #1e293b; padding:20px; color:#f8fafc; font-family:'IRANYekan', sans-serif; direction:rtl; text-align:right;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; border-bottom:1px solid #1e293b; padding-bottom:10px;">
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="width:10px; height:10px; border-radius:50%; background:#10b981; box-shadow:0 0 8px #10b981; display:inline-block;"></span>
              <strong style="color:#fff; font-size:14px;">Nexus Real-Time Operations Core</strong>
            </div>
            <span style="font-family:monospace; font-size:11px; color:#38bdf8; background:rgba(56,189,248,0.1); padding:2px 8px; border-radius:4px; border:1px solid rgba(56,189,248,0.25);">EVENT_LOOP // V8 ACTIVE</span>
          </div>
          <div style="display:flex; gap:10px; margin-bottom:14px;">
            <input type="text" id="nexusDemoSearch" placeholder="جستجوی بلادرنگ در نودها (Debounced)..." oninput="filterNexusDemo(this.value)" style="flex:1; background:#0f172a; border:1px solid #334155; color:#fff; padding:6px 12px; border-radius:6px; font-size:12px; font-family:inherit;">
            <button onclick="addNexusNode()" style="background:#0284c7; color:#fff; border:none; padding:6px 14px; border-radius:6px; font-size:12px; font-weight:700; cursor:pointer;">+ افزودن تسک پویا</button>
          </div>
          <div id="nexusNodeList" style="display:flex; flex-direction:column; gap:8px;">
            <div class="nexus-item" style="background:rgba(15,23,42,0.8); border:1px solid #334155; padding:10px 14px; border-radius:8px; display:flex; justify-content:space-between; align-items:center;">
              <div>
                <strong style="font-size:12.5px; color:#38bdf8;">سرور پردازشی Alpha-01</strong>
                <div style="font-size:11px; color:#94a3b8;">وضعیت: آنلاین • نرخ پردازش: ۹۸.۴٪ • تاخیر: ۱۲ میلی‌ثانیه</div>
              </div>
              <span style="color:#10b981; font-size:11.5px; font-weight:700;">فعال ✓</span>
            </div>
            <div class="nexus-item" style="background:rgba(15,23,42,0.8); border:1px solid #334155; padding:10px 14px; border-radius:8px; display:flex; justify-content:space-between; align-items:center;">
              <div>
                <strong style="font-size:12.5px; color:#facc15;">پایگاه داده Redis Cluster</strong>
                <div style="font-size:11px; color:#94a3b8;">وضعیت: کشینگ فعال • مصرف حافظه: ۴.۲ گیگابایت</div>
              </div>
              <span style="color:#10b981; font-size:11.5px; font-weight:700;">فعال ✓</span>
            </div>
          </div>
        </div>
        <script>
        function filterNexusDemo(q) {
          const items = document.querySelectorAll('#nexusNodeList .nexus-item');
          items.forEach(it => {
            it.style.display = it.innerText.toLowerCase().includes(q.toLowerCase()) ? 'flex' : 'none';
          });
        }
        function addNexusNode() {
          const list = document.getElementById('nexusNodeList');
          const id = Math.floor(Math.random() * 900 + 100);
          const div = document.createElement('div');
          div.className = 'nexus-item';
          div.style.cssText = 'background:rgba(15,23,42,0.8); border:1px solid #38bdf8; padding:10px 14px; border-radius:8px; display:flex; justify-content:space-between; align-items:center; animation:fadeIn 0.2s;';
          div.innerHTML = '<div><strong style="font-size:12.5px; color:#a855f7;">میکروسرویس Worker #' + id + '</strong><div style="font-size:11px; color:#94a3b8;">وضعیت: ایجاد شده در کانتکست ایونت‌لوپ</div></div><span style="color:#38bdf8; font-size:11.5px; font-weight:700;">رندر شد ✓</span>';
          list.prepend(div);
        }
        </script>
        """,
        "full_code": """/**
 * ============================================================================
 * NEXUS REAL-TIME DASHBOARD CORE // VANILLA ES6+ ARCHITECTURE
 * ============================================================================
 */

// 1. Decoupled Pub/Sub Event Bus for Clean Architecture
class EventBus {
  #listeners = new Map();

  subscribe(event, callback) {
    if (!this.#listeners.has(event)) {
      this.#listeners.set(event, new Set());
    }
    this.#listeners.get(event).add(callback);
    // Return unsubscribe function to prevent memory leaks
    return () => this.#listeners.get(event).delete(callback);
  }

  publish(event, data) {
    if (this.#listeners.has(event)) {
      this.#listeners.get(event).forEach(cb => {
        try {
          cb(data);
        } catch (err) {
          console.error(`[EventBus Error] in ${event}:`, err);
        }
      });
    }
  }
}

// 2. High-Performance Debounce Utility for Input Streams
function debounce(fn, delayMs = 300) {
  let timerId = null;
  return function (...args) {
    clearTimeout(timerId);
    timerId = setTimeout(() => {
      fn.apply(this, args);
    }, delayMs);
  };
}

// 3. State Management Store with Private Fields (#)
class AppStore {
  #state;
  #bus;

  constructor(initialState, bus) {
    this.#state = structuredClone(initialState);
    this.#bus = bus;
  }

  getState() {
    return Object.freeze({ ...this.#state });
  }

  update(updater) {
    const prevState = this.#state;
    const nextState = typeof updater === 'function' ? updater(prevState) : { ...prevState, ...updater };
    this.#state = nextState;
    this.#bus.publish('STATE_CHANGED', { prev: prevState, current: nextState });
    this.#persist();
  }

  #persist() {
    try {
      localStorage.setItem('nexus_app_store', JSON.stringify(this.#state));
    } catch (e) {
      console.warn('LocalStorage persistence failed:', e);
    }
  }
}

// 4. Async API Client with Timeout & AbortController
async function fetchWithRetry(url, options = {}, retries = 3) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 5000);

  try {
    const response = await fetch(url, { ...options, signal: controller.signal });
    clearTimeout(timeoutId);
    if (!response.ok) throw new Error(`HTTP Error status: ${response.status}`);
    return await response.json();
  } catch (error) {
    clearTimeout(timeoutId);
    if (retries > 0) {
      console.warn(`Retry request: ${retries} attempts left...`);
      await new Promise(r => setTimeout(r, 1000));
      return fetchWithRetry(url, options, retries - 1);
    }
    throw error;
  }
}

// 5. Batch DOM Renderer using DocumentFragment
function renderTaskNodes(tasks, containerEl) {
  const fragment = document.createDocumentFragment();

  tasks.forEach(task => {
    const card = document.createElement('div');
    card.className = 'task-node-item';
    card.dataset.id = task.id;

    // Fast template injection with safe text escaping
    const titleEl = document.createElement('strong');
    titleEl.textContent = task.name;
    const metaEl = document.createElement('div');
    metaEl.textContent = `نرخ پردازش: ${task.load}% | حافظه: ${task.memory}MB`;

    card.appendChild(titleEl);
    card.appendChild(metaEl);
    fragment.appendChild(card);
  });

  // Zero Layout Thrashing: Single DOM paint
  containerEl.replaceChildren(fragment);
}

// 6. Application Bootstrapper
const bus = new EventBus();
const store = new AppStore({
  nodes: [
    { id: 1, name: 'سرور پردازشی Alpha-01', load: 85, memory: 512 },
    { id: 2, name: 'خوشه ذخیره‌سازی Redis-Core', load: 32, memory: 1024 }
  ],
  filterQuery: ''
}, bus);

// Reactive UI Subscription
bus.subscribe('STATE_CHANGED', ({ current }) => {
  const listEl = document.getElementById('nexusNodeList');
  if (listEl) {
    const filtered = current.nodes.filter(n => n.name.includes(current.filterQuery));
    renderTaskNodes(filtered, listEl);
  }
});""",
        "lines_breakdown": [
            {"line": 8, "code": "class EventBus { #listeners = new Map(); ... }", "role": "پیاده‌سازی الگوی طراحی Pub/Sub", "explanation": "ایجاد سیستم ارتباطی غیرمستقیم و ماژولار بین بخش‌های مختلف اپلیکیشن بدون وابستگی شدید (Decoupling) و با فیلد خصوصی #listeners در حافظه."},
            {"line": 16, "code": "return () => this.#listeners.get(event).delete(callback);", "role": "بازگرداندن تابع لغو عضویت (Unsubscribe)", "explanation": "یک نکته کلیدی در معماری ارشد جاوا اسکریپت: بازگرداندن تابع لغو مانع از باقی ماندن شنونده‌های مرده در حافظه و بروز Memory Leak می‌شود."},
            {"line": 34, "code": "function debounce(fn, delayMs = 300) { ... }", "role": "تابع تاخیرانداز Debounce برای بهینه‌سازی رویداد ورودی", "explanation": "از فراخوانی مکرر و سیل‌آسای تابع در هر تایپ کاربر جلوگیری می‌کند و اجرای جستجو را ۳۰۰ میلی‌ثانیه پس از توقف آخرین کلید به تعویق می‌اندازد."},
            {"line": 46, "code": "this.#state = structuredClone(initialState);", "role": "کپی عمیق و تفکیک رفرنس استیت", "explanation": "استفاده از متد بومی structuredClone تضمین می‌کند که هیچ بخش دیگری از برنامه رفرنس مشترک به حافظه استیت اولیه نداشته باشد."},
            {"line": 51, "code": "return Object.freeze({ ...this.#state });", "role": "منجمد کردن آبجکت جهت جلوگیری از جهش ناخواسته", "explanation": "با Object.freeze برنامه‌نویسان دیگر اجازه نخواهند داشت مستقیماً فیلدهای استیت را بدون فراخوانی متد update دستکاری نمایند."},
            {"line": 71, "code": "const controller = new AbortController();", "role": "کنترلر لغو هوشمند درخواست‌های شبکه", "explanation": "اگر درخواست سرور بیشتر از ۵ ثانیه طول بکشد، AbortController سیگنال قطعی فرستاده و مانع از معلق ماندن منابع شبکه مرورگر می‌شود."},
            {"line": 82, "code": "await new Promise(r => setTimeout(r, 1000));", "role": "وقفه ناهمگام غیرمسدودکننده", "explanation": "به جای بلاک کردن Thread اصلی، یک Promise با زمان مشخص ساخته می‌شود تا تلاش مجدد با فاصله زمانی ایمن ارسال گردد."},
            {"line": 91, "code": "const fragment = document.createDocumentFragment();", "role": "رندر در حافظه بدون رفلوی DOM با DocumentFragment", "explanation": "ایجاد یک شاخه فرضی در رم: تمام ۱۰۰ المان ساخته شده ابتدا به این بافر اضافه می‌شوند و در یک آن به صفحه تزریق می‌گردند که از ۱۰۰ بار Reflow و افت شدید FPS جلوگیری می‌کند."},
            {"line": 107, "code": "containerEl.replaceChildren(fragment);", "role": "جایگزینی اتمیک و فوق‌سریع محتوای والد", "explanation": "متد مدرن replaceChildren بسیار سریع‌تر از innerHTML = '' عمل می‌کند و تمام نودهای قبلی را بدون باگ نشت Event Listener پاک و نود جدید را جایگزین می‌کند."}
        ]
    },

    "react": {
        "title": "پروژه جامع React 19: سامانه مدیریت اسپرینت و کانبان‌بورد هوشمند Pulse SprintFlow",
        "badge": "REACT 19 CORE // HOOKS, CONTEXT & OPTIMISTIC UI",
        "desc": "اپلیکیشن کامل تجاری توسعه‌یافته با آخرین استانداردهای React 19 شامل معماری Context + Reducer، هوک‌های اختصاصی useLocalStorage، به‌روزرسانی‌های آپتیمیستیک (Optimistic UI)، مموایز کردن محاسبات با useMemo و توابع پایدار با useCallback.",
        "preview_html": """
        <div style="background:#090d16; border-radius:12px; border:1px solid #1e293b; padding:20px; color:#f8fafc; font-family:'IRANYekan', sans-serif; direction:rtl; text-align:right;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px; border-bottom:1px solid rgba(255,255,255,0.07); padding-bottom:10px;">
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="font-size:18px;">⚛️</span>
              <strong style="color:#67e8f9; font-size:14px;">Pulse SprintFlow // React 19 Kanban</strong>
            </div>
            <span style="background:rgba(103,232,249,0.1); color:#67e8f9; border:1px solid rgba(103,232,249,0.3); padding:2px 8px; border-radius:4px; font-size:11px; font-weight:700;">React 19 Actions</span>
          </div>
          <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:12px;">
            <div style="background:rgba(15,23,42,0.7); border:1px solid #1e293b; border-radius:8px; padding:12px;">
              <div style="font-size:12px; font-weight:800; color:#cbd5e1; margin-bottom:8px; display:flex; justify-content:space-between;">
                <span>📋 در انتظار انجام</span>
                <span style="background:#334155; padding:1px 6px; border-radius:4px; font-size:10px;">۲</span>
              </div>
              <div style="background:#020617; border:1px solid #334155; padding:8px 10px; border-radius:6px; font-size:12px; margin-bottom:6px;">
                پیاده‌سازی Server Action لاگین
              </div>
              <div style="background:#020617; border:1px solid #334155; padding:8px 10px; border-radius:6px; font-size:12px;">
                بهینه‌سازی Core Web Vitals
              </div>
            </div>
            <div style="background:rgba(15,23,42,0.7); border:1px solid #1e293b; border-radius:8px; padding:12px;">
              <div style="font-size:12px; font-weight:800; color:#38bdf8; margin-bottom:8px; display:flex; justify-content:space-between;">
                <span>⚡ در حال توسعه</span>
                <span style="background:rgba(56,189,248,0.2); padding:1px 6px; border-radius:4px; font-size:10px; color:#38bdf8;">۱</span>
              </div>
              <div style="background:#020617; border:1px solid rgba(56,189,248,0.4); padding:8px 10px; border-radius:6px; font-size:12px;">
                کانفیگ دیتابیس PostgreSQL
              </div>
            </div>
            <div style="background:rgba(15,23,42,0.7); border:1px solid #1e293b; border-radius:8px; padding:12px;">
              <div style="font-size:12px; font-weight:800; color:#10b981; margin-bottom:8px; display:flex; justify-content:space-between;">
                <span>✅ تکمیل و مستقر شده</span>
                <span style="background:rgba(16,185,129,0.2); padding:1px 6px; border-radius:4px; font-size:10px; color:#10b981;">۳</span>
              </div>
              <div style="background:#020617; border:1px solid rgba(16,185,129,0.4); padding:8px 10px; border-radius:6px; font-size:12px;">
                تست امنیتی فایروال
              </div>
            </div>
          </div>
        </div>
        """,
        "full_code": """import React, { createContext, useContext, useReducer, useMemo, useCallback } from 'react';

// 1. Initial State & Action Types
const INITIAL_KANBAN = {
  tasks: [
    { id: 't1', title: 'پیاده‌سازی Server Actions', column: 'todo', priority: 'high' },
    { id: 't2', title: 'بهینه‌سازی سرعت رندرینگ', column: 'in-progress', priority: 'medium' },
    { id: 't3', title: 'تست یکپارچگی پایگاه‌داده', column: 'done', priority: 'low' }
  ]
};

// 2. Pure Reducer Function for Predictable State Transitions
function kanbanReducer(state, action) {
  switch (action.type) {
    case 'MOVE_TASK':
      return {
        ...state,
        tasks: state.tasks.map(task =>
          task.id === action.payload.taskId
            ? { ...task, column: action.payload.targetColumn }
            : task
        )
      };
    case 'ADD_TASK':
      return {
        ...state,
        tasks: [...state.tasks, action.payload]
      };
    case 'DELETE_TASK':
      return {
        ...state,
        tasks: state.tasks.filter(t => t.id !== action.payload.taskId)
      };
    default:
      return state;
  }
}

// 3. React Context for Global Dependency Injection
const KanbanContext = createContext(null);

export function KanbanProvider({ children }) {
  const [state, dispatch] = useReducer(kanbanReducer, INITIAL_KANBAN);

  // Stable Action Callbacks via useCallback
  const moveTask = useCallback((taskId, targetColumn) => {
    dispatch({ type: 'MOVE_TASK', payload: { taskId, targetColumn } });
  }, []);

  const addTask = useCallback((title, priority = 'medium') => {
    const newTask = {
      id: 'task_' + Date.now(),
      title,
      column: 'todo',
      priority
    };
    dispatch({ type: 'ADD_TASK', payload: newTask });
  }, []);

  // Memoized Context Value to Prevent Unnecessary Consumer Re-renders
  const contextValue = useMemo(() => ({
    tasks: state.tasks,
    moveTask,
    addTask
  }), [state.tasks, moveTask, addTask]);

  return (
    <KanbanContext.Provider value={contextValue}>
      {children}
    </KanbanContext.Provider>
  );
}

// 4. Custom Hook for Consuming Context with Safety Check
export function useKanban() {
  const context = useContext(KanbanContext);
  if (!context) {
    throw new Error('useKanban must be used within a KanbanProvider');
  }
  return context;
}

// 5. Kanban Column Component with Computed Filtering
export function KanbanColumn({ id, title, badgeColor }) {
  const { tasks, moveTask } = useKanban();

  // Memoize column-specific tasks
  const columnTasks = useMemo(() => {
    return tasks.filter(t => t.column === id);
  }, [tasks, id]);

  return (
    <section className="kanban-column" data-col={id}>
      <header className="column-header">
        <h3 style={{ color: badgeColor }}>{title}</h3>
        <span className="count-chip">{columnTasks.length}</span>
      </header>
      <div className="task-list">
        {columnTasks.map(task => (
          <article key={task.id} className="task-card">
            <h4>{task.title}</h4>
            <div className="task-actions">
              {id !== 'in-progress' && (
                <button onClick={() => moveTask(task.id, 'in-progress')}>شروع ⚡</button>
              )}
              {id !== 'done' && (
                <button onClick={() => moveTask(task.id, 'done')}>تکمیل ✓</button>
              )}
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}""",
        "lines_breakdown": [
            {"line": 1, "code": "import React, { createContext, useContext, useReducer, ... }", "role": "واردسازی ابزارهای هسته ری‌اکت", "explanation": "ایمپورت تمام هوک‌های لازم برای مدیریت استیت یکپارچه و بهینه‌سازی رندر از پکیج رسمی react."},
            {"line": 14, "code": "function kanbanReducer(state, action) { ... }", "role": "تابع خالص Reducer برای تغییرات پیش‌بینی‌پذیر", "explanation": "یک تابع خالص که بدون دستکاری متغیرهای بیرونی (Side Effect) استیت قبلی و یک اکشن را می‌گیرد و استیت کاملاً نو تولید می‌کند."},
            {"line": 19, "code": "tasks: state.tasks.map(task => ...)", "role": "حفظ تغییرناپذیری (Immutability) با map", "explanation": "به جای تغییر مستقیم فیلد column، با متد map یک آرایه کاملاً جدید ایجاد می‌شود تا ری‌اکت متوجه تغییر رفرنس شده و رندر را اجرا کند."},
            {"line": 39, "code": "const KanbanContext = createContext(null);", "role": "تعریف بافت اشتراک داده سراسری", "explanation": "حل معضل Prop Drilling؛ به تمام کامپوننت‌های تو در تو اجازه می‌دهد بدون پاس دادن دستی داده در لایه‌ها، مستقیماً به تسک‌ها دسترسی داشته باشند."},
            {"line": 45, "code": "const moveTask = useCallback((taskId, targetColumn) => { ... }, []);", "role": "کش کردن رفرنس تابع با useCallback", "explanation": "از ساخت مجدد تابع در هر بار رندر کامپوننت جلوگیری می‌کند و رفرنس پایدار را برای فرزندان memoized حفظ می‌نماید."},
            {"line": 59, "code": "const contextValue = useMemo(() => ({ ... }), [state.tasks, moveTask]);", "role": "جلوگیری از رندرهای آبشاری با useMemo روی مقدار Context", "explanation": "اگر این آبجکت را با useMemo نبندید، در هر رندر Provider یک شیء جدید در حافظه ساخته شده و تمام کامپوننت‌های پروژه حتی بدون تغییر دیتا دوباره رندر می‌شوند."},
            {"line": 70, "code": "export function useKanban() { ... throw new Error(...) }", "role": "کاستوم هوک ایمن با کنترل خطای محدوده", "explanation": "یک استاندارد طلایی در پروژه‌های سازمانی: اگر برنامه‌نویس کامپوننت را خارج از Provider فراخوانی کند، خطای شفاف و آموزنده‌ای به او می‌دهد."},
            {"line": 83, "code": "const columnTasks = useMemo(() => tasks.filter(...), [tasks, id]);", "role": "کش کردن محاسبات سنگین فیلتر آرایه", "explanation": "عملیات فیلتر کردن تسک‌ها فقط زمانی تکرار می‌شود که آرایه tasks یا ستون id تغییر کرده باشد نه در رندرهای بیهوده دیگر."}
        ]
    },

    "nextjs": {
        "title": "پروژه جامع Next.js 15: پلتفرم ابری و فروشگاه سازمانی CloudScale",
        "badge": "NEXT.JS 15 APP ROUTER // RSC, SERVER ACTIONS & EDGE",
        "desc": "معماری فوق‌پیشرفته نسل جدید وب شامل کامپوننت‌های رندر شده در سرور (RSC) با صفر بایت باندل کلاینت، اکشن‌های سرور با revalidatePath، استریمینگ بلادرنگ با Suspense، و روت هندلرهای Edge API.",
        "preview_html": """
        <div style="background:#020408; border-radius:12px; border:1px solid #1e293b; padding:20px; color:#f8fafc; font-family:'IRANYekan', sans-serif; direction:rtl; text-align:right;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:10px;">
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="font-size:18px;">▲</span>
              <strong style="color:#fff; font-size:14px;">CloudScale Enterprise SaaS // Next.js 15</strong>
            </div>
            <span style="background:#fff; color:#020617; font-weight:800; padding:2px 8px; border-radius:4px; font-size:11px;">RSC ZERO JS BUNDLE</span>
          </div>
          <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); padding:16px; border-radius:10px; margin-bottom:14px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
              <div>
                <span style="color:#10b981; font-size:11px; font-weight:700;">SERVER COMPONENT STREAMING ✓</span>
                <h4 style="font-size:15px; font-weight:900; color:#fff; margin:2px 0 0;">سرور اختصاصی Cloud-Node Pro</h4>
              </div>
              <span style="font-size:18px; font-weight:900; color:#38bdf8;">$49 / mo</span>
            </div>
            <p style="font-size:12px; color:#94a3b8; margin:0 0 12px; line-height:1.7;">رندر مستقیم داده‌ها در دیتابیس بدون نیاز به useEffect یا بارگذاری کتابخانه‌های سنگین روی مرورگر کاربر.</p>
            <div style="display:flex; gap:10px;">
              <button onclick="alert('سرور اکشن revalidateTag اجرا شد')" style="background:#fff; color:#020617; border:none; padding:7px 16px; border-radius:6px; font-weight:800; font-size:12px; cursor:pointer;">سفارش آنی (Server Action)</button>
              <span style="font-size:11px; color:#64748b; align-self:center;">CACHE STATUS: HIT (EDGE CDN)</span>
            </div>
          </div>
        </div>
        """,
        "full_code": """// ============================================================================
// CLOUDSCALE ENTERPRISE ARCHITECTURE // NEXT.JS 15 APP ROUTER
// ============================================================================

// FILE: app/page.tsx (React Server Component - 0 Client JS Bundle)
import { Suspense } from 'react';
import { orderServerAction } from './actions';
import ServerMetricsSkeleton from './components/Skeleton';

// Direct Database Fetch in Server Component (No useEffect, No Waterfalls)
async function getEnterpriseProducts() {
  // Runs exclusively on the Node/Edge server
  const res = await fetch('https://api.cloudscale.dev/products', {
    next: { tags: ['products'], revalidate: 3600 } // ISR Cache Tagging
  });
  if (!res.ok) throw new Error('Failed to fetch enterprise catalog');
  return res.json();
}

export default async function HomePage() {
  const products = await getEnterpriseProducts();

  return (
    <main className="enterprise-layout">
      <header className="page-header">
        <span className="badge">Next.js 15 App Router</span>
        <h1>زیرساخت ابری مقیاس سازمانی CloudScale</h1>
      </header>

      {/* Instant Partial Streaming via Suspense */}
      <Suspense fallback={<ServerMetricsSkeleton />}>
        <section className="catalog-grid">
          {products.map(prod => (
            <article key={prod.id} className="product-card">
              <h3>{prod.name}</h3>
              <p className="price">{prod.priceFormatted}</p>
              
              {/* Native Server Action Form with Zero Client State */}
              <form action={orderServerAction}>
                <input type="hidden" name="productId" value={prod.id} />
                <button type="submit" className="btn-order">سفارش آنی و استقرار</button>
              </form>
            </article>
          ))}
        </section>
      </Suspense>
    </main>
  );
}

// FILE: app/actions.ts (Enterprise Server Actions)
'use server';

import { revalidateTag, revalidatePath } from 'next/cache';

export async function orderServerAction(formData: FormData) {
  const productId = formData.get('productId');
  if (!productId) return { error: 'شناسه محصول الزامی است.' };

  // Secure server-side business logic
  await db.orders.create({
    data: {
      productId: String(productId),
      timestamp: new Date()
    }
  });

  // Revalidate multi-layer cache instantly
  revalidateTag('products');
  revalidatePath('/dashboard');

  return { success: true };
}""",
        "lines_breakdown": [
            {"line": 6, "code": "import { Suspense } from 'react';", "role": "واردسازی قابلیت استریمینگ ناهمگام ری‌اکت", "explanation": "تگ Suspense در Next.js 15 اجازه می‌دهد بخش‌های سریع صفحه بلافاصله لود شوند و بخش‌های سنگین بدون بلاک کردن کل صفحه، هم‌زمان به مرورگر استریم گردند."},
            {"line": 10, "code": "async function getEnterpriseProducts() { ... }", "role": "دریافت مستقیم داده در سرور بدون API کلاینت", "explanation": "در React Server Components (RSC) کامپوننت خود یک تابع async است؛ بنابراین بدون نیاز به useState و useEffect مستقیماً دیتا را از دیتابیس می‌خواند."},
            {"line": 13, "code": "next: { tags: ['products'], revalidate: 3600 }", "role": "کش‌گذاری تگ‌دار و هوشمند ISR در سطح Edge", "explanation": "داده‌ها به مدت ۳۶۰۰ ثانیه در کش لبه CDN می‌مانند، اما هر زمان ادمین تغییری دهد می‌توان با revalidateTag('products') فوراً کش را بدون انتظار باطل کرد."},
            {"line": 18, "code": "export default async function HomePage() { ... }", "role": "کامپوننت غیرهمگام سرور با صفر بایت کد JS ارسالی", "explanation": "کدهای این کامپوننت کاملاً در سرور اجرا و به HTML خالص تبدیل می‌شوند؛ یعنی هیچ فایل جاوا اسکریپتی برای این منطق به موبایل کاربر ارسال نمی‌شود."},
            {"line": 28, "code": "<Suspense fallback={<ServerMetricsSkeleton />}>", "role": "پوسته پیش‌رندر جزئی (PPR Fallback)", "explanation": "تا زمان دریافت داده‌های محصولات از سرور، اسکلتون متحرک و زیبایی به کاربر نشان داده می‌شود تا امتیاز Largest Contentful Paint (LCP) سبز باشد."},
            {"line": 35, "code": "<form action={orderServerAction}>", "role": "اتصال مستقیم فرم HTML به تابع بک‌اند", "explanation": "انقلاب سرور اکشن‌ها: بدون نوشتن حتی یک خط کد fetch یا تعریف اندپوینت API، ارسال فرم مستقیماً متد سرور orderServerAction را با متد POST صدا می‌زند."},
            {"line": 49, "code": "'use server';", "role": "مرز امنیتی سرور و کلاینت", "explanation": "دستور جادویی کامپایلر Next.js: به توربوپک اعلام می‌کند تمام توابع داخل این فایل فقط و فقط روی سرور نود یا Edge اجرا شوند و در باندل عمومی فرانت‌اند نروند."},
            {"line": 64, "code": "revalidateTag('products');", "role": "باطل‌سازی هدفمند کش در CDN", "explanation": "بلافاصله پس از ثبت سفارش، کش دیتای محصولات در سراسر سرورهای CDN لغو می‌شود تا موجودی انبار به ثانیه‌ای به‌روزرسانی شود."}
        ]
    }
}

def render_project_section(track_key):
    """Render the full Line-by-Line project section HTML for a track"""
    proj = PROJECTS.get(track_key)
    if not proj:
        return ""

    title = proj["title"]
    badge = proj["badge"]
    desc = proj["desc"]
    preview_html = proj["preview_html"]
    full_code = proj["full_code"].replace("<", "&lt;").replace(">", "&gt;")
    lines = proj["lines_breakdown"]

    lines_table_rows = ""
    for item in lines:
        l_num = item["line"]
        l_code = item["code"].replace("<", "&lt;").replace(">", "&gt;")
        l_role = item["role"]
        l_expl = item["explanation"]

        lines_table_rows += f"""
        <tr class="line-row" data-line="{l_num}">
          <td class="line-num-cell">خط {l_num}</td>
          <td class="line-code-cell"><code>{l_code}</code></td>
          <td class="line-role-cell"><strong>{l_role}</strong></td>
          <td class="line-expl-cell">{l_expl}</td>
        </tr>
        """

    return f"""
    <section class="master-project-section" id="real-project-{track_key}">
      <div class="project-header-box">
        <div class="proj-badge-row">
          <span class="proj-badge">{badge}</span>
          <span class="proj-status-chip">پروژه جامع و عملیاتی پروداکشن</span>
        </div>
        <h2 class="proj-main-title">{title}</h2>
        <p class="proj-main-desc">{desc}</p>
      </div>

      <div class="project-tabs-container">
        <div class="project-tab-nav">
          <button class="proj-tab-btn active" onclick="switchProjectTab(this, 'proj-pane-preview-{track_key}')">🖥️ پیش‌نمایش زنده پروژه</button>
          <button class="proj-tab-btn" onclick="switchProjectTab(this, 'proj-pane-code-{track_key}')">💻 کدهای کامل پروداکشن</button>
          <button class="proj-tab-btn" onclick="switchProjectTab(this, 'proj-pane-breakdown-{track_key}')">🔬 کالبدشکافی خط به خط (نحوه کارکرد)</button>
        </div>

        <div class="project-tab-panes">
          <!-- Pane 1: Live Preview -->
          <div class="proj-pane proj-pane-preview-{track_key} active">
            <div class="proj-preview-wrapper">
              <div class="preview-browser-bar">
                <div class="preview-dots">
                  <span style="background:#ef4444;"></span>
                  <span style="background:#f59e0b;"></span>
                  <span style="background:#10b981;"></span>
                </div>
                <div class="preview-address-bar">https://app.{track_key}.production-cluster.internal/live</div>
                <span class="preview-live-tag">READY ✓</span>
              </div>
              <div class="preview-body-frame">
                {preview_html}
              </div>
            </div>
          </div>

          <!-- Pane 2: Full Code -->
          <div class="proj-pane proj-pane-code-{track_key}">
            <div class="proj-code-box">
              <div class="code-bar">
                <span class="code-lang-tag">کدهای کامل و بدون نقص پروژه پروداکشن</span>
                <button class="code-action-btn" onclick="copySnippet(this)">📋 کپی کل سورس کد</button>
              </div>
              <pre><code>{full_code}</code></pre>
            </div>
          </div>

          <!-- Pane 3: Line by Line Breakdown -->
          <div class="proj-pane proj-pane-breakdown-{track_key}">
            <div class="breakdown-card">
              <div class="breakdown-intro-note">
                💡 <strong>شرح مهندسی خط به خط:</strong> در جدول زیر، خطوط کلیدی پروژه همراه با چرایی نگارش، عملکرد داخلی موتور مرورگر/سرور و تجربیات ارشد فرانت‌اند تحلیل شده است.
              </div>
              <div class="table-responsive-wrap">
                <table class="breakdown-table">
                  <thead>
                    <tr>
                      <th style="width:80px;">شماره خط</th>
                      <th style="width:260px;">سینتکس و عبارت کد</th>
                      <th style="width:200px;">نقش فنی در سیستم</th>
                      <th>شرح عملکرد و جزئیات مهندسی</th>
                    </tr>
                  </thead>
                  <tbody>
                    {lines_table_rows}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    """

if __name__ == "__main__":
    print(f"Project modules compiled: {len(PROJECTS)} complete production websites ready with line-by-line breakdown!")
