# -*- coding: utf-8 -*-
# Topics 18-42 (Intermediate JavaScript) with practical real-world depth

JS_TOPICS_2 = [
    {
        "id": 18,
        "title": "توابع پیکانی (Arrow Functions) و رفتار کلمه کلیدی this",
        "level": "متوسط",
        "what": "سینتکس مختصر ES6 برای نوشتن توابع () => {}. تفاوت کلیدی آن با توابع سنتی: کلمه کلیدی this اختصاصی برای خود ندارد و this محیط اطرافش (Lexical this) را به ارث می‌برد.",
        "does": "در توابع سنتی، وقتی درون یک تایمر یا رویداد قرار می‌گرفتید، this به پنجره window یا undefined تغییر می‌کرد و دسترسی به اطلاعات آبجکت قطع می‌شد. Arrow Function این مشکل بزرگ را برای همیشه حل کرد.",
        "real": "اجرای شمارنده ثانیه‌شمار یا ارسال درخواست با تایمر بدون نیاز به ترفندهای قدیمی مثل var self = this;",
        "code": "const timer = {\n  seconds: 0,\n  start() {\n    // تابع پیکانی this آبجکت timer را حفظ می‌کند\n    setInterval(() => {\n      this.seconds++;\n      console.log(`زمان سپری شده: ${this.seconds} ثانیه`);\n    }, 1000);\n  }\n};\ntimer.start();"
    },
    {
        "id": 19,
        "title": "حوزه‌ها و قلمروهای متغیر (Global, Function, Block Scope)",
        "level": "متوسط",
        "what": "محدوده‌ای از کد که یک متغیر در آن زنده است و دسترسی به آن امکان‌پذیر است.",
        "does": "متغیر سراسری (Global) در تمام فایل‌ها در دسترس است و خطر بازنویسی تصادفی دارد. حوزه تابع (Function) داخل بدنه تابع محصور است. حوزه بلوک (Block) داخل هر جفت آکولاد {} مثل حلقه یا شرط است که فقط let و const آن را رعایت می‌کنند.",
        "real": "جلوگیری از برخورد متغیر نام کاربری در ماژول چت با متغیر نام کاربری در ماژول پرداخت.",
        "code": "const globalScore = 100; // Global\n\nfunction playLevel() {\n  const levelScore = 50; // Function Scope\n  if (levelScore > 0) {\n    const bonus = 10; // Block Scope\n    console.log(levelScore + bonus); // 60\n  }\n  // console.log(bonus); // خطای ReferenceError!\n}"
    },
    {
        "id": 20,
        "title": "بالا کشیدن متغیرها و توابع (Hoisting) و منطقه مرده زمانی (TDZ)",
        "level": "متوسط",
        "what": "رفتار موتور V8 جاوا اسکریپت در فاز کامپایل، که اعلان متغیرها و توابع را پیش از اجرای خط به خط کد، به بالای اسکوپ می‌برد.",
        "does": "توابع معمولی (Function Declaration) کامل بالا کشیده می‌شوند و می‌توانید قبل از تعریف فراخوانی‌شان کنید. متغیر var با مقدار undefined بالا کشیده می‌شود. اما let و const در منطقه مرده زمانی (Temporal Dead Zone) قرار می‌گیرند و تا قبل از رسیدن خط به تعریفشان، ارور Fatal می‌دهند.",
        "real": "فهم علت باگ‌های عجیب و غریب چاپ undefined به جای خطای متغیر در پروژه‌های قدیمی.",
        "code": "sayHi(); // بدون مشکل چاپ می‌شود!\nfunction sayHi() {\n  console.log(\"سلام! چون اعلان تابع Hoist شد\");\n}\n\n// console.log(myAge); // خطای TDZ: Cannot access before initialization\nconst myAge = 25;"
    },
    {
        "id": 21,
        "title": "پارامترهای پیش‌فرض و پارامتر باقی‌مانده (Default & Rest Parameters)",
        "level": "متوسط",
        "what": "امکان تعیین مقدار پیش‌فرض برای آرگومان‌هایی که پاس داده نشده‌اند، و جمع‌آوری تمام آرگومان‌های نامحدود بعدی در قالب یک آرایه با علامت (...).",
        "does": "دیگر نیازی به نوشتن if (!discount) discount = 0 نیست. عملگر Rest (...args) به جای شیء قدیمی و کند arguments، یک آرایه واقعی و تمیز به شما تحویل می‌دهد.",
        "real": "تابع ارسال پیامک نوتیفیکیشن با متد پیش‌فرض، یا تابع جمع زدن نامحدود قیمت چند سبد خرید.",
        "code": "// Default Parameter: taxPercent پیش‌فرض ۹٪\nfunction calculateTax(price, taxPercent = 9) {\n  return price + (price * taxPercent) / 100;\n}\n\n// Rest Parameter: گرفتن تعداد نامحدود محصول\nfunction logOrders(customer, ...items) {\n  console.log(`مشتری: ${customer}، اقلام خریده شده: ${items.length} عدد`);\n}\nlogOrders(\"عرفان\", \"لپتاپ\", \"ماوس\", \"کیبورد\");"
    },
    {
        "id": 22,
        "title": "عملگر پخش کردن (Spread Operator: ...)",
        "level": "متوسط",
        "what": "پهن کردن و باز کردن اعضای یک آرایه یا خواص یک آبجکت به درون یک آرایه یا آبجکت دیگر.",
        "does": "امکان ترکیب سریع و خوانای آرایه‌ها، اضافه کردن المان جدید، و کپی سطحی (Shallow Copy) اشیاء را بدون تغییر دادن شیء اصلی به صورت ایمن (Immutable) فراهم می‌سازد.",
        "real": "به‌روزرسانی پروفایل کاربر در ریداکس یا استیت ری‌اکت بدون دستکاری مستقیم آبجکت اصلی.",
        "code": "const baseUser = { id: 10, name: \"عرفان\", role: \"user\" };\n\n// ارتقای کاربر به ادمین با حفظ سایر مشخصات به سبک Immutable\nconst updatedUser = {\n  ...baseUser,\n  role: \"admin\",\n  updatedAt: new Date().toISOString()\n};\n\nconsole.log(updatedUser);"
    },
    {
        "id": 23,
        "title": "تخریب و استخراج ساختار (Destructuring)",
        "level": "متوسط",
        "what": "بیرون کشیدن سریع متغیرها از دل آبجکت‌ها و آرایه‌ها در یک خط کد خوانا.",
        "does": "به جای اینکه ۵ خط بنویسید const name = user.name; const email = user.email;، در یک آکولاد { name, email } همه را تمیز بیرون می‌کشید؛ حتی می‌توانید نام مستعار بگذارید یا مقدار پیش‌فرض بدهید.",
        "real": "دریافت اطلاعات ریسپانس API سرور در برنامه‌های تجاری.",
        "code": "const apiResponse = {\n  status: 200,\n  data: {\n    userId: 88,\n    fullName: \"عرفان محمودی\",\n    city: \"تهران\"\n  }\n};\n\n// بیرون کشیدن سریع فیلدها با تغییر نام\nconst { data: { fullName: user, city = \"نامشخص\" } } = apiResponse;\nconsole.log(`کاربر: ${user} از شهر: ${city}`);"
    },
    {
        "id": 24,
        "title": "متدهای پیشرفته آرایه‌ها (map, filter, reduce, find, some, every, sort, flat)",
        "level": "متوسط",
        "what": "مجموعه توابع مرتبه بالای برنامه‌نویسی تابعی (Functional Programming) برای دگرگونی، فیلتر و تجمیع داده‌ها در آرایه بدون استفاده از حلقه‌های سنتی for.",
        "does": "متد map همه اعضا را تغییر شکل می‌دهد؛ filter گزینش می‌کند؛ reduce کل آرایه را به یک عدد یا شیء فشرده خلاصه می‌کند؛ find اولین مورد منطبق را می‌یابد؛ some حداقل یکی را چک می‌کند و every همه را؛ flat آرایه‌های تودرتو را یک‌دست می‌کند.",
        "real": "محاسبه مجموع فاکتور کالاهای موجود در انبار دیجی‌کالا و اعمال کوپن تخفیف.",
        "code": "const products = [\n  { id: 1, title: \"گوشی\", price: 20_000_000, inStock: true },\n  { id: 2, title: \"قاب\", price: 300_000, inStock: false },\n  { id: 3, title: \"شارژر\", price: 1_200_000, inStock: true }\n];\n\n// فیلتر کالاهای موجود + استخراج عنوان\nconst availableTitles = products\n  .filter(p => p.inStock)\n  .map(p => p.title);\n\n// محاسبه قیمت کل کالاهای موجود با reduce\nconst totalAvailablePrice = products\n  .filter(p => p.inStock)\n  .reduce((sum, p) => sum + p.price, 0);\n\nconsole.log(\"کالاهای موجود:\", availableTitles);\nconsole.log(\"مجموع قیمت:\", totalAvailablePrice);"
    },
    {
        "id": 25,
        "title": "توابع کال‌بک (Callback Functions)",
        "level": "متوسط",
        "what": "تابعی که به عنوان آرگومان به تابع دیگری پاس داده می‌شود تا بعد از پایان عملیاتی خاص فراخوانی و اجرا شود.",
        "does": "اساس برنامه‌نویسی آسنکرون در جاوا اسکریپت قدیمی؛ به برنامه اجازه می‌دهد منتظر تمام شدن کاری (مثل پاسخ سرور یا تایمر) بماند و سپس واکنش نشان دهد.",
        "real": "انجام تراکنش بانکی: بعد از تایید شدن کارت، پیامک ارسال کن و سبد خرید را خالی کن.",
        "code": "function processOrder(orderId, onSuccess) {\n  console.log(`در حال پردازش سفارش شماره ${orderId}...`);\n  setTimeout(() => {\n    // پس از ۲ ثانیه کال‌بک را اجرا کن\n    onSuccess({ status: \"SUCCESS\", trackingCode: \"TRK-9842\" });\n  }, 2000);\n}\n\nprocessOrder(405, (result) => {\n  console.log(\"سفارش ثبت شد! کد پیگیری:\", result.trackingCode);\n});"
    },
    {
        "id": 26,
        "title": "دستکاری درخت سند وب (DOM: Selection, Creation, Modification, Removal)",
        "level": "متوسط",
        "what": "واسط برنامه‌نویسی شیء سند (Document Object Model) که به جاوا اسکریپت اجازه می‌دهد تمام تگ‌ها، استایل‌ها و ساختار HTML را دستکاری کند.",
        "does": "با querySelector المان را می‌گیرید، با textContent یا innerHTML متن و محتوا را عوض می‌کنید، با createElement تگ جدید در حافظه می‌سازید و با appendChild یا remove آن را درج یا حذف می‌کنید.",
        "real": "اضافه کردن داینامیک یک پیام چت جدید به صفحه گفتگوی آنلاین تلگرام وب بدون رفرش صفحه.",
        "code": "// پیدا کردن کانتینر چت\nconst chatBox = document.querySelector(\"#chatBox\");\n\n// ساخت المنت پیام جدید\nconst newMsg = document.createElement(\"div\");\nnewMsg.className = \"message-bubble user-message\";\nnewMsg.textContent = \"سلام! سفارش من کی ارسال میشه؟\";\n\n// اضافه کردن به انتهای چت\nchatBox.appendChild(newMsg);"
    },
    {
        "id": 27,
        "title": "رویدادها و انتشار آن‌ها (Events, Bubbling, Capturing, Event Delegation)",
        "level": "متوسط",
        "what": "گوش دادن به واکنش‌های کاربر (کلیک، اسکرول، تایپ). انتشار رویداد از عمیق‌ترین تگ فرزند به سمت بالاترین والد بالا می‌آید (Bubbling).",
        "does": "تکنیک طلایی Event Delegation: به جای اینکه به ۱۰۰۰ سطر جدول ۱۰۰۰ تا Event Listener اضافه کنید و رم مرورگر را بترکانید، یک Event Listener روی والد جدول می‌گذارید و با e.target فرزند کلیک‌شده را تشخیص می‌دهید.",
        "real": "حذف ردیف‌های لیست بی‌پایان سفارشات در پنل ادمین بدون افت فریم و هدررفت رم.",
        "code": "// Event Delegation روی لیست اولیا\nconst list = document.querySelector(\"#todoList\");\n\nlist.addEventListener(\"click\", (e) => {\n  // اگر دکمه حذف فشرده شد\n  if (e.target.matches(\".delete-btn\")) {\n    const item = e.target.closest(\"li\");\n    item.remove(); // سطر مربوطه حذف شد\n  }\n});"
    },
    {
        "id": 28,
        "title": "جلوگیری از رفتار پیش‌فرض و حباب‌زایی (preventDefault & stopPropagation)",
        "level": "متوسط",
        "what": "دستوراتی برای مهار کردن رفتارهای بومی مرورگر یا متوقف کردن زنجیره بالا آمدن رویداد به والدین.",
        "does": "متد preventDefault جلوی رفرش شدن صفحه هنگام ارسال فرم یا پرش لینک به # را می‌گیرد. متد stopPropagation مانع از رسیدن رویداد به تگ‌های بیرونی‌تر می‌شود.",
        "real": "ارسال فرم ثبت‌نام به سرور با Ajax بدون اینکه صفحه وب سفید و رفرش شود.",
        "code": "const loginForm = document.querySelector(\"#loginForm\");\n\nloginForm.addEventListener(\"submit\", (e) => {\n  e.preventDefault(); // مانع رفرش صفحه مرورگر شدیم\n  console.log(\"فرم با Ajax در پس‌زمینه ارسال می‌شود...\");\n});\n\nconst modal = document.querySelector(\".modal-content\");\nmodal.addEventListener(\"click\", (e) => {\n  e.stopPropagation(); // کلیک داخل مودال نباید آن را ببندد\n});"
    },
    {
        "id": 29,
        "title": "مدیریت فرم‌ها و خواندن مقادیر (FormData API)",
        "level": "متوسط",
        "what": "رابط استاندارد مرورگر برای جمع‌آوری و بسته‌بندی تمام اینپوت‌ها و فایل‌های انتخابی یک فرم در قالب یک شیء برای ارسال به سرور.",
        "does": "دیگر نیازی به نوشتن دستی document.getElementById برای تک‌تک فیلدها نیست؛ new FormData(form) کل مقادیر فرم از جمله فایل‌های عکسی را در کسری از ثانیه آماده ارسال با Fetch می‌کند.",
        "real": "آپلود مدارک هویتی و عکس پرسنلی کاربر در سامانه ثبت‌نام دانشگاه یا صرافی.",
        "code": "const form = document.querySelector(\"#profileForm\");\n\nform.addEventListener(\"submit\", async (e) => {\n  e.preventDefault();\n  const formData = new FormData(form);\n  \n  // ارسال راحت به سرور با fetch\n  // await fetch('/api/upload', { method: 'POST', body: formData });\n  console.log(\"نام کاربری:\", formData.get(\"username\"));\n});"
    },
    {
        "id": 30,
        "title": "مفهوم حیاتی کلوژر (Closures)",
        "level": "متوسط",
        "what": "ترکیبی از یک تابع به همراه محیط واژگانی اطرافش (Lexical Scope)؛ به طوری که تابع حتی پس از پایان اجرای تابع والد، متغیرهای خصوصی درون والد را در حافظه زنده نگه می‌دارد.",
        "does": "ایجاد متغیرهای کاملاً خصوصی (Private Variables) که از بیرون فایل قابل دستکاری و هک شدن نیستند، و ساخت توابع کارخانه‌ای و شمارنده‌ها.",
        "real": "مدیریت موجودی کیف پول کاربر به طوری که هیچ کدی در کنسول نتواند مستقیم موجودی را بدون کسر کارمزد زیاد کند.",
        "code": "function createWallet(initialBalance) {\n  let balance = initialBalance; // متغیر خصوصی امن\n  \n  return {\n    deposit(amount) {\n      balance += amount;\n      return balance;\n    },\n    getBalance() {\n      return balance;\n    }\n  };\n}\n\nconst myWallet = createWallet(100_000);\nmyWallet.deposit(50_000);\nconsole.log(myWallet.getBalance()); // 150000\n// console.log(myWallet.balance); // undefined (کاملا محفوظ و پنهان!)"
    },
    {
        "id": 31,
        "title": "کلمه کلیدی this و متدهای تغییر کانتکست (bind, call, apply)",
        "level": "متوسط",
        "what": "کلمه this به شیئی اشاره دارد که در حال حاضر مالک قطعه کد در حال اجراست. متدهای call و apply تابع را با this مشخص فورا اجرا می‌کنند، و bind یک کپی جدید از تابع با this قفل شده می‌سازد.",
        "does": "قرض گرفتن متدهای یک شیء توسط شیء دیگر بدون کپی کردن کد، و تثبیت این که تابع درون کدام کانتکست باید داده بخواند.",
        "real": "قرض گرفتن متد چاپ فاکتور شرکت مادر توسط شرکت‌های زیرمجموعه.",
        "code": "const invoice = {\n  company: \"دیجی‌استایل\",\n  print(tax, discount) {\n    console.log(`فاکتور ${this.company} - مالیات: ${tax}٪، تخفیف: ${discount}٪`);\n  }\n};\n\nconst subCompany = { company: \"اسنپ‌مارکت\" };\n\n// اجرای متد با this شیء دیگر\ninvoice.print.call(subCompany, 9, 20);\n\n// ساخت تابع همیشگی قفل شده روی اسنپ‌مارکت\nconst printSnapp = invoice.print.bind(subCompany, 9, 10);\nprintSnapp();"
    },
    {
        "id": 32,
        "title": "متدهای پیشرفته آبجکت‌ها (keys, values, entries, assign, freeze)",
        "level": "متوسط",
        "what": "ابزارهای مهندسی برای پیمایش، ادغام، و قفل کردن تغییرات در اشیاء جاوا اسکریپت.",
        "does": "متد Object.keys کلیدها را آرایه می‌کند؛ Object.entries جفت‌های [کلید, مقدار] می‌دهد؛ Object.freeze کل شیء را غیرقابل ویرایش (Immutable) می‌کند تا هیچ‌کس نتواند مقداری را تغییر دهد.",
        "real": "قفل کردن تنظیمات بحرانی سرور و کانفیگ دیتابیس در اپلیکیشن.",
        "code": "const APP_CONFIG = Object.freeze({\n  API_URL: \"https://api.site.com\",\n  TIMEOUT: 5000\n});\n\n// تلاش برای تغییر:\nAPP_CONFIG.TIMEOUT = 9999; // تغییر نادیده گرفته می‌شود (در strict mode ارور می‌دهد)\nconsole.log(APP_CONFIG.TIMEOUT); // همچنان 5000"
    },
    {
        "id": 33,
        "title": "فرمت تبادل داده JSON (parse و stringify)",
        "level": "متوسط",
        "what": "استاندارد جهانی متن‌محور جاوا اسکریپت برای تبادل داده بین سرور و مرورگر.",
        "does": "متد JSON.stringify آبجکت یا آرایه را به رشته متنی برای ارسال به وب‌سرویس تبدیل می‌کند. متد JSON.parse رشته دریافتی از سرور را دوباره به شیء قابل برنامه‌ریزی جاوا اسکریپت تبدیل می‌سازد.",
        "real": "ذخیره کردن سبد خرید در مرورگر یا ارسال بدنه درخواست‌های POST به API.",
        "code": "const cart = [{ id: 101, qty: 2 }];\n\n// تبدیل به متن برای ذخیره در دیسک/ارسال به وب‌سرویس\nconst jsonString = JSON.stringify(cart);\nconsole.log(\"متن خروجی:\", jsonString); // '[{\"id\":101,\"qty\":2}]'\n\n// بازیابی و تبدیل مجدد به آبجکت\nconst parsedCart = JSON.parse(jsonString);\nconsole.log(parsedCart[0].id); // 101"
    },
    {
        "id": 34,
        "title": "ذخیره‌سازی در مرورگر (localStorage, sessionStorage, Cookies)",
        "level": "متوسط",
        "what": "انبارهای ذخیره اطلاعات متنی در کلاینت کاربر. localStorage ماندگار و بدون تاریخ انقضاست (تا ۵ مگابایت)؛ sessionStorage با بستن تب بسته می‌شود؛ Cookies برای احراز هویت و ارسال خودکار به سرور استفاده می‌شود.",
        "does": "کاربر نیاز ندارد با هر بار باز کردن سایت دوباره نام تم (تاریک/روشن) را انتخاب کند؛ تنظیمات در هارد دیسک مرورگر ذخیره می‌شود.",
        "real": "ذخیره انتخاب تم تاریک کاربر و توکن لاگین در مرورگر.",
        "code": "// ذخیره تم انتخابی کاربر\nlocalStorage.setItem(\"siteTheme\", \"dark\");\n\n// خواندن تم هنگام لود صفحه بعدی\nconst savedTheme = localStorage.getItem(\"siteTheme\");\nif (savedTheme === \"dark\") {\n  document.body.classList.add(\"dark-mode\");\n}"
    },
    {
        "id": 35,
        "title": "تایمرها و اجرای با تاخیر (setTimeout و setInterval)",
        "level": "متوسط",
        "what": "زمان‌بندی اجرای کد در صف نوبت‌های مرورگر (Web APIs).",
        "does": "دستور setTimeout یک کار را پس از سپری شدن چند میلی‌ثانیه دقیقاً یک‌بار اجرا می‌کند. دستور setInterval کار را به طور مداوم با فاصله زمانی مشخص تکرار می‌کند تا با clearInterval متوقف شود.",
        "real": "ساخت تایمر شمارش معکوس ارسال مجدد پیامک ورود (۶۰ ثانیه).",
        "code": "let countdown = 60;\nconst timerId = setInterval(() => {\n  countdown--;\n  console.log(`امکان ارسال مجدد کد: ${countdown} ثانیه`);\n  \n  if (countdown <= 0) {\n    clearInterval(timerId); // توقف تایمر\n    console.log(\"دکمه ارسال مجدد فعال شد\");\n  }\n}, 1000);"
    },
    {
        "id": 36,
        "title": "مدیریت خطاها (try / catch / finally و throw)",
        "level": "متوسط",
        "what": "سپر محافظتی برنامه برای جلوگیری از کرش کردن کل صفحه وب در صورت وقوع خطای غیرمنتظره.",
        "does": "بلوک try کدهای خطرناک (مثل خواندن از سرور یا پارس جیسون) را اجرا می‌کند؛ اگر اروری پیش بیاید catch آن را شکار می‌کند بدون اینکه صفحه سفید شود؛ بلوک finally در هر دو حالت چه ارور باشد چه نباشد اجرا می‌شود.",
        "real": "پردازش پاسخ بانکی در درگاه پرداخت آنلاین و مدیریت خطای قطعی اینترنت.",
        "code": "function parseServerData(rawJson) {\n  try {\n    const data = JSON.parse(rawJson);\n    return data;\n  } catch (err) {\n    console.error(\"اطلاعات ارسالی از سرور خراب است:\", err.message);\n    return null; // برگرداندن مقدار امن پیش‌فرض\n  } finally {\n    console.log(\"عملیات بررسی دیتای سرور به پایان رسید\");\n  }\n}"
    },
    {
        "id": 37,
        "title": "عبارات باقاعده (Regular Expressions / Regex)",
        "level": "متوسط",
        "what": "الگوهای ریاضی قدرتمند متنی برای اعتبارسنجی و جستجوی فرمت‌های خاص در رشته‌ها.",
        "does": "بررسی فرمت ایمیل، شماره کارت ۱۶ رقمی شتاب بانکی، یا کد پستی بدون نیاز به نوشتن ده‌ها حلقه شرطی.",
        "real": "اعتبارسنجی شماره تلفن‌های همراه ایران در فرم ثبت‌نام.",
        "code": "// الگوی شماره موبایل معتبر ایران\nconst iranPhoneRegex = /^09\\d{9}$/;\n\nconsole.log(iranPhoneRegex.test(\"09123456789\")); // true\nconsole.log(iranPhoneRegex.test(\"02188776655\")); // false"
    },
    {
        "id": 38,
        "title": "ساختارهای داده مدرن (Set, Map, WeakSet, WeakMap)",
        "level": "متوسط",
        "what": "ساختارهای ذخیره‌سازی داده پیشرفته ES6. شیء Set مقادیر کاملاً یکتا و غیرتکراری را نگه می‌دارد. شیء Map کلیدهایی از هر جنسی (حتی آبجکت یا تگ DOM) قبول می‌کند.",
        "does": "حذف موارد تکراری از یک آرایه به سرعت باد در یک خط کد با new Set(arr) به جای نوشتن حلقه‌های سنگین.",
        "real": "حذف تگ‌های تکراری از مقالات وبلاگ و پیدا کردن کاربران فعال آنلاین.",
        "code": "const rawTags = [\"آموزش\", \"فرانت\", \"آموزش\", \"ری‌اکت\", \"فرانت\"];\n\n// حذف فوق سریع مقادیر تکراری با Set\nconst uniqueTags = [...new Set(rawTags)];\nconsole.log(uniqueTags); // ['آموزش', 'فرانت', 'ری‌اکت']"
    },
    {
        "id": 39,
        "title": "زنجیره‌سازی اختیاری (?.) و ادغام تهی (??)",
        "level": "متوسط",
        "what": "عملگرهای شگفت‌انگیز مدرن برای دسترسی به عمق آبجکت‌ها بدون ارور Cannot read properties of undefined و تعیین مقدار پیش‌فرض واقعی.",
        "does": "عملگر ?. اگر شیء null یا undefined باشد، بدون کرش کردن مقدار undefined می‌دهد. عملگر ?? بر خلاف ||، فقط زمانی مقدار پشتیبان را می‌اندازد که مقدار دقیقاً null یا undefined باشد (عدد 0 یا رشته خالی را به اشتباه اوررایت نمی‌کند!).",
        "real": "خواندن آدرس شهر کاربری که شاید اصلاً فیلد پروفایل یا آدرس را پر نکرده باشد.",
        "code": "const order = { id: 501, customer: null };\n\n// بدون باگ کرش کردن کل صفحه!\nconst city = order.customer?.address?.city ?? \"تهران (پیش‌فرض)\";\nconsole.log(city); // \"تهران (پیش‌فرض)\""
    },
    {
        "id": 40,
        "title": "ماژول‌های استاندارد جاوا اسکریپت (ES Modules: import / export)",
        "level": "متوسط",
        "what": "معماری رسمی تکه‌تکه کردن کدهای جاوا اسکریپت به فایل‌های مستقل و وارد کردن آن‌ها در یکدیگر.",
        "does": "امکان استفاده از export default و export const و وارد کردن آن‌ها در فایل‌های دیگر با دستور import، با لود تنبل و ایزوله‌سازی کامل فضای متغیرها.",
        "real": "تفکیک ماژول درگاه پرداخت زرین‌پال از هسته اصلی فروشگاه آنلاین.",
        "code": "// در فایل mathUtils.js\nexport const add = (a, b) => a + b;\nexport default function calculateCart() { /* ... */ }\n\n// در فایل app.js\n// import calculateCart, { add } from './mathUtils.js';"
    },
    {
        "id": 41,
        "title": "کپی سطحی در برابر کپی عمیق (Shallow vs Deep Copy & structuredClone)",
        "level": "متوسط",
        "what": "کپی سطحی (با Spread یا Object.assign) فقط لایه اول را کپی می‌کند و اشیاء تودرتو همچنان آدرس مشترک دارند. کپی عمیق کل درخت آبجکت را مستقل در حافظه بازسازی می‌کند.",
        "does": "تابع بومی جدید مرورگرها به نام structuredClone() بدون نیاز به کتابخانه‌های سنگینی مثل Lodash، کپی کاملاً عمیق و مستقل می‌سازد.",
        "real": "کلون کردن تنظیمات پیش‌فرض برای ویرایش بدون اینکه پروفایل اصلی مخدوش شود.",
        "code": "const original = {\n  name: \"عرفان\",\n  skills: [\"HTML\", \"CSS\"]\n};\n\n// کپی عمیق استاندارد مدرن\nconst cloned = structuredClone(original);\ncloned.skills.push(\"React\");\n\nconsole.log(original.skills); // ['HTML', 'CSS'] (دست‌نخورده و امن!)\nconsole.log(cloned.skills);   // ['HTML', 'CSS', 'React']"
    },
    {
        "id": 42,
        "title": "ارزیابی اتصال کوتاه (Short-circuit Evaluation with && and ||)",
        "level": "متوسط",
        "what": "استفاده هوشمندانه از رفتار عملگرهای منطقی برای نوشتن دستورات شرطی تک‌خطی بدون نیاز به if.",
        "does": "دستور A && B اگر A درست باشد B را اجرا یا برمی‌گرداند؛ دستور A || B اگر A غلط باشد B را اجرا یا برمی‌گرداند.",
        "real": "رندر شرطی بخش‌های صفحه وب در کدهای فرانت‌اند و ری‌اکت.",
        "code": "const isUserLoggedIn = true;\n\n// اگر لاگین است نوتیفیکیشن را نشان بده\nisUserLoggedIn && console.log(\"خوش آمدید! شما ۵ پیام خوانده نشده دارید.\");\n\nconst userDisplayName = \"\" || \"کاربر مهمان\";\nconsole.log(userDisplayName); // \"کاربر مهمان\""
    }
]

print("JS Module 2 (Intermediate: 18-42) Loaded:", len(JS_TOPICS_2))
