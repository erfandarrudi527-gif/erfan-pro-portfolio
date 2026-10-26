// Global Projects Repository Data with 100% Live Deployments
const PROJECTS_DATA = [
  {
    id: "qreet-cms",
    title: "Qreet CMS & Digital Engine",
    slug: "qreet-cms",
    category: "web-apps",
    featured: true,
    year: "2026",
    tagline: "Enterprise Next.js 15 Headless CMS & Dynamic Publishing Engine",
    description: "A full-stack, headless content management system built with Next.js 15 App Router, Prisma ORM, and TipTap block editor. Features multi-tenant architecture, role-based authorization, JWT security, custom media asset pipeline, and responsive management dashboard.",
    stack: ["Next.js 15", "Prisma ORM", "PostgreSQL", "TipTap Editor", "NextAuth", "Tailwind CSS"],
    metrics: [
      { label: "Architecture", value: "App Router" },
      { label: "Security", value: "JWT & CSRF Safe" },
      { label: "Database", value: "Prisma / Postgres" }
    ],
    liveUrl: "https://qreet-cms.vercel.app",
    githubUrl: "https://github.com/erfandarrudi527-gif/qreet-cms",
    badge: "LIVE ON VERCEL",
    color: "#00AEEF",
    caustic: "rgba(0, 174, 239, 0.4)",
    highlights: [
      "Dynamic schema modeling and custom fields",
      "TipTap block-based WYSIWYG editor with image uploader",
      "Strict RBAC with session tokens and bcrypt password hashing",
      "Live production deployment on Vercel Edge"
    ]
  },
  {
    id: "dun-brew-lab",
    title: "DUN Coffee & Interactive Brew Lab",
    slug: "dun-brew-lab",
    category: "web-apps",
    featured: true,
    year: "2026",
    tagline: "Artisan Specialty Coffee Platform with Real-Time Extraction Calculator",
    description: "Crafted with an ultra-dark burnt coffee & pitch espresso aesthetic (#020101). Features an interactive DUN Brew Lab calculating brew ratios (1:14 to 1:18), water volume, extraction yield curves, grind micron guides, and temperature management for V60, Chemex, and Aeropress.",
    stack: ["JavaScript ES6+", "Web Audio API", "Canvas Visualizer", "CSS Custom Properties", "LocalStorage"],
    metrics: [
      { label: "Theme", value: "Pitch Espresso #020101" },
      { label: "Interactive", value: "Real-Time Brew Lab" },
      { label: "Latency", value: "< 1ms Response" }
    ],
    liveUrl: "brew-lab.html",
    githubUrl: "https://github.com/erfandarrudi527-gif/dun-coffee-roastery",
    badge: "LIVE DEMO",
    color: "#E86326",
    caustic: "rgba(232, 99, 38, 0.4)",
    highlights: [
      "Bespoke extraction math engine (TDS, Brew Ratio, Pour Splits)",
      "Multi-method presets: V60, Chemex, Aeropress, French Press",
      "Zero-latency state recalculation with visual pour stage bars",
      "Integrated audio feedback on recipe calibration"
    ]
  },
  {
    id: "webdev-learning-hub",
    title: "WebDev Master Learning Hub",
    slug: "webdev-master-hub",
    category: "tools",
    featured: true,
    year: "2026",
    tagline: "Multi-Track Interactive Developer Learning Platform & In-Browser Sandbox",
    description: "A comprehensive developer portal providing structured learning suites across HTML5, Modern CSS (Grid/Flexbox/Animations), Modern JS, React, and Next.js. Equipped with live in-browser code execution playgrounds, interactive quizzes, and cheat sheets.",
    stack: ["JavaScript", "Prism.js", "Live DOM Sandbox", "CSS Grid", "Markdown Engine"],
    metrics: [
      { label: "Tracks", value: "5 Core Languages" },
      { label: "Sandboxes", value: "Live In-Browser" },
      { label: "Coverage", value: "100+ Tutorials" }
    ],
    liveUrl: "demos/webdev-learning-hub/index.html",
    githubUrl: "https://github.com/erfandarrudi527-gif/webdev-master-learning-hub",
    badge: "LIVE DEMO",
    color: "#22C55E",
    caustic: "rgba(34, 197, 94, 0.4)",
    highlights: [
      "In-browser interactive sandboxes for real-time preview",
      "Categorized lesson suites from fundamentals to architecture",
      "Syntax highlighting and instant code-copying utility",
      "Progress tracking saved to local storage"
    ]
  },
  {
    id: "barg-reader",
    title: "Barg Reader Engine & Mobile APK",
    slug: "barg-reader",
    category: "mobile",
    featured: true,
    year: "2026",
    tagline: "Distraction-Free Reading App with Automated Android APK Build Pipeline",
    description: "An elegant, distraction-free book reader engineered with high-precision RTL typography rendering, dynamic font sizing, chapter bookmarking, and offline service worker caching. Linked with GitHub Actions CI for automated Android APK compilation and signing.",
    stack: ["PWA", "Capacitor", "Android APK Pipeline", "IndexedDB", "Web Workers", "Vazirmatn"],
    metrics: [
      { label: "Platforms", value: "Web & Android APK" },
      { label: "Offline", value: "100% Cacheable" },
      { label: "Typography", value: "Pixel-Perfect RTL" }
    ],
    liveUrl: "demos/barg-reader/index.html",
    githubUrl: "https://github.com/erfandarrudi527-gif/barg-reader-app",
    badge: "LIVE DEMO",
    color: "#06B6D4",
    highlights: [
      "Custom RTL reading canvas with line-height and font scale sliders",
      "Automated GitHub Actions workflow for building release APKs",
      "Night mode, sepia mode, and high-contrast OLED black mode",
      "Offline library storage with zero cloud dependencies"
    ]
  },
  {
    id: "parsa-sports-store",
    title: "Parsa Sports Equipment Store",
    slug: "parsa-sports",
    category: "ecommerce",
    featured: true,
    year: "2026",
    tagline: "High-Performance Athletic E-Commerce Storefront with Reactive State",
    description: "A fast, accessible sports merchandise web application featuring multi-criteria equipment filtering, instantaneous reactive shopping cart state, user authentication, customer checkout flows, and Phosphor Icons micro-interactions.",
    stack: ["Vanilla JS", "Phosphor Icons", "CSS Grid/Flex", "LocalStorage State", "Bi-directional Observers"],
    metrics: [
      { label: "Performance", value: "Zero Dependencies" },
      { label: "Cart Engine", value: "Client-Side Reactive" },
      { label: "Responsive", value: "Mobile-First" }
    ],
    liveUrl: "demos/parsa-sports/index.html",
    githubUrl: "https://github.com/erfandarrudi527-gif/parsa-sports-store",
    badge: "LIVE DEMO",
    color: "#E03B8B",
    caustic: "rgba(224, 59, 139, 0.4)",
    highlights: [
      "Reactive shopping cart drawer with instant quantity calculations",
      "Dynamic filtering by sport category, brand, and price bracket",
      "Persisted cart and wishlist state via LocalStorage",
      "Smooth scroll-reveal animations using IntersectionObserver"
    ]
  },
  {
    id: "habit-tracker-app",
    title: "HabitForge / Habit Tracker PWA",
    slug: "habit-tracker",
    category: "mobile",
    featured: false,
    year: "2026",
    tagline: "Minimalist Daily Habit & Goal Tracking Progressive Web Application",
    description: "A clean, focused productivity tool designed for consistency. Implements streak calculation algorithms, GitHub-style annual consistency heatmaps, custom category tags, and zero-latency local storage persistence.",
    stack: ["PWA", "Service Workers", "HTML5 Canvas", "Modern JavaScript", "LocalStorage"],
    metrics: [
      { label: "Data Storage", value: "Local & Private" },
      { label: "Analytics", value: "Visual Heatmaps" },
      { label: "Latency", value: "Instantaneous" }
    ],
    liveUrl: "demos/habit-tracker/index.html",
    githubUrl: "https://github.com/erfandarrudi527-gif/habit-tracker-pwa",
    badge: "LIVE DEMO",
    color: "#7C3AED",
    caustic: "rgba(124, 58, 237, 0.4)",
    highlights: [
      "Annual heatmap calendar matrix visualizing streaks",
      "Offline-first PWA with install prompt banner",
      "Customizable habit frequency, reminders, and tags",
      "Zero telemetry and 100% privacy-friendly"
    ]
  },
  {
    id: "nova-ui-design-system",
    title: "Nova UI Component System",
    slug: "nova-ui",
    category: "tools",
    featured: false,
    year: "2026",
    tagline: "High-Density Developer UI Kit & Modular Dark Analytics Dashboard",
    description: "A meticulously architected UI design system featuring 30+ dark mode atomic components, metric widgets, glassmorphic cards, data tables, modal drawers, and form controls designed for SaaS control panels.",
    stack: ["CSS Architecture", "Semantic HTML5", "JavaScript ES6+", "Custom Properties"],
    metrics: [
      { label: "Components", value: "30+ Reusable Units" },
      { label: "Design Theme", value: "Slate & Neon Indigo" },
      { label: "Bundle Size", value: "< 20KB CSS" }
    ],
    liveUrl: "demos/nova-ui/index.html",
    githubUrl: "https://github.com/erfandarrudi527-gif/nova-ui-design-system",
    badge: "LIVE DEMO",
    color: "#3B82F6",
    highlights: [
      "Strict CSS custom property token architecture",
      "Accessible ARIA compliant keyboard navigation",
      "High-density responsive data grid layout",
      "Interactive component preview playground"
    ]
  },
  {
    id: "taaghche-book-discovery",
    title: "Taaghche Platform Clone",
    slug: "taaghche-project",
    category: "web-apps",
    featured: false,
    year: "2026",
    tagline: "React-Powered Digital Bookstore & Literary Discovery Platform",
    description: "Modern digital book discovery interface built with React 18, Vite, and Tailwind CSS. Features dynamic catalog searching, multi-genre filtering, rating summaries, and customized personal bookshelf management.",
    stack: ["React 18", "Vite", "Tailwind CSS", "REST API Integration"],
    metrics: [
      { label: "Framework", value: "React 18 + Vite" },
      { label: "Styling", value: "Tailwind Utility" },
      { label: "Search", value: "Instant Client Search" }
    ],
    liveUrl: "demos/taaghche-project/index.html",
    githubUrl: "https://github.com/erfandarrudi527-gif/taaghche-book-platform",
    badge: "LIVE DEMO",
    color: "#14B8A6",
    highlights: [
      "Modular React component structure with hooks",
      "Instant debounced search input across large book catalog",
      "Interactive rating stars and user review section",
      "Optimized production build with Vite bundling"
    ]
  },
  {
    id: "skymission-studio",
    title: "SkyMission Creative Studio",
    slug: "skymission-studio",
    category: "web-apps",
    featured: false,
    year: "2026",
    tagline: "Interactive Digital Agency Landing Page with Dynamic Style Controls",
    description: "High-impact agency showcase featuring dynamic theme controls, magnetic button physics, scroll-linked hero parallax, custom WordPress Elementor integration, and smooth viewport entry animations.",
    stack: ["WordPress", "Elementor Widgets", "PHP", "Motion CSS", "GSAP"],
    metrics: [
      { label: "Animation", value: "60fps Smooth Scroll" },
      { label: "Extensibility", value: "Custom PHP Widgets" },
      { label: "Customization", value: "Live Style Toggles" }
    ],
    liveUrl: "demos/skymission-studio/index.html",
    githubUrl: "https://github.com/erfandarrudi527-gif/skymission-studio",
    badge: "LIVE DEMO",
    color: "#F59E0B",
    highlights: [
      "Custom PHP Elementor repeater widgets",
      "Scroll-driven animation timeline and split hero",
      "Dynamic typography and palette switcher",
      "Cross-browser performance optimization"
    ]
  },
  {
    id: "hotel-reservation-system",
    title: "Grand Horizon Hotel Reservation",
    slug: "hotel-reservation",
    category: "ecommerce",
    featured: false,
    year: "2026",
    tagline: "Full-Featured Hotel Booking Engine & Room Availability Management",
    description: "Comprehensive hospitality booking application supporting date-range availability queries, dynamic pricing calculation based on occupancy, guest room tier comparisons, and automated checkout confirmations.",
    stack: ["JavaScript", "CSS Grid", "REST Mock Server", "Date Utilities"],
    metrics: [
      { label: "Type", value: "Booking Engine" },
      { label: "Engine", value: "Dynamic Rate Calc" },
      { label: "UX Flow", value: "3-Step Checkout" }
    ],
    liveUrl: "demos/hotel-reservation/index.html",
    githubUrl: "https://github.com/erfandarrudi527-gif/hotel-reservation-system",
    badge: "LIVE DEMO",
    color: "#64748B",
    highlights: [
      "Interactive date-range room availability checker",
      "Dynamic cost calculation with tax and extra amenities",
      "Room feature comparison matrix and gallery",
      "Step-by-step reservation confirmation modal"
    ]
  }
];

if (typeof module !== 'undefined') module.exports = { PROJECTS_DATA };
