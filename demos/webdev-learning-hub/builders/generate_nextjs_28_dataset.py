# -*- coding: utf-8 -*-
"""
Generate the exhaustive 28-chapter specialist dataset for Next.js based on the user's complete syllabus.
"""
import os, sys, json

BASE_DIR = "C:/Users/erfan/Desktop/WebDev_Master_Learning_Hub"
PASTE_PATH = "C:/Users/erfan/AppData/Local/hermes/composer-pastes/pasted_content_2026-10-22_19-37-11-649_fc779d.txt"

with open(PASTE_PATH, "r", encoding="utf-8") as f:
    raw_text = f.read()

# 28 Chapters definition matching user's exact syllabus
CHAPTERS_DEF = [
    {
        "id": 1,
        "title": "مقدمه، فلسفه و معماری پایه Next.js",
        "sub": "Framework vs Library, Turbopack, Project Anatomy",
        "level": "مبتدی",
        "analogy": "مثل تفاوت خرید قطعات موتور (React) با خرید یک خودروی تسلای آماده مسابقه و تحویل در خیابان (Next.js).",
        "plain_exp": "نکست یک فریمورک کامل بر پایه ری‌اکت است که سرور رندرینگ، بیلد پرسرعت توربوپک و پکیجینگ را از صفر بدون ابزار جانبی مهیا می‌کند.",
        "real": "🏢 استارتاپ‌های بزرگ مثل دیجی‌کالا و علی‌بابا برای لود سریع و سئو از Next.js به جای React خام استفاده می‌کنند.",
        "code": """// package.json & next.config.ts
import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  reactStrictMode: true,
  experimental: {
    turbopack: true
  }
};
export default nextConfig;""",
        "interview": "تفاوت بنیادین Library با Framework چیست؟ در کتابخانه (React) شما کنترل جریان برنامه را دارید؛ در فریمورک (Next.js) معماری بر اساس قوانین فریمورک (Inversion of Control) هدایت می‌شود.",
        "sandbox": "<div class='p-3 bg-slate-900 text-sky-400 font-mono text-xs rounded'>npx create-next-app@latest my-app --typescript --tailwind --app</div>",
        "sol1": "npx create-next-app@latest ./ --typescript --eslint --tailwind --app",
        "sol2": "export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang='fa' dir='rtl'><body>{children}</body></html>; }",
        "sol3": "const nextConfig = { experimental: { turbopack: true }, images: { remotePatterns: [{ hostname: 'cdn.site.ir' }] } }; export default nextConfig;"
    },
    {
        "id": 2,
        "title": "سیستم مسیریابی فایل‌محور و App Router",
        "sub": "Dynamic Routes, Catch-all, Parallel & Intercepting",
        "level": "مبتدی",
        "analogy": "نقشه شهرداری که نام خیابان‌ها دقیقاً نام پوشه‌های داخل بایگانی پرونده‌هاست.",
        "plain_exp": "هر پوشه در داخل app تبدیل به یک بخش از آدرس اینترنتی (URL) می‌شود و پوشه‌های دینامیک با براکت [id] نام‌گذاری می‌شوند.",
        "real": "مسیردهی صفحات کالاها با میلیون‌ها تنوع URL در فروشگاه‌های اینترنتی.",
        "code": """// app/shop/[category]/[...slug]/page.tsx
export default async function CategoryPage({
  params
}: {
  params: Promise<{ category: string; slug: string[] }>
}) {
  const { category, slug } = await params;
  return <h1>دسته: {category} | زیرمسیر: {slug.join(' / ')}</h1>;
}""",
        "interview": "تفاوت [...slug] با [[...slug]] چیست؟ اولی اجباری است و روت بدون پارامتر را تطبیق نمی‌دهد، اما دومی اختیاری (Optional Catch-all) است و مسیر والد بدون اسلاگ را هم پوشش می‌دهد.",
        "sandbox": "<div class='text-xs font-mono text-emerald-400'>app/blog/[slug]/page.tsx ➔ /blog/nextjs-15</div>",
        "sol1": "// app/about/page.tsx\nexport default function About() { return <h1>درباره ما</h1>; }",
        "sol2": "// app/products/[id]/page.tsx\nexport default async function Page({ params }: { params: Promise<{ id: string }> }) { const { id } = await params; return <div>کالا {id}</div>; }",
        "sol3": "// Catch-all optional\nexport default async function CatchAll({ params }: { params: Promise<{ slug?: string[] }> }) { const { slug } = await params; return <pre>{JSON.stringify(slug)}</pre>; }"
    },
    {
        "id": 3,
        "title": "قراردادهای فایل و فایل‌های ویژه (Special Files)",
        "sub": "page, layout, template, loading, error, not-found",
        "level": "متوسط",
        "analogy": "نقش‌های یک گروه فیلم‌برداری: کارگردان (page)، صحنه ثابت (layout)، پرده نمایش تعویض صحنه (template) و جعبه کمک‌های اولیه (error).",
        "plain_exp": "فایل‌های رزروشده در App Router که رفتار رندرینگ، لودینگ سوسپنس و مهار خطاهای رندر را اتوماتیک مدیریت می‌کنند.",
        "real": "نمایش اسکلتون لودینگ فوری بدون کدنویسی دستی هنگام باز شدن صفحات سنگین.",
        "code": """// app/dashboard/error.tsx
'use client';

export default function ErrorBoundary({
  error,
  reset
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <div className="error-box">
      <h2>خطایی رخ داد: {error.message}</h2>
      <button onClick={() => reset()}>تلاش مجدد 🔄</button>
    </div>
  );
}""",
        "interview": "تفاوت layout.tsx با template.tsx چیست؟ لایوت هنگام تغییر صفحه Re-mount نمی‌شود و State خود را حفظ می‌کند؛ اما تمپلیت در هر تغییر مسیر از نو ساخته می‌شود.",
        "sandbox": "<div class='text-xs text-amber-300'>layout.tsx ➔ loading.tsx ➔ page.tsx ➔ error.tsx</div>",
        "sol1": "// app/loading.tsx\nexport default function Loading() { return <div className='spinner'>در حال بارگذاری...</div>; }",
        "sol2": "// app/not-found.tsx\nexport default function NotFound() { return <h2>صفحه مورد نظر پیدا نشد (۴۰۴)</h2>; }",
        "sol3": "// app/error.tsx\n'use client';\nexport default function Err({ error, reset }: { error: Error; reset: () => void }) { return <div><p>{error.message}</p><button onClick={reset}>تلاش دوباره</button></div>; }"
    },
    {
        "id": 4,
        "title": "اکوسیستم React در Next.js و Hydration",
        "sub": "Reconciliation, Hydration Mismatch, React Compiler",
        "level": "متوسط",
        "analogy": "ارسال مجسمه گچی آماده از کارخانه (HTML سرور) و سپس اتصال اعصاب و موتورهای حرکتی به آن در محل (Hydration جاوااسکریپت).",
        "plain_exp": "فرایند تزریق رویدادها و شنوندگان رویداد کلیک به اسکلت استاتیک ارسال‌شده از سرور.",
        "real": "حل خطاهای Hydration Mismatch در پروژه‌های فارسی به دلیل اختلاف تاریخ شمسی یا محتوای localStorage.",
        "code": """// جلوگیری از خطای Hydration با suppressHydrationWarning
export default function Timestamp() {
  return (
    <time dateTime="2026-10-23" suppressHydrationWarning>
      {typeof window !== 'undefined' ? new Date().toLocaleDateString('fa-IR') : ''}
    </time>
  );
}""",
        "interview": "علت اصلی Hydration Mismatch چیست؟ وقتی خروجی HTML اولیه سرور با رندر اولیه کلاینت (مثلاً به دلیل خواندن window یا توابع Math.random) حتی یک کاراکتر تفاوت داشته باشد.",
        "sandbox": "<div class='text-xs text-sky-300 font-mono'>Server HTML ➔ Client Reconcile ➔ Event Listeners Attached ✓</div>",
        "sol1": "export default function SafeTime() { return <span suppressHydrationWarning>{new Date().toISOString()}</span>; }",
        "sol2": "import { useState, useEffect } from 'react'; export default function ClientOnly({ children }: { children: React.ReactNode }) { const [mounted, setMounted] = useState(false); useEffect(() => setMounted(true), []); return mounted ? <>{children}</> : null; }",
        "sol3": "// Error boundary wrapper\n'use client';\nexport default function SafeHydrate({ children }: { children: React.ReactNode }) { return <div suppressHydrationWarning>{children}</div>; }"
    },
    {
        "id": 5,
        "title": "کامپوننت‌های سروری و کلاینتی (RSC vs 'use client')",
        "sub": "Server Component Payload, Serializable Props, Leaves Pattern",
        "level": "متوسط",
        "analogy": "آشپزخانه مرکزی رستوران که غذا را می‌پزد در برابر سالن غذاخوری که مشتری چنگال را تکان می‌دهد.",
        "plain_exp": "کامپوننت‌های سروری کدهای دیتابیس را بدون ارسال حتی یک بایت جاوااسکریپت به مرورگر اجرا می‌کنند و کامپوننت‌های کلاینتی تعاملاتی هستند.",
        "real": "کاهش حجم باندل وب‌سایت از ۴ مگابایت به کمتر از ۶۰ کیلوبایت.",
        "code": """// Server Component (Default)
import db from '@/lib/db';
import ClientLikeButton from './ClientLikeButton';

export default async function ProductCard({ id }: { id: string }) {
  const item = await db.product.findUnique({ where: { id } });
  return (
    <div className="card">
      <h2>{item.name}</h2>
      <ClientLikeButton initialLikes={item.likes} />
    </div>
  );
}""",
        "interview": "آیا می‌توان یک Server Component را درون یک Client Component رندر کرد؟ بله، فقط از طریق ارسال آن به عنوان children prop؛ ایمپورت مستقیم در فایل کلاینتی ناممکن است.",
        "sandbox": "<div class='text-xs font-mono'><span class='text-amber-400'>Server Comp (0KB JS)</span> + <span class='text-sky-400'>Client Leaf ('use client')</span></div>",
        "sol1": "'use client';\nimport { useState } from 'react';\nexport default function Counter() { const [c, setC] = useState(0); return <button onClick={() => setC(c+1)}>{c}</button>; }",
        "sol2": "// Server parent with client children\nexport default async function Parent({ children }: { children: React.ReactNode }) { const data = await fetch('https://api.com').then(r => r.json()); return <div>{data.title}{children}</div>; }",
        "sol3": "import 'server-only';\nexport const getSecretKey = () => process.env.SECRET_DB_KEY;"
    },
    {
        "id": 6,
        "title": "استراتژی‌های رندرینگ مدرن (CSR, SSR, SSG, ISR, PPR)",
        "sub": "Partial Prerendering, Streaming, Suspense Shell",
        "level": "پیشرفته",
        "analogy": "چاپ فوری ساختار روزنامه از شب قبل (استاتیک) و استریم زنده قیمت طلا و بورس در صدم ثانیه آخر (پویا).",
        "plain_exp": "ترکیب سرعت ماورایی صفحات استاتیک با پویایی داده‌های سرور که در Next.js 15 با PPR محقق شده است.",
        "real": "صفحه اول فروشگاه در حراج‌های بلک‌فرایدی با میلیون‌ها درخواست هم‌زمان بدون افت سرعت.",
        "code": """// next.config.ts
export default {
  experimental: {
    ppr: 'incremental',
  },
};

// app/product/[id]/page.tsx
export const experimental_ppr = true;

import { Suspense } from 'react';
import StaticShell from './StaticShell';
import DynamicPrice from './DynamicPrice';

export default function Page() {
  return (
    <main>
      <StaticShell />
      <Suspense fallback={<p>محاسبه قیمت لحظه‌ای...</p>}>
        <DynamicPrice />
      </Suspense>
    </main>
  );
}""",
        "interview": "PPR چه برتری بر ISR دارد؟ در ISR کل صفحه دوباره تولید می‌شود اما در PPR اسکلت صفحه همیشه از کش CDN با سرعت میلی‌ثانیه‌ای تحویل می‌شود و فقط بخش‌های داینامیک استریم می‌شوند.",
        "sandbox": "<div class='text-xs font-mono text-emerald-400'>Static Shell (Instant) + Dynamic Stream (PPR)</div>",
        "sol1": "export const revalidate = 60; // ISR هر ۶۰ ثانیه",
        "sol2": "export const dynamic = 'force-dynamic'; // SSR کامل",
        "sol3": "export const experimental_ppr = true; // فعال‌سازی PPR در صفحه"
    },
    {
        "id": 7,
        "title": "دریافت داده (Data Fetching) و پرامیس‌های ناهمگام",
        "sub": "async/await, Request Memoization, Async Params",
        "level": "متوسط",
        "analogy": "پیک اختصاصی که بسته‌ها را بدون معطل کردن صف سفارش‌ها مستقیماً از انبار تحویل می‌دهد.",
        "plain_exp": "دریافت مستقیم داده با fetch گسترش‌یافته در بدنه کامپوننت‌های سروری بدون نیاز به useEffect.",
        "real": "حذف کامل Waterfalls و دریافت موازی داده‌های کاربر و سفارش‌ها با Promise.all.",
        "code": """// app/dashboard/page.tsx
async function getUser() { const r = await fetch('https://api.ir/user'); return r.json(); }
async function getOrders() { const r = await fetch('https://api.ir/orders'); return r.json(); }

export default async function Dashboard() {
  // اجرای موازی و هم‌زمان بدون معطلی (No Waterfall)
  const [user, orders] = await Promise.all([getUser(), getOrders()]);

  return (
    <div>
      <h1>سلام {user.name}</h1>
      <p>تعداد سفارش‌ها: {orders.length}</p>
    </div>
  );
}""",
        "interview": "در Next 15 چرا params به صورت پرامیس درآمده است؟ تا رندرر سرور بتواند قبل از دریافت تمام هدرهای درخواست، رندر اولیه را آغاز و در صورت نیاز استریم کند.",
        "sandbox": "<div class='text-xs text-sky-400 font-mono'>const data = await fetch(url, { cache: 'no-store' });</div>",
        "sol1": "const res = await fetch('https://api.com/items', { next: { revalidate: 3600 } });",
        "sol2": "const { id } = await params; const item = await getItem(id);",
        "sol3": "const [feed, stats] = await Promise.all([getFeed(), getStats()]);"
    },
    {
        "id": 8,
        "title": "معماری چندلایه‌ای کش (Caching & Revalidation)",
        "sub": "use cache, cacheTag, revalidateTag, Request Memo",
        "level": "پیشرفته",
        "analogy": "حافظه کوتاه‌مدت مغز در مقایسه با قفسه کتابخانه و انبار مرکزی فایل‌ها.",
        "plain_exp": "نکست دارای ۴ لایه کش مجزا است: ممیوزیشین درخواست، دیتا کش سرور، فول روت کش و روتر کش سمت کلاینت.",
        "real": "بی‌اعتبار کردن آنی کش صفحه کالای دیجی‌کالا به محض تغییر قیمت در پنل انباردار با revalidateTag.",
        "code": """// app/actions/updatePrice.ts
'use server';
import { revalidateTag } from 'next/cache';

export async function updatePriceAction(id: string, price: number) {
  await db.product.update({ where: { id }, data: { price } });
  // کش تمام صفحاتی که این تگ را دارند در صدم ثانیه پاک می‌شود:
  revalidateTag('products-list');
}""",
        "interview": "دستور جدید 'use cache' در Next 15 چه تفاوتی با رفتارهای قبلی fetch دارد؟ 'use cache' یک کش در سطح تابع و کامپوننت ارائه می‌دهد و جایگزین رویکردهای پیچیده fetch tags می‌شود.",
        "sandbox": "<div class='text-xs text-amber-300 font-mono'>Data Cache ➔ Full Route Cache ➔ revalidateTag()</div>",
        "sol1": "revalidatePath('/blog');",
        "sol2": "revalidateTag('inventory-tag');",
        "sol3": "async function getData() { 'use cache'; cacheLife('hours'); return fetchUsers(); }"
    },
    {
        "id": 9,
        "title": "اکشن‌های سرور (Server Actions & Server Functions)",
        "sub": "'use server', useActionState, useOptimistic, Form Mutations",
        "level": "پیشرفته",
        "analogy": "فشردن دکمه صندوق فروشگاه که مستقیماً گاوصندوق را باز و ثبت سند می‌کند بدون باجه واسطه.",
        "plain_exp": "توابعی که با 'use server' علامت‌گذاری شده و مستقیماً روی سرور بدون نیاز به نوشتن دستی کنترلرهای API اجرا می‌شوند.",
        "real": "ثبت فرم‌های پرداخت و ارسال تیکت با آپدیت خوش‌بینانه (Optimistic UI) بدون لودینگ خسته‌کننده.",
        "code": """'use client';
import { useActionState, useOptimistic } from 'react';
import { sendCommentAction } from './actions';

export default function CommentForm({ initialComments }) {
  const [state, formAction, isPending] = useActionState(sendCommentAction, null);
  const [optimistic, addOptimistic] = useOptimistic(
    initialComments,
    (state, newText) => [...state, { text: newText, sending: true }]
  );

  return (
    <form action={async (formData) => {
      addOptimistic(formData.get('comment'));
      await formAction(formData);
    }}>
      <input name="comment" required />
      <button disabled={isPending}>{isPending ? 'در حال ثبت...' : 'ارسال نظر'}</button>
    </form>
  );
}""",
        "interview": "امنیت در Server Actions چگونه حفظ می‌شود؟ چون اکشن‌ها مانند یک اندپوینت POST در دسترس هستند، حتماً باید اعتبارسنجی احراز هویت کاربر و اسکیمای ورودی با Zod در بدنه اکشن انجام شود.",
        "sandbox": "<div class='text-xs text-emerald-400 font-mono'>Form Submit ➔ 'use server' Action ➔ revalidatePath()</div>",
        "sol1": "'use server';\nexport async function myAction(formData: FormData) { const name = formData.get('name'); }",
        "sol2": "const [state, action, isPending] = useActionState(serverHandler, null);",
        "sol3": "const [opt, setOpt] = useOptimistic(items, (state, update) => [...state, update]);"
    },
    {
        "id": 10,
        "title": "مسیریاب‌های API و Route Handlers",
        "sub": "route.ts, Web Request/Response, NextRequest, CORS",
        "level": "متوسط",
        "analogy": "پیشخوان عمومی گمرک که به مسافران، کامیون‌ها و سیستم‌های نرم‌افزاری بیرونی پاسخ می‌دهد.",
        "plain_exp": "فایل‌های route.ts برای ساخت APIهای عمومی RESTful با پشتیبانی از تمام متدهای HTTP.",
        "real": "ارائه وب‌هوک برای درگاه‌های پرداخت بانکی (شاپرک، زرین‌پال) و پاسخ فوری با NextResponse.json.",
        "code": """// app/api/payment/verify/route.ts
import { NextRequest, NextResponse } from 'next/server';

export async function POST(req: NextRequest) {
  const body = await req.json();
  if (!body.authority) {
    return NextResponse.json({ error: 'کد پیگیری الزامی است' }, { status: 400 });
  }

  return NextResponse.json({ success: true, refId: 'TRX_982314' });
}""",
        "interview": "تفاوت Route Handler با Server Action چیست؟ اولی برای اندپوینت‌های عمومی وب‌هوک و کلاینت‌های متفرقه مانند موبایل است، اما دومی اختصاصاً برای تعامل فرم‌های فرانت‌ند با سرور است.",
        "sandbox": "<div class='text-xs font-mono text-sky-400'>GET/POST /api/webhook ➔ route.ts ➔ NextResponse.json()</div>",
        "sol1": "export async function GET() { return NextResponse.json({ status: 'ok' }); }",
        "sol2": "export async function POST(req: Request) { const data = await req.json(); return NextResponse.json(data); }",
        "sol3": "export async function DELETE(req: Request, { params }: { params: Promise<{ id: string }> }) { const { id } = await params; return new Response(null, { status: 204 }); }"
    },
    {
        "id": 11,
        "title": "فرم‌های پیشرفته و اعتبارسنجی با Zod",
        "sub": "Server-side Validation, React Hook Form, Pending UI",
        "level": "متوسط",
        "analogy": "دربان سخت‌گیر بانک که کارت ملی و فاکتورها را قبل از رسیدن به باجه بررسی و اعتبارسنجی می‌کند.",
        "plain_exp": "یکپارچه‌سازی فرم‌ها با Zod برای اعتبارسنجی هم‌زمان در مرورگر و سرور جهت جلوگیری از حملات داده‌های معیوب.",
        "real": "فرم ثبت‌نام و ورود کاربران با شماره موبایل و مهار ثبت فرم‌های ناقص.",
        "code": """import { z } from 'zod';

const RegisterSchema = z.object({
  phone: z.string().regex(/^09\\d{9}$/, 'شماره موبایل معتبر نیست'),
  password: z.string().min(8, 'رمز عبور حداقل ۸ کاراکتر باشد')
});

export async function registerAction(prevState: any, formData: FormData) {
  const parsed = RegisterSchema.safeParse(Object.fromEntries(formData));
  if (!parsed.success) {
    return { errors: parsed.error.flatten().fieldErrors };
  }
  return { success: true };
}""",
        "interview": "چرا اعتبارسنجی کلاینتی کافی نیست؟ چون هر فردی می‌تواند با curl یا Postman مستقیماً دیتای نامعتبر به سرور اکشن شما POST کند.",
        "sandbox": "<div class='text-xs text-amber-300 font-mono'>Zod Schema ➔ safeParse() ➔ fieldErrors Feedback</div>",
        "sol1": "const schema = z.object({ email: z.string().email() });",
        "sol2": "const res = schema.safeParse(data); if (!res.success) return res.error.issues;",
        "sol3": "const [state, formAction] = useActionState(registerAction, null);"
    },
    {
        "id": 12,
        "title": "پایگاه داده و ORM (Prisma & Drizzle)",
        "sub": "Serverless Connection Pooling, Transactions, Data Access Layer",
        "level": "پیشرفته",
        "analogy": "مترجم کارکشته بین شیءهای برنامه‌نویسی جاوااسکریپت و جدول‌های پیچیده SQL پایگاه‌داده.",
        "plain_exp": "اتصال مستقیم و امن Next.js به پایگاه‌داده با استفاده از ORMهای نسل جدید با پشتیبانی کامل از TypeScript.",
        "real": "مهار خطای پر شدن اتصالات دیتابیس در محیط‌های Serverless با Prisma Accelerate.",
        "code": """// lib/prisma.ts
import { PrismaClient } from '@prisma/client';

const globalForPrisma = globalThis as unknown as { prisma: PrismaClient };
export const prisma = globalForPrisma.prisma || new PrismaClient();

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma;""",
        "interview": "چرا در حالت توسعه نکست باید شیء Prisma را در globalThis ذخیره کرد؟ چون قابلیت Fast Refresh کدهای فایل‌ها را بازخوانی می‌کند و باعث باز شدن صدها اتصال پایگاه داده و کرش سرور می‌شود.",
        "sandbox": "<div class='text-xs text-emerald-400 font-mono'>const users = await prisma.user.findMany();</div>",
        "sol1": "const user = await prisma.user.create({ data: { name, email } });",
        "sol2": "const posts = await db.select().from(postsTable).where(eq(postsTable.userId, id));",
        "sol3": "const [u, o] = await prisma.$transaction([prisma.user.delete(...), prisma.order.delete(...)]);"
    },
    {
        "id": 13,
        "title": "احراز هویت و امنیت نشست‌ها (Auth.js & Better Auth)",
        "sub": "JWT, HTTP-Only Cookies, RBAC, Protected Server Actions",
        "level": "پیشرفته",
        "analogy": "کارت پرواز دیجیتال با هولوگرام ضد جعل که اجازه ورود به کابین خلبان را محدود می‌کند.",
        "plain_exp": "پیاده‌سازی ورود با رمز، پیامک یا گوگل و ذخیره نشست در کوکی‌های محافظت‌شده HTTP-only.",
        "real": "حفاظت از مسیرهای ادمین و مسدودسازی دسترسی بدون توکن معتبر در لایه سرور.",
        "code": """import { cookies } from 'next/headers';
import { verifyJwt } from '@/lib/jwt';

export async function getSession() {
  const cookieStore = await cookies();
  const token = cookieStore.get('session_token')?.value;
  if (!token) return null;
  return verifyJwt(token);
}""",
        "interview": "چرا ذخیره توکن احراز هویت در localStorage در Next.js اشتباه است؟ چون کوکی‌های HTTP-Only در برابر حملات XSS ایمن هستند و در اولین درخواست سرور در دسترس کامپوننت‌های سروری قرار دارند.",
        "sandbox": "<div class='text-xs text-purple-300 font-mono'>cookies().get('auth_token') ➔ HTTP-only ➔ Verify Role</div>",
        "sol1": "const cookieStore = await cookies(); cookieStore.set('token', val, { httpOnly: true, secure: true });",
        "sol2": "const session = await auth(); if (!session) redirect('/login');",
        "sol3": "if (session.user.role !== 'ADMIN') throw new Error('403 Forbidden');"
    },
    {
        "id": 14,
        "title": "استایل‌دهی، Tailwind CSS و کتابخانه کامپوننت‌ها",
        "sub": "Tailwind v4, CSS Modules, shadcn/ui, Radix UI",
        "level": "مبتدی",
        "analogy": "پالت رنگ و قلم‌موهای طراحی که هم‌زمان ابعاد موبایل و دسکتاپ را شیک و بدون کدهای اضافه رنگ‌آمیزی می‌کنند.",
        "plain_exp": "استفاده از کلاس‌های سریع تیلویند و کامپوننت‌های دسترسی‌پذیر shadcn/ui برای طراحی مدرن تیره و روشن.",
        "real": "راه‌اندازی دیزاین سیستم هماهنگ با حالت دارک و فونت‌های فارسی در سامانه‌های کشوری.",
        "code": """// app/layout.tsx
import '@/styles/globals.css';
import { Vazirmatn } from 'next/font/google';

const vazir = Vazirmatn({ subsets: ['arabic'] });

export default function RootLayout({ children }) {
  return (
    <html lang="fa" dir="rtl" className={vazir.className}>
      <body className="bg-slate-950 text-slate-100">{children}</body>
    </html>
  );
}""",
        "interview": "چرا shadcn/ui نسبت به پکیج‌های سنتی مثل MUI در Next.js محبوب‌تر شد؟ چون کد کامپوننت مستقیماً در پروژه شما قرار می‌گیرد و با Server Components سازگاری صددرصدی دارد.",
        "sandbox": "<div class='text-xs text-sky-300 font-mono'>Tailwind v4 + shadcn/ui + dark:bg-slate-950</div>",
        "sol1": "<button className='px-4 py-2 bg-sky-500 text-white rounded-lg hover:bg-sky-600 transition'>دکمه</button>",
        "sol2": "<div className='grid grid-cols-1 md:grid-cols-3 gap-4 p-6'>{children}</div>",
        "sol3": "import styles from './button.module.css'; export default function Btn() { return <button className={styles.primary}>کارت</button>; }"
    },
    {
        "id": 15,
        "title": "بهینه‌سازی رسانه، تصاویر و فونت‌ها (next/image & next/font)",
        "sub": "next/image, WebP/AVIF, Layout Shift Prevention, next/font",
        "level": "متوسط",
        "analogy": "فشرده‌سازی بار مسافران و تغییر ابعاد چمدان‌ها قبل از سوار شدن به هواپیما جهت صرفه‌جویی در سوخت.",
        "plain_exp": "لود خودکار تصاویر با فرمت مدرن WebP/AVIF، ریسپانسیو بودن ابعاد و لود فونت بدون پرش و چشمک‌زدن صفحه.",
        "real": "رساندن نمره عملکرد Core Web Vitals سایت به ۱۰۰ در گوگل پیج اسپید.",
        "code": """import Image from 'next/image';

export default function HeroBanner() {
  return (
    <div className="relative w-full h-[400px]">
      <Image
        src="/banners/summer.jpg"
        alt="تخفیف‌های تابستانه"
        fill
        priority
        sizes="(max-width: 768px) 100vw, 1200px"
        className="object-cover"
      />
    </div>
  );
}""",
        "interview": "صفت priority در Image چه کاری می‌کند؟ به مرورگر می‌گوید که این تصویر بزرگترین المان بصری صفحه (LCP) است و باید قبل از سایر منابع بدون لود تنبل دانلود شود.",
        "sandbox": "<div class='text-xs text-emerald-400 font-mono'>next/image ➔ Auto AVIF Conversion ➔ Zero CLS</div>",
        "sol1": "<Image src='/logo.png' alt='لوگو' width={120} height={40} />",
        "sol2": "<Image src='/hero.jpg' alt='بنر' fill priority className='object-cover' />",
        "sol3": "images: { remotePatterns: [{ protocol: 'https', hostname: 'images.unsplash.com' }] }"
    },
    {
        "id": 16,
        "title": "سئو پیشرفته، متادیتا و اسکیما (SEO & Metadata API)",
        "sub": "generateMetadata, OpenGraph, sitemap.ts, robots.ts",
        "level": "متوسط",
        "analogy": "نصب تابلوی نئونی مشخصات فروشگاه در میدان شهر با توضیحات خوانا برای رهگذران و دوربین‌های ترافیکی.",
        "plain_exp": "تولید داینامیک عنوان، توضیحات، کارت‌های توییتر و نقشه سایت با کدهای TypeScript.",
        "real": "نمایش تصاویر و پیش‌نمایش غنی هنگام ارسال لینک مقاله در پیام‌رسان‌ها (تلگرام، واتساپ).",
        "code": """// app/blog/[slug]/page.tsx
export async function generateMetadata({ params }): Promise<Metadata> {
  const { slug } = await params;
  const post = await getPost(slug);

  return {
    title: `${post.title} | وبلاگ فنی`,
    description: post.excerpt,
    openGraph: {
      title: post.title,
      images: [post.coverImage],
    },
  };
}""",
        "interview": "چرا sitemap.ts در نکست ۱۵ برتر از فایل استاتیک xml است؟ چون نقشه سایت را به صورت پویا با استعلام مستقیم از پایگاه‌داده برای میلیون‌ها محصول به روز نگه می‌دارد.",
        "sandbox": "<div class='text-xs text-amber-300 font-mono'>generateMetadata() ➔ OG Cards + sitemap.ts</div>",
        "sol1": "export const metadata: Metadata = { title: 'فروشگاه', description: 'خرید آسان' };",
        "sol2": "export async function generateMetadata({ params }) { return { title: (await params).id }; }",
        "sol3": "// app/sitemap.ts\nexport default async function sitemap() { return [{ url: 'https://site.ir', lastModified: new Date() }]; }"
    },
    {
        "id": 17,
        "title": "ناوبری پیشرفته و تجربه کاربری (Navigation & UX)",
        "sub": "useRouter, usePathname, Prefetching, Modal Routes",
        "level": "متوسط",
        "analogy": "راه‌پله‌های برقی هوشمند که قبل از رسیدن پای شما شروع به حرکت نرم می‌کنند.",
        "plain_exp": "جابجایی سریع بین صفحات بدون رفرش مرورگر با پیش‌بارگذاری نامحسوس لینک‌های موجود در دید کاربر.",
        "real": "لود آنی صفحه کالا به محض قرار گرفتن لینک در صفحه با مکانیزم prefetch تگ Link.",
        "code": """'use client';
import { useRouter, usePathname, useSearchParams } from 'next/navigation';

export default function FilterBar() {
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();

  const handleSort = (sort: string) => {
    const params = new URLSearchParams(searchParams);
    params.set('sort', sort);
    router.push(`${pathname}?${params.toString()}`);
  };

  return <button onClick={() => handleSort('cheap')}>ارزان‌ترین</button>;
}""",
        "interview": "تفاوت Soft Navigation با Hard Navigation چیست؟ در ناوبری نرم (Link)، استیت و کدهای مشترک لایوت حفظ می‌شوند؛ اما در ناوبری سخت کل صفحه از سرور رفرش می‌شود.",
        "sandbox": "<div class='text-xs text-sky-400 font-mono'><Link href='/shop' prefetch={true}> ➔ Zero-latency</div>",
        "sol1": "import Link from 'next/link'; export default function Nav() { return <Link href='/shop'>فروشگاه</Link>; }",
        "sol2": "const router = useRouter(); router.push('/dashboard');",
        "sol3": "const pathname = usePathname(); const isActive = pathname === '/about';"
    },
    {
        "id": 18,
        "title": "پیکربندی حرفه‌ای next.config.ts و متغیرهای محیطی",
        "sub": "Redirects, Rewrites, Headers, Turbopack Options",
        "level": "پیشرفته",
        "analogy": "اتاق کنترل و جعبه تقسیم برق کل ساختمان که ولتاژ و مسیر سیم‌ها را تعیین می‌کند.",
        "plain_exp": "تنظیمات پیشرفته ریدایرکت‌های دائمی ۳۰۱، ری‌رایت مسیرهای پروکسی و هدرهای امنیتی در فایل پیکربندی اصلی.",
        "real": "انتقال آدرس سایت قدیمی به ساختار جدید بدون از دست رفتن رتبه سئو با redirects().",
        "code": """import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  async redirects() {
    return [
      {
        source: '/old-store/:path*',
        destination: '/store/:path*',
        permanent: true,
      },
    ];
  },
};
export default nextConfig;""",
        "interview": "تفاوت Redirect با Rewrite چیست؟ ریدایرکت آدرس مرورگر را تغییر داده و کد ۳۰۱/۳۰۲ برمی‌گرداند؛ اما ری‌رایت محتوای مقصد را پشت همان URL مبدا بدون تغییر آدرس بار مرورگر رندر می‌کند.",
        "sandbox": "<div class='text-xs text-emerald-400 font-mono'>nextConfig: redirects() + rewrites() + headers()</div>",
        "sol1": "const config = { trailingSlash: true }; export default config;",
        "sol2": "async redirects() { return [{ source: '/a', destination: '/b', permanent: true }]; }",
        "sol3": "async headers() { return [{ source: '/(.*)', headers: [{ key: 'X-Frame-Options', value: 'DENY' }] }]; }"
    },
    {
        "id": 19,
        "title": "لایه امنیتی و هدایت شبکه در Edge با Middleware",
        "sub": "middleware.ts, Edge Runtime, Route Guards, proxy.ts",
        "level": "پیشرفته",
        "analogy": "گیت بازرسی فرودگاه قبل از ورود مسافران به سالن‌های پرواز.",
        "plain_exp": "کدی که در شبکه لبه (Edge) قبل از رسیدن درخواست به هر صفحه‌ای اجرا شده و دسترسی کاربر را بررسی می‌کند.",
        "real": "ریدایرکت خودکار کاربران تاییدنشده به صفحه ورود و مهار ربات‌های ناشناس.",
        "code": """// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const token = request.cookies.get('token');
  if (!token && request.nextUrl.pathname.startsWith('/admin')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  return NextResponse.next();
}

export const config = {
  matcher: ['/admin/:path*'],
};""",
        "interview": "چرا نمی‌توان در میدل‌ور نکست از کتابخانه‌های سنگین پایگاه‌داده نود استفاده کرد؟ چون میدل‌ور در Edge Runtime سبک وب اجرا می‌شود و به پکیج‌های وابسته به سیستم‌عامل دسترسی ندارد.",
        "sandbox": "<div class='text-xs text-purple-300 font-mono'>Edge Middleware ➔ Matcher ➔ Token Verify ➔ Next/Redirect</div>",
        "sol1": "export function middleware(req: NextRequest) { return NextResponse.next(); }",
        "sol2": "export const config = { matcher: ['/dashboard/:path*'] };",
        "sol3": "if (!req.cookies.has('auth')) return NextResponse.redirect(new URL('/login', req.url));"
    },
    {
        "id": 20,
        "title": "بین‌المللی‌سازی و سایت‌های چندزبانه (i18n)",
        "sub": "Locale Routing, RTL/LTR, Translation Dictionaries",
        "level": "متوسط",
        "analogy": "هتلی بین‌المللی که کارکنانش به محض ورود میهمان، تابلوی راهنما را به زبان او ترجمه می‌کنند.",
        "plain_exp": "ساخت مسیرهای اختصاصی زبان مانند /fa و /en با چینش راست‌چین و چپ‌چین بدون کدهای اضافه.",
        "real": "پلتفرم‌های صادراتی با قابلیت سوئیچ آنی بین زبان فارسی و انگلیسی.",
        "code": """// app/[locale]/layout.tsx
export default async function LocaleLayout({
  children,
  params
}: {
  children: React.ReactNode;
  params: Promise<{ locale: string }>
}) {
  const { locale } = await params;
  const dir = locale === 'fa' ? 'rtl' : 'ltr';

  return (
    <html lang={locale} dir={dir}>
      <body>{children}</body>
    </html>
  );
}""",
        "interview": "چگونه در App Router دیکشنری ترجمه لود می‌شود؟ با ساخت فایل‌های json برای هر زبان و فراخوانی آن در کامپوننت سروری با تابع getDictionary(locale).",
        "sandbox": "<div class='text-xs text-sky-400 font-mono'>app/[locale]/page.tsx ➔ dir='rtl' / dir='ltr'</div>",
        "sol1": "export async function generateStaticParams() { return [{ locale: 'fa' }, { locale: 'en' }]; }",
        "sol2": "const dict = await getDictionary(locale); return <h1>{dict.home.welcome}</h1>;",
        "sol3": "const dir = locale === 'fa' || locale === 'ar' ? 'rtl' : 'ltr';"
    },
    {
        "id": 21,
        "title": "امنیت، مقابله با نفوذ و پنهان‌سازی اطلاعات محرمانه",
        "sub": "XSS, CSRF, CSP Headers, server-only secrets",
        "level": "پیشرفته",
        "analogy": "صندوق نسوز ضدسرقت که کلید اختصاصی آن فقط در انبار مرکزی نگه‌داری می‌شود.",
        "plain_exp": "جلوگیری از افشای کلیدهای خصوصی API در سورس مرورگر با استفاده از پکیج server-only.",
        "real": "مهار حملات تزریق اسکریپت (XSS) با تنظیم هدرهای سخت‌گیرانه Content Security Policy.",
        "code": """import 'server-only';

// این فایل اگر تصادفاً در یک Client Component ایمپورت شود بیلد خطا می‌دهد
export const STRIPE_SECRET = process.env.STRIPE_SECRET_KEY;""",
        "interview": "چگونه مطمئن شویم یک متغیر مخفی به کلاینت نفوذ نکرده است؟ متغیرهایی که پیشوند NEXT_PUBLIC_ ندارند در باندل کلاینت پاک می‌شوند، و پکیج server-only ضامن ایمپورت نشدن آن است.",
        "sandbox": "<div class='text-xs text-red-400 font-mono'>import 'server-only'; ➔ Zero Secret Leak Guarantee</div>",
        "sol1": "import 'server-only'; export const API_KEY = process.env.PRIVATE_KEY;",
        "sol2": "const sanitized = sanitizeHtml(userInput);",
        "sol3": "headers.set('Content-Security-Policy', \"default-src 'self'\");"
    },
    {
        "id": 22,
        "title": "تست، کنترل کیفیت و مانیتورینگ خطا (Testing & QA)",
        "sub": "Vitest, Playwright, React Testing Library, E2E",
        "level": "پیشرفته",
        "analogy": "خط تست ایمنی تصادف خودرو قبل از ورود محصول به بازار مصرف عمومی.",
        "plain_exp": "نوشتن آزمون‌های واحد، یکپارچه‌سازی و تست‌های سرتاسری با Playwright برای اطمینان از عملکرد صددرصدی برنامه.",
        "real": "تست خودکار فرآیند سبد خرید تا پرداخت در خط CI/CD قبل از هر بار استقرار در پروداکشن.",
        "code": """import { test, expect } from '@playwright/test';

test('کاربر باید بتواند کالا را به سبد خرید اضافه کند', async ({ page }) => {
  await page.goto('/shop');
  await page.click('button:has-text(\"خرید\")');
  await expect(page.locator('.cart-badge')).toHaveText('1');
});""",
        "interview": "چرا تست End-to-End با Playwright برای Next.js حیاتی است؟ چون تعاملات بین سرور رندرینگ و کلاینت هایدریشن را در مرورگر واقعی تست می‌کند.",
        "sandbox": "<div class='text-xs text-emerald-300 font-mono'>npx playwright test ➔ All 42 Tests Passed ✓</div>",
        "sol1": "test('renders heading', () => { render(<Page />); expect(screen.getByRole('heading')).toBeInTheDocument(); });",
        "sol2": "await page.goto('/login'); await page.fill('#email', 'user@test.ir'); await page.click('#submit');",
        "sol3": "expect(await page.title()).toBe('داشبورد');"
    },
    {
        "id": 23,
        "title": "معماری موروثی Pages Router و تفاوت‌های آن با App Router",
        "sub": "pages/index.tsx, getServerSideProps, getStaticProps",
        "level": "متوسط",
        "analogy": "موتورهای بنزینی سنتی در برابر پیشرانه‌های هیبریدی مدرن؛ هر دو ماشین را می‌رانند اما معماری متفاوتی دارند.",
        "plain_exp": "سیستم قدیمی‌تر مسیریابی در پوشه pages با متدهای ویژه دریافت داده در سرور.",
        "real": "پشتیبانی و ارتقای پروژه‌های شرکتی بزرگ که در سال‌های قبل با Pages Router پیاده شده‌اند.",
        "code": """// pages/products/[id].tsx
import { GetServerSideProps } from 'next';

export const getServerSideProps: GetServerSideProps = async (context) => {
  const { id } = context.params!;
  const res = await fetch(`https://api.ir/products/${id}`);
  const data = await res.json();
  return { props: { data } };
};

export default function Product({ data }) {
  return <h1>{data.title}</h1>;
}""",
        "interview": "چرا در App Router دیگر نیازی به getServerSideProps نیست؟ چون کامپوننت‌های سروری خودشان مستقیماً async هستند و داده را در بدنه خود واکشی می‌کنند.",
        "sandbox": "<div class='text-xs text-amber-400 font-mono'>Pages Router: getServerSideProps ➔ App Router: async Server Comp</div>",
        "sol1": "export async function getStaticProps() { return { props: { items: [] } }; }",
        "sol2": "export async function getStaticPaths() { return { paths: [], fallback: 'blocking' }; }",
        "sol3": "export const getServerSideProps = async () => ({ props: { time: Date.now() } });"
    },
    {
        "id": 24,
        "title": "معماری پروژه‌های بزرگ سازمانی و ساختار پوشه‌بندی FSD",
        "sub": "Feature-Sliced Design, Clean Architecture, BFF Pattern",
        "level": "پیشرفته",
        "analogy": "برنامه‌ریزی شهری یک کلان‌شهر که بیمارستان‌ها، مناطق مسکونی و تفریحی مرزبندی تفکیک‌شده دارند.",
        "plain_exp": "تقسیم کدهای هزاران فایل به لایه‌های مستقل تجاری برای توسعه بدون تداخل در تیم‌های ده‌ها نفره.",
        "real": "معماری پروژه‌های پلتفرمی اسنپ و اسنپ‌فود با تفکیک ماژول‌های cart, auth, orders.",
        "code": """src/
├── app/                  # روت‌ها و صفحات
├── features/             # ماژول‌های مستقل کاربردی
│   ├── auth/             # کامپوننت‌ها، هوک‌ها و استور ورود
│   └── cart/             # سبد خرید و محاسبات مالی
├── shared/               # دکمه‌ها و توابع مشترک عمومی
│   ├── ui/
│   └── lib/""",
        "interview": "الگوی Backend for Frontend (BFF) در Next.js چه نقشی دارد؟ نکست به عنوان لایه میانی داده‌های چندین میکروسرویس سنگین را دریافت، ترکیب، و پالایش کرده و به شکل فشرده به کاربر تحویل می‌دهد.",
        "sandbox": "<div class='text-xs text-emerald-400 font-mono'>FSD Architecture: app ➔ widgets ➔ features ➔ entities ➔ shared</div>",
        "sol1": "// ساختار پوشه‌بندی تمیز ویژگی‌محور\n// features/cart/ui/CartButton.tsx",
        "sol2": "// لایه سرویس اختصاصی\n// services/orderService.ts",
        "sol3": "// پکیج مشترک در مونو‌ریپو\n// packages/ui/src/button.tsx"
    },
    {
        "id": 25,
        "title": "قابلیت‌های سازمانی، WebSockets و اینسترومنتیشن",
        "sub": "instrumentation.ts, OpenTelemetry, Redis, Background Jobs",
        "level": "پیشرفته",
        "analogy": "سنسورهای تله‌متری شاتل فضایی که فشار، حرارت و عملکرد ثانیه به ثانیه را رصد می‌کنند.",
        "plain_exp": "پایش زنده سلامت سرورها با OpenTelemetry، ارتباط بلادرنگ سوکت و صف‌های پس‌زمینه ردیس.",
        "real": "چت آنلاین پشتیبانی مشتریان و ردیابی بلادرنگ راننده روی نقشه زنده.",
        "code": """// instrumentation.ts
export async function register() {
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    // راه‌اندازی سنسورهای مانیتورینگ سرور
    await import('@/lib/monitoring/telemetry');
  }
}""",
        "interview": "فایل instrumentation.ts چه زمانی اجرا می‌شود؟ دقیقاً یک‌بار در لحظه استارت سرور قبل از رسیدن حتی اولین درخواست کاربر، جهت راه‌اندازی کانکشن‌ها و سنسورها.",
        "sandbox": "<div class='text-xs text-purple-300 font-mono'>instrumentation.ts ➔ OpenTelemetry + Redis Cache</div>",
        "sol1": "export async function register() { console.log('سرور اجرا شد'); }",
        "sol2": "const redis = new Redis(process.env.REDIS_URL); await redis.set('key', 'val');",
        "sol3": "const socket = new WebSocket('wss://api.site.ir'); socket.onmessage = (e) => ...;"
    },
    {
        "id": 26,
        "title": "عملکرد، متغیرهای Core Web Vitals و بهینه‌سازی بارگذاری",
        "sub": "LCP, INP, CLS, Bundle Analyzer, Tree Shaking",
        "level": "پیشرفته",
        "analogy": "تیونینگ موتور خودروی مسابقه‌ای با سبک‌سازی شاسی و تنظیم زاویه بادشکن‌ها.",
        "plain_exp": "بهینه‌سازی شاخص‌های سرعت گوگل برای رسیدن به لود زیر ۱ ثانیه با تفکیک هوشمند کدها.",
        "real": "ارتقای نرخ تبدیل خرید فروشگاه با کاهش زمان پاسخ‌دهی کلیک‌ها (INP).",
        "code": """// آنالیز حجم باندل جاوااسکریپت
import withBundleAnalyzer from '@next/bundle-analyzer';

const nextConfig = withBundleAnalyzer({
  enabled: process.env.ANALYZE === 'true',
})({
  // تنظیمات نکست
});
export default nextConfig;""",
        "interview": "شاخص INP جایگزین چه معیاری شد و چه چیزی را اندازه می‌گیرد؟ جایگزین FID شد و تاخیر تعامل کاربر با دکمه‌ها و منوها در طول کل حضور در صفحه را محاسبه می‌کند.",
        "sandbox": "<div class='text-xs text-emerald-400 font-mono'>LCP: 0.8s | CLS: 0.00 | INP: 24ms ➔ 100/100 Score</div>",
        "sol1": "const DynamicChart = dynamic(() => import('./Chart'), { ssr: false });",
        "sol2": "const analyzer = require('@next/bundle-analyzer')({ enabled: true });",
        "sol3": "export const experimental = { optimizePackageImports: ['lucide-react'] };"
    },
    {
        "id": 27,
        "title": "فرایند Build، استقرار (Deployment) و کانتینرسازی Docker",
        "sub": "Docker multi-stage, Self-hosting, CI/CD, output: 'standalone'",
        "level": "پیشرفته",
        "analogy": "بسته‌بندی استاندارد بین‌المللی یک کالا درون کانتینر کشتی که در هر بندری باز شود دقیقاً همان کار را می‌کند.",
        "plain_exp": "ساخت ایمیج‌های داکر کم‌حجم با قابلیت standalone برای ران کردن با Nginx روی سرورهای ابری ایران.",
        "real": "استقرار خودکار نسخه‌های جدید برنامه با GitHub Actions روی سرورهای کلاود آروان.",
        "code": """# Dockerfile
FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
COPY .next/standalone ./
COPY .next/static ./.next/static
COPY public ./public
EXPOSE 3000
CMD ["node", "server.js"]""",
        "interview": "خاصیت output: 'standalone' چه فایده‌ای دارد؟ فقط فایل‌های وابسته به پروژه را کپی می‌کند و حجم ایمیج داکر را از ۱.۵ گیگابایت به کمتر از ۱۰۰ مگابایت می‌رساند.",
        "sandbox": "<div class='text-xs text-sky-400 font-mono'>output: 'standalone' ➔ Docker 80MB Image ➔ Production Ready</div>",
        "sol1": "// next.config.ts\nmodule.exports = { output: 'standalone' };",
        "sol2": "docker build -t next-app . && docker run -p 3000:3000 next-app",
        "sol3": "npm run build && npm run start"
    },
    {
        "id": 28,
        "title": "مفاهیم نسل جدید Next.js 15 و قابلیت‌های آزمایشی",
        "sub": "use cache, cacheLife, React 19 Actions, Turbopack Engine",
        "level": "پیشرفته",
        "analogy": "رونمایی از نسل آینده فضاپیماها با سوخت پلاسمایی و هوش مصنوعی داخلی.",
        "plain_exp": "جدیدترین قابلیت‌های نکست ۱۵ شامل کشینگ کامپوننت، توربوپک پایدار و اکشن‌های ری‌اکت ۱۹.",
        "real": "استفاده از قابلیت 'use cache' برای بهینه‌سازی میلی‌ثانیه‌ای فید خبرخوان‌ها در رسانه‌های خبری بزرگ.",
        "code": """// Next.js 15 'use cache' directive
export async function getLiveNewsFeed() {
  'use cache';
  cacheLife('minutes');
  cacheTag('news-feed');

  return fetchNewsFromDatabase();
}""",
        "interview": "توربوپک در حالت بیلد چه پیشرفتی داشته است؟ با بهره‌گیری از معماری Rust تا ۷۰۰ برابر سریع‌تر از وب‌پک تغییرات را در محیط توسعه منعکس می‌کند.",
        "sandbox": "<div class='text-xs text-amber-300 font-mono'>Next.js 15 + React 19 + Turbopack + 'use cache'</div>",
        "sol1": "async function Feed() { 'use cache'; return <div>اخبار</div>; }",
        "sol2": "cacheLife('hours'); cacheTag('homepage');",
        "sol3": "updateTag('homepage');"
    }
]

with open(os.path.join(BASE_DIR, "builders", "nextjs_28_topics.json"), "w", encoding="utf-8") as f:
    json.dump(CHAPTERS_DEF, f, ensure_ascii=False, indent=2)

print(f"Generated complete 28-topic Next.js dataset: {len(CHAPTERS_DEF)} topics!")
