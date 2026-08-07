(function () {
  'use strict';
  var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var DUR = 5500;

  /* ===== Hero 轮播 ===== */
  var slides = document.querySelectorAll('.hslide');
  var dots = document.querySelectorAll('#heroDots span');
  var hero = document.getElementById('hero');
  if (slides.length) {
    var cur = 0, timer = null, paused = false;

    function restartDot(i) {
      dots.forEach(function (d, k) {
        d.classList.toggle('on', k === i);
        var bar = d.querySelector('i');
        if (bar) {
          bar.style.animation = 'none';
          void bar.offsetWidth;
          if (k === i && !reduced) bar.style.animation = 'dotfill ' + DUR + 'ms linear forwards';
        }
      });
    }
    function go(i) {
      cur = (i + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.classList.toggle('on', k === cur); });
      restartDot(cur);
    }
    function play() {
      if (reduced) return;
      stop();
      timer = setInterval(function () { if (!paused) go(cur + 1); }, DUR);
    }
    function stop() { if (timer) { clearInterval(timer); timer = null; } }

    var prev = document.getElementById('heroPrev');
    var next = document.getElementById('heroNext');
    if (prev) prev.addEventListener('click', function () { go(cur - 1); play(); });
    if (next) next.addEventListener('click', function () { go(cur + 1); play(); });
    dots.forEach(function (d, k) {
      d.addEventListener('click', function () { go(k); play(); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') { go(cur - 1); play(); }
      if (e.key === 'ArrowRight') { go(cur + 1); play(); }
    });
    if (hero) {
      hero.addEventListener('mouseenter', function () { paused = true; });
      hero.addEventListener('mouseleave', function () { paused = false; });
      var tx = 0;
      hero.addEventListener('touchstart', function (e) { tx = e.touches[0].clientX; }, { passive: true });
      hero.addEventListener('touchend', function (e) {
        var dx = e.changedTouches[0].clientX - tx;
        if (Math.abs(dx) > 46) { go(cur + (dx < 0 ? 1 : -1)); play(); }
      }, { passive: true });
    }
    go(0);
    play();
  }

  /* ===== 导航滚动反馈 ===== */
  var head = document.getElementById('g-head');
  var hint = document.getElementById('scrollHint');
  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (head) head.classList.toggle('scrolled', y > 40);
    if (hint && !reduced) {
      hint.style.opacity = Math.max(0, 1 - y / 260);
      hint.style.transform = 'translateY(' + Math.min(y * 0.25, 60) + 'px)';
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ===== 滚动渐入 ===== */
  var reveals = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window && !reduced) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          var el = en.target;
          var d = parseInt(getComputedStyle(el).getPropertyValue('--d')) || 0;
          setTimeout(function () { el.classList.add('revealed'); }, d);
          io.unobserve(el);
        }
      });
    }, { threshold: 0.15 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('revealed'); });
  }

  /* ===== 数字计数 ===== */
  var counters = document.querySelectorAll('[data-count]');
  function countUp(el) {
    var target = parseInt(el.getAttribute('data-count'), 10);
    var t0 = null, dur = 1400;
    function step(ts) {
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var ease = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * ease);
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ('IntersectionObserver' in window && !reduced) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { countUp(en.target); cio.unobserve(en.target); }
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { cio.observe(el); });
  } else {
    counters.forEach(function (el) { el.textContent = el.getAttribute('data-count'); });
  }

  /* ===== 滚动提示点击 ===== */
  if (hint) {
    hint.addEventListener('click', function () {
      var stats = document.querySelector('.stats-band');
      if (stats) stats.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth' });
    });
  }
})();
