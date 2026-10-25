# -*- coding: utf-8 -*-
# Topics 43-75 (Advanced JavaScript) with practical real-world depth

JS_TOPICS_3 = [
    {
        "id": 43,
        "title": "پرامیس‌ها (Promises: pending, fulfilled, rejected, all, race, allSettled, any)",
        "level": "پیشرفته",
        "what": "اشیاء قول‌دهنده برای مدیریت نتایج عملیات غیرهمگام (Asynchronous). پرامیس در ابتدا در وضعیت انتظار (Pending) است تا در آینده یا با موفقیت انجام شود (Fulfilled) یا با شکست مواجه گردد (Rejected).",
        "does": "پایان دادن به جهنم کال‌بک‌ها (Callback Hell). با متد Promise.all می‌توانید ۱۰ درخواست را هم‌زمان به سرور بفرستید و فقط وقتی همه آماده شدند صفحه را رندر کنید. متد Promise.allSettled وضعیت تک‌تک آن‌ها را بدون کرش کردن بازمی‌گرداند.",
        "real": "لود هم‌زمان اطلاعات کاربر، موجودی کیف پول، و لیست تخفیف‌ها در صفحه اول اپلیکیشن دیجی‌کالا.",
        "code": "const fetchUser = fetch('/api/user').then(r => r.json());\nconst fetchOrders = fetch('/api/orders').then(r => r.json());\n\n// منتظر ماندن برای هر دو به صورت موازی\nPromise.all([fetchUser, fetchOrders])\n  .then(([user, orders]) => {\n    console.log(`خوش آمدید ${user.name}! شما ${orders.length} سفارش فعال دارید.`);\n  })\n  .catch(err => console.error(\"خطا در دریافت اطلاعات:\", err));"
    },
    {
        "id": 44,
        "title": "دستورات مدرن ناهمگام (async / await)",
        "level": "پیشرفته",
        "what": "سینتکس مدرن روی پرامیس‌ها که اجازه می‌دهد کدهای آسنکرون را مثل کدهای معمولی خط‌به‌خط و تمیز بنویسید.",
        "does": "با قرار دادن کلمه await قبل از پرامیس، اجرای خطوط بعدی متوقف می‌شود تا پاسخ بیاید، و همراه با try/catch استانداردترین الگوی فرانت‌اند مدرن را تشکیل می‌دهد.",
        "real": "ثبت تراکنش و هدایت به درگاه پرداخت در نرم‌افزارهای تجاری.",
        "code": "async function handleCheckout(cartId) {\n  try {\n    const response = await fetch(`/api/checkout/${cartId}`, { method: 'POST' });\n    const data = await response.json();\n    window.location.href = data.paymentUrl; // پرش به درگاه بانک\n  } catch (error) {\n    alert(\"خطا در اتصال به درگاه بانکی\");\n  }\n}"
    },
    {
        "id": 45,
        "title": "ارتباط با وب‌سرویس‌ها (Fetch API و AJAX)",
        "level": "پیشرفته",
        "what": "ابزار داخلی مرورگر برای ارسال درخواست‌های HTTP (GET, POST, PUT, DELETE) به سرور بدون بارگذاری مجدد صفحه.",
        "does": "جایگزین مدرن XMLHttpRequest قدیمی؛ ارسال هدرهای توکن، ارسال بادی جیسون و دریافت داده در پس‌زمینه.",
        "real": "ارسال نظر جدید برای یک پست بلاگ با متد POST و نمایش فوری آن در صفحه.",
        "code": "async function submitComment(postId, commentText) {\n  const res = await fetch(`https://api.site.com/posts/${postId}/comments`, {\n    method: 'POST',\n    headers: {\n      'Content-Type': 'application/json',\n      'Authorization': 'Bearer my_token_123'\n    },\n    body: JSON.stringify({ text: commentText })\n  });\n  return await res.json();\n}"
    },
    {
        "id": 46,
        "title": "لغو درخواست‌های شبکه (AbortController)",
        "level": "پیشرفته",
        "what": "کنترلر داخلی مرورگر برای متوقف کردن و لغو اضطراری درخواست‌های Fetch در حال اجرا.",
        "does": "جلوگیری از باگ Race Condition در سرچ‌باکس: وقتی کاربر کلمه جدیدی تایپ می‌کند، درخواست‌های قبلی را کنسل می‌کند تا پاسخ قدیمی پاسخ جدید را اوررایت نکند.",
        "real": "سرچ زنده محصولات در نوار جستجوی فروشگاه اینترنتی.",
        "code": "let controller = null;\n\nfunction searchProducts(query) {\n  // اگر درخواست قبلی هنوز در راه است، لغوش کن!\n  if (controller) controller.abort();\n  controller = new AbortController();\n\n  fetch(`/api/search?q=${query}`, { signal: controller.signal })\n    .then(r => r.json())\n    .then(data => renderResults(data))\n    .catch(err => {\n      if (err.name === 'AbortError') console.log('درخواست قبلی با موفقیت لغو شد');\n    });\n}"
    },
    {
        "id": 47,
        "title": "حلقه رویداد و صف‌ها (Event Loop, Call Stack, Microtask & Macrotask)",
        "level": "پیشرفته",
        "what": "معماری تک‌نخی (Single-Threaded) جاوا اسکریپت؛ ترتیب اجرای کدهای سنکرون در Call Stack و کدهای آسنکرون در صف‌ها.",
        "does": "موتور جاوا اسکریپت اول تمام Call Stack را خالی می‌کند، سپس صف Microtaskها (Promiseها، queueMicrotask) را تا انتها اجرا می‌کند و در آخر سراغ Macrotaskها (setTimeout, setInterval, I/O) می‌رود.",
        "real": "فهمیدن اینکه چرا setTimeout(fn, 0) حتی با تاخیر صفر بعد از پرامیس‌ها اجرا می‌شود.",
        "code": "console.log('۱. شروع (Stack)');\nsetTimeout(() => console.log('۴. تایمر (Macrotask)'), 0);\nPromise.resolve().then(() => console.log('۳. پرامیس (Microtask)'));\nconsole.log('۲. پایان (Stack)');\n// خروجی به ترتیب: ۱ -> ۲ -> ۳ -> ۴"
    },
    {
        "id": 48,
        "title": "زنجیره پروتوتایپ و وراثت (Prototypes & Prototype Chain)",
        "level": "پیشرفته",
        "what": "مکانیسم زیربنایی وراثت در جاوا اسکریپت؛ هر شیء لینکی به شیء دیگری به نام __proto__ دارد که خواص و متدهای آن را به ارث می‌برد.",
        "does": "اشتراک‌گذاری متدها در حافظه بدون کپی شدن روی هر نمونه (Instance) جدید از شیء، که مصرف رم را به شدت کاهش می‌دهد.",
        "real": "اضافه کردن متد سفارشی به کلاس‌های اصلی یا فهم کارکرد متدهای پیش‌فرض آرایه.",
        "code": "function Vehicle(name) {\n  this.name = name;\n}\n// تعریف متد در پروتوتایپ برای صرفه‌جویی در رم\nVehicle.prototype.start = function() {\n  return `${this.name} روشن شد!`;\n};\n\nconst car = new Vehicle('پژو ۲۰۶');\nconsole.log(car.start()); // متد از زنجیره پروتوتایپ فراخوانی شد"
    },
    {
        "id": 49,
        "title": "کلاس‌ها در جاوا اسکریپت مدرن (Classes, Private Fields, Getters/Setters)",
        "level": "پیشرفته",
        "what": "پوشش سینتکسی تمیز (Syntactic Sugar) روی پروتوتایپ‌ها برای پیاده‌سازی شیء‌گرایی.",
        "does": "تعریف constructor برای مقداردهی، کلمه extends و super برای وراثت، علامت # برای فیلدهای ۱۰۰٪ خصوصی محافظت‌شده در سطح موتور، و get/set برای کنترل اعتبارسنجی مقادیر.",
        "real": "ساخت کلاس مدیریت سبد خرید (CartService) در یک اپلیکیشن سازمانی.",
        "code": "class BankAccount {\n  #balance = 0; // فیلد خصوصی با هشتگ\n  \n  constructor(owner) {\n    this.owner = owner;\n  }\n  deposit(amount) {\n    if (amount > 0) this.#balance += amount;\n  }\n  get balance() {\n    return `${this.#balance.toLocaleString()} تومان`;\n  }\n}\nconst acc = new BankAccount('عرفان');\nacc.deposit(500000);\nconsole.log(acc.balance); // 500,000 تومان"
    },
    {
        "id": 50,
        "title": "الگوهای طراحی شی‌گرایی (OOP Design Patterns: Singleton, Factory, Observer)",
        "level": "پیشرفته",
        "what": "الگوهای معماری اثبات‌شده برای حل مسائل تکرارشونده در ساختارهای نرم‌افزاری.",
        "does": "الگوی Singleton تضمین می‌کند فقط یک نمونه از یک کلاس (مثل اتصال دیتابیس یا مدیر سوکت) در کل برنامه وجود داشته باشد؛ Observer برای سیستم‌های رخدادمحور و اشتراک‌گذاری رویدادهاست.",
        "real": "ساخت سیستم گوش دادن به نوتیفیکیشن‌ها یا ماژول کانکشن اختصاصی چت روم.",
        "code": "// نمونه الگوی Singleton\nclass DatabaseConnection {\n  static #instance = null;\n  constructor() {\n    if (DatabaseConnection.#instance) return DatabaseConnection.#instance;\n    this.status = 'CONNECTED';\n    DatabaseConnection.#instance = this;\n  }\n}\nconst db1 = new DatabaseConnection();\nconst db2 = new DatabaseConnection();\nconsole.log(db1 === db2); // true (دقیقاً یک شیء در کل رم وجود دارد)"
    },
    {
        "id": 51,
        "title": "توابع مرتبه بالا و کریینگ (Higher-Order Functions & Currying)",
        "level": "پیشرفته",
        "what": "توابعی که تابع دیگر را به عنوان ورودی می‌گیرند یا یک تابع جدید تولید می‌کنند. Currying تکنیک تبدیل تابعی با چند آرگومان به زنجیره‌ای از توابع تک‌آرگومانی است.",
        "does": "امکان ساخت توابع تخصصی با قفل کردن پارامترهای پایه (مثل ثبت نرخ مالیات یا لاگ با پیشوند اختصاصی).",
        "real": "ساخت میدل‌ورهای احراز هویت در فرانت‌اند و بک‌اند.",
        "code": "// Currying برای ساخت لاگر سفارشی\nconst logger = (prefix) => (message) => console.log(`[${prefix}] ${message}`);\n\nconst authLogger = logger('AUTH_SERVICE');\nconst payLogger = logger('PAYMENT_GATEWAY');\n\nauthLogger('کاربر با موفقیت لاگین کرد'); // [AUTH_SERVICE] کاربر با موفقیت لاگین کرد\npayLogger('تراکنش ۱۲۳ تایید شد');       // [PAYMENT_GATEWAY] تراکنش ۱۲۳ تایید شد"
    },
    {
        "id": 52,
        "title": "توابع خالص و ترکیب توابع (Pure Functions & Composition)",
        "level": "پیشرفته",
        "what": "تابع خالص (Pure) تابعی است که به ازای ورودی یکسان، همیشه خروجی یکسان بدهد و هیچ عارضه جانبی (Side Effect) روی متغیرهای بیرونی نگذارد.",
        "does": "کدنویسی بدون باگ، قابل تست آسان، و پیش‌بینی‌پذیر که پایه و اساس ریداکس و استیت منیجمنت ری‌اکت است.",
        "real": "محاسبه فاکتور سفارش در سیستم‌های مالی و حسابداری بدون تغییر دیتابیس اصلی.",
        "code": "// Pure Function: هیچ وابستگی بیرونی ندارد و چیزی را تغییر نمی‌دهد\nconst addVat = (amount) => amount * 1.09;\nconst applyDiscount = (amount) => amount - 50000;\n\n// ترکیب توابع (Composition)\nconst calculateFinal = (price) => applyDiscount(addVat(price));\nconsole.log(calculateFinal(1000000));"
    },
    {
        "id": 53,
        "title": "برنامه‌نویسی تابعی (Functional Programming Paradigms)",
        "level": "پیشرفته",
        "what": "پارادایم توسعه نرم‌افزار بر پایه تغییرناپذیری (Immutability)، دوری از تغییر وضعیت (Shared State)، و تبدیل داده‌ها از طریق خطوط لوله (Pipelines).",
        "does": "حذف باگ‌های تغییر تصادفی متغیرها در برنامه‌های بزرگ و امکان کش کردن خودکار نتایج.",
        "real": "معماری مدرن اپلیکیشن‌های تک‌صفحه‌ای با ریداکس یا زاستند.",
        "code": "const rawUsers = [{ name: 'عرفان', active: true }, { name: 'امیر', active: false }];\n\n// خط لوله تابعی بدون دست زدن به آرایه اصلی\nconst activeUserNames = rawUsers\n  .filter(u => u.active)\n  .map(u => u.name.toUpperCase());\nconsole.log(activeUserNames); // ['عرفان']"
    },
    {
        "id": 54,
        "title": "تکرارکننده‌ها و ساختارهای پیمایش‌پذیر (Iterators & Iterables)",
        "level": "پیشرفته",
        "what": "پروتکل رسمی جاوا اسکریپت برای اینکه یک شیء بتواند در حلقه for...of پیمایش شود (با داشتن متد [Symbol.iterator]).",
        "does": "امکان ساخت ساختارهای داده دلخواه با قابلیت پیمایش تک‌به‌تک و تنبل با متد next().",
        "real": "پیمایش گام‌به‌گام مراحل یک ویزارد ثبت‌نام چندمرحله‌ای.",
        "code": "const stepWizard = {\n  steps: ['اطلاعات فردی', 'آدرس', 'پرداخت'],\n  [Symbol.iterator]() {\n    let index = 0;\n    return {\n      next: () => ({\n        value: this.steps[index++],\n        done: index > this.steps.length\n      })\n    };\n  }\n};\nfor (const step of stepWizard) {\n  console.log('مرحله:', step);\n}"
    },
    {
        "id": 55,
        "title": "ژنراتورها (Generators: function* و yield)",
        "level": "پیشرفته",
        "what": "توابعی که می‌توان اجرای آن‌ها را در میانه کار با دستور yield متوقف کرد و بعداً در صورت نیاز ادامه داد.",
        "does": "تولید توالی‌های نامحدود داده در حافظه رم با اشغال نزدیک به صفر بایت حافظه (Lazy Evaluation).",
        "real": "تولید شناسه‌های عددی ترتیبی یکتا یا مدیریت جریان داده در کتابخانه Redux Saga.",
        "code": "function* idGenerator() {\n  let id = 1000;\n  while (true) {\n    yield id++;\n  }\n}\nconst gen = idGenerator();\nconsole.log(gen.next().value); // 1000\nconsole.log(gen.next().value); // 1001\nconsole.log(gen.next().value); // 1002"
    },
    {
        "id": 56,
        "title": "نمادها (Symbols و Well-known Symbols)",
        "level": "پیشرفته",
        "what": "نوع داده اولیه کاملاً منحصر‌به‌فرد و یکتا در حافظه که امکان برخورد کلیدهای دو آبجکت را به صفر می‌رساند.",
        "does": "تعریف کلیدهای خصوصی در آبجکت‌ها و دستکاری رفتارهای درونی جاوا اسکریپت مثل تبدیل به رشته یا پیمایش با Well-known Symbols.",
        "real": "افزودن متادیتای اختصاصی به آبجکت‌ها در کتابخانه‌های متن‌باز بدون تداخل با کدهای کاربر.",
        "code": "const INTERNAL_ID = Symbol('id');\nconst user = {\n  name: 'عرفان',\n  [INTERNAL_ID]: 'secret-hash-99'\n};\nconsole.log(user[INTERNAL_ID]); // secret-hash-99\nconsole.log(Object.keys(user)); // فقط ['name'] نمایش داده می‌شود!"
    },
    {
        "id": 57,
        "title": "پراکسی و بازتاب (Proxy & Reflect)",
        "level": "پیشرفته",
        "what": "شکارچی عملیات اساسی اشیاء؛ ایجاد یک بادی‌گارد هوشمند دور آبجکت برای رهگیری خواندن، نوشتن یا حذف فیلدها.",
        "does": "پایه‌گذار سیستم واکنش‌پذیری (Reactivity) در فریمورک‌های مدرنی مثل Vue 3؛ وقتی مقداری عوض می‌شود، پراکسی متوجه شده و صفحه وب را خودکار آپدیت می‌کند.",
        "real": "اعتبارسنجی سن کاربر: نگذارید عددی منفی برای فیلد age ثبت شود.",
        "code": "const validator = {\n  set(target, prop, value) {\n    if (prop === 'age' && (typeof value !== 'number' || value <= 0)) {\n      throw new Error('سن باید یک عدد مثبت باشد');\n    }\n    target[prop] = value;\n    return true;\n  }\n};\nconst profile = new Proxy({}, validator);\nprofile.age = 25; // بدون مشکل ست می‌شود\n// profile.age = -5; // ارور امنیتی پرتاب می‌کند!"
    },
    {
        "id": 58,
        "title": "تکنیک‌های کنترل نرخ اجرا (Debounce و Throttle)",
        "level": "پیشرفته",
        "what": "الگوهای حیاتی بهینه‌سازی عملکرد. Debounce تا زمانی که کاربر دست از تایپ نکشد اجرا را به تعویق می‌اندازد. Throttle اجرا را روی حداکثر یک‌بار در هر چند میلی‌ثانیه قفل می‌کند.",
        "does": "جلوگیری از هنگ کردن مرورگر هنگام اسکرول سریع یا تایپ در باکس جستجو.",
        "real": "جستجوی زنده در فروشگاه با Debounce و محاسبه موقعیت اسکرول بار با Throttle.",
        "code": "function debounce(fn, delay) {\n  let timeoutId;\n  return function(...args) {\n    clearTimeout(timeoutId);\n    timeoutId = setTimeout(() => fn.apply(this, args), delay);\n  };\n}\n// فقط وقتی کاربر ۳۰۰ میلی‌ثانیه دست از تایپ کشید ریکوئست بفرست\nconst sendSearch = debounce((q) => console.log('درخواست جستجو به سرور برای:', q), 300);"
    },
    {
        "id": 59,
        "title": "تکنیک مِمویزیشن (Memoization)",
        "level": "پیشرفته",
        "what": "کش کردن نتایج محاسبات سنگین ریاضی بر مبنای آرگومان‌های ورودی تابع.",
        "does": "اگر تابع با ورودی یکسان صدا زده شود، به جای محاسبه مجدد چندثانیه‌ای، جواب ذخیره‌شده را از رم در چند میلی‌ثانیه تحویل می‌دهد.",
        "real": "محاسبه فاکتوریل، محاسبات پیچیده نمودارها در داشبورد یا رندر مجدد هوک useMemo در ری‌اکت.",
        "code": "function memoize(fn) {\n  const cache = {};\n  return function(...args) {\n    const key = JSON.stringify(args);\n    if (cache[key]) return cache[key];\n    const result = fn(...args);\n    cache[key] = result;\n    return result;\n  };\n}"
    },
    {
        "id": 60,
        "title": "بازگشت و بهینه‌سازی فراخوانی انتهایی (Recursion & Tail Call Optimization)",
        "level": "پیشرفته",
        "what": "فراخوانی یک تابع توسط خودش تا رسیدن به شرط توقف (Base Case).",
        "does": "بهترین روش برای پیمایش ساختارهای درختی مثل کامنت‌های تودرتو یا فولدرهای یک فایل سیستم.",
        "real": "محاسبه مجموع قیمت دسته‌بندی‌های تودرتوی محصولات در فروشگاه اینترنتی.",
        "code": "function sumFolderSize(folder) {\n  let total = folder.size || 0;\n  if (folder.subFolders) {\n    for (const sub of folder.subFolders) {\n      total += sumFolderSize(sub); // فراخوانی بازگشتی\n    }\n  }\n  return total;\n}"
    },
    {
        "id": 61,
        "title": "رابط‌های پیشرفته وب (Intersection, Mutation & Resize Observers)",
        "level": "پیشرفته",
        "what": "ناظران با کارایی بالا در مرورگر بدون نیاز به لیسنرهای سنگین اسکرول.",
        "does": "ناظر IntersectionObserver ورود المان به کادر دید را می‌فهمد (لود تنبل تصاویر و اسکرول بی‌پایان). ResizeObserver تغییر اندازه المان را می‌سنجد و MutationObserver تغییرات کدهای DOM را شکار می‌کند.",
        "real": "لود تنبل بی‌نقص ویدیوها و اسکرول نامحدود در اکسپلور اینستاگرام.",
        "code": "const observer = new IntersectionObserver((entries) => {\n  entries.forEach(entry => {\n    if (entry.isIntersecting) {\n      console.log('عکس وارد کادر دید کاربر شد؛ اکنون لودش کن!');\n      observer.unobserve(entry.target);\n    }\n  });\n});\n// observer.observe(document.querySelector('#myImage'));"
    },
    {
        "id": 62,
        "title": "ورکرهای پس‌زمینه (Web Workers & Service Workers)",
        "level": "پیشرفته",
        "what": "اجرای کدهای جاوا اسکریپت روی نخ‌های مجزای پردازنده (Multi-threading).",
        "does": "دستور Web Worker محاسبات سنگین (مثل فیلتر عکس یا هوش مصنوعی) را روی نخ دیگر می‌اندازد تا رابط کاربری هرگز قفل نشود. دستور Service Worker برای کش آفلاین و ساخت PWA است.",
        "real": "پردازش و ادیت تصویر کاربر در فتوشاپ وب بدون اینکه صفحه فریز شود.",
        "code": "// اجرای ورکر مجزا در پس‌زمینه\n// const worker = new Worker('heavy-calc.js');\n// worker.postMessage({ numbers: [1, 2, 3, 4] });\n// worker.onmessage = (e) => console.log('نتیجه محاسبات سنگین:', e.data);"
    },
    {
        "id": 63,
        "title": "ارتباط زنده دوطرفه (WebSocket & Server-Sent Events)",
        "level": "پیشرفته",
        "what": "ارتباط دائمی بر بستر سوکت TCP که سرور می‌تواند بدون نیاز به رفرش یا درخواست کاربر، فورا داده بفرستد.",
        "does": "بر خلاف HTTP که درخواست-پاسخ است، وب‌سوکت اتصال زنده باز نگه می‌دارد تا چت و قیمت‌های لحظه‌ای در صدم ثانیه رد و بدل شوند.",
        "real": "نمودار زنده قیمت بیت‌کوین در صرافی نوبیتکس و سیستم چت پشتیبانی آنلاین.",
        "code": "const socket = new WebSocket('wss://stream.binance.com:9443/ws/btcusdt@trade');\nsocket.onmessage = (event) => {\n  const trade = JSON.parse(event.data);\n  console.log(`قیمت لحظه‌ای بیت‌کوین: $${trade.p}`);\n};"
    },
    {
        "id": 64,
        "title": "پایگاه داده درون‌مرورگری (IndexedDB)",
        "level": "پیشرفته",
        "what": "دیتابیس تراکنشی و سندمحور غول‌پیکر (NoSQL) درون مرورگر کاربر با ظرفیت صدها مگابایت.",
        "does": "ذخیره فایل‌های حجیم صوتی، اسناد و رکوردهای کامل پروژه برای کارکرد آفلاین کامل نرم‌افزار بدون اینترنت.",
        "real": "کارکرد آفلاین گوگل داکس و ترلو حین قطع شدن اتصال شبکه.",
        "code": "const request = indexedDB.open('OfflineStore', 1);\nrequest.onupgradeneeded = (e) => {\n  const db = e.target.result;\n  db.createObjectStore('drafts', { keyPath: 'id' });\n};\nconsole.log('دیتابیس کلاینت آماده ذخیره‌سازی هزاران سند است');"
    },
    {
        "id": 65,
        "title": "مدیریت حافظه و جمع‌آوری زباله (Memory Management & Garbage Collection)",
        "level": "پیشرفته",
        "what": "نحوه تخصیص رم (Stack برای اولیه، Heap برای اشیاء) و فرآیند پاکسازی خودکار متغیرهای بی‌استفاده با الگوریتم Mark-and-Sweep.",
        "does": "آشنایی با اینکه حافظه چگونه آزاد می‌شود و جلوگیری از پر شدن حافظه موقت سیستم کاربر.",
        "real": "طراحی اپلیکیشن‌های داشبورد سازمانی که روزها بدون بستن مرورگر باید نرم و سریع کار کنند.",
        "code": "let heavyData = { buffer: new Array(1000000) };\nheavyData = null; // اتصال مرجع قطع شد؛ در چرخه بعدی Garbage Collector رم را آزاد می‌کند"
    },
    {
        "id": 66,
        "title": "نشت حافظه و روش‌های پیشگیری (Memory Leaks Prevention)",
        "level": "پیشرفته",
        "what": "حالتی که کدی در برنامه به اشیاء دیگر دسترسی نگه می‌دارد و مانع از آزاد شدن رم توسط Garbage Collector می‌شود و بعد از مدتی تب مرورگر کرش می‌کند.",
        "does": "مهم‌ترین عوامل نشت حافظه: تایمرهای فراموش‌شده (setInterval بدون پاکسازی)، لیسنرهای رهاشده، و کلوژرهای سنگین سراسری.",
        "real": "جلوگیری از پر شدن رم دستگاه مشتری در نرم‌افزارهای چت و اسکرول طولانی.",
        "code": "// روش صحیح: همیشه هنگام بستن بخش، لیسنر را حذف کنید\nfunction setupListener() {\n  const handler = () => console.log('کلیک');\n  window.addEventListener('resize', handler);\n  \n  return () => window.removeEventListener('resize', handler); // تمیزکاری الزامی!\n}"
    },
    {
        "id": 67,
        "title": "قالب‌های برچسب‌دار (Tagged Template Literals)",
        "level": "پیشرفته",
        "what": "فراخوانی توابع با رشته‌های تمپلیت بدون پرانتز fn`hello ${name}` برای تجزیه و بهینه‌سازی عبارات متنی.",
        "does": "تکنولوژی زیربنایی کتابخانه‌های محبوب فرانت‌اند مثل styled-components یا ماژول‌های امنیتی پاکسازی SQL/HTML.",
        "real": "ساخت کامپوننت‌های استایل‌داده شده در ری‌اکت یا جلوگیری از حملات XSS.",
        "code": "function sanitize(strings, ...values) {\n  return strings.reduce((acc, str, i) => {\n    const val = values[i - 1] ? String(values[i - 1]).replace(/</g, '&lt;') : '';\n    return acc + val + str;\n  });\n}\nconst userInput = \"<script>alert('hack')</script>\";\nconst safeHTML = sanitize`<div>${userInput}</div>`;\nconsole.log(safeHTML); // ایمن‌سازی کامل شد"
    },
    {
        "id": 68,
        "title": "بارگذاری پویا و تکه‌تکه کردن کد (Dynamic Import & Code Splitting)",
        "level": "پیشرفته",
        "what": "لود کردن ماژول‌های جاوا اسکریپت فقط زمانی که کاربر واقعاً به آن‌ها نیاز دارد با import('./module.js').",
        "does": "کاهش حجم لود اولیه سایت از ۵ مگابایت به ۲۰۰ کیلوبایت؛ بخش پنل ادمین یا رسم نمودار فقط وقتی کاربر دکمه مربوطه را زد دانلود می‌شود.",
        "real": "لود کتابخانه سنگین Chart.js فقط زمانی که کاربر تب «گزارش مالی» را باز می‌کند.",
        "code": "const reportBtn = document.querySelector('#viewChart');\nreportBtn.addEventListener('click', async () => {\n  // دانلود فقط در زمان نیاز (On-Demand)\n  const { renderChart } = await import('./chartsModule.js');\n  renderChart();\n});"
    },
    {
        "id": 69,
        "title": "تکان دادن درخت کدها (Tree Shaking)",
        "level": "پیشرفته",
        "what": "فرایند حذف خودکار کدهای مرده و توابع استفاده نشده از فایل نهایی بیلد توسط باندلرهای مدرن.",
        "does": "اگر کتابخانه‌ای ۱۰۰۰ تابع دارد و شما فقط ۲ تای آن را ایمپورت کردید، ۹۹۸ تابع بقیه دور ریخته می‌شوند تا کاربر فایل کم‌حجم دانلود کند.",
        "real": "کاهش حجم باندل نهایی پروژه‌های سازمانی برای ارتقای سئو و سرعت لود.",
        "code": "// باندلر فقط تابع add را نگه می‌دارد و multiply را از فایل نهایی حذف می‌کند:\nimport { add } from './mathUtils.js';"
    },
    {
        "id": 70,
        "title": "ابزارهای بسته‌بندی و کامپایلرها (Webpack, Vite & Babel)",
        "level": "پیشرفته",
        "what": "ابزارهایی برای تبدیل، کامپایل و تجمیع صدها فایل، ماژول و تایپ‌اسکریپت به یک پکیج آماده برای مرورگر.",
        "does": "کامپایلر Babel ویژگی‌های مدرن جاوا اسکریپت را به کدهای سازگار با مرورگرهای قدیمی تبدیل می‌کند. Vite با استفاده از ES Modules سرور توسعه فوق سریع صدم ثانیه‌ای ارائه می‌دهد.",
        "real": "پیکربندی استک توسعه در تمام شرکت‌های معتبر نرم‌افزاری جهان.",
        "code": "// vite.config.js\nimport { defineConfig } from 'vite';\nexport default defineConfig({\n  server: { port: 3000 },\n  build: { target: 'esnext' }\n});"
    },
    {
        "id": 71,
        "title": "تست‌نویسی نرم‌افزار (Testing: Jest & Vitest)",
        "level": "پیشرفته",
        "what": "نوشتن کدهایی برای ارزیابی صحت عملکرد سایر کدهای برنامه (Unit Tests, Integration Tests).",
        "does": "اطمینان ۱۰۰٪ از اینکه تغییرات جدید کد، بخش پرداخت و فاکتورها را در نیمه‌شب خراب نکرده است.",
        "real": "تست درگاه پرداخت و محاسبه سبد خرید قبل از دپلویمنت روی سرور لایو.",
        "code": "// تست تابع تخفیف با Vitest\nimport { expect, test } from 'vitest';\n\ntest('محاسبه صحیح تخفیف ۲۰ درصدی', () => {\n  const result = 100000 * 0.8;\n  expect(result).toBe(80000);\n});"
    },
    {
        "id": 72,
        "title": "مبانی تایپ‌اسکریپت (TypeScript: Interfaces, Generics, Enums)",
        "level": "پیشرفته",
        "what": "ابرجاوا اسکریپت نوع‌دار (Typed Superset) که خطاهای متغیرها و توابع را در حین کدنویسی در VS Code قبل از اجرا شکار می‌کند.",
        "does": "پایان دادن به خطاهای runtime مثل ارورهای تایپی؛ پروژه‌های تیمی بزرگ بدون تایپ‌اسکریپت غیرقابل نگهداری هستند.",
        "real": "تعریف دقیق قرارداد ورودی‌ها و خروجی‌های وب‌سرویس بک‌اند در فرانت‌اند.",
        "code": "interface UserProfile {\n  id: number;\n  name: string;\n  role: 'admin' | 'user';\n}\n\nfunction printProfile(user: UserProfile) {\n  console.log(`کاربر: ${user.name} (${user.role})`);\n}"
    },
    {
        "id": 73,
        "title": "امنیت در جاوا اسکریپت (XSS, CSRF, CORS & Data Sanitization)",
        "level": "پیشرفته",
        "what": "مفاهیم و استانداردهای دفاع در برابر نفوذ هکرها به مرورگر کاربران.",
        "does": "حمله XSS با تزریق کدهای مخرب در کامنت‌ها توکن را می‌دزدد؛ پاکسازی (Sanitization) با DOMPurify جلوی آن را می‌گیرد. CORS سیاست امنیتی مرورگر برای بستن درخواست دامنه‌های ناشناس است.",
        "real": "پاکسازی نظرات کاربران قبل از درج مستقیم در صفحه برای جلوگیری از هک حساب‌ها.",
        "code": "// پاکسازی ورودی کاربر برای جلوگیری از تزریق اسکریپت\n// const cleanHTML = DOMPurify.sanitize(userBioInput);\n// document.querySelector('#bio').innerHTML = cleanHTML;"
    },
    {
        "id": 74,
        "title": "بهینه‌سازی عملکرد (Performance Optimization & Web Vitals)",
        "level": "پیشرفته",
        "what": "سنجه‌های حیاتی سرعت گوگل (LCP, CLS, INP) و کاهش مصرف پردازنده و رم در مرورگر.",
        "does": "سرعت بالا باعث رتبه ۱ گوگل در سئو و افزایش فروش می‌شود؛ پرهیز از Forced Layout Thrashing با کش کردن ابعاد المان‌ها.",
        "real": "رساندن نمره سرعت سایت در Google Lighthouse به ۱۰۰ سبز.",
        "code": "// اندازه‌گیری دقیق زمان اجرای یک بلاک کد\nconsole.time('OrderComputation');\n// عملیات سنگین...\nconsole.timeEnd('OrderComputation');"
    },
    {
        "id": 75,
        "title": "آشنایی با Node.js در بک‌اند (File System, Path, NPM)",
        "level": "پیشرفته",
        "what": "محیط اجرای جاوا اسکریپت خارج از مرورگر بر پایه موتور V8 گوگل کروم برای ساخت سرورها، اسکریپت‌های اتوماسیون و ابزارهای ساخت.",
        "does": "دسترسی مستقیم به فایل‌های هارد دیسک، مدیریت پکیج‌ها با npm و ساخت وب‌سرورهای پرسرعت با Express یا Fastify.",
        "real": "ساخت اسکریپت‌های اتوماسیون بیلد، ربات‌های تلگرام و وب‌سرویس‌های تجاری.",
        "code": "// خواندن فایل متنی از دیسک با نود جی‌اس\n// const fs = require('fs');\n// const content = fs.readFileSync('config.json', 'utf-8');\n// console.log('محتوای فایل کانفیگ:', content);"
    }
]

print("JS Module 3 (Advanced: 43-75) Loaded:", len(JS_TOPICS_3))
