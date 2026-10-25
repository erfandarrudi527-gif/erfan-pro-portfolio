/**
 * MAHASTAN HOTEL - CART PAGE LOGIC
 */

function renderCartPage() {
  const cartItemsContainer = document.getElementById("cartItems");
  const subtotalEl = document.getElementById("subtotalPrice");
  const discountEl = document.getElementById("discountAmount");
  const finalPriceEl = document.getElementById("finalPrice");

  if (!cartItemsContainer) return;

  const cart = getCart();
  cartItemsContainer.innerHTML = "";

  if (cart.length === 0) {
    cartItemsContainer.innerHTML = `
      <div class="empty-cart reveal">
        <i class="fa-solid fa-hotel" style="font-size: 3rem; color: var(--gold-primary); margin-bottom: 15px;"></i>
        <p>سبد رزرو شما در حال حاضر خالی است.</p>
        <a href="Room.html" class="btn-gold" style="margin-top: 20px; display: inline-flex;">مشاهده و رزرو اتاق‌ها</a>
      </div>
    `;
    if (subtotalEl) subtotalEl.textContent = "۰ تومان";
    if (discountEl) discountEl.textContent = "۰ تومان";
    if (finalPriceEl) finalPriceEl.textContent = "۰ تومان";
    return;
  }

  let subtotal = 0;

  cart.forEach(item => {
    const itemTotal = (item.price || 2000000) * (item.quantity || 1);
    subtotal += itemTotal;

    const imgPath = formatImagePath(item.image);

    const itemEl = document.createElement("div");
    itemEl.className = "cart-item reveal";
    itemEl.innerHTML = `
      <div style="display: flex; align-items: center; gap: 16px;">
        <img src="${imgPath}" alt="${item.title}" style="width: 90px; height: 70px; object-fit: cover; border-radius: 8px; border: 1px solid var(--border-gold);" />
        <div class="cart-item-details">
          <h3>${item.title}</h3>
          <div class="cart-meta">
            <span>تعداد شب/اتاق: ${item.quantity}</span>
            <span>قیمت: ${(item.price || 2000000).toLocaleString('fa-IR')} تومان</span>
          </div>
        </div>
      </div>
      <div style="display: flex; align-items: center; gap: 20px;">
        <div class="cart-item-total">
          <span style="font-size: 0.75rem; color: var(--text-muted);">جمع این اتاق</span>
          <span class="price">${itemTotal.toLocaleString('fa-IR')} تومان</span>
        </div>
        <button class="btn-remove" onclick="removeFromCart(${item.id})">
          <i class="fa-solid fa-trash"></i>
        </button>
      </div>
    `;
    cartItemsContainer.appendChild(itemEl);
  });

  // Calculate Discounts
  const currentDiscountPercent = parseInt(localStorage.getItem("mahastan_discount_percent") || "0", 10);
  const discountAmount = Math.round((subtotal * currentDiscountPercent) / 100);
  const finalPrice = subtotal - discountAmount;

  if (subtotalEl) subtotalEl.textContent = `${subtotal.toLocaleString('fa-IR')} تومان`;
  if (discountEl) discountEl.textContent = `${discountAmount.toLocaleString('fa-IR')} تومان (${currentDiscountPercent}٪)`;
  if (finalPriceEl) finalPriceEl.textContent = `${finalPrice.toLocaleString('fa-IR')} تومان`;

  initScrollReveal();
}

function applyDiscountCode() {
  const inputEl = document.getElementById("discountInput");
  if (!inputEl) return;

  const code = inputEl.value.trim().toUpperCase();
  const codes = {
    "OFF10": 10,
    "OFF15": 15,
    "OFF25": 25,
    "GOLD30": 30
  };

  if (codes[code]) {
    localStorage.setItem("mahastan_discount_percent", codes[code]);
    showToast(`کد تخفیف ${codes[code]}٪ با موفقیت اعمال شد!`, 'success');
    renderCartPage();
  } else {
    showToast("کد تخفیف وارد شده نامعتبر است.", 'error');
  }
}

function checkoutCart() {
  const cart = getCart();
  if (cart.length === 0) {
    showToast("سبد رزرو شما خالی است!", 'error');
    return;
  }

  showToast("در حال انتقال به درگاه پرداخت بانکی مهستان...", 'success');
  setTimeout(() => {
    localStorage.removeItem("mahastan_cart");
    localStorage.removeItem("mahastan_discount_percent");
    updateCartBadge();
    renderCartPage();
    alert("رزرو شما با موفقیت ثبت شد و شماره پیگیری برای شما پیامک گردید ✨");
  }, 2000);
}

document.addEventListener("DOMContentLoaded", () => {
  renderCartPage();
});
