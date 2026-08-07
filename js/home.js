(function () {
  'use strict';
  var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var DUR = 6000;
  var isMobile = function () { return window.innerWidth <= 900; };

  /* ===== Hero 轮播（滑动 + 淡入 + Ken Burns） ===== */
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
    function go(i, dir) {
      var from = cur;
      cur = (i + slides.length) % slides.length;
      slides.forEach(function (s, k) {
        var going = k === cur, leaving = k === from && !going;
        s.classList.remove('slide-in-l', 'slide-in-r', 'slide-out-l', 'slide-out-r');
        if (going) {
          s.classList.add('on');
          if (!reduced) s.classList.add(dir < 0 ? 'slide-in-l' : 'slide-in-r');
        } else if (leaving) {
          if (!reduced) s.classList.add(dir < 0 ? 'slide-out-l' : 'slide-out-r');
          setTimeout(function () { s.classList.remove('on'); }, 600);
        } else {
          s.classList.remove('on');
        }
      });
      restartDot(cur);
    }
    function play() {
      if (reduced) return;
      stop();
      timer = setInterval(function () { if (!paused) go(cur + 1, 1); }, DUR);
    }
    function stop() { if (timer) { clearInterval(timer); timer = null; } }

    var prev = document.getElementById('heroPrev');
    var next = document.getElementById('heroNext');
    if (prev) prev.addEventListener('click', function () { go(cur - 1, -1); play(); });
    if (next) next.addEventListener('click', function () { go(cur + 1, 1); play(); });
    dots.forEach(function (d, k) {
      d.addEventListener('click', function () { go(k, k > cur ? 1 : -1); play(); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') { go(cur - 1, -1); play(); }
      if (e.key === 'ArrowRight') { go(cur + 1, 1); play(); }
    });
    if (hero) {
      hero.addEventListener('mouseenter', function () { paused = true; });
      hero.addEventListener('mouseleave', function () { paused = false; });
      var tx = 0, tdir = 0;
      hero.addEventListener('touchstart', function (e) { tx = e.touches[0].clientX; }, { passive: true });
      hero.addEventListener('touchmove', function (e) { tdir = e.touches[0].clientX - tx; }, { passive: true });
      hero.addEventListener('touchend', function (e) {
        var dx = e.changedTouches[0].clientX - tx;
        if (Math.abs(dx) > 46) { go(cur + (dx < 0 ? 1 : -1), dx < 0 ? 1 : -1); play(); }
        tdir = 0;
      }, { passive: true });
    }
    go(0, 1);
    play();
  }

  /* ===== 阅读进度条 ===== */
  var pbar = document.getElementById('readProgress');
  if (pbar) {
    var docH = 0;
    function onResize() { docH = document.documentElement.scrollHeight - window.innerHeight; }
    window.addEventListener('resize', onResize); onResize();
    function onScrollP() {
      var y = window.scrollY || window.pageYOffset;
      pbar.style.width = docH > 0 ? Math.min((y / docH) * 100, 100) + '%' : '0%';
    }
    window.addEventListener('scroll', onScrollP, { passive: true });
    onScrollP();
  }

  /* ===== 北大式整屏切换：Hero 下滑 / 回顶 ===== */
  var bodyHome = document.getElementById('bodyHome');
  var bodyMain = document.getElementById('bodyMain');
  var hintBtn = document.getElementById('scrollHint');
  var switching = false;

  function goDown() {
    if (!bodyHome || switching) return;
    switching = true;
    if (!reduced) bodyHome.classList.add('leave');
    else bodyHome.classList.add('leave');
    setTimeout(function () { switching = false; }, 900);
  }
  function goUp() {
    if (!bodyHome || switching) return;
    if (!bodyHome.classList.contains('leave')) return;
    switching = true;
    bodyHome.classList.remove('leave');
    window.scrollTo(0, 0);
    setTimeout(function () { switching = false; }, 900);
  }

  /* 滚轮：Hero 内下滑 -> 整屏切换；内容层顶部上滚 -> 回 Hero */
  var wheelLock = false;
  window.addEventListener('wheel', function (e) {
    if (wheelLock) { e.preventDefault(); return; }
    var y = window.scrollY || window.pageYOffset;
    var atTop = y < 8;
    if (e.deltaY > 0 && atTop && bodyHome && !bodyHome.classList.contains('leave')) {
      e.preventDefault();
      wheelLock = true;
      goDown();
      setTimeout(function () { wheelLock = false; }, 1200);
    } else if (e.deltaY < 0 && atTop && bodyHome && bodyHome.classList.contains('leave')) {
      e.preventDefault();
      wheelLock = true;
      goUp();
      setTimeout(function () { wheelLock = false; }, 1200);
    }
  }, { passive: false });

  /* 点击右下滚动提示 -> 下滑 */
  if (hintBtn) {
    hintBtn.addEventListener('click', function () {
      if (!bodyHome.classList.contains('leave')) goDown();
    });
  }

  /* 键盘：↓/PgDn 下滑，↑/PgUp 回顶 */
  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowDown' || e.key === 'PageDown' || e.key === ' ') {
      if ((window.scrollY || 0) < 8 && bodyHome && !bodyHome.classList.contains('leave')) {
        e.preventDefault(); goDown();
      }
    }
    if (e.key === 'ArrowUp' || e.key === 'PageUp') {
      if ((window.scrollY || 0) < 8 && bodyHome) {
        e.preventDefault(); goUp();
      }
    }
  });

  /* 触摸：Hero 内上滑 -> 下滑；内容层顶部下拉 -> 回顶 */
  if (bodyHome) {
    var tStart = 0;
    bodyHome.addEventListener('touchstart', function (e) { tStart = e.touches[0].clientY; }, { passive: true });
    bodyHome.addEventListener('touchend', function (e) {
      var dy = e.changedTouches[0].clientY - tStart;
      if (dy < -30 && !bodyHome.classList.contains('leave')) goDown();
    }, { passive: true });
  }
  if (bodyMain) {
    var mStart = 0;
    bodyMain.addEventListener('touchstart', function (e) { mStart = e.touches[0].clientY; }, { passive: true });
    bodyMain.addEventListener('touchend', function (e) {
      var dy = e.changedTouches[0].clientY - mStart;
      if (dy > 30 && (window.scrollY || 0) < 8) goUp();
    }, { passive: true });
  }

  /* ===== 导航滚动反馈 + 返回顶部 ===== */
  var head = document.getElementById('g-head');
  var topBtn = document.getElementById('backTop');
  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (head) head.classList.toggle('scrolled', y > 40);
    if (topBtn) topBtn.classList.toggle('show', y > 600);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  if (topBtn) {
    topBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: reduced ? 'auto' : 'smooth' });
    });
  }

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

  /* ===== 移动端菜单：手风琴 + 自动关闭 ===== */
  var nav = document.querySelector('.g-nav');
  var toggle = document.querySelector('.nav-toggle');
  function closeMenu() { if (nav) nav.classList.remove('open'); }
  if (toggle) {
    toggle.addEventListener('click', function (e) {
      e.stopPropagation();
      nav.classList.toggle('open');
    });
  }
  if (nav) {
    nav.addEventListener('click', function (e) {
      var link = e.target.closest('a');
      if (link) {
        var li = link.parentElement;
        var sub = li.querySelector('.sub');
        if (sub && isMobile()) {
          e.preventDefault();
          e.stopPropagation();
          var open = sub.classList.toggle('show');
          li.classList.toggle('open', open);
          sub.setAttribute('aria-hidden', open ? 'false' : 'true');
        } else if (!link.closest('.sub')) {
          closeMenu();
        }
      }
    });
    document.addEventListener('click', function (e) {
      if (!nav.contains(e.target) && !(toggle && toggle.contains(e.target))) closeMenu();
    });
  }
  var subs = document.querySelectorAll('.g-nav .sub');
  subs.forEach(function (s) { s.setAttribute('aria-hidden', 'true'); });
})();
