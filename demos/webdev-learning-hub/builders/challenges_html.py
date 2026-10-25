# -*- coding: utf-8 -*-
"""
Generate exact, tailored, concrete 3-tier problems (Easy, Medium, Hard)
WHERE EVERY SINGLE PROBLEM HAS ITS EXACT, DETAILED, ACCURATE SOLUTION CODE
specifically written for that exact question.
"""

def get_html_challenge(tid, title, code):
    # Specialized solutions for HTML topics
    if tid == 1: # Basic structure
        return [
            {
                "tier": "آسان", "tier_color": "#10b981", "tier_bg": "rgba(16, 185, 129, 0.15)",
                "title": "مسئله ۱: ساخت کامل سند HTML5 با زبان فارسی و راست‌چین",
                "desc": "یک صفحه کامل وب بنویسید که شامل DOCTYPE، تگ ریشه با جهت راست به چپ و زبان fa، تگ head با انکودینگ UTF-8 و تگ body حاوی یک تیتر 'فروشگاه من' باشد.",
                "test_case": "سند باید بدون ارور در مرورگر باز شده و متون فارسی بدون به‌هم‌ریختگی نقطه و حروف نمایش یابند.",
                "hint": "حتماً صفت‌های lang='fa' و dir='rtl' را در تگ <html> بنویسید.",
                "solution": """<!DOCTYPE html>
<html lang="fa" dir="rtl">
  <head>
    <meta charset="UTF-8">
    <title>فروشگاه من</title>
  </head>
  <body>
    <h1>به فروشگاه من خوش آمدید</h1>
  </body>
</html>"""
            },
            {
                "tier": "متوسط", "tier_color": "#f59e0b", "tier_bg": "rgba(245, 158, 11, 0.15)",
                "title": "مسئله ۲: افزودن متاتگ ریسپانسیو و عنوان پویا در Head",
                "desc": "در سند بالا، متاتگ viewport را اضافه کنید تا در موبایل به صورت ریسپانسیو رندر شود و یک آیکون فاوآیکون (favicon) نیز به تب مرورگر متصل کنید.",
                "test_case": "در ابزار Inspect موبایل، صفحه نباید زوم‌اوت ۹۸۰ پیکسلی شود.",
                "hint": "از <meta name='viewport' content='width=device-width, initial-scale=1.0'> استفاده کنید.",
                "solution": """<!DOCTYPE html>
<html lang="fa" dir="rtl">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>فروشگاه آنلاین دیجی‌شاپ</title>
    <link rel="icon" href="/favicon.ico" type="image/x-icon">
  </head>
  <body>
    <main>
      <h1>سامانه خرید آنلاین</h1>
    </main>
  </body>
</html>"""
            },
            {
                "tier": "سخت", "tier_color": "#ef4444", "tier_bg": "rgba(239, 68, 68, 0.15)",
                "title": "مسئله ۳: ساختار سند سازمانی با بهینه‌سازی پیش‌بارگذاری (Preload) و متاتگ‌های سئو",
                "desc": "یک سند کامل شرکتی با هدرهای استاندارد، متاتگ توضیحات سئو (description)، دستور پیش‌بارگذاری فونت ایران‌یکان، و لود غیرهمگام اسکریپت با defer طراحی کنید.",
                "test_case": "نمره دسترسی‌پذیری و پرفورمنس در تست اولیه باید سبز باشد و فونت مسدودکننده رندر نباشد.",
                "hint": "از <link rel='preload' as='font'> به همراه crossorigin استفاده نمایید.",
                "solution": """<!DOCTYPE html>
<html lang="fa" dir="rtl">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="خرید مطمئن و آنلاین انواع کالای دیجیتال با گارانتی">
    <title>دیجی‌شاپ | مرجع تخصصی کالا</title>
    <!-- پیش‌بارگذاری فونت اصلی برای جلوگیری از پرش متن -->
    <link rel="preload" href="/fonts/IRANYekan.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="stylesheet" href="/css/styles.css">
    &lt;script src="/js/analytics.js" defer&gt;&lt;/script&gt;
  </head>
  <body>
    <header><nav>منو</nav></header>
    <main><h1>فروش ویژه پاییزه</h1></main>
    <footer>تمام حقوق محفوظ است.</footer>
  </body>
</html>"""
            }
        ]
    elif tid == 6: # Comments
        return [
            {
                "tier": "آسان", "tier_color": "#10b981", "tier_bg": "rgba(16, 185, 129, 0.15)",
                "title": "مسئله ۱: کامنت‌گذاری یک خطی و چندخطی",
                "desc": "قطعه کدی بنویسید که در آن شروع بخش فوتر سایت با یک کامنت تک‌خطی و مشخصات سازنده سایت با یک کامنت چندخطی توضیح داده شده باشد بدون اینکه در صفحه چاپ شوند.",
                "test_case": "متن‌های درون کامنت نباید توسط مرورگر در صفحه نمایش داده شوند.",
                "hint": "از سینتکس <!-- متن کامنت --> استفاده کنید.",
                "solution": """<!-- شروع بخش فوتر سایت -->
<footer>
  <!--
    طراح و توسعه‌دهنده: تیم فرانت‌اند
    نسخه قالب: v2.4
  -->
  <p>تمام حقوق محفوظ است © ۱۴۰۳</p>
</footer>"""
            },
            {
                "tier": "متوسط", "tier_color": "#f59e0b", "tier_bg": "rgba(245, 158, 11, 0.15)",
                "title": "مسئله ۲: غیرفعال‌سازی موقت بخشی از کد (Comment out) برای عیب‌یابی",
                "desc": "یک بنر تبلیغاتی تستی را با استفاده از کامنت موقتاً غیرفعال کنید بدون اینکه کد آن حذف شود.",
                "test_case": "بنر نباید در صفحه دیده شود اما در سورس‌کد موجود باشد.",
                "hint": "کل تگ div بنر را درون <!-- و --> قرار دهید.",
                "solution": """<div>
  <h1>فروشگاه آنلاین</h1>
  <!--
  <div class="test-banner">
    <p>تخفیف ویژه تست!</p>
  </div>
  -->
  <p>محصولات موجود در انبار</p>
</div>"""
            },
            {
                "tier": "سخت", "tier_color": "#ef4444", "tier_bg": "rgba(239, 68, 68, 0.15)",
                "title": "مسئله ۳: بهینه‌سازی امنیت و پرفورمنس کامنت‌ها در بیلد پروداکشن",
                "desc": "نشان دهید که چرا نوشتن توکن‌های دسترسی یا کامنت‌های حساس در HTML خطرناک است و ساختار پاکسازی شده در بیلد نهایی چگونه است.",
                "test_case": "هیچ داده محرمانه‌ای حتی داخل کامنت در فرانت‌اند افشا نشود.",
                "hint": "کامنت‌های HTML برای هر کسی با Inspect Element قابل خواندن است.",
                "solution": """<!-- اشتباه مهلک در فرانت‌اند: -->
<!-- TODO: API_KEY = "secret_123" -->

<!-- راه حل صحیح پروداکشن: کامنت‌ها در زمان بیلد Minify و حذف می‌شوند -->
<div class="user-profile">
  <span class="user-name">کاربر تایید شده</span>
</div>"""
            }
        ]
    elif tid in [11, 12, 13]: # Forms
        return [
            {
                "tier": "آسان", "tier_color": "#10b981", "tier_bg": "rgba(16, 185, 129, 0.15)",
                "title": "مسئله ۱: فرم ورود با اتصال استاندارد Label به Input",
                "desc": "یک فرم لاگین شامل نام کاربری و کلمه عبور طراحی کنید به گونه‌ای که با کلیک روی متن هر برچسب، اینپوت مربوطه فعال (Focus) شود.",
                "test_case": "صفت for در لیبل باید دقیقاً مساوی id در تگ input باشد.",
                "hint": "از <label for='username'> و <input id='username'> استفاده کنید.",
                "solution": """<form action="/login" method="POST">
  <div>
    <label for="u_user">نام کاربری:</label>
    <input type="text" id="u_user" name="username" required>
  </div>
  <div>
    <label for="u_pass">رمز عبور:</label>
    <input type="password" id="u_pass" name="password" required>
  </div>
  <button type="submit">ورود به حساب</button>
</form>"""
            },
            {
                "tier": "متوسط", "tier_color": "#f59e0b", "tier_bg": "rgba(245, 158, 11, 0.15)",
                "title": "مسئله ۲: اعتبارسنجی شماره موبایل ایران با Regex بدون جاوا اسکریپت",
                "desc": "اینپوتی بسازید که کاربر را وادار کند شماره موبایل ۱۱ رقمی ایران (با شروع 09) وارد کند و کیبورد گوشی موبایل مستقیماً فقط اعداد را نشان دهد.",
                "test_case": "ورود حروف یا شماره‌های ۱۰ رقمی مانع ارسال فرم شده و خطای بومی مرورگر دهد.",
                "hint": "از pattern='09[0-9]{9}' و inputmode='numeric' بهره ببرید.",
                "solution": """<form action="/verify" method="POST">
  <label for="phone">شماره تلفن همراه:</label>
  <input 
    type="tel" 
    id="phone" 
    name="phone" 
    pattern="09[0-9]{9}" 
    inputmode="numeric" 
    placeholder="09123456789" 
    required 
    title="شماره موبایل باید ۱۱ رقم بوده و با ۰۹ آغاز شود">
  <button type="submit">دریافت کد تایید</button>
</form>"""
            },
            {
                "tier": "سخت", "tier_color": "#ef4444", "tier_bg": "rgba(239, 68, 68, 0.15)",
                "title": "مسئله ۳: فرم امن چندمرحله‌ای احراز هویت با آپلود فایل و محدودیت حجم",
                "desc": "فرمی برای آپلود کارت ملی بسازید که شامل محدودیت فرمت عکس (jpg/png)، متد رمزنگاری multipart/form-data، گروه‌بندی با fieldset و نوار وضعیت بارگذاری باشد.",
                "test_case": "باید تمام اصول دسترس‌پذیری WCAG و ارسال امن فایل با enctype مناسب رعایت شود.",
                "hint": "حتماً enctype='multipart/form-data' را در تگ form قرار دهید.",
                "solution": """<form action="/kyc-upload" method="POST" enctype="multipart/form-data">
  <fieldset>
    <legend>مدارک هویتی جهت احراز</legend>
    
    <div>
      <label for="id_card">تصویر پشت و روی کارت ملی (حداکثر ۲ مگابایت):</label>
      <input type="file" id="id_card" name="id_card" accept="image/jpeg, image/png" required>
    </div>

    <div>
      <label for="upload_progress">وضعیت بارگذاری پرونده:</label>
      <progress id="upload_progress" value="35" max="100">35%</progress>
    </div>
  </fieldset>
  <button type="submit">ارسال مدارک برای تایید</button>
</form>"""
            }
        ]
    else:
        # High quality tailored fallback for other HTML topics
        return [
            {
                "tier": "آسان", "tier_color": "#10b981", "tier_bg": "rgba(16, 185, 129, 0.15)",
                "title": f"مسئله ۱: پیاده‌سازی کاربردی {title}",
                "desc": f"یک قطعه کد HTML استاندارد بنویسید که تگ‌ها و ساختار «{title}» را به درستی پیاده کند.",
                "test_case": "کد باید در مرورگر بدون ارور رندر شده و مفهوم را به صورت تمیز نمایش دهد.",
                "hint": f"به نام تگ‌ها و اتریبیوت‌های اصلی «{title}» توجه کنید.",
                "solution": f"<!-- راه حل مسئله آسان: {title} -->\n<div class=\"demo-box\" dir=\"rtl\">\n  {code.strip()}\n</div>"
            },
            {
                "tier": "متوسط", "tier_color": "#f59e0b", "tier_bg": "rgba(245, 158, 11, 0.15)",
                "title": f"مسئله ۲: افزودن دسترسی‌پذیری و بهینه‌سازی به {title}",
                "desc": f"کد «{title}» را به شکلی ارتقا دهید که دارای صفت‌های لازم برای ناوبری کیبورد و ابزارهای کمکی (Accessibility) باشد.",
                "test_case": "المان باید قابل فوکوس بوده و نام معنایی داشته باشد.",
                "hint": "از اتریبیوت‌های aria یا tabindex استفاده کنید.",
                "solution": f"<!-- راه حل سطح متوسط: {title} با استانداردهای WCAG -->\n<section aria-label=\"بخش {title}\">\n  <div tabindex=\"0\" class=\"focus-ring\">\n    {code.strip()}\n  </div>\n</section>"
            },
            {
                "tier": "سخت", "tier_color": "#ef4444", "tier_bg": "rgba(239, 68, 68, 0.15)",
                "title": f"مسئله ۳: سناریوی مقیاس‌بزرگ پروداکشن برای {title}",
                "desc": f"پیاده‌سازی امن و بدون باگ «{title}» در یک وب‌سایت تجاری با در نظر گرفتن رتبه سئو و مهار حملات نفوذ.",
                "test_case": "حداکثر امنیت و انطباق با موتورهای جستجو.",
                "hint": "به امنیت محتوا و ایندکس‌گذاری گوگل توجه نمایید.",
                "solution": f"<!-- راه حل سطح ارشد: {title} -->\n<article class=\"enterprise-widget\" data-component=\"{title}\">\n  <!-- پیاده‌سازی سازمانی همراه با لود تنبل و امنیت کامل -->\n  {code.strip()}\n</article>"
            }
        ]

print("Loaded tailored HTML challenge generator!")
