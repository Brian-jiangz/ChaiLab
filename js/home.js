(function () {
  'use strict';
  var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var DUR = 6000;

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
        var v = s.querySelector('video');
        if (v) {
          if (going) { try { v.play(); } catch (e) {} }
          else { v.pause(); }
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

  /* ===== 学术·科研面板：左侧索引 hover 切换右侧大图 ===== */
  var acaIndex = document.querySelector('.aca-index');
  var acaImgs = document.querySelectorAll('.aca-stage-img, .aca-stage-video');
  var acaCapT = document.querySelector('.aca-stage-cap .cap-t');
  var acaCapD = document.querySelector('.aca-stage-cap .cap-d');
  if (acaIndex && acaImgs.length) {
    var acaItems = acaIndex.querySelectorAll('li');
    acaItems.forEach(function (li, k) {
      li.addEventListener('mouseenter', function () {
        acaItems.forEach(function (x, j) { x.classList.toggle('on', j === k); });
        acaImgs.forEach(function (img, j) {
          img.classList.toggle('on', j === k);
          var v = img.querySelector('video');
          if (v) { if (j === k) { try { v.play(); } catch (e) {} } else { v.pause(); } }
        });
        if (acaCapT) acaCapT.textContent = li.querySelector('.t').textContent;
        if (acaCapD) acaCapD.textContent = li.querySelector('.d').textContent;
      });
      li.addEventListener('click', function () {
        var link = li.getAttribute('data-link');
        if (link && link.indexOf('http') === 0) window.open(link, '_blank');
        else if (link) window.location.href = link;
      });
    });
  }

  /* ===== 北大式整屏切换：内容层上滑盖住 Hero / 下滑退出 ===== */
  var bodyHome = document.getElementById('bodyHome');
  var bodyMain = document.getElementById('bodyMain');
  var hintBtn = document.getElementById('scrollHint');
  var switching = false;

  function goDown() {
    if (!bodyMain || switching) return;
    switching = true;
    bodyMain.classList.add('show');
    document.body.classList.remove('locked');
    if (head) head.classList.add('scrolled');
    if (bodyHome) bodyHome.style.pointerEvents = 'none';
    setTimeout(function () { switching = false; }, 900);
  }
  function goUp() {
    if (!bodyMain || switching) return;
    if (!bodyMain.classList.contains('show')) return;
    switching = true;
    bodyMain.classList.remove('show');
    document.body.classList.add('locked');
    if (head) head.classList.remove('scrolled');
    if (bodyHome) bodyHome.style.pointerEvents = '';
    setTimeout(function () { switching = false; }, 900);
  }

  /* 初始状态：Hero 显示，锁定滚动 */
  if (bodyHome) document.body.classList.add('locked');

  /* 滚轮：Hero 上向下 -> 内容上滑；内容顶部向上 -> 回 Hero（仅首页）
     用时间戳防抖（Date.now 真实时间，不受 bfcache 定时器冻结影响） */
  var lastSwitch = 0;
  var SWITCH_LOCK = 1100;
  function onWheel(e) {
    if (!bodyMain) return;
    if (Date.now() - lastSwitch < SWITCH_LOCK) { e.preventDefault(); return; }
    var y = window.scrollY || window.pageYOffset;
    var atTop = y < 8;
    var shown = bodyMain.classList.contains('show');
    if (e.deltaY > 0 && atTop && !shown) {
      e.preventDefault();
      lastSwitch = Date.now();
      goDown();
    } else if (e.deltaY < 0 && atTop && shown) {
      e.preventDefault();
      lastSwitch = Date.now();
      goUp();
    }
  }
  function bindWheel() {
    window.removeEventListener('wheel', onWheel);
    window.addEventListener('wheel', onWheel, { passive: false });
  }
  bindWheel();

  /* 离开页面时记录整屏状态（sessionStorage），供 bfcache 刷新后恢复 */
  function saveScreenState() {
    if (!bodyMain) return;
    try {
      sessionStorage.setItem('chai_screen', JSON.stringify({
        show: bodyMain.classList.contains('show'),
        y: window.scrollY || 0
      }));
      sessionStorage.setItem('chai_reload_pending', '1');
    } catch (e) {}
  }
  window.addEventListener('pagehide', saveScreenState);

  /* bfcache 恢复（浏览器返回）：状态错乱的根因是 bfcache 冻结 JS 定时器/监听器。
     终极方案：强制刷新重建页面，再用 sessionStorage 恢复离开时的界面状态。 */
  window.addEventListener('pageshow', function (e) {
    if (!e.persisted) return;
    saveScreenState();
    window.location.reload();
  });
  /* 刷新/重载后：仅当存在 pending 标志（确实经历了 bfcache 刷新）才恢复状态 */
  function restoreScreen() {
    var pending = false, raw = null;
    try {
      pending = !!sessionStorage.getItem('chai_reload_pending');
      sessionStorage.removeItem('chai_reload_pending');
      raw = sessionStorage.getItem('chai_screen');
      sessionStorage.removeItem('chai_screen');
    } catch (e) {}
    if (!pending || !raw || !bodyMain) return;
    try {
      var s = JSON.parse(raw);
      if (s.show) {
        bodyMain.classList.add('show');
        document.body.classList.remove('locked');
        if (head) head.classList.add('scrolled');
        window.scrollTo(0, s.y || 0);
      }
    } catch (e) {}
  }

  /* 点击右下滚动提示 -> 下滑 */
  if (hintBtn) {
    hintBtn.addEventListener('click', function () {
      if (!bodyMain.classList.contains('show')) goDown();
    });
  }

  /* 键盘：↓/PgDn 下滑，↑/PgUp 回顶（仅首页） */
  document.addEventListener('keydown', function (e) {
    if (!bodyMain) return;
    var atTop = (window.scrollY || 0) < 8;
    var shown = bodyMain.classList.contains('show');
    if ((e.key === 'ArrowDown' || e.key === 'PageDown' || e.key === ' ') && atTop && !shown) {
      e.preventDefault(); goDown();
    }
    if ((e.key === 'ArrowUp' || e.key === 'PageUp') && atTop && shown) {
      e.preventDefault(); goUp();
    }
  });

  /* 触摸：Hero 内上滑 -> 下滑；内容层顶部下拉 -> 回顶 */
  if (bodyHome) {
    var tStart = 0;
    bodyHome.addEventListener('touchstart', function (e) { tStart = e.touches[0].clientY; }, { passive: true });
    bodyHome.addEventListener('touchend', function (e) {
      var dy = e.changedTouches[0].clientY - tStart;
      if (dy < -30 && !bodyMain.classList.contains('show')) goDown();
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
  var hasScreens = !!(document.getElementById('bodyMain'));
  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (!hasScreens && head) head.classList.toggle('scrolled', y > 40);
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

  /* ===== 窄屏菜单：点击展开 / 自动收回 ===== */
  var nav = document.querySelector('.g-nav');
  var toggle = document.querySelector('.nav-toggle');
  var mqNarrow = window.matchMedia('(max-width: 1100px)');
  function closeSubs() {
    if (nav) nav.querySelectorAll('.has-sub.open').forEach(function (el) { el.classList.remove('open'); });
  }
  function closeMenu() { closeSubs(); if (nav) nav.classList.remove('open'); }
  if (toggle) {
    toggle.addEventListener('click', function (e) {
      e.stopPropagation();
      nav.classList.toggle('open');
      if (!nav.classList.contains('open')) closeSubs();
    });
  }
  if (nav) {
    nav.addEventListener('click', function (e) {
      var subLi = e.target.closest('.has-sub');
      if (subLi && mqNarrow.matches) {
        e.preventDefault();
        var wasOpen = subLi.classList.contains('open');
        closeSubs();
        if (!wasOpen) subLi.classList.add('open');
      } else if (e.target.closest('a')) {
        closeMenu();
      }
    });
    document.addEventListener('click', function (e) {
      if (!nav.contains(e.target) && !(toggle && toggle.contains(e.target))) closeMenu();
    });
    window.addEventListener('scroll', function () {
      if (nav.classList.contains('open')) closeMenu();
    }, { passive: true });
    window.addEventListener('resize', function () {
      if (nav.classList.contains('open')) closeMenu();
    });
  }
  /* ===== 二级页面：左侧竖排导航滚动高亮 ===== */
  var subNav = document.getElementById('subNav');
  if (subNav) {
    var subLinks = Array.prototype.slice.call(subNav.querySelectorAll('a[href*="#"]'));
    var subTargets = subLinks.map(function (a) {
      var id = a.getAttribute('href').split('#')[1];
      return id ? document.getElementById(id) : null;
    }).filter(Boolean);
    function onScrollSpy() {
      if (!subTargets.length) return;
      var y = (window.scrollY || 0) + 130;
      var cur = subTargets[0];
      subTargets.forEach(function (t) {
        if (t && t.offsetTop <= y) cur = t;
      });
      subLinks.forEach(function (a) {
        var id = a.getAttribute('href').split('#')[1];
        var on = cur && id === cur.id;
        a.classList.toggle('active', on);
      });
    }
    window.addEventListener('scroll', onScrollSpy, { passive: true });
    window.addEventListener('resize', onScrollSpy);
    onScrollSpy();
  }

  /* ===== 成员筛选：胶囊标签（全部/教师/博后/博硕/校友） ===== */
  document.querySelectorAll('.tabnav-filter').forEach(function (tabnav) {
    var items = Array.prototype.slice.call(tabnav.querySelectorAll('.tabnav-item'));
    var tiles = document.querySelectorAll('.tile[data-cat]');
    function activate(i) {
      items.forEach(function (btn, idx) {
        btn.classList.toggle('active', idx === i);
      });
      var cat = items[i].getAttribute('data-filter');
      tiles.forEach(function (tile) {
        tile.style.display = (cat === 'all' || tile.getAttribute('data-cat') === cat) ? '' : 'none';
      });
    }
    items.forEach(function (btn, i) {
      btn.addEventListener('click', function () { activate(i); });
    });
    var activeIdx = items.findIndex(function (b) { return b.classList.contains('active'); });
    if (activeIdx < 0) activate(0);
  });

  /* ===== 语言切换：保留当前页面，不跳回首页 ===== */
  (function () {
    var page = (location.pathname.split('/').pop() || 'index.html').replace(/\/$/, '');
    var inEn = /\/en\//.test(location.pathname);
    var links = document.querySelectorAll('.lang-switch, .m-lang a');
    links.forEach(function (a) {
      a.href = inEn ? '../' + page : 'en/' + page;
    });
  })();

  /* bfcache 刷新后恢复整屏状态（head 已就绪） */
  restoreScreen();
})();
