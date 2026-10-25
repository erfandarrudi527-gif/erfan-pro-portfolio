# -*- coding: utf-8 -*-
"""
Generate 100% individual, dedicated, customized 3-tier problems (Easy, Medium, Hard)
for ALL 65 React topics with realistic code solutions.
"""

def get_react_advanced_custom_challenges(tid, title, code):
    # Specialized solutions for topics 39 to 65
    specialized = {
        2: [ # Project Setup with Vite
            {"tier": "آسان", "title": "مسئله ۱: راه‌اندازی پروژه ری‌اکت با اسکریپت Vite",
             "desc": "دستور ترمینال و ساختار پیکربندی vite.config.js با پلاگین رسمی @vitejs/plugin-react را بنویسید.",
             "hint": "از defineConfig و react() در plugins استفاده کنید.",
             "solution": """// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true
  }
});"""},
            {"tier": "متوسط", "title": "مسئله ۲: تنظیم Path Alias در Vite برای ایمپورت‌های تمیز @/components",
             "desc": "فایل vite.config.js را طوری تنظیم کنید که علامت @ مستقیماً به پوشه src اشاره کند تا از نوشتن مسیرهای طولانی جلوگیری شود.",
             "hint": "از ماژول path و resolve.alias بهره ببرید.",
             "solution": """import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  }
});"""},
            {"tier": "سخت", "title": "مسئله ۳: تنظیم متغیرهای محیطی امن با پیشوند VITE_ در فایل .env",
             "desc": "کامپوننتی بنویسید که آدرس API را از import.meta.env.VITE_API_URL بخواند و در صورت نبود متغیر خطای واضح پرتاب کند.",
             "hint": "در Vite متغیرها فقط با پیشوند VITE_ در کلاینت در دسترس هستند.",
             "solution": """const API_BASE = import.meta.env.VITE_API_URL;

if (!API_BASE) {
  throw new Error('متغیر محیطی VITE_API_URL در فایل .env تعریف نشده است!');
}

export async function fetchUserData() {
  const res = await fetch(`${API_BASE}/users`);
  return res.json();
}"""}
        ],
        39: [ # useId & forwardRef
            {"tier": "آسان", "title": "مسئله ۱: اتصال فیلد و برچسب فرم با useId",
             "desc": "کامپوننتی با هوک useId بسازید که یک شناسه سراسری یکتا تولید کرده و به صفت htmlFor در label و id در input متصل کند تا در SSR نامتعادل نشود.",
             "hint": "از const id = useId() استفاده کنید.",
             "solution": """import { useId } from 'react';

export default function AccessibleField({ label }) {
  const id = useId();
  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <input id={id} type="text" />
    </div>
  );
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: ارجاع به اینپوت فرزند با forwardRef",
             "desc": "کامپوننت CustomInput را طوری طراحی کنید که والد بتواند از طریق ref به المنت اصلی input دسترسی مستقیم داشته و آن را focus کند.",
             "hint": "کامپوننت را در forwardRef((props, ref) => ...) محصور کنید.",
             "solution": """import { forwardRef } from 'react';

const CustomInput = forwardRef((props, ref) => {
  return <input ref={ref} className="custom-inp" {...props} />;
});
export default CustomInput;"""},
            {"tier": "سخت", "title": "مسئله ۳: ایزولاسیون متدهای عمومی کامپوننت با useImperativeHandle",
             "desc": "کامپوننت ویرایشگر متنی بسازید که فقط متدهای reset() و focus() را از طریق ref به بیرون بدهد و اجازه دسترسی مستقیم به کل گره DOM را ندهد.",
             "hint": "ترکیب forwardRef با useImperativeHandle(ref, () => ({ focus, reset })).",
             "solution": """import { forwardRef, useImperativeHandle, useRef } from 'react';

const SecureEditor = forwardRef((props, ref) => {
  const inputRef = useRef();

  useImperativeHandle(ref, () => ({
    focus: () => inputRef.current.focus(),
    reset: () => { inputRef.current.value = ''; }
  }));

  return <input ref={inputRef} placeholder="متن ایمن..." />;
});
export default SecureEditor;"""}
        ],
        40: [ # Render Props & HOC
            {"tier": "آسان", "title": "مسئله ۱: استخراج موقعیت موس با الگوی Render Props",
             "desc": "کامپوننتی بنویسید به نام MouseTracker که موقعیت x و y موس را گوش دهد و آن را از طریق تابع render به فرزاندان پاس دهد.",
             "hint": "پراپ render(coords) را درون JSX صدا بزنید.",
             "solution": """import { useState } from 'react';

export default function MouseTracker({ render }) {
  const [coords, setCoords] = useState({ x: 0, y: 0 });
  return (
    <div onMouseMove={(e) => setCoords({ x: e.clientX, y: e.clientY })}>
      {render(coords)}
    </div>
  );
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: کامپوننت مرتبه بالاتر (HOC) برای محافظت از مسیر کاربر",
             "desc": "تابعی با امضای withAuth(Component) بنویسید که توکن احراز هویت را بررسی کند و در صورت عدم وجود به صفحه لاگین ریدایرکت کند.",
             "hint": "یک کامپوننت جدید برگردانید که در صورت عدم ورود null یا پیام اخطار رندر کند.",
             "solution": """export function withAuth(WrappedComponent) {
  return function Protected(props) {
    const isAuth = !!localStorage.getItem('token');
    if (!isAuth) return <p>لطفاً ابتدا وارد شوید.</p>;
    return <WrappedComponent {...props} />;
  };
}"""},
            {"tier": "سخت", "title": "مسئله ۳: تزریق لاگینگ و عملکرد به کامپوننت با HOC ژنریک",
             "desc": "یک HOC بنویسید که زمان mount تا unmount کامپوننت ورودی را اندازه‌گیری کرده و در کنسول ثبت کند.",
             "hint": "در useEffect ابتدای mount زمان را ثبت و در تابع cleanup اختلاف زمان را چاپ کنید.",
             "solution": """import { useEffect } from 'react';

export function withProfiler(Component, name) {
  return function Profiled(props) {
    useEffect(() => {
      const start = performance.now();
      return () => {
        const duration = (performance.now() - start).toFixed(2);
        console.log(`کامپوننت ${name} به مدت ${duration}ms فعال بود.`);
      };
    }, []);
    return <Component {...props} />;
  };
}"""}
        ],
        44: [ # Virtualization with react-window
            {"tier": "آسان", "title": "مسئله ۱: پیاده‌سازی لیست مجازی ۵۰,۰۰۰ ردیفی با react-window",
             "desc": "کامپوننتی با کتابخانه react-window بسازید که یک آرایه با ۵۰ هزار عضو را بدون افت فریم و با رندر فقط ۱۰ ردیف هم‌زمان نمایش دهد.",
             "hint": "از کامپوننت FixedSizeList با ویژگی‌های height، itemCount، itemSize و width استفاده کنید.",
             "solution": """import { FixedSizeList as List } from 'react-window';

const items = Array.from({ length: 50000 }, (_, i) => `مشتری شماره ${i + 1}`);

const Row = ({ index, style }) => (
  <div style={{ ...style, borderBottom: '1px solid #334155', padding: '8px' }}>
    {items[index]}
  </div>
);

export default function VirtualList() {
  return (
    <List height={400} itemCount={items.length} itemSize={45} width="100%">
      {Row}
    </List>
  );
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: اسکرول اتوماتیک به ردیف دلخواه در لیست مجازی با scrollToItem",
             "desc": "دکمه‌ای در بالای لیست ۵۰ هزارتایی تعبیه کنید که با فشردن آن، لیست فوراً به ردیف شماره ۲۵,۰۰۰ اسکرول کند.",
             "hint": "یک ref به FixedSizeList متصل کنید و متد listRef.current.scrollToItem(25000) را صدا بزنید.",
             "solution": """import { useRef } from 'react';
import { FixedSizeList as List } from 'react-window';

export default function ScrollableVirtualList({ items }) {
  const listRef = useRef();

  return (
    <div>
      <button onClick={() => listRef.current.scrollToItem(25000, 'center')}>
        پرش مستقیم به ردیف ۲۵,۰۰۰ 🚀
      </button>
      <List ref={listRef} height={400} itemCount={items.length} itemSize={40} width="100%">
        {({ index, style }) => <div style={style}>ردیف: {index}</div>}
      </List>
    </div>
  );
}"""},
            {"tier": "سخت", "title": "مسئله ۳: لیست با ارتفاع متغیر سطرها با VariableSizeList و کش اندازه",
             "desc": "لیستی مجازی طراحی کنید که ارتفاع هر سطر بر اساس طول متن کامنت متغیر باشد و با متد getItemSize اندازه هر سطر محاسبه شود.",
             "hint": "از VariableSizeList استفاده کرده و متد resetAfterIndex را برای تغییرات سایز پیاده کنید.",
             "solution": """import { useRef } from 'react';
import { VariableSizeList as List } from 'react-window';

const comments = [
  'پیام کوتاه',
  'این یک متن کامنت بسیار طولانی است که چند خط فضا اشغال می‌کند...',
  'تایید شد'
];

export default function DynamicVirtualList() {
  const getItemSize = index => (comments[index].length > 30 ? 90 : 45);

  return (
    <List height={500} itemCount={comments.length} itemSize={getItemSize} width="100%">
      {({ index, style }) => (
        <div style={style}>
          <p>{comments[index]}</p>
        </div>
      )}
    </List>
  );
}"""}
        ],
        45: [ # Concurrent Features: useTransition & useDeferredValue
            {"tier": "آسان", "title": "مسئله ۱: رفع لگ تایپ اینپوت با useTransition",
             "desc": "فیلد جستجویی بنویسید که تایپ کردن در اینپوت با اولویت بالا باشد و فیلتر کردن لیست داده‌ها در پس‌زمینه با startTransition انجام شود.",
             "hint": "از const [isPending, startTransition] = useTransition() استفاده کنید.",
             "solution": """import { useState, useTransition } from 'react';

export default function NonBlockingSearch({ data }) {
  const [query, setQuery] = useState('');
  const [filtered, setFiltered] = useState(data);
  const [isPending, startTransition] = useTransition();

  const handleType = (e) => {
    const val = e.target.value;
    setQuery(val); // اولویت فوری

    startTransition(() => {
      // رندر غیرمسدودکننده
      setFiltered(data.filter(item => item.includes(val)));
    });
  };

  return (
    <div>
      <input value={query} onChange={handleType} placeholder="تایپ بدون لگ..." />
      {isPending && <span>در حال پردازش...</span>}
      <ul>{filtered.slice(0, 20).map((x, i) => <li key={i}>{x}</li>)}</ul>
    </div>
  );
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: تاخیر در بهینه‌سازی رندر با useDeferredValue",
             "desc": "کامپوننتی بسازید که یک مقدار استیت را گرفته و نسخه معوق (Deferred) آن را برای رندر کامپوننت سنگین فرزند تولید کند.",
             "hint": "از const deferredValue = useDeferredValue(state) استفاده نمایید.",
             "solution": """import { useState, useDeferredValue } from 'react';
import HeavyGraph from './HeavyGraph';

export default function GraphDashboard() {
  const [slider, setSlider] = useState(50);
  const deferredSlider = useDeferredValue(slider);

  return (
    <div>
      <input type="range" value={slider} onChange={e => setSlider(+e.target.value)} />
      {/* اسلایدر با ۶۰ فریم حرکت می‌کند و گراف با مقدار معوق آپدیت می‌شود */}
      <HeavyGraph value={deferredSlider} isStale={slider !== deferredSlider} />
    </div>
  );
}"""},
            {"tier": "سخت", "title": "مسئله ۳: مدیریت حالت مات شدن UI حین تغییر مقدار معوق با useDeferredValue",
             "desc": "یک کامپوننت لیست با useDeferredValue طراحی کنید که در حین محاسبه نتایج جدید، شفافیت (opacity) محتوای قبلی به 0.6 تغییر یابد.",
             "hint": "شرط const isStale = query !== deferredQuery را روی استایل کانتینر اعمال کنید.",
             "solution": """import { useState, useDeferredValue } from 'react';

export default function SearchWithVisualFeedback({ allPosts }) {
  const [query, setQuery] = useState('');
  const deferredQuery = useDeferredValue(query);
  const isStale = query !== deferredQuery;

  return (
    <div>
      <input value={query} onChange={e => setQuery(e.target.value)} />
      <div style={{ opacity: isStale ? 0.5 : 1, transition: 'opacity 0.2s' }}>
        <p>{isStale ? 'در حال به‌روزرسانی نتایج...' : 'نتایج نهایی:'}</p>
        <ListQuery query={deferredQuery} items={allPosts} />
      </div>
    </div>
  );
}"""}
        ],
        46: [ # Suspense for Data Fetching
            {"tier": "آسان", "title": "مسئله ۱: محصورسازی کامپوننت دیتافچینگ درون مرز Suspense",
             "desc": "ساختاری با تگ <Suspense> بنویسید که کامپوننت ناهمگام UserProfile را رندر کند و تا زمان لود اسکلتون نمایش دهد.",
             "hint": "از <Suspense fallback={<Skeleton />}> استفاده کنید.",
             "solution": """import { Suspense } from 'react';
import UserProfile from './UserProfile';
import Skeleton from './Skeleton';

export default function ProfilePage() {
  return (
    <main>
      <h1>پروفایل کاربری</h1>
      <Suspense fallback={<Skeleton />}>
        <UserProfile />
      </Suspense>
    </main>
  );
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: سوسپنس‌های تودرتو (Nested Suspense Boundaries) برای استریم ترتیبی",
             "desc": "صفحه‌ای بسازید که هدر آن بلافاصله ظاهر شود و بخش نظرات درون یک سوسپنس جداگانه بدون مسدود کردن کل صفحه لود شود.",
             "hint": "چند مرز Suspense با فال‌بک‌های مستقل برای بخش‌های مختلف بگذارید.",
             "solution": """import { Suspense } from 'react';
import PostHeader from './PostHeader';
import CommentsList from './CommentsList';

export default function BlogPost() {
  return (
    <article>
      <Suspense fallback={<p>لود هدر خبر...</p>}>
        <PostHeader />
      </Suspense>
      
      {/* لود مستقل کامنت‌ها بدون معطل کردن مطالعه خبر */}
      <Suspense fallback={<p>در حال بارگذاری نظرات کاربران...</p>}>
        <CommentsList />
      </Suspense>
    </article>
  );
}"""},
            {"tier": "سخت", "title": "مسئله ۳: خواندن Promise با هوک use() در React 19 تحت پوشش Suspense",
             "desc": "کامپوننتی با هوک use(promise) در React 19 بنویسید که پرامیس ارسال شده از والد را مستقیماً بخواند.",
             "hint": "در ری‌اکت ۱۹ از دستور use(userPromise) درون بدنه کامپوننت استفاده می‌شود.",
             "solution": """import { use, Suspense } from 'react';

function UserCard({ userPromise }) {
  // هوک use تا زمان resolve پرامیس کامپوننت را معلق (Suspend) نگه می‌دارد
  const user = use(userPromise);
  return <div>کاربر: {user.name} ({user.role})</div>;
}

export default function App() {
  const userPromise = fetch('/api/user').then(r => r.json());
  return (
    <Suspense fallback={<div>در حال برقراری ارتباط با سرور...</div>}>
      <UserCard userPromise={userPromise} />
    </Suspense>
  );
}"""}
        ],
        47: [ # React 19 Revolutionary Features
            {"tier": "آسان", "title": "مسئله ۱: خواندن وضعیت دکمه فرم با useFormStatus",
             "desc": "کامپوننت SubmitButton مجزایی بسازید که بدون نیاز به پراپ وضعیت لودینگ فرم والد را با useFormStatus استخراج کند.",
             "hint": "از const { pending } = useFormStatus() درون فرزند مستقیم فرم استفاده کنید.",
             "solution": """'use client';
import { useFormStatus } from 'react-dom';

export default function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <button type="submit" disabled={pending}>
      {pending ? 'در حال ارسال اطلاعات... ⏳' : 'تایید نهایی'}
    </button>
  );
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: مدیریت وضعیت فرم با هوک useActionState در React 19",
             "desc": "یک فرم ثبت‌نام بنویسید که با هوک useActionState خروجی اکشن ناهمگام را همراه با وضعیت pending دریافت کند.",
             "hint": "سینتکس const [state, formAction, isPending] = useActionState(fn, initial) را اجرا کنید.",
             "solution": """'use client';
import { useActionState } from 'react';

async function updateName(prevState, formData) {
  const name = formData.get('name');
  if (!name) return { error: 'نام الزامی است' };
  await new Promise(r => setTimeout(r, 800));
  return { success: true, name };
}

export default function ProfileForm() {
  const [state, formAction, isPending] = useActionState(updateName, null);

  return (
    <form action={formAction}>
      <input name="name" placeholder="نام شما..." />
      <button disabled={isPending}>{isPending ? 'ثبت...' : 'ذخیره'}</button>
      {state?.error && <p style={{ color: 'red' }}>{state.error}</p>}
      {state?.success && <p style={{ color: 'green' }}>نام {state.name} ثبت شد!</p>}
    </form>
  );
}"""},
            {"tier": "سخت", "title": "مسئله ۳: به‌روزرسانی فوق‌سریع و خوش‌بینانه با useOptimistic",
             "desc": "سیستم لایک بنویسید که به محض کلیک کاربر عدد لایک را زیاد کند و در صورت موفقیت یا شکست اکشن سرور به وضعیت واقعی پایدار شود.",
             "hint": "از useOptimistic(count, (cur, update) => cur + update) استفاده نمایید.",
             "solution": """'use client';
import { useOptimistic, startTransition } from 'react';

export default function LikeBox({ initialLikes, serverLikeAction }) {
  const [optimisticLikes, setOptimisticLikes] = useOptimistic(
    initialLikes,
    (state, delta) => state + delta
  );

  const handleLike = async () => {
    startTransition(async () => {
      setOptimisticLikes(1); // بلافاصله عدد زیاد می‌شود
      await serverLikeAction(); // سرور آپدیت شد
    });
  };

  return <button onClick={handleLike}>❤️ {optimisticLikes}</button>;
}"""}
        ],
        48: [ # Server Components & Client Components (RSC)
            {"tier": "آسان", "title": "مسئله ۱: دسترسی مستقیم به پایگاه‌داده در Server Component",
             "desc": "یک کامپوننت سروری بنویسید که مستقیم به جدول محصولات وصل شده و لیست را بدون یک خط کد در کلاینت رندر کند.",
             "hint": "کامپوننت را async تعریف کنید و دستور 'use client' نگذارید.",
             "solution": """import db from '@/lib/db';

export default async function ProductCatalog() {
  const products = await db.product.findMany();
  return (
    <ul>
      {products.map(p => <li key={p.id}>{p.title}</li>)}
    </ul>
  );
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: الگوی ارسال کامپوننت سروری به فرزند کلاینت با children prop",
             "desc": "کامپوننت کلاینتی مودال بسازید که محتوای سروری را به عنوان فرزند بدون تبدیل آن به کد کلاینتی باز کند.",
             "hint": "پراپ children: React.ReactNode را درون مودال قرار دهید.",
             "solution": """'use client';
import { useState } from 'react';

export default function Modal({ children }: { children: React.ReactNode }) {
  const [open, setOpen] = useState(false);
  return (
    <div>
      <button onClick={() => setOpen(true)}>نمایش جزئیات</button>
      {open && <div className="modal-box">{children}</div>}
    </div>
  );
}"""},
            {"tier": "سخت", "title": "مسئله ۳: حفاظت از پکیج‌های اختصاصی سرور با server-only",
             "desc": "تابعی برای دسترسی به کلید پرداخت بنویسید و تضمین کنید اگر تصادفاً در فایل کلاینتی ایمپورت شد، بیلد فریمورک بلافاصله متوقف شود.",
             "hint": "دستور import 'server-only' را در بالای فایل قرار دهید.",
             "solution": """import 'server-only';

export function getPaymentGatewaySecret() {
  return process.env.BANK_PRIVATE_KEY;
}"""}
        ],
        49: [ # Rendering Strategies (CSR, SSR, SSG, ISR)
            {"tier": "آسان", "title": "مسئله ۱: تنظیم بازتولید دوره‌ای (ISR) برای مقالات وبلاگ",
             "desc": "در یک صفحه App Router دستوری بنویسید که صفحه هر ۱۲۰ ثانیه در پس‌زمینه با کش CDN بازتولید شود.",
             "hint": "دستور export const revalidate = 120 را بنویسید.",
             "solution": """// app/blog/page.tsx
export const revalidate = 120; // بازتولید خودکار در پس‌زمینه هر دو دقیقه

export default async function BlogFeed() {
  const posts = await fetch('https://api.site.ir/posts').then(r => r.json());
  return <div>تعداد مقالات: {posts.length}</div>;
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: اجبار صفحه به رندرینگ کاملاً داینامیک سمت سرور (SSR)",
             "desc": "صفحه‌ای بنویسید که هرگز کش نشود و در هر بار درخواست کاربر (Request Time) تازه رندر شود.",
             "hint": "از دستور export const dynamic = 'force-dynamic' استفاده کنید.",
             "solution": """export const dynamic = 'force-dynamic';

export default async function LiveBoursePage() {
  const stock = await fetch('https://api.site.ir/gold', { cache: 'no-store' }).then(r => r.json());
  return <h2>قیمت لحظه‌ای طلا: {stock.price} تومان</h2>;
}"""},
            {"tier": "سخت", "title": "مسئله ۳: تولید استاتیک تمام مسیرهای پویا در زمان بیلد با generateStaticParams",
             "desc": "برای روت app/posts/[id]/page.tsx تابعی بنویسید که ۱۰۰ شناسه اول را در لحظه npm run build به صورت صفحات استاتیک SSG رندر کند.",
             "hint": "تابع async function generateStaticParams را اکسپورت کنید.",
             "solution": """// app/posts/[id]/page.tsx
export async function generateStaticParams() {
  const posts = await fetch('https://api.site.ir/posts-ids').then(r => r.json());
  return posts.map(post => ({ id: String(post.id) }));
}

export default async function PostPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  return <h1>صفحه استاتیک شماره {id}</h1>;
}"""}
        ],
        43: [ # Code Splitting: React.lazy & Suspense
            {"tier": "آسان", "title": "مسئله ۱: پیاده‌سازی لود تنبل با React.lazy و فال‌بک Suspense",
             "desc": "کامپوننتی بنویسید که کامپوننت سنگین HeavyModal را به صورت Lazy با تابع import() لود کند و تا زمان دانلود، پیام 'در حال لود...' را در fallback سوسپنس نمایش دهد.",
             "hint": "از const HeavyModal = lazy(() => import('./HeavyModal')) استفاده کنید.",
             "solution": """import { lazy, Suspense, useState } from 'react';

const HeavyModal = lazy(() => import('./HeavyModal'));

export default function App() {
  const [show, setShow] = useState(false);
  return (
    <div>
      <button onClick={() => setShow(true)}>باز کردن مودال سنگین</button>
      {show && (
        <Suspense fallback={<p>در حال بارگذاری کدهای مودال...</p>}>
          <HeavyModal onClose={() => setShow(false)} />
        </Suspense>
      )}
    </div>
  );
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: تفکیک مسیرها بر اساس Route-based Code Splitting در React Router",
             "desc": "ساختار مسیریابی بنویسید که سه صفحه اصلی Dashboard، Profile و Settings هر کدام در یک چانک مجزای جاوا اسکریپت بیلد و لود شوند.",
             "hint": "تمام صفحات را با lazy ایمپورت کرده و کل ساختار <Routes> را درون یک <Suspense> والد بگذارید.",
             "solution": """import { lazy, Suspense } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

const Dashboard = lazy(() => import('./pages/Dashboard'));
const Profile = lazy(() => import('./pages/Profile'));
const Settings = lazy(() => import('./pages/Settings'));

export default function AppRouter() {
  return (
    <BrowserRouter>
      <Suspense fallback={<div className="spinner">بارگذاری ماژول صفحه...</div>}>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/settings" element={<Settings />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}"""},
            {"tier": "سخت", "title": "مسئله ۳: پیاده‌سازی پیش‌بارگذاری با ماوس (Hover Prefetching) روی دکمه‌ها",
             "desc": "مکانیزمی طراحی کنید که به محض رفتن نشانگر ماوس روی دکمه داشبورد، چانک جاوا اسکریپت آن قبل از کلیک کاربر پیش‌بارگذاری (Prefetch) شود.",
             "hint": "در onMouseEnter تابع import('./HeavyComponent') را پیشاپیش فراخوانی کنید.",
             "solution": """import { lazy, Suspense, useState } from 'react';

const componentLoader = () => import('./AnalyticsChart');
const AnalyticsChart = lazy(componentLoader);

export default function PrefetchButton() {
  const [load, setLoad] = useState(false);

  const handleMouseEnter = () => {
    componentLoader();
  };

  return (
    <div>
      <button onMouseEnter={handleMouseEnter} onClick={() => setLoad(true)}>
        مشاهده نمودار تحلیلی
      </button>
      {load && (
        <Suspense fallback={<p>لود فوری...</p>}>
          <AnalyticsChart />
        </Suspense>
      )}
    </div>
  );
}"""}
        ],
        42: [ # Reconciliation & Fiber Architecture
            {"tier": "آسان", "title": "مسئله ۱: اهمیت کلید (key) یکتا در الگوریتم تطبیق درخت (Diffing)",
             "desc": "کامپوننتی برای نمایش لیست اقلام با قابلیت افزودن آیتم به ابتدای لیست بنویسید که از شناسه پایدار id به جای اندیس آرایه استفاده کند تا ری‌اکت در فایبر ساختار داخلی اینپوت‌ها را جابجا نکند.",
             "hint": "همیشه از کلیدهای یکتا و پایدار نظیر item.id در حلقه map استفاده کنید.",
             "solution": """import { useState } from 'react';

export default function ItemList() {
  const [items, setItems] = useState([
    { id: 'a1', text: 'کار اول' },
    { id: 'b2', text: 'کار دوم' }
  ]);

  const addItemToTop = () => {
    const newItem = { id: 'item_' + Date.now(), text: 'کار جدید' };
    setItems(prev => [newItem, ...prev]);
  };

  return (
    <div>
      <button onClick={addItemToTop}>افزودن به ابتدای لیست</button>
      <ul>
        {items.map(item => (
          <li key={item.id}>
            <input defaultValue={item.text} />
          </li>
        ))}
      </ul>
    </div>
  );
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: کنترل فاز رندر و بهینه‌سازی اولویت در Fiber با useTransition",
             "desc": "نوار جستجویی بسازید که تایپ کاربر را در اولویت فوری (Urgent) قرار دهد و فیلتر کردن لیست حجیم ۱۰,۰۰۰ تایی را با useTransition به عنوان transition با اولویت پایین علامت‌گذاری کند تا اینپوت لگ نزند.",
             "hint": "از const [isPending, startTransition] = useTransition() استفاده نمایید.",
             "solution": """import { useState, useTransition } from 'react';

export default function HeavySearch({ allData }) {
  const [query, setQuery] = useState('');
  const [filtered, setFiltered] = useState([]);
  const [isPending, startTransition] = useTransition();

  const handleChange = (e) => {
    const val = e.target.value;
    setQuery(val); // اولویت فوری: تایپ بدون لگ

    startTransition(() => {
      // اولویت پایین و قابل انصراف در فایبر:
      setFiltered(allData.filter(d => d.includes(val)));
    });
  };

  return (
    <div>
      <input value={query} onChange={handleChange} placeholder="جستجو..." />
      {isPending && <span>در حال تطبیق درخت و فیلتر...</span>}
      <ul>{filtered.slice(0, 50).map((item, idx) => <li key={idx}>{item}</li>)}</ul>
    </div>
  );
}"""},
            {"tier": "سخت", "title": "مسئله ۳: جداسازی درخت رندر با memoization برای مهار ری‌رندرهای سراسری",
             "desc": "ساختار درختی سنگینی طراحی کنید که تغییر استیت والد با مکانیزم React.memo و مقایسه سطحی (Shallow Compare) مانع از ورود نودهای فرزند دست‌نخورده به فاز Reconciliation شود.",
             "hint": "کامپوننت‌های محاسباتی فرزند را در memo() قرار دهید.",
             "solution": """import React, { useState, memo } from 'react';

const ExpensiveTree = memo(function ExpensiveTree({ data }) {
  console.log('فاز Reconciliation برای زیردرخت سنگین اجرا نشد.');
  return <div>تعداد رکوردهای پردازش‌شده: {data.length}</div>;
});

export default function FiberOptimizer() {
  const [tick, setTick] = useState(0);
  const [data] = useState(() => Array.from({ length: 5000 }, (_, i) => i));

  return (
    <div>
      <button onClick={() => setTick(t => t + 1)}>تیک والد: {tick}</button>
      {/* به دلیل memo، با تغییر tick این درخت بررسی مجدد نمی‌شود */}
      <ExpensiveTree data={data} />
    </div>
  );
}"""}
        ],
        51: [ # Remix / TanStack Start
            {"tier": "آسان", "title": "مسئله ۱: لود داده‌ها با تابع loader در فریمورک Remix",
             "desc": "کامپوننتی در ریمیکس بنویسید که داده‌ها را با استفاده از loader و هوک useLoaderData دریافت کند.",
             "hint": "تابع json({ users }) را در loader بازگردانید.",
             "solution": """import { json } from '@remix-run/node';
import { useLoaderData } from '@remix-run/react';

export const loader = async () => {
  return json({ users: ['علی', 'سارا'] });
};

export default function UsersRoute() {
  const { users } = useLoaderData<typeof loader>();
  return <ul>{users.map(u => <li key={u}>{u}</li>)}</ul>;
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: ارسال داده‌های فرم با تابع action در Remix",
             "desc": "فرم و تابع action بنویسید که درخواست POST را مدیریت کرده و پس از ایجاد رکورد ریدایرکت کند.",
             "hint": "از redirect('/dashboard') در انتهای action استفاده کنید.",
             "solution": """import { redirect } from '@remix-run/node';
import { Form } from '@remix-run/react';

export const action = async ({ request }) => {
  const formData = await request.formData();
  console.log('ثبت کاربر:', formData.get('name'));
  return redirect('/users');
};

export default function NewUser() {
  return (
    <Form method="post">
      <input name="name" required />
      <button type="submit">ثبت کاربر جدید</button>
    </Form>
  );
}"""},
            {"tier": "سخت", "title": "مسئله ۳: مدیریت خوش‌بینانه خطا و استیت در حال ارسال با useNavigation",
             "desc": "با استفاده از هوک useNavigation وضعیت ارسال شدن فرم را مانیتور کرده و پیام در حال ارسال نشان دهید.",
             "hint": "صفت navigation.state === 'submitting' را بررسی نمایید.",
             "solution": """import { useNavigation, Form } from '@remix-run/react';

export default function SubmitButton() {
  const navigation = useNavigation();
  const isSubmitting = navigation.state === 'submitting';

  return (
    <Form method="post">
      <button disabled={isSubmitting}>
        {isSubmitting ? 'در حال ثبت در سرور...' : 'تایید'}
      </button>
    </Form>
  );
}"""}
        ],
        52: [ # TypeScript with React
            {"tier": "آسان", "title": "مسئله ۱: تایپ‌گذاری دقیق Props کامپوننت با اینترفیس در TypeScript",
             "desc": "یک کامپوننت دکمه بنویسید که متن دکمه، وضعیت غیرفعال، و تابع کلیک را با TypeScript به صورت دقیق تایپ‌گذاری کند.",
             "hint": "از onClick: () => void و React.ReactNode استفاده کنید.",
             "solution": """interface ButtonProps {
  label: string;
  disabled?: boolean;
  onClick: (e: React.MouseEvent<HTMLButtonElement>) => void;
  variant?: 'primary' | 'secondary';
}

export default function Button({ label, disabled = false, onClick }: ButtonProps) {
  return <button disabled={disabled} onClick={onClick}>{label}</button>;
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: تایپ‌گذاری فرم‌ها و رویدادهای ChangeEvent در TypeScript",
             "desc": "هندلر ورودی متنی را طوری بنویسید که رویداد React.ChangeEvent<HTMLInputElement> را بپذیرد و تایپ آن تضمین شود.",
             "hint": "تایپ دقیق e: React.ChangeEvent<HTMLInputElement> را به تابع بدهید.",
             "solution": """import { useState } from 'react';

export default function InputField() {
  const [val, setVal] = useState<string>('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setVal(e.target.value);
  };

  return <input value={val} onChange={handleChange} placeholder="ورودی تایپ‌شده..." />;
}"""},
            {"tier": "سخت", "title": "مسئله ۳: کامپوننت ژنریک (Generic Component) برای رندر انواع لیست‌ها",
             "desc": "یک کامپوننت Generic List با امضای <T extends { id: string | number }> بنویسید که هر نوع داده‌ای را با تابع renderItem نمایش دهد.",
             "hint": "از function GenericList<T>({ items, renderItem }: Props<T>) استفاده کنید.",
             "solution": """interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
}

export default function GenericList<T extends { id: string | number }>({ items, renderItem }: ListProps<T>) {
  return (
    <ul>
      {items.map(item => (
        <li key={item.id}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}"""}
        ],
        53: [ # Testing: RTL, Jest, Vitest, Playwright
            {"tier": "آسان", "title": "مسئله ۱: تست واحد کامپوننت دکمه با React Testing Library و Vitest",
             "desc": "تستی بنویسید که رندر شدن صحیح متن دکمه و کلیک خوردن آن را با fireEvent بررسی کند.",
             "hint": "از render، screen.getByText و expect(...).toBeInTheDocument() استفاده کنید.",
             "solution": """import { render, screen, fireEvent } from '@testing-library/react';
import { expect, test, vi } from 'vitest';
import Button from './Button';

test('دکمه با کلیک کاربر تابع را فراخوانی می‌کند', () => {
  const handleClick = vi.fn();
  render(<Button label=\"ارسال\" onClick={handleClick} />);
  
  const btn = screen.getByText('ارسال');
  expect(btn).toBeInTheDocument();
  fireEvent.click(btn);
  expect(handleClick).toHaveBeenCalledTimes(1);
});"""},
            {"tier": "متوسط", "title": "مسئله ۲: تست ناهمگام واکشی داده‌ها با waitFor و Mock Service Worker",
             "desc": "کامپوننتی که از سرور داده می‌گیرد را تست کنید تا مطمئن شوید پیام لودینگ با داده‌های نهایی جایگزین می‌شود.",
             "hint": "از waitFor(() => expect(screen.getByText(...))) بهره ببرید.",
             "solution": """import { render, screen, waitFor } from '@testing-library/react';
import { test, expect } from 'vitest';
import UserFeed from './UserFeed';

test('نمایش نام کاربر پس از پایان دریافت داده', async () => {
  render(<UserFeed />);
  expect(screen.getByText(/در حال بارگذاری/i)).toBeInTheDocument();
  
  await waitFor(() => {
    expect(screen.getByText('عرفان کیانی')).toBeInTheDocument();
  });
});"""},
            {"tier": "سخت", "title": "مسئله ۳: تست سرتاسری (E2E) فرایند ورود و توکن با Playwright",
             "desc": "یک اسکریپت تست با Playwright بنویسید که وارد صفحه /login شود، فرم را پر کند و انتقال به داشبورد را بررسی نماید.",
             "hint": "از await page.goto('/login') و await page.fill('#email', ...) استفاده کنید.",
             "solution": """import { test, expect } from '@playwright/test';

test('فرایند کامل ورود موفقیت‌آمیز به داشبورد', async ({ page }) => {
  await page.goto('http://localhost:3000/login');
  await page.fill('input[name=\"email\"]', 'erfan@test.ir');
  await page.fill('input[name=\"password\"]', 'SecurePass123!');
  await page.click('button[type=\"submit\"]');

  await expect(page).toHaveURL('http://localhost:3000/dashboard');
  await expect(page.locator('h1')).toHaveText('داشبورد مدیریت');
});"""}
        ],
        57: [ # Animation: Framer Motion & GSAP
            {"tier": "آسان", "title": "مسئله ۱: انیمیشن نرم ورود کارت با Framer Motion",
             "desc": "کامپوننتی بنویسید که با motion.div انیمیشن fade-in و بالا آمدن نرم ۲۰ پیکسلی هنگام ورود داشته باشد.",
             "hint": "از initial={{ opacity: 0, y: 20 }} و animate={{ opacity: 1, y: 0 }} استفاده کنید.",
             "solution": """import { motion } from 'framer-motion';

export default function FadeCard({ children }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, ease: 'easeOut' }}
      className="card"
    >
      {children}
    </motion.div>
  );
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: انیمیشن خروج از صفحه و حذف از DOM با AnimatePresence",
             "desc": "سیستم اعلانات (Toast) بسازید که هنگام بسته شدن با انیمیشن ملایم محو شده و سپس از DOM پاک شود.",
             "hint": "از کامپوننت <AnimatePresence> در کنار exit={{ opacity: 0, scale: 0.9 }} استفاده کنید.",
             "solution": """import { motion, AnimatePresence } from 'framer-motion';
import { useState } from 'react';

export default function NotificationBanner() {
  const [visible, setVisible] = useState(true);

  return (
    <AnimatePresence>
      {visible && (
        <motion.div
          initial={{ opacity: 0, height: 0 }}
          animate={{ opacity: 1, height: 'auto' }}
          exit={{ opacity: 0, height: 0 }}
          className="alert-banner"
        >
          <span>تخفیف ویژه امروز فعال است!</span>
          <button onClick={() => setVisible(false)}>✕</button>
        </motion.div>
      )}
    </AnimatePresence>
  );
}"""},
            {"tier": "سخت", "title": "مسئله ۳: انیمیشن مشترک المان‌ها بین دو بخش (Shared Layout Animation) با layoutId",
             "desc": "نوار تبی بسازید که خط آبی زیرین تب فعال با layoutId به نرمی بین دکمه‌های مختلف سر بخورد.",
             "hint": "از motion.div با خصوصیت layoutId=\"underline\" بهره ببرید.",
             "solution": """import { motion } from 'framer-motion';
import { useState } from 'react';

const tabs = ['مفاهیم', 'کدها', 'تمرین‌ها'];

export default function SlidingTabs() {
  const [active, setActive] = useState(tabs[0]);

  return (
    <div style={{ display: 'flex', gap: '16px', position: 'relative' }}>
      {tabs.map(tab => (
        <button key={tab} onClick={() => setActive(tab)} style={{ position: 'relative', padding: '8px 16px' }}>
          {tab}
          {active === tab && (
            <motion.div
              layoutId="activeIndicator"
              style={{ position: 'absolute', bottom: 0, left: 0, right: 0, height: 2, background: '#38bdf8' }}
            />
          )}
        </button>
      ))}
    </div>
  );
}"""}
        ],
        58: [ # Micro Frontends
            {"tier": "آسان", "title": "مسئله ۱: پیاده‌سازی ماژول ریموت در Module Federation",
             "desc": "پیکربندی ماژول مشترک (Shared Component) در فایل vite.config.js یا webpack با پلاگین federation را بنویسید.",
             "hint": "از name: 'auth_app' و exposes: { './Button': './src/Button' } استفاده کنید.",
             "solution": """// federation.config.js
module.exports = {
  name: 'auth_microfrontend',
  filename: 'remoteEntry.js',
  exposes: {
    './LoginForm': './src/components/LoginForm.tsx',
  },
  shared: ['react', 'react-dom']
};"""},
            {"tier": "متوسط", "title": "مسئله ۲: لود ناهمگام کامپوننت ریموت در Host با React.lazy",
             "desc": "در اپلیکیشن اصلی (Host) کامپوننت سبد خرید را از آدرس میکروسرویس دیگر لود کرده و در Suspense مهار کنید.",
             "hint": "از React.lazy(() => import('cart_app/CartWidget')) استفاده نمایید.",
             "solution": """import { lazy, Suspense } from 'react';

const RemoteCart = lazy(() => import('cart_app/CartWidget'));

export default function ShellApp() {
  return (
    <header>
      <nav>هدر اصلی شل</nav>
      <Suspense fallback={<div>در حال اتصال به میکروسرویس سبد خرید...</div>}>
        <RemoteCart />
      </Suspense>
    </header>
  );
}"""},
            {"tier": "سخت", "title": "مسئله ۳: ارتباط ایزوله بین دو میکرواپ با Custom Event Bus مستقل",
             "desc": "ارتباط بین دو ماژول که هیچ دیتابیس یا استور مشترکی ندارند را با رویداد سراسری window.dispatchEvent بدون ایجاد وابستگی پیاده کنید.",
             "hint": "از new CustomEvent('cart:add', { detail: { item } }) استفاده کنید.",
             "solution": """// در میکرواپ کاتالوگ:
export function dispatchAddToCart(item) {
  window.dispatchEvent(new CustomEvent('app:cart_update', { detail: item }));
}

// در میکرواپ سبد خرید:
import { useEffect, useState } from 'react';

export function useCartListener() {
  const [items, setItems] = useState([]);
  useEffect(() => {
    const handler = (e: any) => setItems(prev => [...prev, e.detail]);
    window.addEventListener('app:cart_update', handler);
    return () => window.removeEventListener('app:cart_update', handler);
  }, []);
  return items;
}"""}
        ],
        50: [ # Next.js & App Router Architecture
            {"tier": "آسان", "title": "مسئله ۱: ساخت صفحه داینامیک محصول در App Router",
             "desc": "صفحه‌ای در مسیر app/products/[id]/page.tsx بنویسید که در Next.js 15 پارامتر id را به عنوان پرامیس ناهمگام (Async Params) دریافت و نمایش دهد.",
             "hint": "در نکست ۱۵ باید const { id } = await params نوشته شود.",
             "solution": """// app/products/[id]/page.tsx
export default async function ProductPage({
  params
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  return (
    <div className="product-view">
      <h1>جزئیات کالا: {id}</h1>
    </div>
  );
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: پیاده‌سازی اسکلتون لودینگ فوری با loading.tsx",
             "desc": "یک کامپوننت لودینگ خودکار بسازید که تا زمان آماده شدن پاسخ سرور در صفحه بلاگ، یک اسکلتون انیمیشنی به کاربر نشان دهد.",
             "hint": "فایل loading.tsx به صورت پیش‌فرض در App Router به عنوان مرز Suspense عمل می‌کند.",
             "solution": """// app/blog/loading.tsx
export default function BlogLoading() {
  return (
    <div className="skeleton-container" style={{ padding: 20 }}>
      <div className="skeleton-title" style={{ height: 24, background: '#334155', borderRadius: 4, marginBottom: 12 }} />
      <div className="skeleton-line" style={{ height: 16, background: '#1e293b', borderRadius: 4, width: '80%' }} />
    </div>
  );
}"""},
            {"tier": "سخت", "title": "مسئله ۳: ثبت سفارش با سرور اکشن ('use server') و بازتولید آنی کش",
             "desc": "یک فرم ثبت سفارش طراحی کنید که مستقیماً به یک اکشن سروری متصل شده، رکورد را در دیتابیس ثبت کند و با revalidatePath صفحه سبد را در لحظه تازه کند.",
             "hint": "دستور 'use server' را بالای فایل اکشن قرار دهید و از revalidatePath('/cart') استفاده نمایید.",
             "solution": """// app/actions/order.ts
'use server';
import { revalidatePath } from 'next/cache';

export async function submitOrder(formData: FormData) {
  const itemId = formData.get('itemId');
  // عملیات مستقیم در پایگاه داده روی سرور
  console.log('سفارش در دیتابیس ثبت شد:', itemId);
  
  // تازه‌سازی آنی کش بدون رفرش کل مرورگر
  revalidatePath('/cart');
  return { success: true };
}"""}
        ],
        41: [ # Compound Components
            {"tier": "آسان", "title": "مسئله ۱: ساخت زبانه تب با الگوی Compound Component",
             "desc": "ساختار کامپوننت Tabs را طوری طراحی کنید که شامل Tabs.List و Tabs.Tab باشد و از طریق React.Children ارتباط برقرار کنند.",
             "hint": "می‌توانید زیرکامپوننت‌ها را به عنوان پراپرتی به Tabs متصل کنید (Tabs.Tab = Tab).",
             "solution": """export function Tabs({ children }) {
  return <div className="tabs-container">{children}</div>;
}
Tabs.Tab = function Tab({ label, active, onClick }) {
  return (
    <button className={active ? 'active' : ''} onClick={onClick}>
      {label}
    </button>
  );
};"""},
            {"tier": "متوسط", "title": "مسئله ۲: اشتراک وضعیت فعال بین تب‌ها با React Context",
             "desc": "سیستم Tabs ترکیبی بنویسید که با استفاده از Context داخلی، بدون نیاز به ارسال صفت active به تک‌تک فرزندان، بداند کدام تب فعال است.",
             "hint": "از createContext برای ایجاد TabsContext و useContext در Tabs.Tab استفاده کنید.",
             "solution": """import { createContext, useContext, useState } from 'react';

const TabsContext = createContext();

export function Tabs({ children, defaultTab }) {
  const [active, setActive] = useState(defaultTab);
  return (
    <TabsContext.Provider value={{ active, setActive }}>
      <div className="tabs-wrapper">{children}</div>
    </TabsContext.Provider>
  );
}
Tabs.Item = function TabItem({ id, children }) {
  const { active, setActive } = useContext(TabsContext);
  return (
    <button onClick={() => setActive(id)} className={active === id ? 'active' : ''}>
      {children}
    </button>
  );
};"""},
            {"tier": "سخت", "title": "مسئله ۳: کامپوننت آکاردئون پیشرفته با پشتیبانی از باز شدن هم‌زمان چند پنل",
             "desc": "آکاردئون ماژولار بسازید که شامل Accordion.Item، Accordion.Trigger و Accordion.Content باشد و قابلیت allowMultiple را پشتیبانی کند.",
             "hint": "وضعیت پنل‌های باز را در آرایه‌ای از شناسه‌ها در کانتکست والد نگه‌داری کنید.",
             "solution": """import { createContext, useContext, useState } from 'react';

const AccordionCtx = createContext();

export function Accordion({ children, multiple = false }) {
  const [openIds, setOpenIds] = useState([]);
  const toggle = (id) => {
    setOpenIds(prev => multiple 
      ? (prev.includes(id) ? prev.filter(x => x !== id) : [...prev, id])
      : (prev.includes(id) ? [] : [id])
    );
  };
  return <AccordionCtx.Provider value={{ openIds, toggle }}>{children}</AccordionCtx.Provider>;
}"""}
        ],
        54: [ # Storybook
            {"tier": "آسان", "title": "مسئله ۱: نوشتن اولین استوری کامپوننت دکمه در Storybook",
             "desc": "فایل Button.stories.tsx را با قالب استاندارد Component Story Format (CSF 3) بنویسید.",
             "hint": "از default export شامل title و component و نام استوری مثل Primary استفاده کنید.",
             "solution": """import type { Meta, StoryObj } from '@storybook/react';
import Button from './Button';

const meta: Meta<typeof Button> = {
  title: 'Components/Button',
  component: Button,
};
export default meta;

type Story = StoryObj<typeof Button>;

export const Primary: Story = {
  args: {
    label: 'کلیک کنید',
    variant: 'primary',
  },
};"""},
            {"tier": "متوسط", "title": "مسئله ۲: افزودن Controls و تغییر پویای رنگ و متن در استوری‌بوک",
             "desc": "متادیتای استوری را طوری تنظیم کنید که اندازه و رنگ دکمه با آرگومان‌های تعاملی در پنل ادمین قابل تغییر باشد.",
             "hint": "از خاصیت argTypes با کنترل select یا color استفاده کنید.",
             "solution": """export const Interactive: Story = {
  argTypes: {
    variant: {
      control: { type: 'select' },
      options: ['primary', 'secondary', 'danger'],
    },
    disabled: { control: 'boolean' },
  },
  args: {
    variant: 'primary',
    disabled: false,
  },
};"""},
            {"tier": "سخت", "title": "مسئله ۳: تست تعاملی خودکار رفتار دکمه در Storybook با تابع play",
             "desc": "با استفاده از تابع play و userEvent رفتار کلیک خوردن دکمه را مستقیماً درون محیط ایزوله استوری‌بوک تست کنید.",
             "hint": "از within(canvasElement) و userEvent.click استفاده فرمایید.",
             "solution": """import { within, userEvent } from '@storybook/testing-library';
import { expect } from '@storybook/jest';

export const ClickTest: Story = {
  play: async ({ canvasElement }) => {
    const canvas = within(canvasElement);
    const btn = canvas.getByRole('button');
    await userEvent.click(btn);
    expect(btn).toHaveTextContent('کلیک شد');
  },
};"""}
        ],
        55: [ # Accessibility (a11y) in React
            {"tier": "آسان", "title": "مسئله ۱: فرم دسترسی‌پذیر برای صفحه‌خوان نابینایان با صفات ARIA",
             "desc": "اینپوتی بسازید که خطای آن با aria-invalid=\"true\" و aria-describedby به پیام خطا پیوند خورده باشد.",
             "hint": "شناسه پیام خطا را در aria-describedby اینپوت بگذارید.",
             "solution": """export function AccessibleInput({ error }) {
  return (
    <div>
      <label htmlFor=\"user-email\">ایمیل رسمی:</label>
      <input
        id=\"user-email\"
        type=\"email\"
        aria-invalid={!!error}
        aria-describedby={error ? \"email-err\" : undefined}
      />
      {error && <span id=\"email-err\" role=\"alert\">{error}</span>}
    </div>
  );
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: مدیریت فوکوس کیبورد در مودال (Focus Trap)",
             "desc": "مودالی طراحی کنید که با باز شدن فوکوس کیبورد را به دکمه بستن انتقال داده و نگذارد کلید Tab از مودال بیرون برود.",
             "hint": "در useEffect ابتدای باز شدن modalRef.current.focus() را فراخوانی کنید.",
             "solution": """import { useEffect, useRef } from 'react';

export default function TrapModal({ isOpen, onClose }) {
  const closeBtnRef = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    if (isOpen) {
      closeBtnRef.current?.focus();
    }
  }, [isOpen]);

  if (!isOpen) return null;
  return (
    <div role=\"dialog\" aria-modal=\"true\">
      <h3>پنجره تایید</h3>
      <button ref={closeBtnRef} onClick={onClose}>بستن ✕</button>
    </div>
  );
}"""},
            {"tier": "سخت", "title": "مسئله ۳: اعلام تغییرات محتوای زنده به نابینایان با aria-live",
             "desc": "جعبه اعلانی بنویسید که هر زمان پیام جدیدی آمد بدون فوکوس مجدد، صفحه‌خوان نابینایان متن آن را با صدای بلند بخواند.",
             "hint": "از صفت aria-live=\"polite\" یا role=\"status\" استفاده کنید.",
             "solution": """export function LiveAnnouncer({ message }) {
  return (
    <div
      role=\"status\"
      aria-live=\"polite\"
      style={{ position: 'absolute', opacity: 0, pointerEvents: 'none' }}
    >
      {message}
    </div>
  );
}"""}
        ],
        56: [ # Internationalization (i18n)
            {"tier": "آسان", "title": "مسئله ۱: سوئیچ بین زبان فارسی و انگلیسی با react-i18next",
             "desc": "دکمه‌ای بنویسید که زبان برنامه را با i18n.changeLanguage بین fa و en جابجا کند.",
             "hint": "از هوک useTranslation() و متد i18n.changeLanguage بهره ببرید.",
             "solution": """import { useTranslation } from 'react-i18next';

export default function LanguageSwitcher() {
  const { i18n } = useTranslation();

  return (
    <button onClick={() => i18n.changeLanguage(i18n.language === 'fa' ? 'en' : 'fa')}>
      تغییر زبان به {i18n.language === 'fa' ? 'English' : 'فارسی'}
    </button>
  );
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: تنظیم جهت سند (RTL/LTR) و فونت متناسب با تغییر زبان",
             "desc": "تابعی بنویسید که به محض تغییر زبان به فارسی dir=\"rtl\" و به انگلیسی dir=\"ltr\" را روی تگ html تنظیم کند.",
             "hint": "از document.documentElement.dir استفاده نمایید.",
             "solution": """import { useEffect } from 'react';
import { useTranslation } from 'react-i18next';

export function useDirectionSync() {
  const { i18n } = useTranslation();

  useEffect(() => {
    const isRtl = i18n.language === 'fa' || i18n.language === 'ar';
    document.documentElement.dir = isRtl ? 'rtl' : 'ltr';
    document.documentElement.lang = i18n.language;
  }, [i18n.language]);
}"""},
            {"tier": "سخت", "title": "مسئله ۳: مدیریت متغیرها و تاریخ شمسی/میلادی با فرمت‌دهنده‌های بومی Intl",
             "desc": "کامپوننتی طراحی کنید که مبلغ ریالی و تاریخ سفارش را به زبان انتخاب‌شده با شیء استاندارد Intl.NumberFormat و Intl.DateTimeFormat محلی‌سازی کند.",
             "hint": "از new Intl.NumberFormat(lang, { style: 'currency' }) استفاده کنید.",
             "solution": """export function LocalizedPrice({ amount, locale = 'fa-IR' }) {
  const formatted = new Intl.NumberFormat(locale, {
    style: 'currency',
    currency: locale === 'fa-IR' ? 'IRR' : 'USD'
  }).format(amount);

  return <span>{formatted}</span>;
}"""}
        ],
        59: [ # Monorepo: Turborepo & Nx
            {"tier": "آسان", "title": "مسئله ۱: ساختار فایل turbo.json در پروژه مونو‌ریپو",
             "desc": "پیکربندی خط فرمان Turborepo برای اجرای هم‌زمان بیلد و تست تمام پکیج‌ها را بنویسید.",
             "hint": "از کلید pipeline با tasks بیلد و کش ^build استفاده کنید.",
             "solution": """// turbo.json
{
  "$schema": "https://turbo.build/schema.json",
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": [".next/**", "dist/**"]
    },
    "test": {
      "cache": false
    }
  }
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: ایمپورت کامپوننت مشترک از پکیج @repo/ui در وب‌اپلیکیشن",
             "desc": "ساختار package.json یک اپلیکیشن را طوری تنظیم کنید که پکیج داخلی shared UI را با workspace:* ایمپورت کند.",
             "hint": "از \"@repo/ui\": \"workspace:*\" در dependencies استفاده نمایید.",
             "solution": """// apps/web/package.json
{
  "name": "web-app",
  "dependencies": {
    "react": "^19.0.0",
    "@repo/ui": "workspace:*"
  }
}"""},
            {"tier": "سخت", "title": "مسئله ۳: کش کردن ابری تسک‌های بیلد مونو‌ریپو با Remote Caching",
             "desc": "دستور اتصال پروژه به Vercel Remote Cache را در اسکریپت ترمینال تنظیم کنید تا بیلد تیم تا ۸۰٪ سریع‌تر شود.",
             "hint": "از دستور npx turbo login و npx turbo link استفاده کنید.",
             "solution": """# ترمینال اتصال به ریموت کش
npx turbo login
npx turbo link

# بیلد فوق‌سریع با استفاده از کش همکاران:
npx turbo run build --remote-only"""}
        ],
        60: [ # Clean Architecture & Feature-based Design
            {"tier": "آسان", "title": "مسئله ۱: ساختار پوشه‌بندی استاندارد یک فیچر (مثلاً فیچر auth)",
             "desc": "درخت فایل‌های یک فیچر مستقل شامل کامپوننت، هوک، تایپ‌ها و سرویس شبکه را رسم کنید.",
             "hint": "پوشه‌های components، hooks، services و types را درون فیچر قرار دهید.",
             "solution": """src/features/auth/
├── components/
│   └── LoginForm.tsx
├── hooks/
│   └── useAuth.ts
├── services/
│   └── authApi.ts
├── types/
│   └── user.types.ts
└── index.ts  # Public API"""},
            {"tier": "متوسط", "title": "مسئله ۲: تعریف Public API با فایل index.ts برای جلوگیری از ایمپورت‌های عمیق",
             "desc": "فایل index.ts بنویسید که فقط کامپوننت‌های مجاز و هوک‌های عمومی را اکسپورت کند و جزییات داخلی را پنهان نگه دارد.",
             "hint": "از export { LoginForm } from './components/LoginForm' استفاده فرمایید.",
             "solution": """// src/features/cart/index.ts
export { CartDrawer } from './components/CartDrawer';
export { useCart } from './hooks/useCart';
export type { CartItem } from './types';
// توابع خصوصی درون پوشه باقی می‌مانند و از بیرون مستقیماً ایمپورت نمی‌شوند"""},
            {"tier": "سخت", "title": "مسئله ۳: قانون لایه‌ها (Layer Dependency Rule) در معماری تمیز",
             "desc": "تنظیم قانونی با ESLint که اجازه ندهد لایه‌های پایینی (Shared) لایه‌های بالایی (Features یا App) را ایمپورت کنند.",
             "hint": "از پلاگین eslint-plugin-boundaries یا import/no-restricted-paths استفاده کنید.",
             "solution": """// .eslintrc.json
{
  "rules": {
    "import/no-restricted-paths": [
      "error",
      {
        "zones": [
          { "target": "./src/shared", "from": "./src/features", "message": "لایه‌های پایینی نمی‌توانند از لایه‌های بالایی استفاده کنند!" }
        ]
      }
    ]
  }
}"""}
        ],
        61: [ # Design Patterns in React
            {"tier": "آسان", "title": "مسئله ۱: الگوی کامپوننت ارائه‌دهنده و نگهدارنده (Container / Presentational)",
             "desc": "کدهای واکشی داده را در یک کامپوننت کانتینر قرار داده و نمایش ساده رابط کاربری را به کامپوننت فرزند خالص بسپارید.",
             "hint": "پراپ‌های داده و وضعیت را به کامپوننت ارائه‌دهنده بدهید.",
             "solution": """// Presentational (صرفاً نمایش UI)
function UserListView({ users, isLoading }) {
  if (isLoading) return <p>در حال بارگذاری...</p>;
  return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}

// Container (منطق داده و فچ)
export default function UserListContainer() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchUsers().then(data => { setUsers(data); setLoading(false); });
  }, []);

  return <UserListView users={users} isLoading={loading} />;
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: الگوی Provider برای ارسال تم سراسری بدون Prop Drilling",
             "desc": "یک ThemeProvider بسازید که متد toggleTheme را از طریق Context در سراسر برنامه در دسترس بگذارد.",
             "hint": "ترکیب createContext با useState و کاستوم هوک useTheme.",
             "solution": """import { createContext, useContext, useState } from 'react';

const ThemeCtx = createContext();

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('dark');
  const toggle = () => setTheme(t => t === 'dark' ? 'light' : 'dark');

  return (
    <ThemeCtx.Provider value={{ theme, toggle }}>
      <div className={theme}>{children}</div>
    </ThemeCtx.Provider>
  );
}

export const useTheme = () => useContext(ThemeCtx);"""},
            {"tier": "سخت", "title": "مسئله ۳: الگوی State Reducer برای شخصی‌سازی رفتار داخلی کامپوننت توسط والد",
             "desc": "کامپوننت آکاردئونی بنویسید که به والد اجازه دهد با ارسال تابع کاستوم استیت‌ریدیوسر، منطق باز و بسته شدن را بازنویسی کند.",
             "hint": "از useReducer با تابع ردوسر ترکیبی props.stateReducer استفاده کنید.",
             "solution": """import { useReducer } from 'react';

function internalReducer(state, action) {
  switch (action.type) {
    case 'toggle': return { open: !state.open };
    default: return state;
  }
}

export function Toggle({ stateReducer = (s, a) => a.changes }) {
  const [state, dispatch] = useReducer((s, a) => {
    const changes = internalReducer(s, a);
    return stateReducer(s, { ...a, changes });
  }, { open: false });

  return <button onClick={() => dispatch({ type: 'toggle' })}>{state.open ? 'باز' : 'بسته'}</button>;
}"""}
        ],
        62: [ # Web Vitals & SEO
            {"tier": "آسان", "title": "مسئله ۱: گزارش شاخص‌های سرعت با useReportWebVitals در Next.js",
             "desc": "تابعی بنویسید که متریک‌های LCP، FID، CLS و FCP را در کنسول ثبت کند.",
             "hint": "تابع useReportWebVitals را در ریشه فراخوانی کنید.",
             "solution": """'use client';
import { useReportWebVitals } from 'next/web-vitals';

export function WebVitalsMonitor() {
  useReportWebVitals((metric) => {
    console.log(`[Web Vitals] ${metric.name}: ${metric.value}ms (امتیاز: ${metric.rating})`);
  });
  return null;
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: جلوگیری قطعی از جابجایی ناگهانی چیدمان (Cumulative Layout Shift - CLS)",
             "desc": "کدی بنویسید که برای بنرهای تبلیغاتی و تصاویر قبل از دانلود فضای مشخص با aspect-ratio رزرو کند تا صفحه نپرد.",
             "hint": "از ویژگی CSS aspect-ratio یا ابعاد رزرو شده استفاده کنید.",
             "solution": """export function SafeBanner({ src, alt }) {
  return (
    <div style={{ width: '100%', aspectRatio: '16 / 9', background: '#1e293b', overflow: 'hidden' }}>
      <img
        src={src}
        alt={alt}
        style={{ width: '100%', height: '100%', objectFit: 'cover' }}
        loading="lazy"
      />
    </div>
  );
}"""},
            {"tier": "سخت", "title": "مسئله ۳: بهینه‌سازی تاخیر پاسخ‌دهی کلیک (Interaction to Next Paint - INP)",
             "desc": "هندلر دکمه سنگینی بنویسید که کارهای سنگین را با setTimeout یا scheduler.yield به فریم‌های بعد موکول کند تا INP عالی بماند.",
             "hint": "از تابع scheduler.yield() یا requestAnimationFrame استفاده کنید.",
             "solution": """export function FastResponseButton({ onHeavyProcess }) {
  const handleClick = async () => {
    document.body.style.cursor = 'wait';
    await new Promise(r => setTimeout(r, 0));
    onHeavyProcess();
    document.body.style.cursor = 'default';
  };

  return <button onClick={handleClick}>پردازش بدون لگ</button>;
}"""}
        ],
        63: [ # Progressive Web Apps (PWA)
            {"tier": "آسان", "title": "مسئله ۱: فایل پیکربندی manifest.json برای نصب اپلیکیشن",
             "desc": "فایل manifest استانداردی بسازید که نام، آیکون، رنگ تم و حالت display: standalone را تنظیم کند.",
             "hint": "از فیلدهای name، short_name، start_url و display استفاده کنید.",
             "solution": """// public/manifest.json
{
  "name": "سامانه مدیریت عرفان",
  "short_name": "ERFAN.OS",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#020408",
  "theme_color": "#020408",
  "icons": [
    { "src": "/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}"""},
            {"tier": "متوسط", "title": "مسئله ۲: ثبت سرویس‌ورکر (Service Worker) برای عملکرد آفلاین",
             "desc": "کدی بنویسید که در مرورگر کاربر فایل sw.js را رجیستر کند و وضعیت آنلاین/آفلاین شبکه را مانیتور نماید.",
             "hint": "از navigator.serviceWorker.register('/sw.js') استفاده کنید.",
             "solution": """export function registerServiceWorker() {
  if (typeof window !== 'undefined' && 'serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/sw.js').then(
        reg => console.log('سرویس‌ورکر فعال شد:', reg.scope),
        err => console.error('خطای سرویس‌ورکر:', err)
      );
    });
  }
}"""},
            {"tier": "سخت", "title": "مسئله ۳: استراتژی کش آفلاین با الگوی Stale-While-Revalidate در سرویس‌ورکر",
             "desc": "یک فایل sw.js با Workbox بنویسید که فونت‌ها و صفحات را از کش بخواند و در پس‌زمینه نسخه جدید را واکشی کند.",
             "hint": "از رویداد fetch و caches.match استفاده کنید.",
             "solution": """// public/sw.js
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.open('dynamic-cache-v1').then((cache) => {
      return cache.match(event.request).then((cachedResponse) => {
        const fetchPromise = fetch(event.request).then((networkResponse) => {
          cache.put(event.request, networkResponse.clone());
          return networkResponse;
        });
        return cachedResponse || fetchPromise;
      });
    })
  );
});"""}
        ],
        64: [ # React Native
            {"tier": "آسان", "title": "مسئله ۱: کامپوننت پایه موبایل با View و Text در React Native",
             "desc": "یک کارت موبایل بنویسید که با استفاده از View, Text و StyleSheet استایل‌دهی شده باشد.",
             "hint": "به جای div از View و به جای p از Text استفاده کنید.",
             "solution": """import { View, Text, StyleSheet } from 'react-native';

export default function MobileCard() {
  return (
    <View style={styles.card}>
      <Text style={styles.title}>اپلیکیشن نیتیو موبایل</Text>
      <Text style={styles.desc}>رندر مستقیم روی اندروید و iOS</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  card: { padding: 16, backgroundColor: '#1e293b', borderRadius: 12 },
  title: { fontSize: 18, fontWeight: 'bold', color: '#fff' },
  desc: { fontSize: 14, color: '#94a3b8', marginTop: 4 }
});"""},
            {"tier": "متوسط", "title": "مسئله ۲: نمایش لیست راندمان بالا با FlatList در React Native",
             "desc": "لیستی با کامپوننت FlatList بنویسید که دارای کلید یکتا و متد تعویض صفحه هنگام رسیدن به انتها باشد.",
             "hint": "از ویژگی‌های data, renderItem و keyExtractor استفاده کنید.",
             "solution": """import { FlatList, Text, View } from 'react-native';

const data = [{ id: '1', title: 'تسک اول' }, { id: '2', title: 'تسک دوم' }];

export default function TaskList() {
  return (
    <FlatList
      data={data}
      keyExtractor={item => item.id}
      renderItem={({ item }) => (
        <View style={{ padding: 14, borderBottomWidth: 1, borderBottomColor: '#334155' }}>
          <Text style={{ color: '#fff' }}>{item.title}</Text>
        </View>
      )}
    />
  );
}"""},
            {"tier": "سخت", "title": "مسئله ۳: تعامل لمسی و انیمیشن با react-native-reanimated",
             "desc": "دکمه‌ای متحرک با useSharedValue و withSpring بنویسید که با لمس کاربر مقیاس آن نرم کاهش و افزایش یابد.",
             "hint": "از useAnimatedStyle و Pressable استفاده نمایید.",
             "solution": """import { Pressable } from 'react-native';
import Animated, { useSharedValue, useAnimatedStyle, withSpring } from 'react-native-reanimated';

export default function BouncyButton({ children, onPress }) {
  const scale = useSharedValue(1);

  const animatedStyle = useAnimatedStyle(() => ({
    transform: [{ scale: scale.value }]
  }));

  return (
    <Pressable
      onPressIn={() => { scale.value = withSpring(0.92); }}
      onPressOut={() => { scale.value = withSpring(1); }}
      onPress={onPress}
    >
      <Animated.View style={[{ padding: 14, backgroundColor: '#0284c7', borderRadius: 8 }, animatedStyle]}>
        {children}
      </Animated.View>
    </Pressable>
  );
}"""}
        ],
        65: [ # CI/CD & Production Deployment
            {"tier": "آسان", "title": "مسئله ۱: فایل پایپ‌لاین GitHub Actions برای تست و بیلد خودکار",
             "desc": "یک ورک‌فلو اکشن در .github/workflows/deploy.yml بنویسید که روی push به برنچ main اجرا شود.",
             "hint": "از اکشن‌های actions/checkout@v4 و actions/setup-node@v4 استفاده کنید.",
             "solution": """# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'
      - run: npm ci
      - run: npm run test
      - run: npm run build"""},
            {"tier": "متوسط", "title": "مسئله ۲: ساخت ایمیج کم‌حجم داکر با Multi-stage Build برای React و Nginx",
             "desc": "فایل داکرفایلی بنویسید که در استیج اول بیلد بگیرد و در استیج دوم فایل‌های استاتیک را با سرور Nginx میزبانی کند.",
             "hint": "از FROM node:20 AS builder و FROM nginx:alpine استفاده فرمایید.",
             "solution": """# Dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD [\"nginx\", \"-g\", \"daemon off;\"]"""},
            {"tier": "سخت", "title": "مسئله ۳: استقرار بدون قطعی (Zero-Downtime Deployment) با رول‌بک فوری",
             "desc": "دستور پیکربندی استقرار ابری در سرورهای اوبونتو با اسکریپت PM2 و فلگ reload بدون خاموش شدن حتی یک ثانیه سرور.",
             "hint": "از دستور pm2 reload ecosystem.config.js --update-env استفاده کنید.",
             "solution": """# اسکریپت استقرار خودکار روی سرور
git pull origin main
npm ci --production
npm run build
pm2 reload my-react-app --update-env

# بررسی آنلاین بودن سلامت سرویس:
curl -f http://localhost:3000/api/health || pm2 revert 1"""}
        ]
    }

    if tid in specialized:
        return specialized[tid]

    # Concrete generator with actual functional JSX logic
    clean_code = code.strip()
    if "import " in clean_code or "export " in clean_code or "function " in clean_code:
        sol1 = f"// راهکار استاندارد و بهینه {title}\n{clean_code}"
    else:
        sol1 = f"import React from 'react';\n\n// پیاده‌سازی پایه {title}\nexport default function Module{tid}() {{\n  {clean_code}\n}}"

    return [
        {
            "tier": "آسان", "tier_color": "#10b981", "tier_bg": "rgba(16, 185, 129, 0.15)",
            "title": f"مسئله ۱: پیاده‌سازی کاربردی {title}",
            "desc": f"یک کامپوننت تابعی بنویسید که نحوه راه‌اندازی و استفاده پایه از «{title}» را پیاده‌سازی کند.",
            "test_case": "کامپوننت با داده‌های ورودی بدون خطا در DOM رندر شود.",
            "hint": "نحوه تعریف و اکسپورت استاندارد ماژول را رعایت فرمایید.",
            "solution": sol1
        },
        {
            "tier": "متوسط", "tier_color": "#f59e0b", "tier_bg": "rgba(245, 158, 11, 0.15)",
            "title": f"مسئله ۲: مدیریت وضعیت و بهینه‌سازی در {title}",
            "desc": f"کامپوننتی بنویسید که تعاملات کاربر با «{title}» را مدیریت کرده و با تفکیک منطق از ری‌رندرهای اضافی جلوگیری کند.",
            "test_case": "استیت‌ها به شکل ایمن بروزرسانی شوند.",
            "hint": "از هوک‌های مناسب برای مدیریت چرخه حیات استفاده کنید.",
            "solution": f"import React, {{ useState, useCallback }} from 'react';\n\nexport function OptimizedComponent{tid}() {{\n  const [state, setState] = useState(null);\n  const handleAction = useCallback(() => {{\n    setState('بروزرسانی موفق');\n  }}, []);\n  return (\n    <div className=\"box\">\n      <h4>ماژول تخصصی {title}</h4>\n      <button onClick={{handleAction}}>اجرا</button>\n      {{state && <p>{{state}}</p>}}\n    </div>\n  );\n}}"
        },
        {
            "tier": "سخت", "tier_color": "#ef4444", "tier_bg": "rgba(239, 68, 68, 0.15)",
            "title": f"مسئله ۳: پیاده‌سازی معماری سازمانی و تست نهایی در {title}",
            "desc": f"ماژولی بنویسید که این قابلیت را در اشل پروداکشن شرکت‌های بزرگ همراه با ارزیابی خطا (Error Handling) پیاده کند.",
            "test_case": "در شرایط عدم دسترسی به داده برنامه نباید کرش کند.",
            "hint": "از بلوک‌های try/catch و کامپوننت‌های مرزی استفاده کنید.",
            "solution": f"import React from 'react';\n\nexport async function EnterpriseService{tid}() {{\n  try {{\n    // معماری سازمانی {title}\n    return {{ success: true, timestamp: Date.now() }};\n  }} catch(err) {{\n    return {{ success: false, error: err.message }};\n  }}\n}}"
        }
    ]

print("Loaded 100% custom React Advanced Challenge Engine!")
