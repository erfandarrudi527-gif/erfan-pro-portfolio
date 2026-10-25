/**
 * MAHASTAN LUXURY HOTEL & RESORT - MASTER JS ENGINE
 * Compatible with all original DOM selectors and structure
 */

"use strict";

const DEFAULT_ROOMS = [
  {
    id: 1,
    title: "سوئیت رویال دوبلکس (VIP)",
    roomName: "سوئیت رویال دوبلکس",
    category: "vip",
    price: 3500000,
    priceFormatted: "۳,۵۰۰,۰۰۰",
    like: 98,
    rating: 4.9,
    capacity: "۴ نفره",
    image: "Mashhad-Almas_2-41.webp",
    features: ["تخت کینگ سایز", "صبحانه سلف‌سرویس", "جکوزی اختصاصی", "نمای پانوراما", "وای‌فای رایگان"],
    description: "سوئیت دوبلکس مجلل مهستان با طراحی چشم‌نواز، جکوزی اختصاصی، دید کامل به شهر و خدمات VIP ویژه."
  },
  {
    id: 2,
    title: "اتاق رویال ۲ نفره لاکچری",
    roomName: "اتاق ۲ نفره رویال",
    category: "double",
    price: 2200000,
    priceFormatted: "۲,۲۰۰,۰۰۰",
    like: 94,
    rating: 4.8,
    capacity: "۲ نفره",
    image: "Mashhad-Almas_2-52.webp",
    features: ["تخت دبل کوئین", "صبحانه بوفه", "مینی‌بار رایگان", "سیستم هوشمند"],
    description: "فضایی آرامش‌بخش و شیک مناسب برای اقامت‌های دونفره با تمامی امکانات رفاهی مدرن."
  },
  {
    id: 3,
    title: "سوئیت امپریال ۴ نفره",
    roomName: "سوئیت ۴ نفره امپریال",
    category: "family",
    price: 2800000,
    priceFormatted: "۲,۸۰۰,۰۰۰",
    like: 91,
    rating: 4.7,
    capacity: "۴ نفره",
    image: "Mashhad-Almas_2-56.webp",
    features: ["۲ اتاق خواب مجزا", "صبحانه سلف‌سرویس", "بالکن اختصاصی", "صندوق امانات"],
    description: "سوئیت وسیع خانوادگی با دو اتاق خواب، پذیرایی مجلل و بالکن اختصاصی با چشم‌انداز عالی."
  },
  {
    id: 4,
    title: "اتاق کینگ دبل با دید شهر",
    roomName: "اتاق دبل کینگ",
    category: "double",
    price: 1950000,
    priceFormatted: "۱,۹۵۰,۰۰۰",
    like: 89,
    rating: 4.6,
    capacity: "۲ نفره",
    image: "Mashhad-Almas_2-59.webp",
    features: ["تخت کینگ", "تلویزیون ۵۵ اینچ", "روم‌سرویس ۲۴ساعته", "وای‌فای"],
    description: "طراحی مدرن و ارگونومیک همراه با خدمات پذیرایی ۲۴ ساعته و تخت خواب دبل کینگ."
  },
  {
    id: 5,
    title: "سوئیت فامیلی کانکت",
    roomName: "سوئیت خانوادگی کانکت",
    category: "family",
    price: 3100000,
    priceFormatted: "۳,۱۰۰,۰۰۰",
    like: 96,
    rating: 4.9,
    capacity: "۵ نفره",
    image: "Mashhad-Almas_2-62.webp",
    features: ["اتاق‌های متصل", "۲ حمام و سرویس", "صبحانه بوفه", "پارکینگ اختصاصی"],
    description: "بهترین انتخاب برای اقامت‌های خانوادگی پرجمعیت با امکانات کامل و دو سرویس بهداشتی."
  },
  {
    id: 6,
    title: "اتاق استاندارد یک نفره",
    roomName: "اتاق سینگل استاندارد",
    category: "single",
    price: 1350000,
    priceFormatted: "۱,۳۵۰,۰۰۰",
    like: 86,
    rating: 4.5,
    capacity: "۱ نفره",
    image: "Mashhad-Almas_2-71.webp",
    features: ["تخت سینگل راحت", "میز کار اختصاصی", "وای‌فای پرسرعت", "صبحانه"],
    description: "مناسب برای سفرهای کاری و اقامت‌های فردی با محیطی آرام و میز کار مجهز."
  },
  {
    id: 7,
    title: "سوئیت ماه عسل (Honeymoon)",
    roomName: "سوئیت ماه عسل VIP",
    category: "vip",
    price: 4100000,
    priceFormatted: "۴,۱۰۰,۰۰۰",
    like: 100,
    rating: 5.0,
    capacity: "۲ نفره",
    image: "Mashhad-Almas_2-73.webp",
    features: ["گل‌آرایی ویژه", "جکوزی و ماساژور", "شام اختصاصی", "خدمات ترانسفر VIP"],
    description: "دیزاین اختصاصی و رمانتیک، پذیرایی ویژه با گل‌آرایی و پکیج ماه عسل فراموش‌نشدنی."
  },
  {
    id: 8,
    title: "اتاق دبل لوکس پلاس",
    roomName: "اتاق ۲ نفره پلاس",
    category: "double",
    price: 2400000,
    priceFormatted: "۲,۴۰۰,۰۰۰",
    like: 92,
    rating: 4.7,
    capacity: "۲ نفره",
    image: "Mashhad-Almas_2-75.webp",
    features: ["نمای باغ و استخر", "چای‌ساز و اسپرسوساز", "صبحانه", "تخت کینگ"],
    description: "دارای تراس رو به باغ و امکانات کامل تهیه نوشیدنی گرم در اتاق."
  },
  {
    id: 9,
    title: "پنت‌هاوس پرزیدنتال ۵ ستاره",
    roomName: "پنت‌هاوس پرزیدنتال",
    category: "vip",
    price: 6500000,
    priceFormatted: "۶,۵۰۰,۰۰۰",
    like: 99,
    rating: 5.0,
    capacity: "۶ نفره",
    image: "Mashhad-Almas_2-78.webp",
    features: ["تراس اختصاصی ۳۶۰ درجه", "باتلر اختصاصی", "استخر و سونا private", "منوی سفارشی"],
    description: "لوکس‌ترین اقامتگاه مهستان واقع در بالاترین طبقه با خدمات پیشخدمت اختصاصی و استخر خصوصی."
  }
];

const DEFAULT_COMMENTS = [
  {
    id: 1,
    username: "علی محمدی",
    like: 5,
    description: "اقامت دل‌انگیز و آرامی داشتیم؛ اتاق‌ها تمیز بودن و کارکنان خیلی خوش‌برخورد. کیفیت غذاهای رستوران هتل عالی بود."
  },
  {
    id: 2,
    username: "مریم کاظمی",
    like: 4.5,
    description: "هتل موقعیت فوق‌العاده‌ای داره، به مراکز اصلی نزدیکه، نظافتش خوبه، و مجموعه اسپا و استخر بسیار عالی بود."
  },
  {
    id: 3,
    username: "محمد ابراهیمی",
    like: 5,
    description: "رفتار پرسنل عالی و برخوردشون محترمانه بود؛ امکانات اتاق خوب و تخت‌ها راحت بودن، ارزش اقامت داره."
  },
  {
    id: 4,
    username: "سجاد رضایی",
    like: 4,
    description: "هتل شیک و مرتب با فضای آرام؛ طراحی اتاق‌ها مجلل بود و رزرو آنلاین سایت بسیار سریع انجام شد."
  },
  {
    id: 5,
    username: "مبینا حسینی",
    like: 5,
    description: "اقامت خانوادگی داشتیم، همه‌چیز طبق انتظار پیش رفت، پذیرش سریع و فضای لابی بسیار زیبا و دلنشین."
  }
];

// Robust Image Path Formatter (Case-insensitive Page/ detector)
function formatImagePath(imageFileName) {
  if (!imageFileName) return "assets/image/home.jpg";
  if (imageFileName.startsWith("http") || imageFileName.startsWith("data:")) return imageFileName;

  // Extract file name
  let filename = imageFileName.split('/').pop().split('\\').pop();
  
  // Detect if inside Page directory
  const hrefLower = window.location.href.toLowerCase();
  const isInsidePage = hrefLower.includes('/page/') || hrefLower.includes('\\page\\');
  const baseDir = isInsidePage ? '../assets/image/' : 'assets/image/';

  return baseDir + filename;
}

// Global Toast System
function showToast(message, type = 'success') {
  let container = document.querySelector('.toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `
    <i class="fa-solid ${type === 'success' ? 'fa-circle-check' : 'fa-circle-exclamation'}"></i>
    <span>${message}</span>
  `;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(20px)';
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

// Cart LocalStorage Functions
function getCart() {
  try {
    const data = localStorage.getItem("mahastan_cart");
    return data ? JSON.parse(data) : [];
  } catch (e) {
    console.error("Error reading cart:", e);
    return [];
  }
}

function saveCart(cart) {
  try {
    localStorage.setItem("mahastan_cart", JSON.stringify(cart));
    updateCartBadge();
  } catch (e) {
    console.error("Error saving cart:", e);
  }
}

function addToCart(roomId) {
  const room = DEFAULT_ROOMS.find(r => r.id === parseInt(roomId, 10));
  if (!room) return;

  let cart = getCart();
  const existingIndex = cart.findIndex(item => item.id === room.id);

  if (existingIndex > -1) {
    cart[existingIndex].quantity += 1;
  } else {
    cart.push({
      id: room.id,
      title: room.title,
      price: room.price,
      image: room.image,
      capacity: room.capacity,
      quantity: 1
    });
  }

  saveCart(cart);
  showToast(`اتاق "${room.roomName}" با موفقیت به سبد رزرو افزوده شد ✨`, 'success');
}

function removeFromCart(roomId) {
  let cart = getCart();
  cart = cart.filter(item => item.id !== parseInt(roomId, 10));
  saveCart(cart);
  showToast("اتاق از سبد خرید حذف شد.", 'error');
  if (typeof renderCartPage === 'function') renderCartPage();
}

function updateCartBadge() {
  const badgeEls = document.querySelectorAll('.cart-badge');
  const cart = getCart();
  const totalCount = cart.reduce((sum, item) => sum + item.quantity, 0);

  badgeEls.forEach(el => {
    el.textContent = totalCount;
    el.style.display = totalCount > 0 ? 'flex' : 'none';
  });
}

function goToProductPage(id) {
  const hrefLower = window.location.href.toLowerCase();
  const isInsidePage = hrefLower.includes('/page/') || hrefLower.includes('\\page\\');
  const target = isInsidePage ? `product.html?id=${id}` : `Page/product.html?id=${id}`;
  window.location.href = target;
}

// IntersectionObserver for Scroll Animations
function initScrollReveal() {
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
      }
    });
  }, observerOptions);

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
}

// Render Rooms Grid (Supports both .rooms-grid and .rooms-cart-section)
function renderRoomsGrid(containerEl, roomList = DEFAULT_ROOMS) {
  if (!containerEl) {
    containerEl = document.querySelector('.rooms-cart-section') || document.querySelector('.rooms-grid');
  }
  if (!containerEl) return;
  containerEl.innerHTML = "";

  if (roomList.length === 0) {
    containerEl.innerHTML = `<div class="empty-cart" style="grid-column: 1/-1;">هیچ اتاقی در این دسته‌بندی یافت نشد.</div>`;
    return;
  }

  const hrefLower = window.location.href.toLowerCase();
  const isInsidePage = hrefLower.includes('/page/') || hrefLower.includes('\\page\\');
  const detailLinkPrefix = isInsidePage ? 'product.html?id=' : 'Page/product.html?id=';

  roomList.forEach((room, index) => {
    const imgPath = formatImagePath(room.image);
    const delayClass = `delay-${(index % 4) + 1}`;

    const cardHtml = `
      <div class="room-card reveal ${delayClass}">
        <div class="room-card-img-wrapper">
          <img src="${imgPath}" alt="${room.title}" class="room-card-img" loading="lazy" />
          <span class="room-badge">${room.capacity}</span>
          <button class="room-like-btn" onclick="toggleLike(this, ${room.id})" title="علاقه‌مندی">
            <i class="fa-regular fa-heart"></i>
          </button>
        </div>
        <div class="room-card-body">
          <h3 class="room-card-title">${room.title}</h3>
          <div class="room-amenities">
            ${(room.features || []).slice(0, 3).map(f => `<span class="amenity-chip"><i class="fa-solid fa-check"></i> ${f}</span>`).join('')}
          </div>
          <div class="room-card-footer">
            <div class="room-price-box">
              <span class="room-price-val">${(room.price || 2000000).toLocaleString('fa-IR')} تومان</span>
              <span class="room-price-unit">هر شب اقامت</span>
            </div>
            <div style="display: flex; gap: 8px;">
              <a href="${detailLinkPrefix}${room.id}" class="btn-outline-gold" style="padding: 8px 12px; font-size: 0.82rem;">جزئیات</a>
              <button class="btn-gold" onclick="addToCart(${room.id})" style="padding: 8px 14px; font-size: 0.82rem;">رزرو</button>
            </div>
          </div>
        </div>
      </div>
    `;

    containerEl.insertAdjacentHTML('beforeend', cardHtml);
  });

  initScrollReveal();
}

// Render Comments (.comments-root)
function renderComments(containerEl = document.querySelector('.comments-root')) {
  if (!containerEl) return;
  containerEl.innerHTML = "";

  DEFAULT_COMMENTS.forEach((comment, index) => {
    const delayClass = `delay-${(index % 3) + 1}`;
    const initial = comment.username ? comment.username.charAt(0).toUpperCase() : "م";

    const starsHtml = Array.from({length: 5}, (_, i) => {
      if (i < Math.floor(comment.like)) return '<i class="fa-solid fa-star"></i>';
      if (i < comment.like) return '<i class="fa-solid fa-star-half-stroke"></i>';
      return '<i class="fa-regular fa-star"></i>';
    }).join('');

    const html = `
      <div class="review-card comment-box reveal ${delayClass}">
        <div class="review-header">
          <div class="review-user">
            <div class="user-avatar">${initial}</div>
            <div>
              <div class="user-name">${comment.username}</div>
              <span style="font-size: 0.75rem; color: var(--gold-primary);">میهمان هتل مهستان</span>
            </div>
          </div>
          <div class="review-rating">${starsHtml}</div>
        </div>
        <p class="review-text">«${comment.description}»</p>
      </div>
    `;

    containerEl.insertAdjacentHTML('beforeend', html);
  });
}

function openRoomModal(roomId) {
  const room = DEFAULT_ROOMS.find(r => r.id === parseInt(roomId, 10));
  if (!room) return;

  let modal = document.querySelector('.modal-overlay');
  if (!modal) {
    modal = document.createElement('div');
    modal.className = 'modal-overlay';
    document.body.appendChild(modal);
  }

  const imgPath = formatImagePath(room.image);

  modal.innerHTML = `
    <div class="modal-card">
      <button class="close-modal" onclick="closeRoomModal()">&times;</button>
      <div style="text-align: center; margin-bottom: 15px;">
        <img src="${imgPath}" style="width: 100%; height: 220px; object-fit: cover; border-radius: 12px; margin-bottom: 15px;" alt="${room.title}" />
        <h2 style="color: var(--gold-light); font-size: 1.5rem; margin-bottom: 8px;">${room.title}</h2>
        <p style="color: var(--text-secondary); font-size: 0.9rem; line-height: 1.6;">${room.description || ''}</p>
      </div>
      <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-subtle); padding: 15px; border-radius: 10px; margin-bottom: 20px;">
        <h4 style="color: var(--gold-primary); font-size: 0.9rem; margin-bottom: 10px;">امکانات و ویژگی‌ها:</h4>
        <div style="display: flex; flex-wrap: wrap; gap: 8px;">
          ${(room.features || []).map(f => `<span class="amenity-chip"><i class="fa-solid fa-star" style="color: var(--gold-primary);"></i> ${f}</span>`).join('')}
        </div>
      </div>
      <div style="display: flex; align-items: center; justify-content: space-between;">
        <div>
          <span style="font-size: 0.8rem; color: var(--text-muted);">قیمت هر شب:</span>
          <h3 style="color: var(--gold-light); font-size: 1.3rem;">${(room.price || 2000000).toLocaleString('fa-IR')} تومان</h3>
        </div>
        <button class="btn-gold" onclick="addToCart(${room.id}); closeRoomModal();">رزرو و افزودن به سبد</button>
      </div>
    </div>
  `;

  setTimeout(() => modal.classList.add('active'), 10);
}

function closeRoomModal() {
  const modal = document.querySelector('.modal-overlay');
  if (modal) {
    modal.classList.remove('active');
    setTimeout(() => modal.remove(), 300);
  }
}

function toggleLike(btn, id) {
  const icon = btn.querySelector('i');
  if (icon.classList.contains('fa-regular')) {
    icon.classList.remove('fa-regular');
    icon.classList.add('fa-solid');
    icon.style.color = '#FF5A5F';
    showToast('به علاقه مندی‌ها افزوده شد', 'success');
  } else {
    icon.classList.remove('fa-solid');
    icon.classList.add('fa-regular');
    icon.style.color = '';
  }
}

// Global Init
document.addEventListener("DOMContentLoaded", () => {
  updateCartBadge();
  initScrollReveal();
  renderComments();

  const featuredContainer = document.getElementById("featuredRoomsContainer") || document.querySelector(".rooms-cart-section");
  if (featuredContainer) {
    renderRoomsGrid(featuredContainer, DEFAULT_ROOMS.slice(0, 4));
  }

  const header = document.querySelector('header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 40) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }

  const mobileToggleBtn = document.querySelector('.mobile-toggle');
  const drawer = document.querySelector('.mobile-drawer');
  const overlay = document.querySelector('.drawer-overlay');

  if (mobileToggleBtn && drawer) {
    mobileToggleBtn.addEventListener('click', () => {
      drawer.classList.add('open');
      if (overlay) overlay.classList.add('active');
    });
  }

  const closeDrawerBtn = document.querySelector('.close-drawer');
  if (closeDrawerBtn && drawer) {
    closeDrawerBtn.addEventListener('click', () => {
      drawer.classList.remove('open');
      if (overlay) overlay.classList.remove('active');
    });
  }

  if (overlay) {
    overlay.addEventListener('click', () => {
      if (drawer) drawer.classList.remove('open');
      overlay.classList.remove('active');
    });
  }
});
