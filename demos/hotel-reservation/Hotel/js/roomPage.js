/**
 * MAHASTAN HOTEL - ROOM CATALOG PAGE JS
 */

document.addEventListener("DOMContentLoaded", () => {
  const roomsContainer = document.querySelector(".rooms-grid") || document.querySelector(".rooms-cart-section");
  if (roomsContainer) {
    renderRoomsGrid(roomsContainer, DEFAULT_ROOMS);
  }

  // Filter Buttons Initialization
  const filterBtns = document.querySelectorAll(".filter-btn");
  filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      filterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      const category = btn.getAttribute("data-filter");
      if (!category || category === "all") {
        renderRoomsGrid(roomsContainer, DEFAULT_ROOMS);
      } else {
        const filtered = DEFAULT_ROOMS.filter(r => r.category === category);
        renderRoomsGrid(roomsContainer, filtered);
      }
    });
  });
});
