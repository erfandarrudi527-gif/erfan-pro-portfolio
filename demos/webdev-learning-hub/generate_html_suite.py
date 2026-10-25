# -*- coding: utf-8 -*-
import os, subprocess

html_topics = [
    # مبتدی (1-10)
    ("1. ساختار پایه سند", "<!DOCTYPE>, html, head, body", "مبتدی",
     "اسکلت بدن انسان یا کادر اولیه یک برگه اداری؛ سر (head) حاوی مغز و مشخصات پنهان است و تن (body) هر آن چیزی است که به چشم می‌آید.",
     "سند با <!DOCTYPE html> آغاز می‌شود که زبان و نسخه را به مرورگر می‌گوید. تگ html کل صفحه را در بر می‌گیرد، head برای تنظیمات، تیتر تب و استایل‌هاست و body محل نمایش متون و عکس‌هاست.",
     "<!DOCTYPE html>\n<html lang=\"fa\" dir=\"rtl\">\n  <head>\n    <meta charset=\"UTF-8\">\n    <title>صفحه اول</title>\n  </head>\n  <body>\n    <h1>سلام دنیا!</h1>\n  </body>\n</html>",
     "همیشه dir=\"rtl\" را بگذارید تا چیدمان جملات فارسی از راست به چپ منظم باشد."),

    ("2. تگ‌های متنی", "h1-h6, p, span, strong, em, br, hr", "مبتدی",
     "تیترهای روزنامه (h1 تا h6)، پاراگراف‌های مقاله (p)، ماژیک فسفری برای پررنگ کردن (strong) و خط‌کش برای جدا کردن بخش‌ها (hr).",
     "تیترها با h1 بزرگ‌ترین تا h6 کوچک‌ترین تعریف می‌شوند. برای متن‌های معمولی از p، برای پررنگ کردن معنایی از strong، برای تاکید مورب از em، برای شکستن خط از br و برای خط افقی از hr استفاده می‌شود.",
     "<h1>تیتر اصلی صفحه</h1>\n<p>این یک پاراگراف است که کلمه <strong>مهم</strong> در آن پررنگ شده است.</p>\n<hr>\n<p>خط جدید با <br> شکسته شد.</p>",
     "در هر صفحه وب فقط یک بار از h1 استفاده کنید تا موتورهای جستجو موضوع اصلی صفحه را گم نکنند."),

    ("3. لیست‌ها", "ul, ol, li, dl", "مبتدی",
     "لیست خرید بقالی بدون ترتیب (ul با بولت)، دستور پخت کیک با ترتیب مراحل شماره‌دار (ol)، و واژه‌نامه انگلیسی با تعریف (dl).",
     "تگ ul لیست نامرتب (نقطه‌ای) و ol لیست مرتب (۱، ۲، ۳) می‌سازد. هر قلم داخل li قرار می‌گیرد. تگ dl برای لیست توضیحات (شامل dt برای عنوان و dd برای شرح) است.",
     "<!-- لیست نامرتب -->\n<ul>\n  <li>نان</li>\n  <li>شیر</li>\n</ul>\n\n<!-- لیست شماره‌دار -->\n<ol>\n  <li>مرحله اول</li>\n  <li>مرحله دوم</li>\n</ol>",
     "بخش‌های ناوبری سایت (منوها) را همیشه داخل یک ul درون تگ nav بسازید."),

    ("4. لینک‌ها", "a، لینک داخلی، خارجی، anchor", "مبتدی",
     "درب‌های جادویی بین اتاق‌ها یا آسانسوری که شما را به طبقه خاصی از همان صفحه پرتاب می‌کند.",
     "تگ <a> با ویژگی href آدرس مقصد را می‌گیرد. برای لینک خارجی آدرس کامل با https، برای لینک داخلی مسیر فایل و برای پرش درون صفحه آیدی المان (#section-id) وارد می‌شود.",
     "<a href=\"https://google.com\" target=\"_blank\">رفتن به گوگل</a>\n<a href=\"/about.html\">درباره ما</a>\n<a href=\"#contact\">پرش به فرم تماس</a>",
     "وقتی لینک خارجی با target=\"_blank\" باز می‌کنید، حتما rel=\"noopener noreferrer\" اضافه کنید تا امنیت صفحه حفظ شود."),

    ("5. تصاویر", "img، alt، width/height", "مبتدی",
     "قاب عکسی که روی دیوار می‌زنید، به همراه یک توضیح زیر عکس برای افراد نابینا یا وقتی عکس بارگذاری نمی‌شود.",
     "تگ <img> تگ تک‌بخشی بدون بسته شدن است. آدرس عکس در src، و متن جایگزین برای دسترسی‌پذیری و سئو در alt قرار می‌گیرد. وارد کردن width و height از پرش صفحه جلوگیری می‌کند.",
     "<img src=\"banner.jpg\" alt=\"تصویر همایش برنامه‌نویسی تهران\" width=\"800\" height=\"400\">",
     "ویژگی alt را هرگز خالی نگذارید؛ این متن هویت عکس برای موتورهای جستجو و صفحه‌خوان‌هاست."),

    ("6. کامنت‌ها", "<!-- ... -->", "مبتدی",
     "یادداشت‌های چسبان پشت صحنه که فقط خودت و برنامه‌نویس بعدی می‌بینید و مشتری اصلاً از وجودش باخبر نمی‌شود.",
     "کامنت‌ها کدهایی هستند که توسط مرورگر اجرا یا نمایش داده نمی‌شوند و برای توضیح بخش‌های مختلف کد کاربرد دارند.",
     "<!-- این بخش مربوط به فوتر سایت است -->\n<footer>\n  <p>تمام حقوق محفوظ است</p>\n</footer>",
     "اطلاعات حساس مثل رمز عبور یا کلیدهای امنیتی را حتی داخل کامنت هم در فرانت‌اند ننویسید."),

    ("7. ویژگی‌ها (Attributes)", "id, class, title, style", "مبتدی",
     "کد ملی (id: یکتا در کل دنیا)، فرم مدرسه یا لباس ورزشی (class: اشتراکی بین خیلی‌ها)، و تول‌تیپ کمکی (title).",
     "ویژگی‌ها اطلاعات و رفتار اضافی به تگ می‌دهند. id باید در تمام صفحه تک و منحصر‌به‌فرد باشد، در حالی که class می‌تواند روی بی‌شمار المان اعمال شود.",
     "<button id=\"submit-btn\" class=\"btn btn-primary\" title=\"ارسال فرم\">\n  ارسال\n</button>",
     "هیچ‌وقت دو المان با یک id مشابه در یک صفحه نسازید؛ جاوا اسکریپت و استایل‌ها به مشکل می‌خورند."),

    ("8. المنت‌های Block و Inline", "تفاوت جریان نمایش", "مبتدی",
     "المنت Block مثل یک آجر مستطیل سنگین است که کل عرض ردیف را می‌گیرد؛ المنت Inline مثل یک کلمه درون متن است که فقط به اندازه خودش جا می‌گیرد.",
     "عناصر Block مثل div, p, h1 به صورت پیش‌فرض در خط جدید شروع شده و کل عرض را پر می‌کنند. عناصر Inline مثل span, a, strong در ادامه متن جاری می‌نشینند.",
     "<p>این بلاک است و کل عرض را می‌گیرد.</p>\n<p>اینجا یک کلمه <span style=\"color:red;\">قرمز</span> درون متن است.</p>",
     "داخل یک المان Inline نباید یک المان Block قرار دهید (مگر تگ <a> در HTML5 که می‌تواند کارت‌ها را لینک کند)."),

    ("9. جدول‌ها", "table, tr, td, th, thead, tbody, colspan, rowspan", "مبتدی",
     "شیت اکسل با سطرهای افقی، ستون‌های عمودی، سربرگ پررنگ و امکان ادغام سلول‌ها مثل جدول نمرات دانش‌آموزان.",
     "تگ table کل جدول را تشکیل می‌دهد، tr نشان‌دهنده سطر، th سلول سربرگ پررنگ، و td داده‌های عادی است. thead و tbody دسته‌بندی سمانتیک به جدول می‌دهند. colspan و rowspan برای ادغام ستون و سطر هستند.",
     "<table border=\"1\">\n  <thead>\n    <tr><th>نام</th><th>سن</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>عرفان</td><td>۲۴</td></tr>\n  </tbody>\n</table>",
     "از جدول فقط برای نمایش داده‌های جدولی استفاده کنید، هرگز ساختار و چیدمان کل صفحه را با جدول نسازید!"),

    ("10. موجودیت‌ها (Entities)", "&nbsp;, &lt;, &gt;, &amp;", "مبتدی",
     "کدهای رمزی فرار برای کاراکترهایی که مرورگر فکر می‌کند دستور هستند؛ مثلا وقتی می‌خواهید علامت < را چاپ کنید بدون اینکه تگ باز شود.",
     "در HTML کاراکترهایی مثل < یا > رزرو شده‌اند. برای چاپ مستقیم آن‌ها از entity استفاده می‌کنیم: &lt; برای کوچکتر، &gt; برای بزرگتر، و &nbsp; برای فاصله نشکن.",
     "<p>برای نوشتن تگ، بنویسید: &lt;div&gt; &amp; &lt;span&gt;</p>\n<p>فاصله&nbsp;&nbsp;&nbsp;زیاد بین دو کلمه</p>",
     "برای علامت کپی‌رایت همیشه از &copy; استفاده کنید تا در تمام مرورگرها استاندارد رندر شود."),

    # متوسط (11-23)
    ("11. فرم‌ها", "form, input, textarea, select, button, label, fieldset", "متوسط",
     "برگه ثبت‌نام کاغذی بانک با کادرهای پر کردنی، منوی انتخاب شهر، و دکمه امضا و تحویل به باجه.",
     "تگ form چارچوب جمع‌آوری داده‌هاست. label نام و راهنمای هر فیلد، textarea برای متن‌های طولانی چندخطی، select برای منوی کرکره‌ای و button برای ارسال است.",
     "<form action=\"/submit\" method=\"POST\">\n  <fieldset>\n    <legend>اطلاعات کاربری</legend>\n    <label for=\"user\">نام کاربری:</label>\n    <input type=\"text\" id=\"user\" name=\"username\">\n    <button type=\"submit\">ورود</button>\n  </fieldset>\n</form>",
     "همیشه label را با ویژگی for به id اینپوت وصل کنید تا وقتی روی متن کلیک شد، اینپوت فوکوس بگیرد."),

    ("12. انواع input", "text, email, password, number, date, checkbox, radio, file, range, color", "متوسط",
     "انواع مختلف کادرهای فرم؛ جعبه متن، ستاره‌های رمزی، تقویم بازشو، دکمه‌های تیک‌زدنی چندگزینه‌ای، و پالت رنگ.",
     "با تغییر ویژگی type در تگ input، رفتار و کیبورد ورودی موبایل تغییر می‌کند. مثلا email کیبورد @ را نشان می‌دهد و password کاراکترها را ماسک می‌کند.",
     "<input type=\"email\" placeholder=\"ایمیل خود را بزنید\">\n<input type=\"password\" placeholder=\"رمز عبور\">\n<input type=\"color\" value=\"#ff0000\">\n<input type=\"range\" min=\"0\" max=\"100\">",
     "برای دکمه‌های رادیویی هم‌گروه، حتما ویژگی name را یکسان بگذارید تا کاربر فقط بتواند یک گزینه را انتخاب کند."),

    ("13. اعتبارسنجی فرم", "required, pattern, min, max, minlength", "متوسط",
     "دربان هوشمند فرم که نمی‌گذارد بدون کارت ملی، با ایمیل نامعتبر یا رمز کمتر از ۸ کاراکتر وارد شوید.",
     "HTML5 اعتبارسنجی داخلی بدون نیاز به JS ارائه می‌دهد: required فیلد را اجباری می‌کند، minlength حداقل طول کاراکتر را تعیین می‌کند و pattern یک الگوی Regex چک می‌کند.",
     "<input type=\"text\" required minlength=\"3\" maxlength=\"20\" placeholder=\"نام کاربری\">\n<input type=\"tel\" pattern=\"09[0-9]{9}\" placeholder=\"شماره موبایل ایران\">",
     "اعتبارسنجی فرانت‌اند برای تجربه کاربری است؛ اعتبارسنجی اصلی و امنیتی باید حتما در سرور نیز چک شود."),

    ("14. تگ‌های سمانتیک", "header, nav, main, section, article, aside, footer", "متوسط",
     "بخش‌بندی مهندسی یک خانه: سقف و ورودی (header)، راهروها (nav)، سالن اصلی (main)، اتاق‌های مستقل (article) و انباری و زیرزمین (footer).",
     "تگ‌های معنایی به موتورهای جستجو و مرورگرها ساختار منطقی صفحه را می‌فهمانند بدون اینکه نیاز باشد همه چیز را با divهای بی‌معنی پر کنید.",
     "<header><nav>منو</nav></header>\n<main>\n  <article>\n    <h2>مقاله تخصصی</h2>\n    <p>متن مقاله...</p>\n  </article>\n  <aside>سایدبار اخبار</aside>\n</main>\n<footer>کپی‌رایت</footer>",
     "استفاده از تگ‌های معنایی رتبه سئوی سایت را به شدت بالا می‌برد و امتیاز دسترس‌پذیری را ارتقا می‌دهد."),

    ("15. figure و figcaption", "تصویر همراه شرح رسمی", "متوسط",
     "کادرهای مصور کتاب‌های درسی که زیر عکس نوشته شده «شکل شماره ۱-۲: نمودار جریان داده‌ها».",
     "تگ figure تصویر یا دیاگرام را در بر می‌گیرد و figcaption توضیح رسمی متصل به آن تصویر را ارائه می‌دهد که از نظر مفهومی به هم پیوند می‌خورند.",
     "<figure>\n  <img src=\"chart.png\" alt=\"نمودار فروش\">\n  <figcaption>شکل ۱: مقایسه رشد فروش در فصل پاییز</figcaption>\n</figure>",
     "از figcaption برای محتوایی استفاده کنید که بدون آن، درک کامل تصویر برای خواننده دشوار است."),

    ("16. div و span و گروه‌بندی", "جعبه‌های عمومی بدون معنا", "متوسط",
     "کارتن‌های مقوایی خالی (div) و چسب‌های کاغذی (span) که تا رویشان استایل نزنید هویتی ندارند اما برای بسته‌بندی عالی‌اند.",
     "تگ div یک بلوک عمومی برای گروه‌بندی المان‌ها به منظور استایل‌دهی در CSS است. تگ span هم یک اینلاین عمومی برای اعمال استایل روی بخشی از متن است.",
     "<div class=\"card\">\n  <h3>کارت محصول</h3>\n  <p>قیمت: <span class=\"price-tag\">۵۰۰ هزار تومان</span></p>\n</div>",
     "اول فکر کنید آیا تگ سمانتیکی مثل section یا article مناسب‌تر نیست؟ اگر نبود از div استفاده کنید."),

    ("17. چندرسانه‌ای", "audio, video, source, track", "متوسط",
     "تلویزیون و ضبط صوت بومی درون مرورگر بدون نیاز به فلش پلیر یا پلاگین‌های قدیمی.",
     "تگ video و audio برای پخش مستقیم ویدیو و صوت با کنترل‌های پیش‌فرض هستند. تگ source فرمت‌های مختلف را پیشنهاد می‌دهد و track برای زیرنویس است.",
     "<video controls width=\"600\" poster=\"cover.jpg\">\n  <source src=\"movie.mp4\" type=\"video/mp4\">\n  <track src=\"sub-fa.vtt\" kind=\"subtitles\" srclang=\"fa\" label=\"فارسی\">\n  مرورگر شما ویدیو را پشتیبانی نمی‌کند.\n</video>",
     "همیشه ویژگی controls را بگذارید تا کاربر دکمه‌های پخش، توقف و ولوم صدا را داشته باشد."),

    ("18. iframe", "قاب شیشه‌ای به سایت دیگر", "متوسط",
     "پنجره‌ای که در دیوار خانه‌تان باز می‌کنید و منظره خیابان یا سایت یوتیوب و نقشه گوگل را نشان می‌دهد.",
     "تگ <iframe> یک سند HTML دیگر را درون صفحه جاری نمایش می‌دهد. برای جاگذاری نقشه بلد/نشان، ویدیوهای آپارات، یا سامانه‌های پرداخت کاربرد دارد.",
     "<iframe src=\"https://example.com\" width=\"100%\" height=\"400\" style=\"border:none;\" loading=\"lazy\"></iframe>",
     "همیشه ویژگی loading=\"lazy\" اضافه کنید تا لود صفحه تا قبل از رسیدن به اسکرول iframe سنگین نشود."),

    ("19. متا تگ‌ها", "charset, viewport, description", "متوسط",
     "شناسنامه و کارت ملی صفحه در وب برای مرورگرها و ربات‌های جستجوگر گوگل.",
     "متا تگ‌ها درون head قرار می‌گیرند. charset=\"UTF-8\" حروف فارسی را درست می‌کند، viewport صفحه را در موبایل ریسپانسیو می‌سازد و description خلاصه صفحه در نتایج گوگل است.",
     "<meta charset=\"UTF-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n<meta name=\"description\" content=\"آموزش ساده و صفر تا صد فرانت‌اند\">\n<meta name=\"robots\" content=\"index, follow\">",
     "بدون meta viewport، سایت شما در گوشی‌های هوشمند بسیار کوچک و غیرریسپانسیو نمایش داده خواهد شد."),

    ("20. لینک کردن CSS و JS", "link, script, defer, async", "متوسط",
     "آوردن وسایل نقاشی (CSS) و آوردن تیم سیم‌کشی و مهندسین برق (JS) به داخل ساختمان.",
     "فایل استایل با <link rel=\"stylesheet\" href=\"style.css\"> لود می‌شود. برای جاوا اسکریپت از script استفاده می‌شود؛ defer اسکریپت را پس از آماده شدن ساختار HTML اجرا می‌کند.",
     "<link rel=\"stylesheet\" href=\"styles.css\">\n<script src=\"app.js\" defer></script>",
     "برای اسکریپت‌های عادی همیشه از defer استفاده کنید تا مانع لود سریع صفحه و نقاشی HTML نشود."),

    ("21. data-* attributes", "ذخیره متغیرهای اختصاصی در HTML", "متوسط",
     "برچسب‌های پنهانی پشت کالاها که شماره انبار و شناسه داخلی را فقط برای سیستم و جاوا اسکریپت نگه می‌دارند.",
     "با پیشوند data- می‌توانید هر اطلاعات دلخواهی را روی تگ‌های HTML ذخیره کنید و در جاوا اسکریپت از طریق dataset بخوانید.",
     "<button class=\"buy-btn\" data-product-id=\"1045\" data-price=\"350000\">خرید</button>\n<!-- در JS: element.dataset.productId -->",
     "نام بعد از data- نباید حروف بزرگ داشته باشد؛ از حروف کوچک و خط تیره استفاده کنید."),

    ("22. details و summary", "آکاردئون بازشونده بومی بدون JS", "متوسط",
     "جعبه‌های کشویی یا سوالات متداول (FAQ) که با کلیک روی تیتر، محتوای مخفی زیر آن پدیدار می‌شود.",
     "تگ details همراه summary بدون یک خط کد جاوا اسکریپت، قابلیت باز و بسته شدن را به مرورگر محول می‌کند.",
     "<details>\n  <summary>آیا این دوره پیش‌نیاز دارد؟</summary>\n  <p>خیر، همه مباحث از پایه به صورت فوق‌العاده ساده آموزش داده شده است.</p>\n</details>",
     "می‌توانید ویژگی open را به details بدهید تا از ابتدا به صورت باز نمایش داده شود."),

    ("23. datalist, progress, meter", "پیشنهاد خودکار و نوارهای پیشرفت", "متوسط",
     "جعبه هوشمند سرچ با پیشنهادات آماده، نوار دانلود فایل، و درجه بنزین باک ماشین.",
     "تگ datalist به input یک لیست پیشنهادی وصل می‌کند. progress برای درصد انجام کار، و meter برای نشان دادن مقداری از یک بازه معلوم (مثل حرارت یا شارژ) است.",
     "<input list=\"browsers\" placeholder=\"مرورگر خود را انتخاب کنید\">\n<datalist id=\"browsers\">\n  <option value=\"Chrome\">\n  <option value=\"Firefox\">\n</datalist>\n<progress value=\"70\" max=\"100\"></progress>",
     "تگ meter معنای سمانتیک دارد و برای نوارهای پیشرفت دانلودی نیست؛ برای پیشرفت همیشه از progress استفاده کنید."),

    # پیشرفته (24-35)
    ("24. دسترسی‌پذیری (Accessibility)", "aria-*, role, tabindex", "پیشرفته",
     "رمپ مخصوص ویلچر و خط بریل روی کلیدهای آسانسور برای اینکه افراد کم‌بینا و کم‌توان هم از سایت استفاده کنند.",
     "استاندارد ARIA به ابزارهای صفحه‌خوان توضیح می‌دهد المان چیست. ویژگی tabindex تعیین می‌کند فشردن کلید Tab کیبورد چطور بین گزینه‌ها حرکت کند.",
     "<button aria-label=\"بستن پنجره\" tabindex=\"0\">✕</button>\n<nav role=\"navigation\" aria-label=\"منوی اصلی\"></nav>",
     "به جای اینکه به یک div صفت role=\"button\" بدهید، از همان تگ واقعی <button> استفاده کنید که بومی دسترس‌پذیر است."),

    ("25. تصاویر واکنش‌گرا", "picture, srcset, sizes", "پیشرفته",
     "تحویل عکس کوچک برای گوشی با اینترنت ضعیف و عکس باکیفیت 4K برای مانیتور دسکتاپ بزرگ.",
     "تگ picture و srcset به مرورگر اجازه می‌دهند بر اساس رزولوشن نمایشگر و ابعاد صفحه، سبک‌ترین و بهینه‌ترین عکس را دانلود کند.",
     "<picture>\n  <source media=\"(min-width: 800px)\" srcset=\"large.webp\">\n  <source media=\"(min-width: 400px)\" srcset=\"medium.webp\">\n  <img src=\"small.webp\" alt=\"طبیعت زیبا\">\n</picture>",
     "فرمت‌های مدرن مثل WebP یا AVIF را داخل source بگذارید و در تگ img فایل fallback با فرمت jpg قرار دهید."),

    ("26. لود تنبل (Lazy Loading)", "loading=\"lazy\"", "پیشرفته",
     "خریدن میوه فقط زمانی که واقعا می‌خواهید آن را بخورید، به جای پر کردن کل خانه از میوه‌هایی که شاید نبینید.",
     "با صفت loading=\"lazy\" مرورگر تصاویر و iframeهایی که پایین صفحه هستند را لود نمی‌کند تا وقتی کاربر به آن‌ها اسکرول کند؛ این کار سرعت لود اولیه را دوچندان می‌کند.",
     "<img src=\"product-gallery.jpg\" loading=\"lazy\" alt=\"محصول\">\n<iframe src=\"https://map.ir\" loading=\"lazy\"></iframe>",
     "برای تصاویری که بالای صفحه هستند (Hero Banner) لود تنبل نگذارید؛ چون LCP و سرعت اولیه را تخریب می‌کند."),

    ("27. سئو پایه (SEO)", "title, meta, canonical, Open Graph", "پیشرفته",
     "ویترین مغازه رو به خیابان و کارت ویزیت شیک برای اینکه وقتی در تلگرام یا گوگل لینکتان را می‌فرستید عکس و تیتر قشنگ ظاهر شود.",
     "تگ title عنوان اصلی است، canonical آدرس مرجع را تعیین می‌کند تا گوگل محتوای تکراری جریمه نکند، و پروتکل Open Graph برای اشتراک‌گذاری در شبکه‌های اجتماعی است.",
     "<title>آموزش آسان فرانت‌اند | مرجع صفر تا صد</title>\n<link rel=\"canonical\" href=\"https://site.ir/page\">\n<meta property=\"og:title\" content=\"یادگیری ساده فرانت‌اند\">\n<meta property=\"og:image\" content=\"https://site.ir/cover.jpg\">",
     "عنوان صفحه title باید کوتاه، جذاب و حداکثر ۶۰ کاراکتر باشد تا در نتایج گوگل بریده نشود."),

    ("28. ساختار داده (Structured Data)", "JSON-LD, Microdata", "پیشرفته",
     "برچسب بارکد دار و استاندارد روی جعبه برای دستگاه بارکدخوان گوگل تا ستاره‌های رضایت مشتری و قیمت در نتایج ظاهر شوند.",
     "با اضافه کردن اسکریپت type=\"application/ld+json\" اطلاعاتی مثل سوالات متداول، امتیاز، قیمت محصول و نویسنده را به شکل استاندارد به موتور جستجو می‌فهمانید.",
     "<script type=\"application/ld+json\">\n{\n  \"@context\": \"https://schema.org\",\n  \"@type\": \"Product\",\n  \"name\": \"کفش ورزشی\",\n  \"offers\": {\n    \"@type\": \"Offer\",\n    \"price\": \"850000\",\n    \"priceCurrency\": \"IRR\"\n  }\n}\n</script>",
     "همیشه اسکریپت‌های JSON-LD را با ابزار Rich Results Test گوگل اعتبارسنجی کنید."),

    ("29. canvas و svg", "گرافیک شطرنجی و برداری", "پیشرفته",
     "بوم نقاشی پیکسل به پیکسل (canvas برای بازی و انیمیشن سنگین) در مقابل نقشه معماری برداری بی‌نهایت زوم‌شونده (svg برای آیکون و لوگو).",
     "تگ svg با ریاضیات خطوط و دایره‌ها را می‌کشد و با هر زومی تار نمی‌شود. canvas یک بوم خالی در اختیارتان می‌گذارد که با کد جاوا اسکریپت روی آن نقاشی می‌کنید.",
     "<svg width=\"100\" height=\"100\">\n  <circle cx=\"50\" cy=\"50\" r=\"40\" fill=\"#38bdf8\" />\n</svg>\n<canvas id=\"gameCanvas\" width=\"400\" height=\"300\"></canvas>",
     "برای آیکون‌ها و لوگوها همیشه از SVG استفاده کنید چون حجم ناچیز و کیفیت بی‌نهایت دارند."),

    ("30. وب‌کامپوننت‌ها (Web Components)", "template, slot, Custom Elements, Shadow DOM", "پیشرفته",
     "ساختن تگ اختصاصی لگویی خودت مثل <my-slider> که استایل‌ها و رفتارش در دنیای خودش ایزوله است و به بقیه صفحه سرایت نمی‌کند.",
     "با template قالبی می‌سازید که تا صدا نزنید رندر نمی‌شود. با Shadow DOM استایل‌های کامپوننت را محصور می‌کنید تا کلاس‌های صفحه استایل آن را به هم نریزند.",
     "<template id=\"card-temp\">\n  <style>h2 { color: #f59e0b; }</style>\n  <div class=\"user-card\">\n    <h2><slot name=\"name\">نام پیش‌فرض</slot></h2>\n  </div>\n</template>",
     "وب‌کامپوننت‌ها بدون نیاز به هیچ فریمورکی مستقیماً در مرورگر پشتیبانی می‌شوند."),

    ("31. تگ dialog", "مودال بومی بدون دردسر", "پیشرفته",
     "پنجره پاپ‌آپ رسمی مرورگر با پس‌زمینه تیره که فوکوس کیبورد را در خود قفل می‌کند و با زدن دکمه ESC خودبه‌خود بسته می‌شود.",
     "تگ dialog پنجره‌های مودال استاندارد بدون نیاز به کتابخانه‌های سنگین می‌سازد و با متد showModal() باز می‌شود.",
     "<dialog id=\"myModal\">\n  <h3>پیام سیستم</h3>\n  <p>اطلاعات با موفقیت ذخیره شد.</p>\n  <button onclick=\"this.closest('dialog').close()\">بستن</button>\n</dialog>\n<button onclick=\"document.getElementById('myModal').showModal()\">نمایش مودال</button>",
     "استفاده از showModal() خودش یک المان ::backdrop شیشه‌ای زیر مودال می‌اندازد که می‌توانید با CSS استایل دهید."),

    ("32. contenteditable و draggable", "ادیتور آنلاین و قابلیت درگ اند دراپ", "پیشرفته",
     "تبدیل هر بخش از سایت به دفترچه یادداشت تایپ‌کردنی (مثل گوگل داکس) و امکان جابجایی المان‌ها با موس مثل تخته ترلو.",
     "صفت contenteditable=\"true\" به کاربر اجازه می‌دهد متن المان را مستقیماً در صفحه ویرایش کند. draggable=\"true\" المان را قابل کشیدن می‌کند.",
     "<div contenteditable=\"true\" style=\"border:1px dashed #38bdf8; padding:10px;\">\n  روی این متن کلیک کنید و هر چه می‌خواهید بنویسید!\n</div>\n<div draggable=\"true\">مرا بکشید و رها کنید!</div>",
     "متن ویرایش‌شده با رفرش صفحه از بین می‌رود مگر اینکه مقدار جدید را در LocalStorage یا دیتابیس با JS ذخیره کنید."),

    ("33. preload, prefetch, preconnect", "میانبرهای سرعت بارگذاری شبکه", "پیشرفته",
     "پیش‌سفارش قهوه قبل از رسیدن به کافی‌شاپ (preload)، و آماده کردن چمدان فردا برای سفری که احتمالا می‌روید (prefetch).",
     "این صفت‌ها اولویت لود منابع را تنظیم می‌کنند. preconnect اتصال به دامنه را از قبل برقرار می‌کند، preload منبع ضروری صفحه فعلی را زودتر می‌کشد، و prefetch منابع صفحه بعدی را در خلوتی شبکه دانلود می‌کند.",
     "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n<link rel=\"preload\" href=\"IRANYekan.woff2\" as=\"font\" type=\"font/woff2\" crossorigin>\n<link rel=\"prefetch\" href=\"/next-page.html\">",
     "بیش از حد منابع را preload نکنید؛ فقط فونت اصلی و عکس بزرگ بالای صفحه سزاوار preload هستند."),

    ("34. rel=\"noopener noreferrer\" و امنیت", "محافظت در برابر فیشینگ پنجره‌ها", "پیشرفته",
     "بستن درب پشتی وقتی مهمان از در ورودی دیگری می‌رود تا نتواند دزدکی دستگیره در اتاق شما را تکان دهد (Tabnabbing).",
     "وقتی لینکی target=\"_blank\" دارد، تب جدید می‌تواند با window.opener صفحه قبلی شما را دستکاری کند. صفت noopener ارتباط را قطع می‌کند و noreferrer منبع ارجاع را مخفی نگه می‌دارد.",
     "<a href=\"https://external-site.com\" target=\"_blank\" rel=\"noopener noreferrer\">\n  لینک امن به سایت خارجی\n</a>",
     "مرورگرهای مدرن به طور پیش‌فرض این را روی target=\"_blank\" می‌گذارند، اما برای سازگاری همیشه خودتان قید کنید."),

    ("35. sandbox در iframe و CSP", "قرنطینه امنیتی و محدودسازی اسکریپت‌ها", "پیشرفته",
     "گذاشتن محتوای مشکوک داخل قفس شیشه‌ای ضدگلوله تا نتواند ویروس پخش کند، فرم الکی بفرستد، یا پاپ‌آپ باز کند.",
     "ویژگی sandbox دسترسی‌های اسکریپت، پاپ‌آپ، و فرم را درون iframe مسدود می‌کند مگر اینکه با مقادیر مجاز آزاد شوند. CSP (Content Security Policy) تعیین می‌کند منابع از چه دامنه‌هایی اجازه اجرا دارند.",
     "<iframe src=\"user-content.html\" sandbox=\"allow-scripts allow-same-origin\"></iframe>\n<meta http-equiv=\"Content-Security-Policy\" content=\"default-src 'self'; script-src 'self' https://trusted.com;\">",
     "هرگز مقدار allow-top-navigation را به صورت بدون فکر روی iframeهای ناشناس نگذارید تا نتوانند آدرس کل صفحه شما را عوض کنند.")
]

def generate():
    out_dir = "C:/Users/erfan/Desktop/WebDev_Master_Learning_Hub/html"
    os.makedirs(out_dir, exist_ok=True)
    html_path = os.path.join(out_dir, "index.html")

    cards_html = ""
    for t in html_topics:
        num_title, sub, lvl, ana, exp, code, tip = t
        lvl_color = "#38bdf8" if lvl == "مبتدی" else ("#f59e0b" if lvl == "متوسط" else "#a855f7")
        cards_html += f"""
        <article class="topic-card" data-level="{lvl}">
          <div class="card-header">
            <div>
              <span class="level-badge" style="background:{lvl_color}22; color:{lvl_color}; border-color:{lvl_color}44;">{lvl}</span>
              <h3 class="topic-title">{num_title}</h3>
              <p class="topic-sub">{sub}</p>
            </div>
            <button class="copy-btn" onclick="copyCode(this)" title="کپی کد">📋 کپی کد</button>
          </div>
          
          <div class="analogy-box">
            <div class="box-tag">💡 تشبیه به زبان خیلی ساده</div>
            <p>{ana}</p>
          </div>

          <div class="exp-box">
            <div class="box-tag">📖 مفهوم و نحوه کارکرد</div>
            <p>{exp}</p>
          </div>

          <div class="code-wrapper">
            <pre><code>{code.replace('<', '&lt;').replace('>', '&gt;')}</code></pre>
          </div>

          <div class="tip-box">
            <div class="box-tag">⚡ نکته طلایی / اشتباه رایج</div>
            <p>{tip}</p>
          </div>
        </article>
        """

    full_page = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>دانشنامه فوق‌العاده ساده و جامع HTML5 (از صفر تا پیشرفته)</title>
<style>
@font-face {{
  font-family: 'IRANYekan';
  src: url('../fonts/IRANYekanXFaNum-Regular.ttf') format('truetype');
  font-weight: 400;
}}
@font-face {{
  font-family: 'IRANYekan';
  src: url('../fonts/IRANYekanXFaNum-Bold.ttf') format('truetype');
  font-weight: 700;
}}
@font-face {{
  font-family: 'IRANYekan';
  src: url('../fonts/IRANYekanXFaNum-Black.ttf') format('truetype');
  font-weight: 900;
}}

:root {{
  --bg: #090d16;
  --surface: #111827;
  --surface-border: #1e293b;
  --text-main: #f1f5f9;
  --text-muted: #94a3b8;
  --accent: #38bdf8;
  --amber: #f59e0b;
  --green: #10b981;
  --purple: #a855f7;
  --code-bg: #030712;
}}

* {{ margin: 0; padding: 0; box-sizing: border-box; }}

body {{
  font-family: 'IRANYekan', system-ui, Tahoma, sans-serif;
  background-color: var(--bg);
  color: var(--text-main);
  line-height: 1.85;
  padding: 30px 20px;
}}

.container {{
  max-width: 1100px;
  margin: 0 auto;
}}

header.main-header {{
  background: linear-gradient(135deg, #111827 0%, #1e1b4b 100%);
  border: 1px solid var(--surface-border);
  border-radius: 20px;
  padding: 35px 30px;
  margin-bottom: 30px;
  text-align: center;
  position: relative;
  overflow: hidden;
}}

.header-badge {{
  display: inline-block;
  background: rgba(56, 189, 248, 0.15);
  color: var(--accent);
  padding: 4px 16px;
  border-radius: 99px;
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 12px;
  border: 1px solid rgba(56, 189, 248, 0.3);
}}

h1.page-title {{
  font-size: 32px;
  font-weight: 900;
  color: #fff;
  margin-bottom: 10px;
}}

p.header-desc {{
  font-size: 15px;
  color: var(--text-muted);
  max-width: 750px;
  margin: 0 auto 20px;
}}

.header-actions {{
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
}}

.btn {{
  padding: 10px 22px;
  border-radius: 12px;
  font-family: inherit;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.2s ease;
  border: 1px solid transparent;
}}

.btn-primary {{
  background: var(--accent);
  color: #04101e;
}}
.btn-primary:hover {{
  background: #7dd3fc;
  transform: translateY(-2px);
}}

.btn-outline {{
  background: rgba(255,255,255,0.05);
  color: var(--text-main);
  border-color: var(--surface-border);
}}
.btn-outline:hover {{
  background: rgba(255,255,255,0.1);
  transform: translateY(-2px);
}}

/* Navigation & Search Bar */
.controls-bar {{
  background: var(--surface);
  border: 1px solid var(--surface-border);
  border-radius: 16px;
  padding: 16px 20px;
  margin-bottom: 25px;
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
}}

.search-input {{
  flex: 1;
  min-width: 250px;
  background: var(--code-bg);
  border: 1px solid var(--surface-border);
  color: #fff;
  padding: 10px 16px;
  border-radius: 10px;
  font-family: inherit;
  font-size: 14px;
  outline: none;
}}
.search-input:focus {{
  border-color: var(--accent);
}}

.filters {{
  display: flex;
  gap: 8px;
}}

.filter-btn {{
  background: transparent;
  color: var(--text-muted);
  border: 1px solid var(--surface-border);
  padding: 8px 16px;
  border-radius: 8px;
  font-family: inherit;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.15s ease;
}}
.filter-btn.active, .filter-btn:hover {{
  background: rgba(56, 189, 248, 0.15);
  color: var(--accent);
  border-color: var(--accent);
}}

/* Topic Cards */
.topic-card {{
  background: var(--surface);
  border: 1px solid var(--surface-border);
  border-radius: 16px;
  padding: 24px;
  margin-bottom: 22px;
  transition: border-color 0.2s ease, transform 0.2s ease;
}}
.topic-card:hover {{
  border-color: rgba(56, 189, 248, 0.4);
}}

.card-header {{
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 15px;
  margin-bottom: 16px;
}}

.level-badge {{
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  padding: 2px 10px;
  border-radius: 99px;
  border: 1px solid;
  margin-bottom: 6px;
}}

.topic-title {{
  font-size: 20px;
  font-weight: 900;
  color: #fff;
}}

.topic-sub {{
  font-size: 13px;
  color: var(--accent);
  font-family: monospace;
  direction: ltr;
  text-align: right;
}}

.copy-btn {{
  background: rgba(255,255,255,0.05);
  color: var(--text-muted);
  border: 1px solid var(--surface-border);
  padding: 6px 12px;
  border-radius: 8px;
  font-size: 12px;
  font-family: inherit;
  cursor: pointer;
  transition: 0.15s;
}}
.copy-btn:hover {{
  color: #fff;
  border-color: var(--accent);
}}

.box-tag {{
  font-size: 12px;
  font-weight: 700;
  margin-bottom: 4px;
}}

.analogy-box {{
  background: rgba(245, 158, 11, 0.08);
  border-right: 3px solid var(--amber);
  border-radius: 0 10px 10px 0;
  padding: 12px 16px;
  margin-bottom: 12px;
}}
.analogy-box .box-tag {{ color: var(--amber); }}
.analogy-box p {{ font-size: 14px; color: #fde68a; }}

.exp-box {{
  background: rgba(56, 189, 248, 0.06);
  border-right: 3px solid var(--accent);
  border-radius: 0 10px 10px 0;
  padding: 12px 16px;
  margin-bottom: 14px;
}}
.exp-box .box-tag {{ color: var(--accent); }}
.exp-box p {{ font-size: 14px; color: var(--text-main); }}

.code-wrapper {{
  background: var(--code-bg);
  border: 1px solid var(--surface-border);
  border-radius: 10px;
  padding: 14px 18px;
  margin-bottom: 14px;
  direction: ltr;
  text-align: left;
  overflow-x: auto;
}}
.code-wrapper pre code {{
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 13px;
  color: #7dd3fc;
  line-height: 1.6;
}}

.tip-box {{
  background: rgba(16, 185, 129, 0.08);
  border-right: 3px solid var(--green);
  border-radius: 0 10px 10px 0;
  padding: 10px 16px;
}}
.tip-box .box-tag {{ color: var(--green); }}
.tip-box p {{ font-size: 13px; color: #a7f3d0; }}

/* Print Rules */
@media print {{
  body {{ background: #fff !important; color: #000 !important; padding: 0 !important; }}
  header.main-header, .controls-bar, .copy-btn {{ display: none !important; }}
  .topic-card {{ page-break-inside: avoid; border: 1px solid #ccc !important; background: #fff !important; margin-bottom: 20px; }}
  .topic-title {{ color: #000 !important; }}
  .analogy-box {{ background: #fffbeb !important; color: #000 !important; border-color: #d97706 !important; }}
  .analogy-box p {{ color: #78350f !important; }}
  .exp-box {{ background: #f0f9ff !important; color: #000 !important; border-color: #0284c7 !important; }}
  .exp-box p {{ color: #0c4a6e !important; }}
  .code-wrapper {{ background: #f8fafc !important; border-color: #cbd5e1 !important; }}
  .code-wrapper code {{ color: #0f172a !important; }}
  .tip-box {{ background: #ecfdf5 !important; border-color: #059669 !important; }}
  .tip-box p {{ color: #064e3b !important; }}
}}
</style>
</head>
<body>

<div class="container">
  <header class="main-header">
    <span class="header-badge">🏛️ مستندات جامع و فوق‌ساده HTML5</span>
    <h1 class="page-title">دانشنامه کامل مفاهیم HTML</h1>
    <p class="header-desc">
      تمام ۳۵ مفهوم کلیدی HTML از اسکلت پایه تا سمانتیک، فرم‌ها، سئو، دسترسی‌پذیری و وب‌کامپوننت‌ها به ساده‌ترین تمثیل‌های ملموس زندگی روزمره.
    </p>
    <div class="header-actions">
      <a href="../index.html" class="btn btn-outline">🏠 بازگشت به هاب اصلی</a>
      <a href="HTML_Handbook.pdf" class="btn btn-primary" download>📄 دانلود کتابچه PDF (A4)</a>
      <button onclick="window.print()" class="btn btn-outline">🖨️ پرینت مستقیم</button>
    </div>
  </header>

  <section class="controls-bar">
    <input type="text" id="searchInput" class="search-input" placeholder="🔍 جستجوی تگ یا مفهوم (مثلا input, form, video, seo)...">
    <div class="filters">
      <button class="filter-btn active" data-filter="all">همه (۳۵)</button>
      <button class="filter-btn" data-filter="مبتدی">مبتدی (۱۰)</button>
      <button class="filter-btn" data-filter="متوسط">متوسط (۱۳)</button>
      <button class="filter-btn" data-filter="پیشرفته">پیشرفته (۱۲)</button>
    </div>
  </section>

  <main id="topicsGrid">
    {cards_html}
  </main>
</div>

<script>
function copyCode(btn) {{
  const code = btn.closest('.topic-card').querySelector('pre code').innerText;
  navigator.clipboard.writeText(code).then(() => {{
    const old = btn.innerText;
    btn.innerText = '✅ کپی شد!';
    btn.style.borderColor = '#10b981';
    setTimeout(() => {{
      btn.innerText = old;
      btn.style.borderColor = '';
    }}, 1800);
  }});
}}

// Filter and Search
const searchInput = document.getElementById('searchInput');
const filterBtns = document.querySelectorAll('.filter-btn');
const cards = document.querySelectorAll('.topic-card');

function applyFilters() {{
  const q = searchInput.value.toLowerCase().trim();
  const activeLevel = document.querySelector('.filter-btn.active').dataset.filter;

  cards.forEach(card => {{
    const level = card.dataset.level;
    const text = card.innerText.toLowerCase();
    const matchFilter = (activeLevel === 'all' || level === activeLevel);
    const matchSearch = (!q || text.includes(q));

    if (matchFilter && matchSearch) {{
      card.style.display = 'block';
    }} else {{
      card.style.display = 'none';
    }}
  }});
}}

searchInput.addEventListener('input', applyFilters);

filterBtns.forEach(btn => {{
  btn.addEventListener('click', () => {{
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    applyFilters();
  }});
}});
</script>

</body>
</html>
"""
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_page)
    print("HTML page written:", html_path)

    # Compile PDF via Chrome
    pdf_path = os.path.join(out_dir, "HTML_Handbook.pdf")
    cmd = [
        "C:/Program Files/Google/Chrome/Application/chrome.exe",
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--virtual-time-budget=6000",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    subprocess.run(cmd, check=True)
    print("PDF compiled:", pdf_path, "Size:", os.path.getsize(pdf_path))
    
    # Also copy to Desktop directly!
    desktop_pdf = "C:/Users/erfan/Desktop/HTML_Handbook.pdf"
    with open(pdf_path, "rb") as rf:
        with open(desktop_pdf, "wb") as wf:
            wf.write(rf.read())
    print("Copied to Desktop:", desktop_pdf)

if __name__ == "__main__":
    generate()
