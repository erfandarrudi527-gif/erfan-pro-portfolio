# -*- coding: utf-8 -*-
# Topics 43-65 (React 19, Architecture, Next.js & Deployment)

REACT_TOPICS_3 = [
    {
        "id": 43,
        "title": "تقسیم کد و لود تنبل کامپوننت‌ها (Code Splitting: React.lazy & Suspense)",
        "level": "پیشرفته",
        "what": "تکه‌تکه کردن باندل حجیم جاوا اسکریپت اپلیکیشن و دانلود کامپوننت‌های سنگین فقط زمانی که کاربر به آن صفحه می‌رود.",
        "does": "کاهش حجم لود اولیه سایت از ۳ مگابایت به ۱۰۰ کیلوبایت؛ تا زمان دانلود کامپوننت، تگ <Suspense> یک اسپینر لودینگ نشان می‌دهد.",
        "real": "دانلود ماژول رسم نمودار داشبورد فقط وقتی که کاربر روی تب «آمار و نمودار» کلیک کرد.",
        "code": "import { lazy, Suspense } from 'react';\n\nconst HeavyChart = lazy(() => import('./HeavyChart'));\n\nfunction Dashboard() {\n  return (\n    <Suspense fallback={<div>در حال بارگذاری ماژول نمودار...</div>}>\n      <HeavyChart />\n    </Suspense>\n  );\n}"
    },
    {
        "id": 44,
        "title": "مجازی‌سازی لیست‌های غول‌پیکر (Virtualization با react-window)",
        "level": "پیشرفته",
        "what": "رندر کردن فقط و فقط همان ۱۰ ردیفی که کاربر در صفحه نمایشگر می‌بیند، حتی اگر دیتابیس ۱۰ هزار کالا داشته باشد.",
        "does": "جلوگیری از هنگ کردن و ترکیدن رم مرورگر؛ با اسکرول کاربر، سطرهای جدید ساخته شده و سطرهای خارج از کادر از بین می‌روند.",
        "real": "نمایش لیست بی‌پایان مخاطبین تلفن، تراکنش‌ها یا پست‌های اکسپلور.",
        "code": "import { FixedSizeList as List } from 'react-window';\n\nfunction VirtualList({ items }) {\n  return (\n    <List height={500} itemCount={items.length} itemSize={45} width=\"100%\">\n      {({ index, style }) => <div style={style}>آیتم شماره {items[index].id}</div>}\n    </List>\n  );\n}"
    },
    {
        "id": 45,
        "title": "ویژگی‌های هم‌روند و اولویت‌بندی رندر (useTransition و useDeferredValue)",
        "level": "پیشرفته",
        "what": "علامت‌گذاری رندرهای غیرضروری به عنوان اولویت پایین (Transition) تا تایپ کیبورد کاربر هرگز دچار لگ نشود.",
        "does": "تایپ کردن در اینپوت با اولویت آنی اجرا می‌شود، اما فیلتر کردن ۱۰۰۰ کارت سنگین زیر آن در پس‌زمینه با وقفه سبک پردازش می‌شود.",
        "real": "جستجوی زنده در بین هزاران محصول بدون افت فریم تایپ کیبورد.",
        "code": "import { useState, useTransition } from 'react';\n\nfunction SearchPage() {\n  const [isPending, startTransition] = useTransition();\n  const [query, setQuery] = useState('');\n  \n  const handleChange = (e) => {\n    // تایپ فوری\n    const val = e.target.value;\n    // فیلترینگ با اولویت پایین در پس‌زمینه\n    startTransition(() => {\n      setFilter(val);\n    });\n  };\n}"
    },
    {
        "id": 46,
        "title": "سوسپنس برای دریافت داده (Suspense for Data Fetching)",
        "level": "پیشرفته",
        "what": "هماهنگی لودینگ داده‌ها با درخت بصری ری‌اکت بدون نیاز به چک کردن شرط if (isLoading).",
        "does": "کامپوننت به محض نیاز به دیتا یک پرامیس پرتاب می‌کند و سوسپنس والد تا زمان آماده شدن داده اسپینر لودینگ را نگه می‌دارد.",
        "real": "لودینگ مستقل سایدبار، هدر و جدول داده‌ها به صورت مجزا در داشبورد.",
        "code": "<Suspense fallback={<HeaderSkeleton />}>\n  <UserProfile />\n</Suspense>"
    },
    {
        "id": 47,
        "title": "قابلیت‌های انقلابی React 19 (use, useActionState, useOptimistic, useFormStatus)",
        "level": "پیشرفته",
        "what": "نسخه جدید ری‌اکت ۱۹ با اکشن‌های فرم غیرهمگام بومی، هوک جادویی use برای خواندن مستقیم پرامیس در بدنه کامپوننت، و آپدیت خوش‌بینانه رابط کاربری.",
        "does": "با useOptimistic قبل از اینکه پاسخ سرور بیاید، لایک یا پیام جدید روی صفحه ظاهر می‌شود تا حس سرعت ماورایی به کاربر دست دهد و در صورت خطا خودکار برگردانده شود.",
        "real": "ارسال لایک و کامنت در اینستاگرام و توییتر بدون معطلی صدم ثانیه‌ای.",
        "code": "// در React 19:\nimport { useOptimistic } from 'react';\n\nfunction LikeButton({ currentLikes, onLike }) {\n  const [optimisticLikes, setOptimisticLikes] = useOptimistic(\n    currentLikes,\n    (state, update) => state + 1\n  );\n  // کاربر در جا عدد جدید را می‌بیند حتی قبل از بازگشت پاسخ سرور!\n}"
    },
    {
        "id": 48,
        "title": "کامپوننت‌های سروری و کلاینتی (RSC: Server vs Client Components)",
        "level": "پیشرفته",
        "what": "تفکیک کامپوننت‌ها به دو دسته: آن‌هایی که فقط در سرور اجرا شده و هیچ کد جاوا اسکریپتی برای مرورگر کاربر نمی‌فرستند (Server) و آن‌هایی که با دستور 'use client' تعاملی هستند.",
        "does": "کاهش حجم باندل فرانت‌اند تا بیش از ۷۰٪، افزایش چشمگیر سرعت لود در گوشی‌های ضعیف، و دسترسی مستقیم و امن به دیتابیس بدون لو رفتن پسوردها.",
        "real": "خواندن مستقیم دیتابیس در کامپوننت سروری بدون نیاز به نوشتن مسیر API مجزا.",
        "code": "// Server Component (پیش‌فرض در نکست):\nasync function ProductPage({ id }) {\n  const product = await db.query('SELECT * FROM products WHERE id = ?', [id]);\n  return <h1>{product.name}</h1>;\n}"
    },
    {
        "id": 49,
        "title": "استراتژی‌های رندرینگ وب (CSR vs SSR vs SSG vs ISR)",
        "level": "پیشرفته",
        "what": "محل و زمان تبدیل کدهای ری‌اکت به HTML واقعی: کلاینت (CSR)، لحظه‌ای در سرور (SSR)، زمان بیلد پروژه (SSG)، و بازتولید دوره‌ای در پس‌زمینه (ISR).",
        "does": "سئو عالی در گوگل با SSR/SSG، و کش با سرعت سرور ابری CDN بدون نیاز به رندر تکراری در ISR.",
        "real": "صفحه اول و مقالات با SSG و ISR؛ پنل کاربری خصوصی با CSR.",
        "code": "// ISR در Next.js: بازتولید هر ۶۰ ثانیه در پس‌زمینه\n// export const revalidate = 60;"
    },
    {
        "id": 50,
        "title": "فریمورک Next.js و معماری App Router",
        "level": "پیشرفته",
        "what": "فریمورک فول‌استک ری‌اکت استاندارد صنعت نرم‌افزار بر پایه سیستم فایل‌محور App Router.",
        "does": "ارائه مسیردهی بر اساس پوشه‌ها (page.js, layout.js, loading.js)، توابع سرور اکشن برای ثبت فرم در دیتابیس، میدل‌ورهای امنیتی و بهینه‌سازی خودکار فونت و عکس.",
        "real": "توسعه وب‌سایت‌های مقیاس‌پذیر سازمانی دیجی‌کالا، اسنپ و علی‌بابا.",
        "code": "// app/blog/[slug]/page.jsx\nexport default async function BlogPost({ params }) {\n  const { slug } = await params;\n  return <article>مقاله شماره: {slug}</article>;\n}"
    },
    {
        "id": 51,
        "title": "فریمورک‌های مدرن جایگزین (Remix و TanStack Start)",
        "level": "پیشرفته",
        "what": "فریمورک‌های وب مدرن متمرکز بر وب استانداردهای وب بومی مرورگرها (Request, Response, Form actions).",
        "does": "حذف رفتارهای پیچیده کشینگ اختصاصی و سادگی خارق‌العاده با لودرها (Loaders) و اکشن‌ها (Actions).",
        "real": "ساخت داشبوردهای تجاری سنگین با لود سریع فرم‌ها حتی هنگام قطعی موقت شبکه.",
        "code": "// export async function loader() { return fetchUserData(); }"
    },
    {
        "id": 52,
        "title": "تایپ‌اسکریپت در ری‌اکت (TypeScript with React)",
        "level": "پیشرفته",
        "what": "تایپ‌گذاری دقیق پراپ‌ها، هوک‌ها، رویدادها و وضعیت‌ها (React.FC, ComponentProps, ReactNode).",
        "does": "اگر پراپ اجباری را به کامپوننت ندهید یا نوع آن غلط باشد، ادیتور در لحظه خطا می‌دهد و مانع از شکستن کد در دست مشتری می‌شود.",
        "real": "توسعه در تیم‌های ۵۰ نفره بدون ترس از خراب شدن کدهای بقیه اعضا.",
        "code": "type ButtonProps = {\n  label: string;\n  variant?: 'primary' | 'danger';\n  onClick: (e: React.MouseEvent<HTMLButtonElement>) => void;\n};\nfunction SafeButton({ label, variant = 'primary', onClick }: ButtonProps) {\n  return <button onClick={onClick}>{label}</button>;\n}"
    },
    {
        "id": 53,
        "title": "تست‌نویسی کامپوننت‌ها (React Testing Library, Vitest, Playwright)",
        "level": "پیشرفته",
        "what": "آزمون خودکار رفتار رابط کاربری دقیقاً همان‌گونه که یک کاربر واقعی با آن تعامل می‌کند.",
        "does": "تست کلیک روی دکمه، پر کردن اینپوت و اطمینان از اینکه بعد از ثبت، پیام موفقیت در صفحه رندر می‌شود.",
        "real": "تست درگاه پرداخت و افزودن به سبد خرید قبل از ارسال کد به گیت‌هاب.",
        "code": "import { render, screen, fireEvent } from '@testing-library/react';\ntest('افزایش شمارنده با کلیک', () => {\n  render(<Counter />);\n  fireEvent.click(screen.getByText('+'));\n  expect(screen.getByText('2')).toBeInTheDocument();\n});"
    },
    {
        "id": 54,
        "title": "کارگاه طراحی مجزای کامپوننت‌ها با Storybook",
        "level": "پیشرفته",
        "what": "محیط توسعه ایزوله برای ساخت و آزمایش کامپوننت‌های UI بدون نیاز به بالا آوردن کل بک‌اند و دیتابیس.",
        "does": "تیم دیزاین و فرانت‌اند تمام حالات دکمه، کارت، و جدول را در حالت‌های لودینگ، ارور و غیرفعال بررسی و داکیومنت می‌کنند.",
        "real": "سیستم دیزاین سیستم اسنپ یا تپسی برای اشتراک قطعات بین تمام تیم‌ها.",
        "code": "// Button.stories.jsx\nexport default { title: 'Components/Button' };\nexport const Primary = { args: { label: 'تایید', variant: 'primary' } };"
    },
    {
        "id": 55,
        "title": "دسترسی‌پذیری در ری‌اکت (Accessibility: a11y & ARIA)",
        "level": "پیشرفته",
        "what": "اطمینان از اینکه افراد کم‌بینا یا معلول با صفحه‌خوان و کیبورد بتوانند به راحتی از اپلیکیشن استفاده کنند.",
        "does": "استفاده از تگ‌های استاندارد، مدیریت فوکوس کیبورد در مودال‌ها (Focus Trap) و صفات aria-expanded در منوها.",
        "real": "رعایت استانداردهای بین‌المللی دولتی و حقوقی در وب‌سایت‌های بانکی و خدماتی.",
        "code": "<button aria-expanded={isOpen} aria-controls=\"menu-list\" onClick={toggleMenu}>\n  منو\n</button>"
    },
    {
        "id": 56,
        "title": "چندزبانه کردن اپلیکیشن (Internationalization: i18n & react-i18next)",
        "level": "پیشرفته",
        "what": "ترجمه پویا و تغییر خودکار جهت صفحه (RTL برای فارسی و LTR برای انگلیسی).",
        "does": "کاربر با یک کلیک زبان را از فارسی به انگلیسی تغییر می‌دهد و تمام متون، فرمت تاریخ‌ها، و ارقام به شکل استاندارد عوض می‌شوند.",
        "real": "سامانه‌های بین‌المللی فروشگاهی و شرکتی دو زبانه.",
        "code": "import { useTranslation } from 'react-i18next';\nfunction Welcome() {\n  const { t } = useTranslation();\n  return <h1>{t('welcome_message')}</h1>;\n}"
    },
    {
        "id": 57,
        "title": "انیمیشن‌های مدرن در ری‌اکت (Framer Motion)",
        "level": "پیشرفته",
        "what": "بهترین کتابخانه انیمیشن برای ری‌اکت با سینتکس اعلانی بر پایه motion.div.",
        "does": "انیمیشن ورود و خروج نرم کامپوننت‌ها (AnimatePresence)، انیمیشن‌های ژستی هاور و درگ، و اسکرول تعاملی با فریم‌ریت ۶۰ بر ثانیه.",
        "real": "باز و بسته شدن روان منوی کشویی موبایل و کارت‌های تعاملی.",
        "code": "import { motion } from 'framer-motion';\n<motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.3 }}>\n  محتوای متحرک و نرم\n</motion.div>"
    },
    {
        "id": 58,
        "title": "میکروفرانت‌اندها در ری‌اکت (Micro Frontends & Module Federation)",
        "level": "پیشرفته",
        "what": "شکستن یک وب‌اپلیکیشن عظیم به چند اپلیکیشن کوچک مستقل که توسط تیم‌های جداگانه توسعه داده می‌شوند.",
        "does": "تیم پرداخت کد خودش را دپلوید می‌کند بدون اینکه به تیم پروفایل یا تیم چت آسیبی برسد؛ ترکیب آن‌ها در مرورگر با Webpack Module Federation رخ می‌دهد.",
        "real": "معماری مقیاس فوق‌بزرگ در سازمان‌هایی مثل دیجی‌کالا یا علی‌بابا.",
        "code": "// بارگذاری اپلیکیشن پرداخت درون پورتال اصلی در زمان اجرا"
    },
    {
        "id": 59,
        "title": "مدیریت چندپروژه‌ای (Monorepo با Turborepo یا Nx)",
        "level": "پیشرفته",
        "what": "نگهداری سایت، اپ موبایل، پنل ادمین، و پکیج کامپوننت‌های مشترک در یک مخزن واحد گیت (Git Repo).",
        "does": "اشتراک‌گذاری کدها و مدل‌های تایپ‌اسکریپت بین پنل‌ها بدون نیاز به پابلیش مکرر در npm و اجرای فوق سریع بیلدها با کش توربو.",
        "real": "پروژه‌های بزرگ که پنل ادمین، لندینگ پیج و اپلیکیشن اصلی با یک دیزاین‌سیستم کار می‌کنند.",
        "code": "// turbo.json برای زمان‌بندی پایپ‌لاین بیلد و کش خودکار"
    },
    {
        "id": 60,
        "title": "معماری تمیز و پوشه‌بندی ویژگی‌محور (Feature-Sliced Design)",
        "level": "پیشرفته",
        "what": "ساختاربندی پوشه‌های پروژه بر مبنای فیچرها (features/auth, features/cart) به جای دسته‌بندی ابتدایی (components, pages).",
        "does": "نگهداری پروژه‌های چند ده‌هزار خطی را بسیار منظم می‌کند؛ حذف یک ویژگی به سادگی پاک کردن همان یک فولدر فیچر است بدون باقی ماندن کدهای زائد.",
        "real": "استاندارد پوشه‌بندی در تمام پروژه‌های بزرگ صنعتی روز دنیا.",
        "code": "src/\n├── features/cart/     # کامپوننت‌ها، هوک‌ها و استیت مخصوص سبد خرید\n├── features/auth/     # کامپوننت‌ها و لاگین\n├── shared/ui/         # دکمه‌ها و کدهای اشتراکی"
    },
    {
        "id": 61,
        "title": "الگوهای طراحی اختصاصی در ری‌اکت (React Design Patterns)",
        "level": "پیشرفته",
        "what": "پترن‌های اثبات‌شده مثل Container/Presentational (جداسازی منطق داده از لایه دیداری) و Custom Hooks Factory.",
        "does": "کامپوننت‌های ظاهری احمق و خالص (Dumb Components) فقط برای رندر باقی می‌مانند و تست‌پذیری به ۱۰۰٪ می‌رسد.",
        "real": "توسعه ماژولار بخش نمایش مشخصات فاکتور و پرداخت.",
        "code": "// Container دیتا می‌گیرد و Presentational فقط رندر می‌کند"
    },
    {
        "id": 62,
        "title": "سنجه‌های حیاتی وب و بهینه‌سازی سئو (Core Web Vitals & SEO)",
        "level": "پیشرفته",
        "what": "بهینه‌سازی معیارهای LCP (سرعت نمایش محتوای اصلی)، CLS (پایداری چیدمان بدون پرش ناگهانی)، و INP (تاخیر پاسخگویی به کلیک).",
        "does": "افزایش رتبه در گوگل، جلوگیری از پرش المان‌ها حین لود بنرها، و کاهش نرخ پرش کاربران (Bounce Rate).",
        "real": "رساندن نمره لایت‌هاوس سایت به ۱۰۰ سبز برای ورودی ارگانیک از سرچ گوگل.",
        "code": "// تعیین ابعاد دقیق عکس و فونت برای صفر کردن پرش (CLS = 0)"
    },
    {
        "id": 63,
        "title": "اپلیکیشن‌های پیش‌رونده وب در ری‌اکت (PWA: Progressive Web Apps)",
        "level": "پیشرفته",
        "what": "تبدیل سایت ری‌اکت به یک اپلیکیشن قابل نصب در موبایل و دسکتاپ با آیکون اختصاصی و کارکرد کاملاً آفلاین.",
        "does": "با داشتن فایل manifest.json و یک Service Worker هوشمند، کاربر سایت را مثل برنامه بومی نصب می‌کند و پیام‌های نوتیفیکیشن فشاری (Push Notification) می‌گیرد.",
        "real": "نسخه وب‌اپلیکیشن اسنپ، دیجی‌کالا و تلگرام بدون نیاز به نصب از اپ‌استورها.",
        "code": "// manifest.json شامل آیکون، رنگ تم و آدرس لود اولیه آفلاین"
    },
    {
        "id": 64,
        "title": "آشنایی با توسعه موبایل با React Native",
        "level": "پیشرفته",
        "what": "فریمورک ساخت نرم‌افزارهای نیتیو اندروید و iOS با استفاده از همان کدهای ری‌اکت و جاوا اسکریپت.",
        "does": "به جای <div> از <View> و به جای <p> از <Text> استفاده می‌شود که مستقیماً به ویجت‌های بومی کاتلین و سوئیفت در موبایل کامپایل می‌شوند.",
        "real": "ساخت نسخه اندروید و آیفون با یک بار کدنویسی مشترک با وب.",
        "code": "import { View, Text, StyleSheet } from 'react-native';\nexport default function App() {\n  return (\n    <View style={styles.container}>\n      <Text>سلام از دل اپلیکیشن موبایل نیتیو!</Text>\n    </View>\n  );\n}"
    },
    {
        "id": 65,
        "title": "یکپارچه‌سازی و دپلویمنت مداوم (CI/CD, Docker & Vercel/Netlify)",
        "level": "پیشرفته",
        "what": "فرآیند انتشار خودکار نرم‌افزار با هر بار Push کردن به گیت‌هاب.",
        "does": "تست‌ها خودکار در GitHub Actions اجرا می‌شوند، ایمیج Docker ساخته می‌شود و سایت در چند ثانیه روی Vercel یا سرور ابری لایو بالا می‌آید.",
        "real": "انتشار سریع آپدیت‌های محصول در شرکت‌ها بدون دخالت دستی و بدون قطعی سرور (Zero Downtime).",
        "code": "# نمونه گام بیلد در داکر\n# FROM node:alpine AS build\n# RUN npm run build"
    }
]

print("React Module 3 (43-65) Loaded:", len(REACT_TOPICS_3))
