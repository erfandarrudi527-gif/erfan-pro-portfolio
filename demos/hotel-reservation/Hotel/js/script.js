/**
 * MAHASTAN HOTEL - GENERAL SCRIPTS & HOMEPAGE LOGIC
 */

document.addEventListener("DOMContentLoaded", () => {
  const featuredContainer = document.getElementById("featuredRoomsContainer") || document.querySelector(".rooms-cart-section");
  if (featuredContainer) {
    // Show top 4 rooms on home page
    renderRoomsGrid(featuredContainer, DEFAULT_ROOMS.slice(0, 4));
  }
});
