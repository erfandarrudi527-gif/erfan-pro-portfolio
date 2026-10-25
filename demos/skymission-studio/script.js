(function () {
  'use strict';

  const burger = document.querySelector('.navbar__burger');
  const links = document.querySelector('.navbar__links');
  const cta = document.querySelector('.navbar__cta');

  if (!burger || !links) return;

  burger.addEventListener('click', () => {
    const isOpen = links.classList.toggle('navbar__links--open');
    burger.setAttribute('aria-expanded', String(isOpen));
    if (cta) cta.classList.toggle('navbar__cta--open', isOpen);
  });
})();
