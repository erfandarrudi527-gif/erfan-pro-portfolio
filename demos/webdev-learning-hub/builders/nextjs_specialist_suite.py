# -*- coding: utf-8 -*-
"""
Generate the standalone Next.js 15 App Router & Server Architecture Handbook & Web App.
Fully independent with its own topics, problems, solutions, sandbox, and Desktop PDF.
"""
import os, sys, json, subprocess

BASE_DIR = "C:/Users/erfan/Desktop/WebDev_Master_Learning_Hub"
NEXTJS_DIR = os.path.join(BASE_DIR, "nextjs")
os.makedirs(NEXTJS_DIR, exist_ok=True)

NEXTJS_TOPICS = [
    {
        "id": 1,
        "title": "معماری App Router و پوشه‌بندی فایل‌محور در Next.js 15",
        "sub": "Next.js 15 App Directory Routing",
        "level": "مبتدی",
        "analogy": "مثل طبقات منظم یک ساختمان اداری؛ هر پوشه یک اتاق مشخص است و پرونده page.tsx در اتاق، محتوای آن طبقه را تشکیل می‌دهد.",
        "plain_exp": "در نکست ۱۵، مسیرها بر اساس پوشه‌های داخل فولدر app ساخته می‌شوند؛ هر پوشه یک URL جدید می‌سازد و فایل‌های خاص مثل page, layout, loading وظایف معینی دارند.",
        "real": "🏢 پروژه: معماری صفحات فروشگاه دیجی‌کالا و وب‌اپلیکیشن اسنپ\n⚠️ چالش فنی: مدیریت صدها مسیر تودرتو و هدرهای مشترک در سیستم‌های سنتی باعث تکرار کدهای HTML می‌شد.\n💡 معماری پروداکشن: ساخت layout.tsx مشترک در ریشه و ایجاد مسیرهای پویا مثل app/products/[slug]/page.tsx برای لود بلادرنگ هزاران کالا.",
        "code": """// app/products/[id]/page.tsx
interface PageProps {
  params: Promise<{ id: string }>; // در Next 15 پارامترها پرامیس هستند
}

export default async function ProductPage({ params }: PageProps) {
  const { id } = await params;
  return (
    <main className="p-6">
      <h1 className="text-2xl font-bold">مشخصات کالای شماره {id}</h1>
    </main>
  );
}""",
        "interview": "در Next.js 15 چرا params و searchParams اکنون Promise هستند؟ در نکست ۱۵ تمام APIهای مربوط به درخواست کاربر ناهمگام (Async) شدند تا موتور بتواند قبل از رسیدن درخواست کاربر، صفحه را با Partial Prerendering آماده‌سازی کند.",
        "sandbox": """
        <div style="background:#020617; padding:12px; border-radius:8px; border:1px solid #1e293b; font-family:monospace; font-size:12px; color:#38bdf8; direction:ltr; text-align:left;">
          app/<br>
          ├── layout.tsx &nbsp;&nbsp;&nbsp;<span style="color:#64748b;">(قالب سراسری HTML/Body)</span><br>
          ├── page.tsx &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#64748b;">(صفحه اصلی /)</span><br>
          ├── loading.tsx &nbsp;&nbsp;<span style="color:#64748b;">(اسکلتون سوسپنس آنی)</span><br>
          └── blog/[slug]/page.tsx <span style="color:#34d399;">(مسیر داینامیک)</span>
        </div>
        """,
        "problems": [
            {
                "tier": "آسان", "tier_color": "#10b981", "tier_bg": "rgba(16, 185, 129, 0.15)",
                "title": "مسئله ۱: ساخت روت ساده 'تماس با ما' در App Router",
                "desc": "ساختار پوشه و فایل page.tsx را برای ساخت مسیر /contact بنویسید.",
                "hint": "پوشه‌ای به نام contact در app بسازید و داخل آن page.tsx بگذارید.",
                "solution": """// app/contact/page.tsx
export default function ContactPage() {
  return (
    <div className="p-8">
      <h1 className="text-xl font-bold">تماس با ما</h1>
      <p>ایمیل: support@site.ir</p>
    </div>
  );
}"""
            },
            {
                "tier": "متوسط", "tier_color": "#f59e0b", "tier_bg": "rgba(245, 158, 11, 0.15)",
                "title": "مسئله ۲: دریافت پارامتر آیدی در Next.js 15 (Async Params)",
                "desc": "کامپوننت صفحه‌ای بنویسید که در مسیر /users/[userId] پارامتر userId را به صورت ناهمگام استخراج کند.",
                "hint": "در نکست ۱۵ حتماً باید const { userId } = await params نوشته شود.",
                "solution": """// app/users/[userId]/page.tsx
export default async function UserProfilePage({
  params
}: {
  params: Promise<{ userId: string }>;
}) {
  const { userId } = await params;
  return <h2>پروفایل کاربر شناسه: {userId}</h2>;
}"""
            },
            {
                "tier": "سخت", "tier_color": "#ef4444", "tier_bg": "rgba(239, 68, 68, 0.15)",
                "title": "مسئله ۳: مدیریت مسیرهای موازی (Parallel Routes) و رهگیری خطا",
                "desc": "یک layout بنویسید که هم‌زمان دو اسلات مستقل @analytics و @team را در یک صفحه کنار هم رندر کند و فایل error.tsx برای مهار کرش داشته باشد.",
                "hint": "از پراپ‌های اسلات @folder در آرگومان‌های Layout استفاده کنید.",
                "solution": """// app/dashboard/layout.tsx
export default function DashboardLayout({
  children,
  analytics,
  team
}: {
  children: React.ReactNode;
  analytics: React.ReactNode;
  team: React.ReactNode;
}) {
  return (
    <div className="grid grid-cols-3 gap-4 p-6">
      <div className="col-span-2">{children}</div>
      <aside>{analytics}</aside>
      <div>{team}</div>
    </div>
  );
}"""
            }
        ]
    },
    {
        "id": 2,
        "title": "کامپوننت‌های سروری و کلاینتی (RSC vs 'use client')",
        "sub": "React Server Components Architecture",
        "level": "مبتدی",
        "analogy": "پختن غذا در آشپزخانه رستوران (Server) و فقط آوردن بشقاب غذا سر میز، در مقابل آشپزی مسافرتی با پیک‌نیک وسط سالن (Client).",
        "plain_exp": "در نکست تمام کامپوننت‌ها به صورت پیش‌فرض سروری هستند (صفر بایت کد JS به مرورگر می‌رود). فقط وقتی نیاز به هوک‌هایی مثل useState یا کلیک کاربر دارید بالای فایل دستور 'use client' می‌نویسید.",
        "real": "🏢 پروژه: کاهش حجم باندل اولیه در فروشگاه‌های اینترنتی سنگین\n⚠️ چالش فنی: ارسال کدهای جاوا اسکریپت رندرینگ کتابخانه‌های بزرگ به موبایل کاربر باعث کندی لود اولیه می‌شود.\n💡 معماری پروداکشن: قرار دادن عملیات دیتابیس در کامپوننت سروری، و ایزوله کردن دکمه لایک یا سبد در کامپوننت‌های کوچک دارای 'use client'.",
        "code": """// Server Component (حجم جاوا اسکریپت در کلاینت = صفر بایت)
import db from '@/lib/db';
import LikeButton from './LikeButton'; // Client Component

export default async function ProductCard({ id }: { id: string }) {
  const product = await db.product.findUnique({ where: { id } });
  return (
    <div className="card">
      <h2>{product.title}</h2>
      <LikeButton initialLikes={product.likes} />
    </div>
  );
}""",
        "interview": "آیا می‌توان یک کامپوننت سروری را به عنوان فرزند داخل کامپوننت کلاینتی رندر کرد؟ بله! اما فقط از طریق children prop؛ نمی‌توانید مستقیماً درون یک کامپوننت با دستور 'use client' یک کامپوننت سروری را ایمپورت کنید.",
        "sandbox": """
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
          <div style="background:#020617; border:1px solid #f59e0b; padding:10px; border-radius:8px;">
            <span style="color:#f59e0b; font-weight:700; font-size:12px;">Server Component (Default)</span>
            <p style="font-size:11px; color:#94a3b8; margin-top:4px;">دسترسی مستقیم به دیتابیس / 0KB کد JS در مرورگر</p>
          </div>
          <div style="background:#020617; border:1px solid #38bdf8; padding:10px; border-radius:8px;">
            <span style="color:#38bdf8; font-weight:700; font-size:12px;">'use client' Component</span>
            <p style="font-size:11px; color:#94a3b8; margin-top:4px;">هوک‌های useState و رویدادهای onClick</p>
          </div>
        </div>
        """,
        "problems": [
            {
                "tier": "آسان", "tier_color": "#10b981", "tier_bg": "rgba(16, 185, 129, 0.15)",
                "title": "مسئله ۱: تبدیل کامپوننت دکمه به کلاینت با رویداد کلیک",
                "desc": "کامپوننتی برای افزایش شمارنده لایک بسازید که نیاز به استیت داشته باشد و دستور لازم 'use client' را داشته باشد.",
                "hint": "دستور 'use client' باید دقیقاً اولین خط فایل باشد.",
                "solution": """'use client';
import { useState } from 'react';

export default function LikeButton() {
  const [likes, setLikes] = useState(0);
  return (
    <button onClick={() => setLikes(l => l + 1)} className="btn">
      لایک: {likes}
    </button>
  );
}"""
            },
            {
                "tier": "متوسط", "tier_color": "#f59e0b", "tier_bg": "rgba(245, 158, 11, 0.15)",
                "title": "مسئله ۲: عبور از مرز کلاینت/سرور با اسلات Children",
                "desc": "یک کامپوننت مودال کلاینتی ('use client') بنویسید که محتوای سروری را از طریق prop فرزندان (children) بدون تبدیل آن به کلاینت رندر کند.",
                "hint": "در تعریف پراپ از children: React.ReactNode استفاده کنید.",
                "solution": """'use client';
import { useState } from 'react';

export default function ModalWrapper({ children }: { children: React.ReactNode }) {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <div>
      <button onClick={() => setIsOpen(true)}>باز کردن</button>
      {isOpen && <div className="modal">{children}</div>}
    </div>
  );
}"""
            },
            {
                "tier": "سخت", "tier_color": "#ef4444", "tier_bg": "rgba(239, 68, 68, 0.15)",
                "title": "مسئله ۳: بهینه‌سازی درخت کامپوننت و جلوگیری از آلودگی کلاینتی (Poisoning)",
                "desc": "ساختاری طراحی کنید که یک کامپوننت سروری سنگین دسترسی به دیتابیس را حفظ کند در حالی که یک نوار جستجوی کلاینتی در بالای آن تعبیه شده است.",
                "hint": "کامپوننت جستجو را برگ انتهایی درخت نگه دارید (Push Client Components to the Leaves).",
                "solution": """// ProductFeed.tsx (Server Component)
import SearchBar from './SearchBar'; // 'use client' leaf component
import db from '@/lib/db';

export default async function ProductFeed() {
  const products = await db.getProducts();
  return (
    <section>
      <SearchBar />
      <div className="grid">
        {products.map(p => <div key={p.id}>{p.name}</div>)}
      </div>
    </section>
  );
}"""
            }
        ]
    },
    {
        "id": 3,
        "title": "اکشن‌های سمت سرور (Server Actions: 'use server')",
        "sub": "Mutations & Form Handling",
        "level": "متوسط",
        "analogy": "مثل زدن دکمه تایید فاکتور که مستقیم در سرور پردازش می‌شود بدون اینکه نیاز باشد یک باجه جداگانه API باز کنی.",
        "plain_exp": "توابعی که با دستور 'use server' مشخص می‌شوند و مستقیماً روی سرور اجرا می‌شوند؛ می‌توانید فرم‌های HTML را مستقیماً بدون نوشتن کدهای پیچیده fetch به این توابع وصل کنید.",
        "real": "🏢 پروژه: ثبت سفارش خرید و ثبت‌نام در سامانه‌های سازمانی\n⚠️ چالش فنی: ساخت ده‌ها کنترلر جداگانه API Routes برای فرم‌های ساده ورود و ویرایش پروفایل.\n💡 معماری پروداکشن: ساخت Server Actions مستقیم در پوشه actions/ برای اعتبارسنجی در سرور و تغییر دیتابیس همراه با revalidatePath برای تازه شدن آنی صفحه.",
        "code": """// app/actions/createPost.ts
'use server';
import db from '@/lib/db';
import { revalidatePath } from 'next/cache';

export async function createPostAction(formData: FormData) {
  const title = formData.get('title') as string;
  await db.post.create({ data: { title } });
  revalidatePath('/blog'); // تازه‌سازی کش صفحه وبلاگ
}""",
        "interview": "امنیت در Server Actions چگونه تامین می‌شود؟ برخلاف توابع عادی، Server Actionها از طریق POST ارسال می‌شوند و باید حتماً بررسی احراز هویت کاربر و اعتبارسنجی ورودی‌ها با Zod در بدنه همان اکشن انجام شود.",
        "sandbox": """
        <div style="background:#020617; padding:12px; border-radius:8px; border:1px solid #10b981;">
          <form onsubmit="event.preventDefault(); alert('اکشن سرور اجرا شد: revalidatePath(\\'/feed\\')');" style="display:flex; gap:8px;">
            <input type="text" placeholder="عنوان خبر..." style="background:#0f172a; border:1px solid #334155; color:#fff; padding:6px 10px; border-radius:6px; font-size:12px; outline:none;">
            <button type="submit" style="background:#10b981; color:#022c22; font-weight:700; border:none; padding:6px 14px; border-radius:6px; font-size:12px; cursor:pointer;">
              اجرای Server Action
            </button>
          </form>
        </div>
        """,
        "problems": [
            {
                "tier": "آسان", "tier_color": "#10b981", "tier_bg": "rgba(16, 185, 129, 0.15)",
                "title": "مسئله ۱: ساخت یک اکشن سرور برای فرم ارسال نظر",
                "desc": "یک تابع 'use server' بنویسید که داده‌های فرم را بگیرد و متن کامنت را استخراج کند.",
                "hint": "از formData.get('comment') استفاده کنید.",
                "solution": """'use server';

export async function submitComment(formData: FormData) {
  const comment = formData.get('comment');
  console.log('کامنت ثبت‌شده در سرور:', comment);
}"""
            },
            {
                "tier": "متوسط", "tier_color": "#f59e0b", "tier_bg": "rgba(245, 158, 11, 0.15)",
                "title": "مسئله ۲: اعتبارسنجی Zod و مدیریت خطا در Server Action",
                "desc": "اکشنی بنویسید که ایمیل کاربر را با Zod اعتبارسنجی کند و در صورت خطا پیام مناسب برگرداند.",
                "hint": "در صورت نامعتبر بودن مقدار { success: false, error: ... } برگردانید.",
                "solution": """'use server';
import { z } from 'zod';

const schema = z.object({
  email: z.string().email('فرمت ایمیل نامعتبر است')
});

export async function registerEmail(formData: FormData) {
  const parse = schema.safeParse({ email: formData.get('email') });
  if (!parse.success) {
    return { error: parse.error.issues[0].message };
  }
  return { success: true };
}"""
            },
            {
                "tier": "سخت", "tier_color": "#ef4444", "tier_bg": "rgba(239, 68, 68, 0.15)",
                "title": "مسئله ۳: پیاده‌سازی فرم با useActionState و وضعیت Pending در Next 15 / React 19",
                "desc": "یک فرم ورود با هوک مدرن useActionState بسازید که دکمه ارسال را در حین پردازش به حالت لودینگ ببرد.",
                "hint": "از const [state, action, isPending] = useActionState(serverFn, initial) استفاده کنید.",
                "solution": """'use client';
import { useActionState } from 'react';
import { authenticate } from '@/app/actions';

export default function LoginForm() {
  const [state, formAction, isPending] = useActionState(authenticate, null);

  return (
    <form action={formAction}>
      <input name="email" required />
      <button type="submit" disabled={isPending}>
        {isPending ? 'در حال ورود...' : 'ورود به سیستم'}
      </button>
      {state?.error && <p className="error">{state.error}</p>}
    </form>
  );
}"""
            }
        ]
    },
    {
        "id": 4,
        "title": "میدل‌ورها و حفاظت مسیرها (Next.js Middleware & Auth Guards)",
        "sub": "Edge Network Security",
        "level": "پیشرفته",
        "analogy": "دروازه‌بان ورزشگاه که قبل از ورود هر فرد به راهروها بلیت او را چک می‌کند و اگر بلیت نداشت به گیشه فروش بلیت می‌فرستد.",
        "plain_exp": "کدی که در لایه لبه شبکه (Edge) قبل از رسیدن درخواست به هر صفحه‌ای اجرا می‌شود؛ برای بررسی کوکی ورود، ریدایرکت خودکار به /login، و تغییر هدرها.",
        "real": "🏢 پروژه: حفاظت از پنل ادمین و تفکیک مشتریان شرکتی در دیجی‌کالا\n⚠️ چالش فنی: جلوگیری از لود حتی ۱ بایت از کدهای پنل مدیریت برای کاربران عادی.\n💡 معماری پروداکشن: تنظیم middleware.ts در ریشه پروژه با الگوی matcher: ['/admin/:path*'] برای مسدود کردن ورود بدون توکن امنیتی JWT.",
        "code": """// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const token = request.cookies.get('auth_token')?.value;

  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*']
};""",
        "interview": "میدل‌ور نکست در کجا اجرا می‌شود؟ در Edge Runtime بر پایه Web APIs (مانند Fetch و Request)؛ به همین دلیل به متدهای سنگین نود مانند fs یا اتصال مستقیم به پایگاه داده در میدل‌ور دسترسی ندارید.",
        "sandbox": """
        <div style="background:#020617; padding:10px; border-radius:8px; border:1px solid #38bdf8; font-size:12px;">
          <span style="color:#38bdf8; font-weight:700;">میدل‌ور Edge فعال:</span>
          <div style="color:#cbd5e1; margin-top:4px;">درخواست به /dashboard ➔ بررسی توکن کوکی ➔ تایید عبور ✓</div>
        </div>
        """,
        "problems": [
            {
                "tier": "آسان", "tier_color": "#10b981", "tier_bg": "rgba(16, 185, 129, 0.15)",
                "title": "مسئله ۱: ریدایرکت ساده کاربر در میدل‌ور",
                "desc": "میدل‌وری بنویسید که هر کس وارد مسیر /old-shop شد را به مسیر جدید /shop منتقل کند.",
                "hint": "از NextResponse.redirect(new URL('/shop', request.url)) استفاده کنید.",
                "solution": """import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  if (request.nextUrl.pathname === '/old-shop') {
    return NextResponse.redirect(new URL('/shop', request.url));
  }
}"""
            },
            {
                "tier": "متوسط", "tier_color": "#f59e0b", "tier_bg": "rgba(245, 158, 11, 0.15)",
                "title": "مسئله ۲: افزودن هدر امنیتی سفارشی به پاسخ‌ها",
                "desc": "میدل‌وری بنویسید که هدر X-Security-Version: 2.0 را به تمام درخواست‌های صفحه اضافه کند.",
                "hint": "شیء response ساخته و با response.headers.set هدر را تزریق کنید.",
                "solution": """import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const response = NextResponse.next();
  response.headers.set('X-Security-Version', '2.0');
  return response;
}"""
            },
            {
                "tier": "سخت", "tier_color": "#ef4444", "tier_bg": "rgba(239, 68, 68, 0.15)",
                "title": "مسئله ۳: احراز هویت چندلایه با تطبیق نقش‌ها (RBAC) در Middleware",
                "desc": "میدل‌وری بنویسید که کوکی توکن را اعتبارسنجی کند و اگر کاربر نقش 'admin' نداشت دسترسی به /super-admin را با خطای ۴۰۳ مسدود کند.",
                "hint": "توکن JWT را بازخوانی کرده و فیلد role را بررسی نمایید.",
                "solution": """import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const role = request.cookies.get('user_role')?.value;

  if (request.nextUrl.pathname.startsWith('/super-admin') && role !== 'admin') {
    return new NextResponse('دسترسی غیرمجاز (خطای ۴۰۳)', { status: 403 });
  }
  return NextResponse.next();
}"""
            }
        ]
    },
    {
        "id": 5,
        "title": "قابلیت‌های انقلابی Next.js 15 و پیش‌رندر ناقص (Partial Prerendering - PPR)",
        "sub": "Next.js 15 Turbopack & PPR",
        "level": "پیشرفته",
        "analogy": "چاپ فوری کادر و هدر روزنامه از شب قبل (استاتیک)، و چاپ زنده قیمت طلا و ساعت در ثانیه آخر روی همان کاغذ (داینامیک).",
        "plain_exp": "ترکیب سرعت ماورایی SSG با پویایی SSR؛ بخش‌های ثابت صفحه مثل هدر در صدم ثانیه از کش CDN باز می‌شوند، و فقط باکس قیمت یا سبد خرید با Suspense به صورت استریم در جای خود پر می‌شوند.",
        "real": "🏢 پروژه: صفحات کالا در رویدادهای شلوغ تخفیفی با میلیون‌ها درخواست\n⚠️ چالش فنی: کندی لود اولیه اگر کل صفحه SSR شود، و قدیمی بودن داده اگر کل صفحه SSG شود.\n💡 معماری پروداکشن: فعال‌سازی ppr: 'incremental' در next.config.ts برای تحویل آنی ساختار صفحه و لود استریم بخش قیمت کالا.",
        "code": """// next.config.ts
import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  experimental: {
    ppr: 'incremental', // فعال‌سازی پیش‌رندر جزئی
  },
};
export default nextConfig;""",
        "interview": "تفاوت Turbopack با Webpack چیست؟ توربوپک موتور باندلر اختصاصی و پرسرعت Next.js است که با زبان Rust بازنویسی شده و تا ۷۰۰ برابر سریع‌تر از وب‌پک تغییرات کدها را اعمال می‌کند.",
        "sandbox": """
        <div style="background:#020617; padding:10px; border-radius:8px; border:1px solid #10b981; font-size:12px;">
          <div style="color:#10b981; font-weight:700;">Partial Prerendering (PPR):</div>
          <div style="color:#94a3b8; margin-top:2px;">هدر و بنر (استاتیک CDN) + قیمت زنده (استریم سرور با Suspense)</div>
        </div>
        """,
        "problems": [
            {
                "tier": "آسان", "tier_color": "#10b981", "tier_bg": "rgba(16, 185, 129, 0.15)",
                "title": "مسئله ۱: فعال‌سازی توربوپک در حالت توسعه",
                "desc": "دستور اجرای سرور توسعه با توربوپک را در package.json تنظیم کنید.",
                "hint": "از فلگ --turbopack در اسکریپت dev استفاده کنید.",
                "solution": """// package.json
{
  "scripts": {
    "dev": "next dev --turbopack",
    "build": "next build",
    "start": "next start"
  }
}"""
            },
            {
                "tier": "متوسط", "tier_color": "#f59e0b", "tier_bg": "rgba(245, 158, 11, 0.15)",
                "title": "مسئله ۲: پیاده‌سازی سوسپنس برای جداسازی بخش استاتیک از داینامیک",
                "desc": "صفحه‌ای بنویسید که هدر آن استاتیک باشد ولی قیمت کالا درون یک مرز Suspense قرار گرفته باشد.",
                "hint": "از <Suspense fallback={<Skeleton />}> استفاده کنید.",
                "solution": """import { Suspense } from 'react';
import LivePrice from './LivePrice';

export default function ProductPage() {
  return (
    <div>
      <header><h1>کفش نایک اورجینال</h1></header>
      <Suspense fallback={<p>در حال دریافت قیمت لحظه‌ای...</p>}>
        <LivePrice />
      </Suspense>
    </div>
  );
}"""
            },
            {
                "tier": "سخت", "tier_color": "#ef4444", "tier_bg": "rgba(239, 68, 68, 0.15)",
                "title": "مسئله ۳: پیکربندی بازتولید بر اساس تگ (On-Demand Revalidation via Tags)",
                "desc": "درخواستی بنویسید که تگ 'products' داشته باشد و یک سرور اکشن برای بی‌اعتبار کردن فوری این تگ با revalidateTag بنویسید.",
                "hint": "از fetch(url, { next: { tags: ['products'] } }) استفاده کنید.",
                "solution": """// در کامپوننت سروری:
const res = await fetch('https://api.site.com/products', {
  next: { tags: ['products'] }
});

// در سرور اکشن بعد از تغییر قیمت:
'use server';
import { revalidateTag } from 'next/cache';

export async function updateProductPrice() {
  // آپدیت دیتابیس
  revalidateTag('products'); // کش تمام صفحات این تگ در لحظه پاک شد!
}"""
            }
        ]
    }
]

print("Next.js 15 Specialist Dataset prepared.")
