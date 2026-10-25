# -*- coding: utf-8 -*-
# Topics 1-20 (React Beginner & Core Hooks) with practical real-world depth

REACT_TOPICS_1 = [
    {
        "id": 1,
        "title": "React چیست و معماری DOM مجازی (Virtual DOM)",
        "level": "مبتدی",
        "what": "کتابخانه جاوا اسکریپت فیس‌بوک برای ساخت رابط‌های کاربری کامپوننت‌محور و تک‌صفحه‌ای (SPA). DOM مجازی یک کپی سبک و بهینه از درخت HTML واقعی در رم سیستم است.",
        "does": "در جاوا اسکریپت وانیلا اگر مقداری تغییر کند و کل صفحه رندر شود، مرورگر لگ می‌زند. ری‌اکت با الگوریتم Diffing دو درخت مجازی را مقایسه می‌کند و فقط و فقط همان یک کلمه‌ای که عوض شده را در صفحه واقعی بروزرسانی می‌کند (حداقل مصرف پردازنده).",
        "real": "تغییر تعداد لایک یا قیمت زنده سهام در صفحه بدون چشمک زدن یا ری‌لود سایر کارت‌ها.",
        "code": "// ری‌اکت خودش پشت صحنه با این مقایسه هوشمند کار می‌کند\nimport React from 'react';\nimport ReactDOM from 'react-dom/client';\n\nfunction App() {\n  return <h1>سلام به دنیای سریع ری‌اکت!</h1>;\n}\nReactDOM.createRoot(document.getElementById('root')).render(<App />);"
    },
    {
        "id": 2,
        "title": "راه‌اندازی پروژه مدرن با Vite (به جای Create React App منسوخ)",
        "level": "مبتدی",
        "what": "ابزار ساخت نسل جدید و پرسرعت فرانت‌اند که بر پایه ماژول‌های بومی مرورگر (ESM) کار می‌کند.",
        "does": "پروژه‌های قدیمی Create React App برای شروع به ۳۰ ثانیه زمان نیاز داشتند؛ با Vite سرور لوکال در کمتر از ۳۰۰ میلی‌ثانیه بالا می‌آید و هر تغییری در فایل با Hot Module Replacement (HMR) در کسری از ثانیه روی مرورگر اعمال می‌شود.",
        "real": "دستور شروع ساخت تمام پروژه‌های حرفه‌ای ری‌اکت در شرکت‌ها.",
        "code": "# دستور راه‌اندازی سریع در ترمینال\nnpm create vite@latest my-app -- --template react\ncd my-app\nnpm install\nnpm run dev"
    },
    {
        "id": 3,
        "title": "سینتکس JSX و قوانین سه‌گانه آن",
        "level": "مبتدی",
        "what": "ترکیب قدرتمند HTML در دل کدهای جاوا اسکریپت (JavaScript XML).",
        "does": "اجازه می‌دهد ظاهر کامپوننت و منطق آن در یک فایل کنار هم زندگی کنند. قوانین: ۱. همیشه باید یک والد واحد (یا Fragment) داشته باشد ۲. تگ‌ها باید بسته شوند (<img />) ۳. ویژگی‌ها شتری هستند (className به جای class و htmlFor به جای for).",
        "real": "رندر پویا و امن کارت مشخصات کاربر بدون نگرانی از نفوذ XSS.",
        "code": "function UserBadge({ name, avatarUrl }) {\n  return (\n    <div className=\"user-card\">\n      <img src={avatarUrl} alt={name} className=\"avatar-img\" />\n      <h3>{name}</h3>\n    </div>\n  );\n}"
    },
    {
        "id": 4,
        "title": "کامپوننت‌های تابعی (Function Components)",
        "level": "مبتدی",
        "what": "قطعات لگویی چندبار مصرف نرم‌افزار که تابعی ساده هستند که ورودی (Props) می‌گیرند و خروجی JSX می‌دهند.",
        "does": "جایگزین کلاس‌های قدیمی و پیچیده React شدند؛ کدها بسیار خواناتر، تست‌پذیرتر و سبک‌تر شدند.",
        "real": "ساخت دکمه عمومی (<Button />) که در صفحه لاگین، سبد خرید و تنظیمات استفاده می‌شود.",
        "code": "function Button({ text, onClick, variant = 'primary' }) {\n  return (\n    <button className={`btn btn-${variant}`} onClick={onClick}>\n      {text}\n    </button>\n  );\n}"
    },
    {
        "id": 5,
        "title": "ویژگی‌ها و داده‌های ورودی (Props)",
        "level": "مبتدی",
        "what": "ورودی‌های یک‌طرفه (Unidirectional Data Flow) از کامپوننت والد به کامپوننت فرزند؛ کامپوننت فرزند هرگز حق تغییر مستقیم Props خود را ندارد (Read-Only).",
        "does": "شخصی‌سازی قطعات رابط کاربری؛ مثلاً یک قالب کارت محصول می‌سازید و اطلاعات ۱۰۰ کالا را از بیرون به آن پاس می‌دهید.",
        "real": "پاس دادن عنوان، قیمت و تخفیف به کامپوننت نمایش محصول دیجی‌کالا.",
        "code": "function ProductCard({ title, price, discount }) {\n  return (\n    <div className=\"product\">\n      <h4>{title}</h4>\n      <p>قیمت: {price - discount} تومان</p>\n    </div>\n  );\n}\n// استفاده: <ProductCard title=\"کفش نایک\" price={1200000} discount={200000} />"
    },
    {
        "id": 6,
        "title": "پراپ فرزندان (Children Prop)",
        "level": "مبتدی",
        "what": "یک پراپ خاص و بومی در ری‌اکت که هر محتوایی بین تگ باز و بسته کامپوننت (<Card>...</Card>) قرار بگیرد را دریافت می‌کند.",
        "does": "ساخت کامپوننت‌های قالبی (Wrapper / Layout) مانند مودال‌ها، کادرهای هشدار و صفحات بدون وابسته شدن به نوع محتوا.",
        "real": "طراحی کادر مودال بازشونده عمومی که در یک صفحه فرم پرداخت و در صفحه دیگر متن قوانین را نمایش می‌دهد.",
        "code": "function Modal({ isOpen, children, onClose }) {\n  if (!isOpen) return null;\n  return (\n    <div className=\"modal-backdrop\">\n      <div className=\"modal-box\">\n        <button onClick={onClose} className=\"close-btn\">✕</button>\n        {children} {/* هر تگی که داخل مودال بگذارید اینجا رندر می‌شود */}\n      </div>\n    </div>\n  );\n}"
    },
    {
        "id": 7,
        "title": "رندر لیست‌ها و کلید حیاتی (Rendering Lists & Keys)",
        "level": "مبتدی",
        "what": "پیمایش آرایه‌ها با متد map برای تولید لیستی از کارت‌ها، و قرار دادن صفت یکتای key روی بالاترین تگ فرزند.",
        "does": "صفت key مثل کد ملی المان است؛ اگر ردیفی حذف، اضافه یا جابجا شود، ری‌اکت به کمک key می‌فهمد کدام خانه تغییر کرده و نیازی به پاک کردن و از نو ساختن کل لیست پیدا نمی‌کند.",
        "real": "نمایش لیست ۵۰ تراکنش بانکی آخر کاربر در صفحه حساب.",
        "code": "function TransactionList({ items }) {\n  return (\n    <ul>\n      {items.map((item) => (\n        <li key={item.id} className=\"tx-row\">\n          <span>{item.title}</span>\n          <span>{item.amount.toLocaleString()} تومان</span>\n        </li>\n      ))}\n    </ul>\n  );\n}"
    },
    {
        "id": 8,
        "title": "رندر شرطی (Conditional Rendering: &&, Ternary, Early Return)",
        "level": "مبتدی",
        "what": "تصمیم‌گیری برای نمایش یا پنهان کردن یک بخش از رابط کاربری بر اساس وضعیت متغیرها.",
        "does": "نمایش اسپینر لودینگ حین دریافت داده، یا نمایش دکمه «خروج» به جای دکمه «ورود» وقتی توکن معتبر است.",
        "real": "نمایش بنر قرمز «ناموجود» اگر موجودی انبار صفر بود، وگرنه نمایش دکمه «خرید فوری».",
        "code": "function StockStatus({ count }) {\n  if (count === 0) {\n    return <span className=\"badge danger\">کالا ناموجود شد</span>;\n  }\n  return (\n    <div>\n      <span>تنها {count} عدد در انبار باقیست</span>\n      <button className=\"btn-buy\">افزودن به سبد</button>\n    </div>\n  );\n}"
    },
    {
        "id": 9,
        "title": "رویدادها در ری‌اکت (Synthetic Events & Event Handlers)",
        "level": "مبتدی",
        "what": "مدیریت کلیک، تایپ و فرم‌ها به صورت یکپارچه شده در تمام مرورگرها توسط لایه SyntheticEvent ری‌اکت.",
        "does": "رویدادها با حروف شتری (onClick, onChange) تعریف می‌شوند و تابعی را صدا می‌زنند، بدون نیاز به addEventListener دستی و بدون نشت حافظه.",
        "real": "شنیدن کلیک روی دکمه افزودن کالا به سبد خرید همراه با ارسال شناسه محصول.",
        "code": "function CartButton({ productId }) {\n  const handleClick = (e) => {\n    e.stopPropagation(); // جلوگیری از باز شدن لینک کارت\n    console.log(`محصول ${productId} به سبد خرید افزوده شد`);\n  };\n  return <button onClick={handleClick}>خرید کالا</button>;\n}"
    },
    {
        "id": 10,
        "title": "وضعیت و حافظه کامپوننت با هوک useState",
        "level": "مبتدی",
        "what": "هوک پایه برای نگهداری داده‌های تغییرپذیر درون کامپوننت؛ هر بار که تابع تغییر دهنده (Setter) صدا زده شود، ری‌اکت کامپوننت را دوباره رندر می‌کند.",
        "does": "در متغیرهای عادی با تغییر متغیر ظاهر صفحه تکان نمی‌خورد؛ با useState ری‌اکت متوجه تغییر می‌شود و فورا خروجی جدید را به کاربر نشان می‌دهد.",
        "real": "شمارنده تعداد سفارش کالا (+ و -) در سبد خرید آنلاین.",
        "code": "import { useState } from 'react';\n\nfunction Counter() {\n  const [count, setCount] = useState(1);\n  \n  return (\n    <div className=\"counter-box\">\n      <button onClick={() => setCount(prev => Math.max(1, prev - 1))}>-</button>\n      <span>{count}</span>\n      <button onClick={() => setCount(prev => prev + 1)}>+</button>\n    </div>\n  );\n}"
    },
    {
        "id": 11,
        "title": "استایل‌دهی در ری‌اکت (Inline Styles, CSS Modules, Tailwind)",
        "level": "مبتدی",
        "what": "روش‌های ظاهر دادن به قطعات ری‌اکت: شیء استایل اینلاین، ماژول‌های CSS ایزوله (.module.css) و کلاس‌های یوتیلیتی Tailwind.",
        "does": "در CSS Modules نام کلاس‌ها در زمان بیلد هش می‌شود (.btn_3a9f) تا استایل یک کارت هرگز استایل دکمه دیگر را در کل برنامه خراب نکند.",
        "real": "طراحی رابط کاربری ادمین بدون دغدغه تداخل رنگ‌ها و ابعاد بین صفحات مختلف.",
        "code": "/* Product.module.css */\n.title { color: #38bdf8; font-weight: bold; }\n\n// Product.jsx\nimport styles from './Product.module.css';\nfunction Product({ name }) {\n  return <h2 className={styles.title}>{name}</h2>;\n}"
    },
    {
        "id": 12,
        "title": "فرگمنت (<>...</> یا React.Fragment)",
        "level": "مبتدی",
        "what": "تگ نامرئی برای بسته‌بندی چند المان در کنار هم بدون اینکه یک <div> اضافی و بی‌خاصیت در صفحه HTML ساخته شود.",
        "does": "جلوگیری از خراب شدن ساختارهای حساسی مثل فلکس‌باکس، گرید یا سلول‌های جدول (<td>) با دیوهای اضافه.",
        "real": "بازگرداندن چند سلول جدول از داخل یک کامپوننت فرزند بدون شکستن تگ <tr>.",
        "code": "function TableCells({ label, value }) {\n  return (\n    <>\n      <td className=\"font-bold\">{label}</td>\n      <td>{value}</td>\n    </>\n  );\n}"
    },
    {
        "id": 13,
        "title": "کامپوننت‌های کنترل‌شده در فرم‌ها (Controlled Components)",
        "level": "مبتدی",
        "what": "اینپوت‌هایی که مقدارشان (value) مستقیماً توسط استیت ری‌اکت کنترل می‌شود و با رویداد onChange هماهنگ می‌ماند.",
        "does": "ری‌اکت منبع واحد حقیقت (Single Source of Truth) فرم می‌شود؛ اعتبارسنجی کاراکتر به کاراکتر، ماسک کردن شماره کارت و قفل کردن حروف نامعتبر در صدم ثانیه.",
        "real": "فرم ورود شماره شبا که اجازه تایپ حروف فارسی را در لحظه مسدود می‌کند.",
        "code": "function SearchInput() {\n  const [query, setQuery] = useState('');\n  \n  return (\n    <input\n      type=\"text\"\n      value={query}\n      onChange={(e) => setQuery(e.target.value.toLowerCase())}\n      placeholder=\"جستجو در کالاها...\"\n    />\n  );\n}"
    },
    {
        "id": 14,
        "title": "چرخه حیات و عوارض جانبی با هوک useEffect",
        "level": "متوسط",
        "what": "مدیریت ساید‌افکت‌ها (دریافت داده از سرور، تایمرها، تغییر عنوان تب مرورگر، و ارتباط با APIهای خارجی).",
        "does": "آرایه وابستگی ([]): خالی باشد فقط هنگام لود اولیه (Mount) اجرا می‌شود؛ متغیر داشته باشد با تغییر آن متغیر رندر می‌شود؛ تابع بازگشتی (Cleanup) هنگام خارج شدن کامپوننت برای بستن سوکت و تایمر اجرا می‌شود.",
        "real": "دریافت اطلاعات محصول از سرور هنگام لود صفحه و تغییر عنوان تب مرورگر به نام محصول.",
        "code": "import { useState, useEffect } from 'react';\n\nfunction ProductDetails({ productId }) {\n  const [data, setData] = useState(null);\n\n  useEffect(() => {\n    let isMounted = true;\n    fetch(`/api/products/${productId}`)\n      .then(res => res.json())\n      .then(prod => {\n        if (isMounted) setData(prod);\n      });\n\n    return () => { isMounted = false; }; // پاکسازی مانع مموری لیک\n  }, [productId]); // هر بار productId عوض شد دوباره دیتا بگیر\n\n  return data ? <h2>{data.title}</h2> : <p>در حال بارگذاری...</p>;\n}"
    },
    {
        "id": 15,
        "title": "بالا کشیدن وضعیت (Lifting State Up)",
        "level": "متوسط",
        "what": "منتقل کردن استیت مشترک از کامپوننت‌های فرزند به نزدیک‌ترین والد مشترک آن‌ها.",
        "does": "زمانی که دو کامپوننت برادر نیاز دارند داده‌های هم را بدانند (مثلاً فیلتر جستجو در سایدبار و لیست محصولات در صفحه)، استیت باید به کامپوننت پدر برود.",
        "real": "هماهنگ کردن اینپوت سرچ در هدر سایت با کارت‌های نمایش داده در بدنه صفحه.",
        "code": "function ParentShop() {\n  const [search, setSearch] = useState('');\n  return (\n    <div>\n      <SearchBar value={search} onChange={setSearch} />\n      <ProductGrid query={search} />\n    </div>\n  );\n}"
    },
    {
        "id": 16,
        "title": "مشکل پاس دادن عمیق پراپ‌ها (Props Drilling)",
        "level": "متوسط",
        "what": "پاس دادن خسته‌کننده یک پراپ از میان ۵ لایه کامپوننت میانی که خودشان هیچ نیازی به آن دیتا ندارند فقط برای اینکه به دست فرزند عمیق برسد.",
        "does": "کد را به شدت شکننده و نگهداری را سخت می‌کند؛ راه حل آن استفاده از Context API، ترکیب کامپوننت‌ها یا استیت منیجرهاست.",
        "real": "پاس دادن اطلاعات کاربر لاگین کرده از کامپوننت App به Layout سپس Header و در نهایت Avatar.",
        "code": "// مشکل Props Drilling:\n// <App user={user}><Layout user={user}><Nav user={user}><UserMenu user={user} /></Nav></Layout></App>\n// راهکار مدرن: استفاده از useContext"
    },
    {
        "id": 17,
        "title": "دسترسی به المان‌های واقعی و هوک useRef",
        "level": "متوسط",
        "what": "نگهداری یک رفرنس به تگ واقعی DOM در صفحه، یا ذخیره مقداری که با تغییر آن کامپوننت ری‌رندر نشود.",
        "does": "بر خلاف useState، تغییر مقدار ref.current هیچ رندری به دنبال ندارد؛ عالی برای فوکوس دادن به اینپوت، اندازه‌گیری اسکرول، یا نگه داشتن شناسه تایمر.",
        "real": "فوکوس خودکار روی اینپوت کد پیامکی به محض باز شدن صفحه مودال.",
        "code": "import { useRef, useEffect } from 'react';\n\nfunction OtpModal() {\n  const inputRef = useRef(null);\n  \n  useEffect(() => {\n    inputRef.current?.focus(); // فوکوس خودکار بدون نیاز به کد DOM سنتی\n  }, []);\n\n  return <input ref={inputRef} placeholder=\"کد ۴ رقمی پیامک را وارد کنید\" />;\n}"
    },
    {
        "id": 18,
        "title": "مدیریت وضعیت سراسری با کانتکست (Context API & useContext)",
        "level": "متوسط",
        "what": "مکانیسم بومی ری‌اکت برای ارسال اطلاعات به کل درخت کامپوننت‌ها بدون نیاز به Props Drilling.",
        "does": "ساخت یک فرستنده مرکزی (Provider) برای اطلاعات عمومی مثل تم فعال، زبان (فارسی/انگلیسی)، یا وضعیت احراز هویت کاربر.",
        "real": "تغییر تم کل نرم‌افزار به حالت دارک از هر گوشه برنامه با یک دستور.",
        "code": "import { createContext, useContext, useState } from 'react';\n\nconst ThemeContext = createContext();\n\nexport function ThemeProvider({ children }) {\n  const [theme, setTheme] = useState('dark');\n  return (\n    <ThemeContext.Provider value={{ theme, toggle: () => setTheme(t => t === 'dark' ? 'light' : 'dark') }}>\n      {children}\n    </ThemeContext.Provider>\n  );\n}\n\n// در هر کامپوننت فرزند:\nexport const useTheme = () => useContext(ThemeContext);"
    },
    {
        "id": 19,
        "title": "مدیریت استیت‌های پیچیده با هوک useReducer",
        "level": "متوسط",
        "what": "جایگزین ساختاریافته‌تر برای useState در فرم‌ها یا استیت‌های با منطق پیچیده بر مبنای الگوی ریداکس (Action, Reducer, Dispatch).",
        "does": "متمرکز کردن تمام منطق‌های تغییر وضعیت در یک تابع خالص Reducer؛ از بی‌نظمی چندتا useState در یک فرم بزرگ جلوگیری می‌کند.",
        "real": "مدیریت سبد خرید شامل اضافه کردن کالا، حذف، تغییر تعداد، و خالی کردن سبد.",
        "code": "import { useReducer } from 'react';\n\nfunction cartReducer(state, action) {\n  switch (action.type) {\n    case 'ADD_ITEM': return [...state, action.payload];\n    case 'REMOVE_ITEM': return state.filter(i => i.id !== action.payload);\n    case 'CLEAR': return [];\n    default: return state;\n  }\n}\n// const [cart, dispatch] = useReducer(cartReducer, []);\n// dispatch({ type: 'ADD_ITEM', payload: { id: 1, title: 'کتاب' } });"
    },
    {
        "id": 20,
        "title": "هوک‌های سفارشی (Custom Hooks)",
        "level": "متوسط",
        "what": "توابعی که نامشان با use شروع می‌شود و به شما اجازه می‌دهند منطق تکراری هوک‌ها را بسته‌بندی و در چندین کامپوننت استفاده کنید.",
        "does": "تفکیک کامل منطق محاسباتی و فرانت‌اند از لایه دیداری JSX؛ بالا بردن تمیزی و تست‌پذیری کد.",
        "real": "ساخت هوک useFetch یا useLocalStorage برای ذخیره اتوماتیک استیت در دیسک.",
        "code": "import { useState, useEffect } from 'react';\n\nfunction useWindowSize() {\n  const [size, setSize] = useState({ width: window.innerWidth, height: window.innerHeight });\n  useEffect(() => {\n    const onResize = () => setSize({ width: window.innerWidth, height: window.innerHeight });\n    window.addEventListener('resize', onResize);\n    return () => window.removeEventListener('resize', onResize);\n  }, []);\n  return size;\n}\n// استفاده: const { width } = useWindowSize();"
    }
]

print("React Module 1 (1-20) Loaded:", len(REACT_TOPICS_1))
