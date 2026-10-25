# -*- coding: utf-8 -*-
# Topics 21-42 (React Intermediate & Advanced Architecture)

REACT_TOPICS_2 = [
    {
        "id": 21,
        "title": "مسیریابی در ری‌اکت (React Router v6: Routes, Link, Params, Protected Routes)",
        "level": "متوسط",
        "what": "کتابخانه استاندارد مسیریابی چندصفحه‌ای در اپلیکیشن‌های تک‌صفحه‌ای (SPA) بدون رفرش صفحه.",
        "does": "آدرس مرورگر را تغییر می‌دهد و کامپوننت متناظر را رندر می‌کند. پارامترهای پویا مثل /products/:id را با useParams می‌خواند و صفحات محافظت‌شده (Protected Routes) برای کاربران لاگین‌کرده می‌سازد.",
        "real": "هدایت کاربر به صفحه محصول یا مسدود کردن دسترسی مهمان به صفحه سفارشات من.",
        "code": "import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';\n\nfunction ProtectedRoute({ isAuth, children }) {\n  return isAuth ? children : <Navigate to=\"/login\" replace />;\n}\n// <Route path=\"/dashboard\" element={<ProtectedRoute isAuth={user.isLoggedIn}><Dashboard /></ProtectedRoute>} />"
    },
    {
        "id": 22,
        "title": "دریافت داده از سرور در کامپوننت (Data Fetching با fetch یا axios)",
        "level": "متوسط",
        "what": "برقراری ارتباط با APIهای RESTful درون چرخه هوک useEffect.",
        "does": "درخواست به سرور فرستاده می‌شود و پس از دریافت پاسخ، استیت به‌روزرسانی شده و رابط کاربری کارت‌ها را رندر می‌کند.",
        "real": "گرفتن لیست ۵۰ دوره آموزشی جدید از وب‌سرویس بک‌اند.",
        "code": "useEffect(() => {\n  const fetchCourses = async () => {\n    const res = await fetch('https://api.site.ir/courses');\n    const data = await res.json();\n    setCourses(data);\n  };\n  fetchCourses();\n}, []);"
    },
    {
        "id": 23,
        "title": "مدیریت وضعیت‌های لودینگ و خطا (Loading & Error States)",
        "level": "متوسط",
        "what": "سه وضعیت استاندارد هر عملیات شبکه: ۱. در حال بارگذاری (Loading) ۲. موفقیت (Success) ۳. وقوع خطا (Error).",
        "does": "جلوگیری از سفید ماندن صفحه یا گیج شدن کاربر؛ نمایش اسکلتون لودینگ (Skeleton) یا پیام خطای قطعی اینترنت همراه با دکمه تلاش مجدد.",
        "real": "نمایش اسکلتون‌های خاکستری شبیه کارت کالا در دیجی‌کالا قبل از بارگذاری کامل عکس‌ها.",
        "code": "if (loading) return <div className=\"skeleton\">در حال بارگذاری اطلاعات...</div>;\nif (error) return <div className=\"error-banner\">خطا در برقراری ارتباط! <button onClick={retry}>تلاش دوباره</button></div>;\nreturn <ProductList data={data} />;"
    },
    {
        "id": 24,
        "title": "فرم‌های پیشرفته و اعتبارسنجی (React Hook Form + Zod)",
        "level": "متوسط",
        "what": "کتابخانه مدرن مدیریت فرم‌ها با حداقل ری‌رندر ممکن به همراه اسکیما ولیدیشن Zod.",
        "does": "فرم‌های با ۲۰ فیلد را بدون افت فریم پردازش می‌کند و قوانین اعتبارسنجی پیچیده (مثل تطابق تکرار رمز عبور یا فرمت شماره شبا) را با پیام خطای فارسی بررسی می‌کند.",
        "real": "فرم ثبت‌نام و افتتاح حساب آنلاین در سامانه‌های بانکی و صرافی‌ها.",
        "code": "import { useForm } from 'react-hook-form';\nimport { z } from 'zod';\nimport { zodResolver } from '@hookform/resolvers/zod';\n\nconst schema = z.object({\n  phone: z.string().regex(/^09\\d{9}$/, 'شماره موبایل نامعتبر است')\n});\n// const { register, handleSubmit, formState: { errors } } = useForm({ resolver: zodResolver(schema) });"
    },
    {
        "id": 25,
        "title": "کش کردن محاسبات سنگین با useMemo",
        "level": "متوسط",
        "what": "هوک بهینه‌سازی که نتیجه یک محاسبه سنگین ریاضی یا فیلترینگ آرایه را کش (Memoize) می‌کند.",
        "does": "تا زمانی که آرایه وابستگی تغییر نکند، ری‌اکت در ری‌رندرهای بعدی دوباره تابع سنگین را اجرا نمی‌کند و همان نتیجه ذخیره شده در رم را برمی‌گرداند.",
        "real": "فیلتر کردن و مرتب‌سازی لیست ۵۰۰۰ ردیف کالای انبار بر اساس قیمت و موجودی.",
        "code": "const filteredProducts = useMemo(() => {\n  console.log('محاسبه سنگین فیلترینگ انجام شد');\n  return products.filter(p => p.price <= maxPrice && p.title.includes(searchTerm));\n}, [products, maxPrice, searchTerm]);"
    },
    {
        "id": 26,
        "title": "تثبیت مرجع توابع با useCallback",
        "level": "متوسط",
        "what": "کش کردن نمونه تابع بین ری‌رندرها تا آدرس حافظه جدیدی نسازد.",
        "does": "در جاوا اسکریپت با هر رندر، توابع از نو متولد می‌شوند و آدرس جدید می‌گیرند؛ با useCallback آدرس تابع قفل می‌شود تا فرزندانی که React.memo دارند بیهوده ری‌رندر نشوند.",
        "real": "پاس دادن تابع حذف سطر به کامپوننت فرزند سنگین ردیف جدول.",
        "code": "const handleDelete = useCallback((id) => {\n  setItems(prev => prev.filter(item => item.id !== id));\n}, []); // مرجع تابع ثابت می‌ماند"
    },
    {
        "id": 27,
        "title": "جلوگیری از ری‌رندرهای زائد کامپوننت با React.memo",
        "level": "متوسط",
        "what": "کامپوننت مرتبه بالا (HOC) که پراپ‌های قبلی و جدید را مقایسه سطحی (Shallow Compare) می‌کند.",
        "does": "اگر والد ری‌رندر شد اما پراپ‌های این فرزند تغییری نکرده باشند، فرزند از رندر معاف می‌شود و مصرف پردازنده به شدت کاهش می‌یابد.",
        "real": "کارت‌های یک گرید بزرگ محصولات که قیمت و اطلاعاتشان دست نخورده است.",
        "code": "import React from 'react';\n\nconst ProductItem = React.memo(function ProductItem({ title, price }) {\n  console.log(`رندر شد: ${title}`);\n  return <div>{title} - {price} تومان</div>;\n});"
    },
    {
        "id": 28,
        "title": "همگام‌سازی بلافاصله قبل از نقاشی با useLayoutEffect",
        "level": "متوسط",
        "what": "مشابه useEffect با این تفاوت که به صورت همگام (Synchronous) دقیقا قبل از اینکه مرورگر صفحه را نقاشی کند (Paint) اجرا می‌شود.",
        "does": "جلوگیری از پرش تصویر (Flickering) هنگام اندازه‌گیری ابعاد المان در DOM یا انیمیشن‌های شروع موقعیت پاپ‌آپ.",
        "real": "محاسبه دقیق موقعیت تول‌تیپ بازشونده روی یک آیکون قبل از دیده شدن توسط کاربر.",
        "code": "useLayoutEffect(() => {\n  const { height } = ref.current.getBoundingClientRect();\n  setOffset(height + 10); // کاربر هرگز پرش و چشمک زدن تول‌تیپ را نمی‌بیند\n}, []);"
    },
    {
        "id": 29,
        "title": "الگوهای ترکیب کامپوننت (Component Composition)",
        "level": "متوسط",
        "what": "طراحی کامپوننت‌ها به سبک اسلات‌های آزاد به جای پاس دادن ده‌ها پراپ پیکربندی تو در تو.",
        "does": "انعطاف‌پذیری فوق‌العاده رابط کاربری بدون درگیر شدن در باتلاق Props Drilling.",
        "real": "طراحی سایدبار که می‌تواند در یک صفحه آیکون و در صفحه دیگر لیست منو داشته باشد.",
        "code": "function SplitPane({ left, right }) {\n  return (\n    <div className=\"split-layout\">\n      <aside className=\"sidebar\">{left}</aside>\n      <main className=\"content\">{right}</main>\n    </div>\n  );\n}"
    },
    {
        "id": 30,
        "title": "پورتال‌ها برای خروج از والد (React Portals)",
        "level": "متوسط",
        "what": "رندر کردن یک کامپوننت فرزند در یک گره DOM خارج از درخت والد اصلی با createPortal.",
        "does": "مودال‌ها و تول‌تیپ‌ها در تگ‌های والد دارای overflow: hidden یا z-index گیر می‌کنند و بریده می‌شوند؛ پورتال آن‌ها را مستقیماً داخل انتهای تگ <body> شلیک می‌کند.",
        "real": "پاپ‌آپ‌های تمام‌صفحه تایید پرداخت و درگاه بانکی.",
        "code": "import { createPortal } from 'react-dom';\n\nfunction GlobalModal({ children }) {\n  return createPortal(\n    <div className=\"fixed-overlay\">{children}</div>,\n    document.body // مستقیماً در بادی رندر می‌شود\n  );\n}"
    },
    {
        "id": 31,
        "title": "مرزهای خطا (Error Boundaries)",
        "level": "متوسط",
        "what": "سپر دفاعی کامپوننت برای شکار خطاهای جاوا اسکریپت در فرزندان و نمایش رابط کاربری پشتیبان (Fallback).",
        "does": "اگر یک کامپوننت فرعی (مثلاً ویجت آب و هوا) خطا دهد، کل سایت سفید نمی‌شود؛ بلکه فقط همان کادر پیام «این بخش موقتا در دسترس نیست» نشان می‌دهد و بقیه سایت کار می‌کند.",
        "real": "ایزوله کردن ویجت نظرات کاربران در صفحه خرید کالا.",
        "code": "class ErrorBoundary extends React.Component {\n  state = { hasError: false };\n  static getDerivedStateFromError() { return { hasError: true }; }\n  render() {\n    return this.state.hasError ? <h3>بخشی از صفحه دچار خطا شد!</h3> : this.props.children;\n  }\n}"
    },
    {
        "id": 32,
        "title": "مدیریت استیت سراسری (Redux Toolkit vs Zustand)",
        "level": "متوسط",
        "what": "انبارهای ذخیره‌سازی وضعیت سراسری اپلیکیشن خارج از درخت کامپوننت‌ها.",
        "does": "ریداکس تولکیت (RTK) استاندارد سازمانی است و ساختاریافته کار می‌کند؛ زاستند (Zustand) سبک‌ترین و محبوب‌ترین کتابخانه مدرن بدون کدهای تکراری اضافه و با هوک‌های مستقیم است.",
        "real": "نگهداری سبد خرید و توکن احراز هویت در تمام صفحات اپلیکیشن.",
        "code": "// Zustand Store ساده و تمیز\nimport { create } from 'zustand';\n\nexport const useCartStore = create((set) => ({\n  items: [],\n  addItem: (item) => set((state) => ({ items: [...state.items, item] })),\n  clearCart: () => set({ items: [] })\n}));\n// در کامپوننت: const { items, addItem } = useCartStore();"
    },
    {
        "id": 33,
        "title": "کتابخانه‌های دریافت داده مدرن (TanStack Query / React Query)",
        "level": "متوسط",
        "what": "پادشاه مدیریت دیتای سرور در فرانت‌اند؛ کش هوشمند، تلاش مجدد در صورت قطعی (Retry)، و به‌روزرسانی خودکار در پس‌زمینه.",
        "does": "جایگزین نوشتن دستی useEffect + useState برای فچینگ؛ داده‌ها را کش می‌کند، دکمه رفرش نمی‌خواهد و با بستن تب و برگشت به آن داده را تازه می‌کند.",
        "real": "کش کردن لیست قیمت طلا و ارز در صرافی آنلاین با امکان آپدیت هر ۱۰ ثانیه.",
        "code": "import { useQuery } from '@tanstack/react-query';\n\nfunction CryptoList() {\n  const { data, isLoading, error } = useQuery({\n    queryKey: ['cryptoPrices'],\n    queryFn: () => fetch('/api/prices').then(r => r.json()),\n    staleTime: 1000 * 30 // تا ۳۰ ثانیه معتبر و بدون درخواست اضافه\n  });\n}"
    },
    {
        "id": 34,
        "title": "کتابخانه‌های رابط کاربری (shadcn/ui, MUI, Ant Design)",
        "level": "متوسط",
        "what": "مجموعه قطعات پیش‌ساخته دکمه‌ها، جداول و فرم‌ها. shadcn/ui کد کامپوننت را مستقیماً داخل پروژه شما می‌کپی کند (مالکیت ۱۰۰٪ کد) با Radix UI و Tailwind.",
        "does": "افزایش ۱۰ برابری سرعت توسعه بدون نیاز به اختراع مجدد چرخ دکمه‌ها، دراپ‌داون‌ها و مودال‌های دسترس‌پذیر.",
        "real": "ساخت پنل مدیریت ادمین در چند روز با جداول مدرن و کامپوننت‌های آماده.",
        "code": "// استفاده از دکمه shadcn/ui\nimport { Button } from '@/components/ui/button';\n// <Button variant=\"destructive\" size=\"lg\">حذف رکورد</Button>"
    },
    {
        "id": 35,
        "title": "ترکیب Tailwind CSS و Styled-Components در ری‌اکت",
        "level": "متوسط",
        "what": "دو رویکرد محبوب استایل‌دهی: کلاس‌های کاربردی سرعتی Tailwind در برابر استایل‌های مبتنی بر متغیرهای جاوا اسکریپتی CSS-in-JS.",
        "does": "امکان استایل‌دهی شرطی بر اساس پراپ‌های کامپوننت؛ مثلاً رنگ دکمه متناسب با نوع نقش کاربر در سیستم تغییر کند.",
        "real": "دکمه‌های داینامیک که پراپ variant=\"success\" یا variant=\"danger\" می‌گیرند.",
        "code": "// دکمه منعطف با تیلویند و پکیج clsx / tailwind-merge\nfunction ActionBtn({ isPending, children }) {\n  return (\n    <button className={`px-4 py-2 rounded-xl font-bold transition ${\n      isPending ? 'bg-gray-700 cursor-not-allowed opacity-50' : 'bg-sky-500 hover:bg-sky-400'\n    }`}>\n      {children}\n    </button>\n  );\n}"
    },
    {
        "id": 36,
        "title": "حالت سخت‌گیرانه (React.StrictMode)",
        "level": "متوسط",
        "what": "ابزار کمکی زمان توسعه برای یافتن عوارض جانبی پیش‌بینی‌نشده، کدهای منسوخ و مموری‌لیک‌ها.",
        "does": "در محیط Development تمام کامپوننت‌ها و هوک‌های useEffect را عمداً ۲ بار رندر و اجرا می‌کند تا مطمئن شود توابع پاکسازی (Cleanup) به درستی نوشته شده‌اند.",
        "real": "یافتن تایمرهای رهاشده و باگ‌های حافظه قبل از دپلویمنت روی سرور واقعی.",
        "code": "// index.jsx\n<React.StrictMode>\n  <App />\n</React.StrictMode>"
    },
    {
        "id": 37,
        "title": "متغیرهای محیطی در ری‌اکت (Environment Variables: VITE_*)",
        "level": "متوسط",
        "what": "تنظیمات و آدرس‌های سرور که متناسب با محیط لوکال، تستی یا سرور اصلی تفاوت دارند (فایل‌های .env).",
        "does": "در Vite تمام متغیرها باید با پیشوند VITE_ شروع شوند و از طریق import.meta.env خوانده می‌شوند تا کلیدهای خصوصی به اشتباه وارد بیلد پابلیک نشوند.",
        "real": "تغییر خودکار آدرس سرور API از localhost:5000 به api.mydomain.ir حین انتشار.",
        "code": "# در فایل .env.production\nVITE_BACKEND_URL=https://api.site.com\n\n// در کدهای پروژه:\nconst API_BASE = import.meta.env.VITE_BACKEND_URL;"
    },
    {
        "id": 38,
        "title": "احراز هویت و نگهداری توکن (JWT Auth & Interceptors)",
        "level": "متوسط",
        "what": "جریان لاگین با توکن‌های JWT (شامل Access Token و Refresh Token) و هدایت کاربران به مسیرهای مجاز.",
        "does": "با ساخت Axios Interceptor، توکن به صورت خودکار به هدر Authorization تمام درخواست‌ها تزریق می‌شود و در صورت منقضی شدن توکن (ارور 401)، توکن جدید بی‌صدا درخواست می‌شود.",
        "real": "لاگین ماندن کاربر در اپلیکیشن حتی پس از بستن و باز کردن مجدد مرورگر.",
        "code": "// ارسال توکن در تمام ریکوئست‌ها\napiClient.interceptors.request.use((config) => {\n  const token = localStorage.getItem('access_token');\n  if (token) config.headers.Authorization = `Bearer ${token}`;\n  return config;\n});"
    },
    {
        "id": 39,
        "title": "هوک‌های شناسه و ارجاع پیشرفته (useId, forwardRef, useImperativeHandle)",
        "level": "پیشرفته",
        "what": "ابزارهای کنترل ارجاع و دسترسی‌پذیری. هوک useId شناسه‌های یکتای سازگار با رندر سمت سرور تولید می‌کند؛ forwardRef ارجاع ref را به کامپوننت فرزند پاس می‌دهد.",
        "does": "هوک useImperativeHandle به کامپوننت والد اجازه می‌دهد متدهای خاصی از فرزند را (مثل ریست کردن فرم فرزند یا اسکرول داخلی) صدا بزند بدون اینکه تمام DOM فرزند فاش شود.",
        "real": "طراحی کامپوننت پخش‌کننده ویدیو سفارشی که والد بتواند متد play() آن را کنترل کند.",
        "code": "const CustomInput = forwardRef((props, ref) => {\n  const id = useId();\n  return <div><label htmlFor={id}>نام:</label><input id={id} ref={ref} /></div>;\n});"
    },
    {
        "id": 40,
        "title": "الگوهای پیشرفته اشتراک‌گذاری منطق (HOC و Render Props)",
        "level": "پیشرفته",
        "what": "الگوهای طراحی قدیمی اما مهم برای اشتراک منطق بین کامپوننت‌ها قبل از آمدن هوک‌ها.",
        "does": "کامپوننت مرتبه بالا (HOC) کامپوننت دیگری را به عنوان ورودی می‌گیرد و آن را با قابلیت‌های اضافه (مثل اعتبارسنجی لاگین withAuth) بازمی‌گرداند.",
        "real": "قفل کردن دسترسی صفحات مختلف با پیچیدن کامپوننت در withAuth.",
        "code": "function withAuth(Component) {\n  return function AuthenticatedComponent(props) {\n    const isAuth = checkLogin();\n    return isAuth ? <Component {...props} /> : <Navigate to=\"/login\" />;\n  };\n}"
    },
    {
        "id": 41,
        "title": "الگوی کامپوننت‌های ترکیبی (Compound Components Pattern)",
        "level": "پیشرفته",
        "what": "طراحی کامپوننت‌های هماهنگ با هم شبیه تگ‌های استاندارد <select> و <option> HTML.",
        "does": "کامپوننت والد استیت اشتراکی را از طریق کانتکست داخلی به فرزندان می‌رساند بدون اینکه نیاز باشد کاربر دستی ده‌ها پراپ به تب‌ها یا آکاردئون‌ها پاس دهد.",
        "real": "ساخت تب‌بار مدرن به شکل <Tabs><Tab.List><Tab>۱</Tab></Tab.List><Tab.Panels>...</Tab.Panels></Tabs>.",
        "code": "// الگوی محبوب کتابخانه‌های حرفه‌ای مثل Headless UI و Radix"
    },
    {
        "id": 42,
        "title": "معماری فایبر و تطبیق درخت (Reconciliation & Fiber Architecture)",
        "level": "پیشرفته",
        "what": "موتور بازنویسی شده هسته داخلی ری‌اکت (React Fiber) که عملیات رندر را به کارهای کوچک قابل اولویت‌بندی و توقف تقسیم می‌کند.",
        "does": "دیگر رندر کردن صفحات سنگین رابط کاربری را فریز نمی‌کند؛ ری‌اکت می‌تواند در صورت فشردن یک دکمه توسط کاربر، رندر جاری را متوقف کرده و به تایپ کاربر اولویت فوری بدهد.",
        "real": "حفظ نرمی ۶۰ فریم بر ثانیه انیمیشن‌ها حین بارگذاری سنگین داده‌ها.",
        "code": "// ری‌اکت فایبر پشت صحنه کارها را در فاز Render (آسنکرون و بدون اثر روی DOM) و Commit (همگام روی DOM) انجام می‌دهد."
    }
]

print("React Module 2 (21-42) Loaded:", len(REACT_TOPICS_2))
