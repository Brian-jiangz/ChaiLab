#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成课题组网站（中英双语，多页面结构）"""

ZH, EN = 'zh', 'en'

NAV_ZH = [
    ('index.html', '首页'), ('about.html', '课题组简介'), ('members.html', '成员介绍'),
    ('research.html', '研究方向'),
    ('papers.html', '发表论文'), ('news.html', '新闻动态'), ('links.html', '相关链接'),
]
NAV_EN = [
    ('index.html', 'Home'), ('about.html', 'About'), ('members.html', 'Members'),
    ('research.html', 'Research'),
    ('papers.html', 'Publications'), ('news.html', 'News'), ('links.html', 'Links'),
]

TXT = {
    'zh': {
        'site_name': '柴扉教授课题组',
        'site_sub': 'Chai Group · Xiamen University',
        'lang_switch': 'English',
        'lang_short': 'En',
        'lang_url': 'en/index.html',
        'footer_name': '柴扉教授课题组',
        'footer_org': '海洋生物地球化学全国重点实验室（厦门大学）',
        'footer_addr': '厦门大学翔安校区周隆泉楼',
        'footer_contact': '联系方式',
        'footer_email': '邮箱：fchai@xmu.edu.cn',
        'footer_zip': '邮编：361102',
        'footer_nav': '快速导航',
        'footer_about': '课题组简介',
        'footer_members': '成员介绍',
        'footer_project': 'CESM-CoSiNE',
        'footer_links': '相关链接',
        'footer_copy': '© 2026 柴扉教授课题组 · 厦门大学海洋生物地球化学全国重点实验室',
    },
    'en': {
        'site_name': 'Chai Group',
        'site_sub': 'Xiamen University · MEL',
        'lang_switch': '中文',
        'lang_short': '中文',
        'lang_url': '../index.html',
        'footer_name': 'Chai Group',
        'footer_org': 'State Key Laboratory of Marine Environmental Science (MEL), Xiamen University',
        'footer_addr': 'Zhoulongquan Building, Xiang\u2019an Campus, Xiamen University',
        'footer_contact': 'Contact',
        'footer_email': 'Email: fchai@xmu.edu.cn',
        'footer_zip': 'Postal code: 361102',
        'footer_nav': 'Quick Links',
        'footer_about': 'About',
        'footer_members': 'Members',
        'footer_project': 'CESM-CoSiNE',
        'footer_links': 'Related Links',
        'footer_copy': '© 2026 Chai Group · State Key Laboratory of Marine Environmental Science, Xiamen University',
    },
}

DD_ZH = {
    'research': [
        ('research.html#r0', '生态系统与生物地球化学模拟'),
        ('research.html#r1', '碳循环与气候反馈'),
        ('research.html#r2', '次中尺度过程与生态效应'),
        ('research.html#r3', '古气候与古海洋模拟'),
        ('research.html#r4', '海洋数字孪生'),
        ('research.html#r5', '观测—模拟融合'),
        ('research.html#project', 'CESM-CoSiNE 项目'),
    ],
    'links': [
        ('https://coeoa.xmu.edu.cn/t/CF/', '柴扉教授个人主页', '_blank'),
        ('https://meli.xmu.edu.cn/', 'MEL 实验室官网', '_blank'),
        ('links.html', '全部相关链接', ''),
    ],
}
DD_EN = {
    'research': [
        ('research.html#r0', 'Ecosystem & Biogeochemical Modeling'),
        ('research.html#r1', 'Carbon Cycle & Climate Feedbacks'),
        ('research.html#r2', 'Submesoscale Processes'),
        ('research.html#r3', 'Paleoclimate Modeling'),
        ('research.html#r4', 'Ocean Digital Twin'),
        ('research.html#r5', 'Observation\u2013Model Integration'),
        ('research.html#project', 'CESM-CoSiNE Project'),
    ],
    'links': [
        ('https://coeoa.xmu.edu.cn/t/CF/', "Prof. Chai's Homepage", '_blank'),
        ('https://meli.xmu.edu.cn/', 'MEL Official Site', '_blank'),
        ('links.html', 'All Related Links', ''),
    ],
}

def nav(active, lang):
    items = NAV_EN if lang == EN else NAV_ZH
    dd = DD_EN if lang == EN else DD_ZH
    t = TXT[lang]
    parts = []
    for f, name in items:
        cls = ' class="active"' if f == active else ''
        if f == 'research.html':
            subs = '\n'.join(f'          <dd><a href="{u}">{n}</a></dd>' for u, n in dd['research'])
            parts.append(f'''        <li class="has-sub"><a href="{f}"{cls}>{name}</a>
          <div class="sub"><dl>
{subs}
          </dl></div>
        </li>''')
        elif f == 'links.html':
            subs = '\n'.join(
                f'          <dd><a href="{u}"{(" target=" + chr(34) + tgt + chr(34)) if tgt else ""}>{n}</a></dd>'
                for u, n, tgt in dd['links'])
            parts.append(f'''        <li class="has-sub"><a href="{f}"{cls}>{name}</a>
          <div class="sub"><dl>
{subs}
          </dl></div>
        </li>''')
        else:
            parts.append(f'        <li><a href="{f}"{cls}>{name}</a></li>')
    lis = '\n'.join(parts)
    return f'''<!-- 顶部导航 -->
<header class="g-head" id="g-head">
  <div class="inner main">
    <a href="index.html" class="logo">
      <img src="images/xmu_logo.png" alt="Xiamen University" class="logo-xmu">
      <img src="images/mel_logo.svg" alt="MEL" class="logo-mel">
      <div class="txt">
        <strong>{t['site_name']}</strong>
      </div>
    </a>
    <nav class="g-nav">
      <ul>
{lis}
        <li class="m-lang"><a href="{t['lang_url']}">{t['lang_switch']}</a></li>
      </ul>
    </nav>
    <a class="lang-switch" href="{t['lang_url']}">{t['lang_short']}</a>
    <button class="nav-toggle" onclick="document.querySelector('.g-nav').classList.toggle('open')">☰</button>
  </div>
</header>'''

def footer(lang):
    t = TXT[lang]
    if lang == EN:
        qlinks = [
            ('about.html', 'About'), ('members.html', 'Members'), ('research.html', 'Research'),
            ('papers.html', 'Publications'), ('news.html', 'News'), ('links.html', 'Links'),
        ]
        rlinks = [
            ('https://coeoa.xmu.edu.cn/t/CF/', "Prof. Chai's Homepage", ' target="_blank"'),
            ('https://meli.xmu.edu.cn/', 'MEL, Xiamen University', ' target="_blank"'),
            ('https://www.xmu.edu.cn/', 'Xiamen University', ' target="_blank"'),
        ]
    else:
        qlinks = [
            ('about.html', '课题组简介'), ('members.html', '成员介绍'), ('research.html', '研究方向'),
            ('papers.html', '发表论文'), ('news.html', '新闻动态'), ('links.html', '相关链接'),
        ]
        rlinks = [
            ('https://coeoa.xmu.edu.cn/t/CF/', '柴扉教授个人主页', ' target="_blank"'),
            ('https://meli.xmu.edu.cn/', '海洋生物地球化学全国重点实验室', ' target="_blank"'),
            ('https://www.xmu.edu.cn/', '厦门大学', ' target="_blank"'),
        ]
    q_html = ''.join(f'<a href="{u}">{n}</a>' for u, n in qlinks)
    r_html = ''.join(f'<a href="{u}"{x}>{n}</a>' for u, n, x in rlinks)
    return f'''<!-- 页脚 -->
<footer class="footer">
  <div class="inner">
    <div class="f-brand">
      <h5>{t['footer_name']}</h5>
      <p>{t['footer_org']}</p>
      <p>{t['footer_addr']}</p>
    </div>
    <div>
      <h5>{t['footer_nav']}</h5>
      <div class="f-links">{q_html}</div>
    </div>
    <div>
      <h5>{t['footer_links']}</h5>
      <div class="f-links">{r_html}</div>
    </div>
    <div>
      <h5>{t['footer_contact']}</h5>
      <p>{t['footer_email']}</p>
      <p>{t['footer_zip']}</p>
    </div>
    <div class="copy">{t['footer_copy']}</div>
  </div>
</footer>'''

def page(fname, title, en_sub, body, lang, extra='', banner=True, scripts=''):
    t = TXT[lang]
    sitename = t['site_name']
    banner_html = f'''
<div class="page-banner">
  <h1>{title}</h1>
  <p>{en_sub}</p>
</div>
''' if banner else ''
    scripts_html = f'<script>document.documentElement.classList.add("anim");</script>\n<script src="{scripts}" defer></script>' if scripts else ''
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="images/favicon.svg" type="image/svg+xml">
<title>{title} | {sitename} · Xiamen University</title>
<link rel="stylesheet" href="css/style.css">
{scripts_html}
</head>
<body>

{nav(fname, lang)}
{banner_html}
{body}
{footer(lang)}
{extra}
</body>
</html>
'''

SVG_WAVE = '''<svg class="icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><path d="M2 12c1.8-2.5 3.6-2.5 5.4 0s3.6 2.5 5.4 0 3.6-2.5 5.4 0 3.6 2.5 5.4 0"/><path d="M2 17c1.8-2.5 3.6-2.5 5.4 0s3.6 2.5 5.4 0 3.6-2.5 5.4 0 3.6 2.5 5.4 0"/><path d="M2 7c1.8-2.5 3.6-2.5 5.4 0s3.6 2.5 5.4 0 3.6-2.5 5.4 0 3.6 2.5 5.4 0"/></svg>'''
SVG_GLOBE = '''<svg class="icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18a14 14 0 0 1 0-18"/></svg>'''
SVG_BIO = '''<svg class="icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><path d="M12 12m-4.5 0a4.5 4.5 0 1 0 9 0a4.5 4.5 0 1 0-9 0"/><path d="M12 12l6-5"/><path d="M12 12l-7-2"/><path d="M12 12l3 6"/><path d="M12 12l-4 5"/></svg>'''
SVG_TIME = '''<svg class="icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/><path d="M7 3.5C8.5 4.8 10.2 5.5 12 5.5s3.5-.7 5-2"/></svg>'''
SVG_DIGI = '''<svg class="icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><rect x="3" y="4" width="18" height="12" rx="1"/><path d="M8 20h8"/><path d="M12 16v4"/></svg>'''
SVG_SAT = '''<svg class="icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><circle cx="12" cy="12" r="1.5" fill="currentColor"/><path d="M9 9a4.2 4.2 0 0 1 6 0"/><path d="M6.8 6.8a8 8 0 0 1 10.4 0"/><path d="M15 15a4.2 4.2 0 0 1-6 0"/><path d="M17.2 17.2a8 8 0 0 0-10.4 0"/></svg>'''
SVG_USER = '''<svg class="icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.6-6 8-6s6.5 2 8 6"/></svg>'''
SVG_LAB = '''<svg class="icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><path d="M10 2v6l-6.5 11A2.2 2.2 0 0 0 5.3 22h13.4a2.2 2.2 0 0 0 1.8-3L14 8V2"/><path d="M7.5 14h9"/><path d="M10 2h4"/></svg>'''

# ============ 内容（中英双语） ============

ABOUT_BODY = {
'zh': '''<div class="section">
  <div class="intro-grid">
    <div class="intro-card">
      <p>本课题组依托厦门大学海洋生物地球化学全国重点实验室，长期从事海洋物理—生态—生物地球化学耦合研究，聚焦海洋碳循环、营养盐循环与生态系统对气候变化的响应与反馈。</p>
      <p>课题组以自主发展的 CESM-CoSiNE 海洋生态系统—生物地球化学模块为核心工具，结合观测资料与数值模拟，研究北太平洋、南海及全球大洋中浮游生态系统与碳循环的调控机制，并拓展至古气候重建与海洋数字孪生等前沿方向。</p>
      <p id="join">课题组面向全球招聘博士后、博士生与硕士生，欢迎对海洋生物地球化学、气候模拟与计算海洋学感兴趣的同学加入。</p>
      <p style="margin-top:28px"><a class="btn btn-solid" href="members.html">了解课题组成员 →</a></p>
    </div>
    <div class="pi-card">
      <div class="pi-avatar"><img src="images/chai_fei.jpg" alt="柴扉教授"></div>
      <h3>柴扉 教授</h3>
      <div class="title">"唐世凤"海洋学科讲席教授 · PI</div>
      <ul class="info">
        <li><b>单位：</b>海洋生物地球化学全国重点实验室（厦门大学）</li>
        <li><b>地址：</b>厦门大学翔安校区周隆泉楼</li>
        <li><b>邮箱：</b>fchai@xmu.edu.cn</li>
        <li><b>学历：</b>杜克大学 生物海洋学博士（1991–1995）</li>
        <li><b>经历：</b>曾任美国缅因大学海洋学院教授（终身教职）</li>
      </ul>
    </div>
  </div>
</div>''',
'en': '''<div class="section">
  <div class="intro-grid">
    <div class="intro-card">
      <p>Affiliated with the State Key Laboratory of Marine Environmental Science (MEL) at Xiamen University, our group conducts research on coupled physical\u2013ecological\u2013biogeochemical oceanography, with a focus on the marine carbon cycle, nutrient cycles, and the response and feedback of marine ecosystems to climate change.</p>
      <p>Centered on the CESM-CoSiNE marine ecosystem\u2013biogeochemistry module, which we develop in-house, and combining observations with numerical simulation, the group studies the controls of planktonic ecosystems and the carbon cycle in the North Pacific, the South China Sea, and the global ocean, extending to paleoclimate reconstruction and ocean digital twins.</p>
      <p id="join">The group welcomes postdoctoral researchers and PhD/Master's students from around the world with interests in marine biogeochemistry, climate modeling, and computational oceanography.</p>
      <p style="margin-top:28px"><a class="btn btn-solid" href="members.html">Meet the Team →</a></p>
    </div>
    <div class="pi-card">
      <div class="pi-avatar"><img src="images/chai_fei.jpg" alt="Prof. Fei Chai"></div>
      <h3>Prof. Fei Chai</h3>
      <div class="title">Tang Shifeng Chair Professor in Marine Sciences · PI</div>
      <ul class="info">
        <li><b>Unit:</b> State Key Laboratory of Marine Environmental Science (MEL), XMU</li>
        <li><b>Office:</b> Zhoulongquan Building, Xiang\u2019an Campus, XMU</li>
        <li><b>Email:</b> fchai@xmu.edu.cn</li>
        <li><b>Ph.D.:</b> Biological Oceanography, Duke University (1991\u20131995)</li>
        <li><b>Career:</b> Former Professor (tenured), School of Marine Sciences, University of Maine</li>
      </ul>
    </div>
  </div>
</div>''',
}

def research_tiles(lang):
    tiles_html = tiles_body(lang)
    proj = project_box(lang, full=False)
    return f'''<div class="section">
  <div class="research">
{tiles_html}
  </div>
</div>

<div class="section">
  {proj}
</div>'''

def tiles_body(lang, href_base='#'):
    if lang == EN:
        items = [
            'Marine Ecosystem and Biogeochemical Modeling',
            'Marine Carbon Cycle and Climate Feedbacks',
            'Submesoscale Processes and Ecological Effects',
            'Paleoclimate and Paleoceanography',
            'Ocean Digital Twin',
            'Observation\u2013Model Integration',
        ]
        descs = [
            'Development and improvement of the CESM-CoSiNE coupled marine ecosystem\u2013biogeochemistry module to simulate the spatiotemporal evolution of phytoplankton, nutrients, and the carbon cycle.',
            'Quantifying the ocean\u2019s role in regulating atmospheric CO\u2082, biological pump efficiency, and the response of the marine carbon cycle to future climate change.',
            'Exploring how submesoscale physical processes (fronts, eddies) regulate planktonic ecosystems and carbon export fluxes.',
            'Earth system modeling of key periods such as the Last Interglacial to understand the long-term evolution of the carbon cycle.',
            'Building ocean digital twin systems to empower blue-economy innovation and integrated ocean observation\u2013simulation\u2013prediction.',
            'Combining in-situ observations, satellite remote sensing, and numerical models to quantify uncertainty and improve ecosystem model parameterizations.',
        ]
    else:
        items = [
            '海洋生态系统与生物地球化学模拟',
            '海洋碳循环与气候反馈',
            '海洋次中尺度过程与生态效应',
            '古气候与古海洋模拟',
            '海洋数字孪生',
            '观测—模拟融合',
        ]
        descs = [
            '发展并改进 CESM-CoSiNE 海洋生态系统—生物地球化学耦合模式，模拟浮游植物、营养盐与碳循环的时空演变。',
            '研究海洋对大气 CO₂ 的调控作用、生物泵效率及海洋碳循环对未来气候变化的响应。',
            '探索次中尺度物理过程（锋面、涡旋）对浮游生态系统与碳输出通量的调控机制。',
            '利用地球系统模式开展末次间冰期等关键时期古气候模拟，理解碳循环的长期演化。',
            '构建海洋数字孪生系统，赋能蓝色经济创新，服务海洋观测—模拟—预测一体化。',
            '结合现场观测、卫星遥感与数值模式，量化评估模式不确定性，改进生态模型参数化。',
        ]
    return '\n'.join(
        f'''    <a class="rtile rt-bg{i}" id="r{i}" href="{href_base}r{i}" data-reveal style="--d:{i*70}ms">
      <div class="rnum">0{i+1}</div>
      <h3>{title}</h3>
      <p>{desc}</p>
      <span class="rt-go">→</span>
    </a>'''
        for i, (title, desc) in enumerate(zip(items, descs)))

def project_box(lang, full=True):
    if lang == EN:
        body = '''      <div class="kicker">CESM-CoSiNE</div>
      <h3>CESM-CoSiNE: An Ocean Ecosystem\u2013Biogeochemistry Module Embedded in CESM</h3>
      <p>CoSiNE (Carbon, Silicon, Nitrogen Ecosystem) is developed and maintained by our group and has been embedded in the CESM Earth System Model (POP2 ocean component) to study the evolution of planktonic ecosystems and the marine carbon cycle at global and regional scales.</p>'''
        feats = [
            '16 CoSiNE tracers (nutrients, phytoplankton functional groups, zooplankton, DOC, etc.)',
            'V2 extends to 22 tracers with carbon isotope (\u00b9\u00b3C / \u00b9\u2074C) tracking capability',
            'Supports present-day climate, short-term forcing assessments, and paleoclimate (e.g., Last Interglacial) simulations',
            'Outputs global and regional (North Pacific, South China Sea) carbon flux, nutrient, and ecosystem structure diagnostics',
        ]
        works = [
            'CESM-CoSiNE16: An ocean ecosystem\u2013biogeochemistry module embedded in CESM and its short-term forcing assessment',
            'CESM CoSiNE16+5 (CoSiNE22) coupling: expansion of carbon isotope tracers and implementation',
        ]
        btn1, btn2 = 'Project Report (Nature Style)', 'V2 Coupling Manual'
    else:
        body = '''      <div class="kicker">CESM-CoSiNE</div>
      <h3>CESM-CoSiNE：嵌入 CESM 的海洋生态—生物地球化学模块</h3>
      <p>CoSiNE（Carbon, Silicon, Nitrogen Ecosystem）由本课题组维护发展，已嵌入 CESM 地球系统模式（POP2 海洋分量），用于研究浮游生态系统与海洋碳循环在全球及区域尺度上的演变。</p>'''
        feats = [
            '包含 16 个 CoSiNE 示踪物（营养盐、浮游植物功能群、浮游动物、DOC 等）',
            'V2 版本扩展至 22 个示踪物，加入碳同位素（¹³C / ¹⁴C）追踪能力',
            '支持现代气候、短期强迫评估与古气候（如末次间冰期）模拟',
            '输出全球及区域（北太平洋、南海）碳通量、营养盐与生态结构诊断',
        ]
        works = [
            'CESM-CoSiNE16：一个嵌入 CESM 的海洋生态—生物地球化学模块及其短期强迫评估',
            'CESM CoSiNE16+5（CoSiNE22）耦合：碳同位素示踪物扩展与实现',
        ]
        btn1, btn2 = '📄 阅读项目报告（Nature 风格）', '🔧 V2 耦合说明书'
    feats_html = '\n'.join(f'        <li>{x}</li>' for x in feats)
    works_html = '\n'.join(f'        <li>{x}</li>' for x in works)
    extra = f'''
      <h4>{'Model Features' if lang == EN else '模式特色'}</h4>
      <ul>
{feats_html}
      </ul>
      <h4>{'Selected Work' if lang == EN else '代表性工作'}</h4>
      <ul>
{works_html}
      </ul>
      <div class="project-links">
        <a class="btn btn-solid" href="reports/CESM_CoSiNE16_Nature_style_draft_CN.html" target="_blank">{btn1}</a>
        <a class="btn btn-line" href="reports/CESM_CoSiNE16_v2_Process_Manual.html" target="_blank">{btn2}</a>
      </div>''' if full else ''
    return f'''<div class="project-box">
    <div class="project-hero">
      {body}
    </div>
    <div class="project-body">
{extra}
    </div>
  </div>'''

def members_body(lang):
    if lang == EN:
        groups = [
            ('Faculty', [('Fei Chai', 'Chair Professor / PI', 'Marine biogeochemistry, physics-ecology coupling, climate modeling', 'fchai@xmu.edu.cn'),
                          ('TBD', 'Associate Professor / Researcher', 'Member information under construction\u2026', '\u2014')]),
            ('Postdocs', [('TBD', 'Postdoctoral Researcher', 'Member information under construction\u2026', '\u2014')]),
            ('Students', [('TBD', 'PhD Student', 'Member information under construction\u2026', '\u2014'),
                          ('TBD', 'PhD Student', 'Member information under construction\u2026', '\u2014'),
                          ('TBD', "Master's Student", 'Member information under construction\u2026', '\u2014'),
                          ('TBD', "Master's Student", 'Member information under construction\u2026', '\u2014')]),
        ]
    else:
        groups = [
            ('教授 / 研究员', [('柴扉', '讲席教授 / PI', '海洋生物地球化学、物理—生态耦合、气候模拟', 'fchai@xmu.edu.cn'),
                          ('（待补充）', '副教授 / 研究员', '成员信息整理中……', '—')]),
            ('博士后', [('（待补充）', '博士后', '成员信息整理中……', '—')]),
            ('研究生', [('（待补充）', '博士研究生', '成员信息整理中……', '—'),
                          ('（待补充）', '博士研究生', '成员信息整理中……', '—'),
                          ('（待补充）', '硕士研究生', '成员信息整理中……', '—'),
                          ('（待补充）', '硕士研究生', '成员信息整理中……', '—')]),
        ]
    out = ['<div class="section">']
    for i, (gtitle, members) in enumerate(groups):
        style = ' style="margin-top:72px"' if i > 0 else ''
        out.append(f'  <div class="sec-head"{style}>\n    <h2>{gtitle}</h2>\n  </div>')
        cards = '\n'.join(
            f'''    <div class="member">
      <div class="m-avatar">{name[0]}</div>
      <h4>{name}</h4>
      <div class="role">{role}</div>
      <div class="dir">{dir_}</div>
      <div class="email">{email}</div>
    </div>''' for name, role, dir_, email in members)
        out.append(f'  <div class="members">\n{cards}\n  </div>')
    out.append('</div>')
    return '\n'.join(out)

def project_body(lang):
    if lang == EN:
        return '''<div class="section">
  <div class="project-box">
    <div class="project-hero">
      <div class="kicker">CESM-CoSiNE PROJECT</div>
      <h3>CESM-CoSiNE: An Ocean Ecosystem\u2013Biogeochemistry Module Embedded in CESM</h3>
      <p>CoSiNE (Carbon, Silicon, Nitrogen Ecosystem) is developed and maintained by our group and has been embedded in the CESM Earth System Model (POP2 ocean component) to study the evolution of planktonic ecosystems and the marine carbon cycle at global and regional scales.</p>
    </div>
    <div class="project-body">
      <h4>Model Features</h4>
      <ul>
        <li>16 CoSiNE tracers (nutrients, phytoplankton functional groups, zooplankton, DOC, etc.)</li>
        <li>V2 extends to 22 tracers with carbon isotope (\u00b9\u00b3C / \u00b9\u2074C) tracking capability</li>
        <li>Supports present-day climate, short-term forcing assessments, and paleoclimate (e.g., Last Interglacial) simulations</li>
        <li>Outputs global and regional (North Pacific, South China Sea) carbon flux, nutrient, and ecosystem structure diagnostics</li>
      </ul>
      <h4>Selected Work</h4>
      <ul>
        <li>CESM-CoSiNE16: An ocean ecosystem\u2013biogeochemistry module embedded in CESM and its short-term forcing assessment</li>
        <li>CESM CoSiNE16+5 (CoSiNE22) coupling: expansion of carbon isotope tracers and implementation</li>
      </ul>
      <div class="project-links">
        <a class="btn btn-solid" href="reports/CESM_CoSiNE16_Nature_style_draft_CN.html" target="_blank">Project Report (Nature Style)</a>
        <a class="btn btn-line" href="reports/CESM_CoSiNE16_v2_Process_Manual.html" target="_blank">V2 Coupling Manual</a>
      </div>
    </div>
  </div>
</div>'''
    return '''<div class="section">
  <div class="project-box">
    <div class="project-hero">
      <div class="kicker">CESM-CoSiNE PROJECT</div>
      <h3>CESM-CoSiNE：嵌入 CESM 的海洋生态—生物地球化学模块</h3>
      <p>CoSiNE（Carbon, Silicon, Nitrogen Ecosystem）由本课题组维护发展，已嵌入 CESM 地球系统模式（POP2 海洋分量），用于研究浮游生态系统与海洋碳循环在全球及区域尺度上的演变。</p>
    </div>
    <div class="project-body">
      <h4>模式特色</h4>
      <ul>
        <li>包含 16 个 CoSiNE 示踪物（营养盐、浮游植物功能群、浮游动物、DOC 等）</li>
        <li>V2 版本扩展至 22 个示踪物，加入碳同位素（¹³C / ¹⁴C）追踪能力</li>
        <li>支持现代气候、短期强迫评估与古气候（如末次间冰期）模拟</li>
        <li>输出全球及区域（北太平洋、南海）碳通量、营养盐与生态结构诊断</li>
      </ul>
      <h4>代表性工作</h4>
      <ul>
        <li>CESM-CoSiNE16：一个嵌入 CESM 的海洋生态—生物地球化学模块及其短期强迫评估</li>
        <li>CESM CoSiNE16+5（CoSiNE22）耦合：碳同位素示踪物扩展与实现</li>
      </ul>
      <div class="project-links">
        <a class="btn btn-solid" href="reports/CESM_CoSiNE16_Nature_style_draft_CN.html" target="_blank">📄 阅读项目报告（Nature 风格）</a>
        <a class="btn btn-line" href="reports/CESM_CoSiNE16_v2_Process_Manual.html" target="_blank">🔧 V2 耦合说明书</a>
      </div>
    </div>
  </div>
</div>'''

def papers_body(lang):
    if lang == EN:
        return '''<div class="section">
  <ul class="papers">
    <li class="paper">
      <div class="year">2026</div>
      <div>
        <div class="t">(To be added) Paper title</div>
        <div class="a">Authors: TBD</div>
        <div class="j">Journal: TBD</div>
      </div>
    </li>
    <li class="paper">
      <div class="year">2025</div>
      <div>
        <div class="t">(To be added) Paper title</div>
        <div class="a">Authors: TBD</div>
        <div class="j">Journal: TBD</div>
      </div>
    </li>
    <li class="paper">
      <div class="year">\u2014</div>
      <div>
        <div class="t">Publication list under construction</div>
        <div class="a">For a complete list, please visit Prof. Chai\u2019s homepage</div>
        <div class="j"><a href="https://coeoa.xmu.edu.cn/t/CF/" target="_blank" style="color:var(--navy-3)">coeoa.xmu.edu.cn/t/CF/ \u2192</a></div>
      </div>
    </li>
  </ul>
</div>'''
    return '''<div class="section">
  <ul class="papers">
    <li class="paper">
      <div class="year">2026</div>
      <div>
        <div class="t">（待补充）论文标题</div>
        <div class="a">作者：待补充</div>
        <div class="j">期刊：待补充</div>
      </div>
    </li>
    <li class="paper">
      <div class="year">2025</div>
      <div>
        <div class="t">（待补充）论文标题</div>
        <div class="a">作者：待补充</div>
        <div class="j">期刊：待补充</div>
      </div>
    </li>
    <li class="paper">
      <div class="year">—</div>
      <div>
        <div class="t">论文列表整理中，敬请期待</div>
        <div class="a">如需完整论文列表，可访问柴扉教授个人主页</div>
        <div class="j"><a href="https://coeoa.xmu.edu.cn/t/CF/" target="_blank" style="color:var(--navy-3)">coeoa.xmu.edu.cn/t/CF/ →</a></div>
      </div>
    </li>
  </ul>
</div>'''

def news_body(lang):
    if lang == EN:
        return '''<div class="section news-page">
  <div class="news-feat">
    <div class="nf-head">
      <span class="date">FEB 2026</span>
      <h2>Prof. Chai\u2019s team reveals ocean digital twins as a new engine for blue-economy innovation</h2>
      <p>The team systematically reviewed the core architecture of ocean digital twins, analyzed key application scenarios in blue-economy development, and provided forward-looking perspectives on challenges and prospects.</p>
    </div>
  </div>
  <div class="news-list">
    <div class="news-item">
      <span class="date">NOV 2025</span>
      <h3>Lujiang Ocean Symposium concludes successfully</h3>
      <p>The ocean symposium co-hosted by Lujiang Innovation Laboratory and the State Key Laboratory of Marine Environmental Science (XMU) was held successfully.</p>
    </div>
    <div class="news-item">
      <span class="date">SEP 2025</span>
      <h3>Group website officially launched</h3>
      <p>The official website of the Chai Group is now live, presenting our research areas, members, and achievements.</p>
    </div>
    <div class="news-item">
      <span class="date">UPDATING</span>
      <h3>Group news continuously updated</h3>
      <p>Stay tuned for the latest research progress, recruitment, and academic exchange activities.</p>
    </div>
  </div>
</div>'''
    return '''<div class="section news-page">
  <div class="news-feat">
    <div class="nf-head">
      <span class="date">2026-02</span>
      <h2>柴扉教授团队揭示海洋数字孪生是赋能蓝色经济创新发展的新引擎</h2>
      <p>团队系统梳理海洋数字孪生核心架构，解析其在蓝色经济发展中的关键应用场景，并对该领域挑战与前景作出前瞻性研判。</p>
    </div>
  </div>
  <div class="news-list">
    <div class="news-item">
      <span class="date">2025-11</span>
      <h3>鹭江海洋研讨会圆满落幕</h3>
      <p>由鹭江创新实验室与海洋生物地球化学全国重点实验室（厦门大学）联合主办的海洋研讨会成功举办。</p>
    </div>
    <div class="news-item">
      <span class="date">2025-09</span>
      <h3>课题组网站全新上线</h3>
      <p>柴扉教授课题组官方网站正式启用，全面展示课题组研究方向、成员与科研成果。</p>
    </div>
    <div class="news-item">
      <span class="date">待更新</span>
      <h3>课题组新闻持续更新中</h3>
      <p>欢迎关注课题组最新科研进展、招生与学术交流动态。</p>
    </div>
  </div>
</div>'''

def links_body(lang):
    if lang == EN:
        return '''<div class="section">
  <div class="links">
    <a class="link-card" href="#" onclick="return false" title="Link to be added">
      <div class="icon">''' + SVG_GLOBE + '''</div>
      <h4>XMU Paleoclimate Digital Earth System</h4>
      <p>Paleoclimate simulation and digital earth platform (link to be added)</p>
      <div class="ext">COMING SOON →</div>
    </a>
    <a class="link-card" href="https://coeoa.xmu.edu.cn/t/CF/" target="_blank">
      <div class="icon">''' + SVG_USER + '''</div>
      <h4>Prof. Fei Chai\u2019s Homepage</h4>
      <p>State Key Laboratory of Marine Environmental Science, XMU</p>
      <div class="ext">coeoa.xmu.edu.cn →</div>
    </a>
    <a class="link-card" href="https://meli.xmu.edu.cn/" target="_blank">
      <div class="icon">''' + SVG_LAB + '''</div>
      <h4>State Key Laboratory of Marine Environmental Science</h4>
      <p>Official website of MEL, Xiamen University</p>
      <div class="ext">meli.xmu.edu.cn →</div>
    </a>
  </div>
</div>'''
    return '''<div class="section">
  <div class="links">
    <a class="link-card" href="#" onclick="return false" title="链接待补充">
      <div class="icon">''' + SVG_GLOBE + '''</div>
      <h4>厦门大学古气候数字地球系统</h4>
      <p>古气候模拟与数字地球平台（链接待补充）</p>
      <div class="ext">敬请期待 →</div>
    </a>
    <a class="link-card" href="https://coeoa.xmu.edu.cn/t/CF/" target="_blank">
      <div class="icon">''' + SVG_USER + '''</div>
      <h4>柴扉教授个人主页</h4>
      <p>厦门大学海洋生物地球化学全国重点实验室</p>
      <div class="ext">coeoa.xmu.edu.cn →</div>
    </a>
    <a class="link-card" href="https://meli.xmu.edu.cn/" target="_blank">
      <div class="icon">''' + SVG_LAB + '''</div>
      <h4>海洋生物地球化学全国重点实验室</h4>
      <p>厦门大学海洋生物地球化学全国重点实验室官网</p>
      <div class="ext">meli.xmu.edu.cn →</div>
    </a>
  </div>
</div>'''

def home_body(lang):
    """首页：清华式布局（Hero轮播+统计条+新闻分栏+研究方向+项目横幅+论文+招生合作）"""
    import os
    if lang == EN:
        slides = [
            ('Marine Biogeochemistry', 'Marine Biogeochemistry and Climate Modeling', 'Ocean Biogeochemistry and Climate Modeling',
             [('About Us', 'about.html'), ('Research', 'research.html')]),
            ('Earth System Modeling', 'The CESM-CoSiNE Marine Ecosystem Model', 'From coupled physics\u2013chemistry\u2013biology to understanding the marine carbon cycle',
             [('CESM-CoSiNE Details', 'research.html#project'), ('Project Report', 'reports/CESM_CoSiNE16_Nature_style_draft_CN.html')]),
            ('Paleoclimate & Digital Earth', 'Paleoclimate and the Digital Earth', 'Reconstruct the past, simulate the present, foresee the future',
             [('Research Areas', 'research.html'), ('About Us', 'about.html')]),
        ]
        stats = [(22, '', 'Model Tracers'), (6, '', 'Research Areas'), (3, '', 'Ocean Regions'), (35, '+', 'Years of Research')]
        news_head = ('News', 'NEWS & UPDATES', 'More')
        news = [
            ('FEB 2026', 'Prof. Chai\u2019s team reveals ocean digital twins as a new engine for blue-economy innovation',
             'The team systematically reviewed the core architecture of ocean digital twins, analyzed key application scenarios in blue-economy development, and provided forward-looking perspectives on challenges and prospects.'),
            ('NOV 2025', 'Lujiang Ocean Symposium concludes successfully',
             'The ocean symposium co-hosted by Lujiang Innovation Laboratory and the State Key Laboratory of Marine Environmental Science (XMU) was held successfully.'),
            ('SEP 2025', 'Group website officially launched',
             'The official website of the Chai Group is now live, presenting our research areas, members, and achievements.'),
            ('UPDATING', 'Group news continuously updated',
             'Stay tuned for the latest research progress, recruitment, and academic exchange activities.'),
        ]
        res_head = ('Research Areas', 'RESEARCH AREAS')
        res_more = 'Learn More'
        cos = ('CESM-CoSiNE', 'CESM-CoSiNE: An Ocean Ecosystem\u2013Biogeochemistry Module Embedded in CESM',
               'Developed and maintained by our group, embedded in the CESM Earth System Model (POP2), studying planktonic ecosystems and the marine carbon cycle at global and regional scales.',
               'Model Details', 'Project Report')
        pub_head = ('Publications', 'SELECTED PUBLICATIONS', 'All Publications')
        pubs = [
            ('2026', '(To be added) Paper title', 'Authors. Journal Name, 2026.'),
            ('2025', '(To be added) Paper title', 'Authors. Journal Name, 2025.'),
            ('2025', '(To be added) Paper title', 'Authors. Journal Name, 2025.'),
            ('2024', '(To be added) Paper title', 'Authors. Journal Name, 2024.'),
        ]
        join = [
            ('Recruitment', 'We recruit PhD and Master\u2019s students year-round and welcome postdoctoral applicants from around the world with interests in marine biogeochemistry, climate modeling, and computational oceanography.', 'mailto:fchai@xmu.edu.cn', 'Send an Application'),
            ('Collaboration', 'The group maintains close collaborations with universities and research institutes at home and abroad. We welcome academic visits, joint training, and project cooperation.', 'links.html', 'Related Links'),
        ]
        scroll_hint = 'Scroll'
        pi = ('Prof. Fei Chai', 'PRINCIPAL INVESTIGATOR', 'Tang Shifeng Chair Professor in Marine Sciences · PI',
              'Marine biogeochemistry, ocean ecosystem modeling, and climate simulation. Ph.D. in Biological Oceanography, Duke University; former Professor (tenured) at the University of Maine.',
              'About the Group', 'Our Team')
    else:
        slides = [
            ('Marine Biogeochemistry', '海洋生物地球化学与气候模拟', 'Ocean Biogeochemistry and Climate Modeling',
             [('了解课题组', 'about.html'), ('研究方向', 'research.html')]),
            ('Earth System Modeling', 'CESM-CoSiNE 海洋生态系统模式', '从物理—化学—生物耦合出发，理解海洋碳循环',
             [('模式详情', 'research.html#project'), ('项目报告', 'reports/CESM_CoSiNE16_Nature_style_draft_CN.html')]),
            ('Paleoclimate & Digital Earth', '古气候与数字地球', '重建过去，模拟现在，预见未来',
             [('研究方向', 'research.html'), ('了解课题组', 'about.html')]),
        ]
        stats = [(22, '', '模式示踪物'), (6, '', '研究方向'), (3, '', '覆盖海域'), (35, '+', '年科研积累')]
        news_head = ('新闻动态', 'NEWS & UPDATES', '更多')
        news = [
            ('2026-02', '柴扉教授团队揭示海洋数字孪生是赋能蓝色经济创新发展的新引擎',
             '团队系统梳理海洋数字孪生核心架构，解析其在蓝色经济发展中的关键应用场景，并对该领域挑战与前景作出前瞻性研判。'),
            ('2025-11', '鹭江海洋研讨会圆满落幕',
             '由鹭江创新实验室与海洋生物地球化学全国重点实验室（厦门大学）联合主办的海洋研讨会成功举办。'),
            ('2025-09', '课题组网站全新上线',
             '柴扉教授课题组官方网站正式启用，全面展示课题组研究方向、成员与科研成果。'),
            ('待更新', '课题组新闻持续更新中',
             '欢迎关注课题组最新科研进展、招生与学术交流动态。'),
        ]
        res_head = ('研究方向', 'RESEARCH AREAS')
        res_more = '了解更多'
        cos = ('CESM-CoSiNE', 'CESM-CoSiNE：嵌入 CESM 的海洋生态—生物地球化学模块',
               '由本课题组自主发展并维护，已嵌入 CESM 地球系统模式（POP2 海洋分量），研究全球及区域尺度浮游生态系统与海洋碳循环的演变。',
               '了解模式详情', '阅读项目报告')
        pub_head = ('代表性论文', 'SELECTED PUBLICATIONS', '全部论文')
        pubs = [
            ('2026', '（待补充）论文标题', 'Authors. Journal Name, 2026.'),
            ('2025', '（待补充）论文标题', 'Authors. Journal Name, 2025.'),
            ('2025', '（待补充）论文标题', 'Authors. Journal Name, 2025.'),
            ('2024', '（待补充）论文标题', 'Authors. Journal Name, 2024.'),
        ]
        join = [
            ('招生招聘', '课题组长期招收博士研究生、硕士研究生，并面向全球招聘博士后。欢迎对海洋生物地球化学、气候模拟与计算海洋学感兴趣的同学与我们联系。', 'mailto:fchai@xmu.edu.cn', '发送申请邮件'),
            ('合作交流', '课题组与国内外多所高校及研究机构保持紧密合作，欢迎就学术访问、联合培养与项目合作事宜洽谈。', 'links.html', '查看相关链接'),
        ]
        scroll_hint = '向下滚动'
        pi = ('柴扉 教授', 'PRINCIPAL INVESTIGATOR', '"唐世凤"海洋学科讲席教授 · PI',
              '长期从事海洋生物地球化学与气候模拟研究。美国杜克大学生物海洋学博士，曾任美国缅因大学海洋学院教授（终身教职），现任厦门大学海洋生物地球化学全国重点实验室讲席教授。',
              '了解课题组', '我们的团队')

    deco_wave = '''      <svg class="hdeco" viewBox="0 0 1440 560" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
        <g stroke="rgba(255,255,255,.07)" fill="none">
          <path d="M-40,440 C200,380 400,490 640,430 S1080,370 1480,440"/>
          <path d="M-40,478 C200,418 400,528 640,468 S1080,408 1480,478"/>
          <path d="M-40,516 C200,456 400,566 640,506 S1080,446 1480,516"/>
        </g>
        <g stroke="rgba(255,255,255,.04)">
          <line x1="0" y1="140" x2="1440" y2="140"/><line x1="0" y1="280" x2="1440" y2="280"/>
          <line x1="360" y1="0" x2="360" y2="560"/><line x1="720" y1="0" x2="720" y2="560"/><line x1="1080" y1="0" x2="1080" y2="560"/>
        </g>
      </svg>'''
    deco_dots = '''      <svg class="hdeco" viewBox="0 0 1440 560" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
        <g fill="rgba(255,255,255,.06)">
          <circle cx="140" cy="120" r="3"/><circle cx="300" cy="70" r="2"/><circle cx="520" cy="150" r="3.5"/>
          <circle cx="700" cy="90" r="2.5"/><circle cx="880" cy="160" r="3"/><circle cx="1060" cy="80" r="2"/>
          <circle cx="1250" cy="140" r="3.5"/><circle cx="1380" cy="70" r="2.5"/><circle cx="200" cy="230" r="2.5"/>
          <circle cx="420" cy="260" r="2"/><circle cx="640" cy="220" r="3"/><circle cx="860" cy="250" r="2.5"/>
          <circle cx="1080" cy="230" r="2"/><circle cx="1300" cy="270" r="3"/><circle cx="80" cy="350" r="3.5"/>
          <circle cx="260" cy="390" r="2"/><circle cx="460" cy="340" r="2.5"/><circle cx="660" cy="380" r="3"/>
          <circle cx="880" cy="350" r="2"/><circle cx="1100" cy="390" r="2.5"/><circle cx="1320" cy="360" r="3"/>
        </g>
        <g stroke="rgba(255,255,255,.05)" fill="none">
          <path d="M-40,470 C200,430 400,510 640,460 S1080,420 1480,470"/>
        </g>
      </svg>'''
    deco_contour = '''      <svg class="hdeco" viewBox="0 0 1440 560" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
        <g fill="none" stroke="rgba(255,255,255,.07)">
          <ellipse cx="720" cy="330" rx="620" ry="150"/>
          <ellipse cx="720" cy="330" rx="460" ry="110"/>
          <ellipse cx="720" cy="330" rx="300" ry="72"/>
          <ellipse cx="720" cy="330" rx="150" ry="36"/>
        </g>
        <g fill="none" stroke="rgba(255,255,255,.05)">
          <path d="M-40,120 H1480"/><path d="M-40,210 H1480"/><path d="M-40,450 H1480"/>
        </g>
      </svg>'''
    decos = [deco_wave, deco_dots, deco_contour]

    slide_parts = []
    for i, (kicker, h, p, ctas) in enumerate(slides):
        photo = f'images/hero{i+1}.jpg' if os.path.exists(f'images/hero{i+1}.jpg') else None
        bg_style = f' style="background-image:linear-gradient(rgba(7,24,42,.5),rgba(7,24,42,.5)),url({photo});background-size:cover;background-position:center"' if photo else ''
        def _cta(j, t, u):
            cls = ' cta-solid' if j == 0 else ''
            ext = ' target="_blank"' if 'reports/' in u else ''
            return f'          <a class="hero-cta{cls}" href="{u}"{ext}>{t} →</a>'
        cta_html = '\n'.join(_cta(j, t, u) for j, (t, u) in enumerate(ctas))
        slide_parts.append(f'''    <div class="hslide{' hs' + str(i+1) if not photo else ''}{' on' if i == 0 else ''}"{bg_style}>
{decos[i]}
      <div class="hcap" data-cap>
        <span class="kicker">{kicker}</span>
        <h2>{h}</h2>
        <p>{p}</p>
        <div class="hero-ctas">
{cta_html}
        </div>
      </div>
    </div>''')

    dots = '\n'.join(f'        <span class="{"on" if i == 0 else ""}" role="button" aria-label="slide {i+1}"><i></i></span>' for i in range(len(slides)))

    stat_parts = '\n'.join(
        f'''      <div class="stat" data-reveal style="--d:{i*90}ms">
        <b><span data-count="{v}">0</span>{suf}</b>
        <span class="stat-label">{lab}</span>
      </div>''' for i, (v, suf, lab) in enumerate(stats))

    feat_d, feat_t, feat_p = news[0]
    pi_name, pi_en, pi_title, pi_bio, pi_btn1, pi_btn2 = pi
    list_parts = '\n'.join(
        f'''      <a class="nitem" href="news.html" data-reveal style="--d:{i*100}ms">
        <span class="date">{d}</span>
        <h4>{t}</h4>
        <span class="arr">→</span>
      </a>''' for i, (d, t, p) in enumerate(news[1:]))

    pub_parts = '\n'.join(
        f'''    <li class="paper" data-reveal style="--d:{i*80}ms">
      <div class="year">{y}</div>
      <div>
        <div class="t">{t}</div>
        <div class="j">{j}</div>
      </div>
    </li>''' for i, (y, t, j) in enumerate(pubs))

    join_parts = '\n'.join(
        f'''    <div class="join-cell" data-reveal style="--d:{i*120}ms">
      <h3>{t}</h3>
      <p>{p}</p>
      <a class="btn btn-ghost" href="{u}">{b} →</a>
    </div>''' for i, (t, p, u, b) in enumerate(join))

    tiles = tiles_body(lang, 'research.html#')

    return f'''<div class="read-progress" id="readProgress" aria-hidden="true"></div>
<!-- 北大式整屏：Hero 层 -->
<div class="body-home" id="bodyHome">
<!-- Hero 轮播 -->
<div class="hero" id="hero">
  <div class="hero-slides" id="heroSlides">
{chr(10).join(slide_parts)}
  </div>
  <div class="hdots" id="heroDots">
{dots}
  </div>
  <button class="scroll-hint" id="scrollHint" aria-label="scroll down">
    <span class="mouse"><i></i></span>
    <span class="hint-txt">{scroll_hint}</span>
  </button>
</div>
</div>
<!-- 内容层 -->
<div class="body-main" id="bodyMain">

<!-- 柴老师简介 -->
<div class="section pi-intro" id="pi">
  <div class="pi-wrap" data-reveal>
    <div class="pi-photo">
      <img src="images/chai_fei.jpg" alt="{pi_name}">
    </div>
    <div class="pi-info">
      <span class="en">{pi_en}</span>
      <h2>{pi_name}</h2>
      <div class="pi-title">{pi_title}</div>
      <p>{pi_bio}</p>
      <div class="pi-actions">
        <a class="btn btn-solid" href="about.html">{pi_btn1} →</a>
        <a class="btn btn-line" href="members.html">{pi_btn2} →</a>
      </div>
    </div>
  </div>
</div>

<!-- 新闻动态 -->
<div class="section home-sec" id="news">
  <div class="sec-row" data-reveal>
    <div class="sec-title">
      <h2>{news_head[0]}</h2>
      <span class="en">{news_head[1]}</span>
    </div>
    <a class="more" href="news.html">{news_head[2]} ›</a>
  </div>
  <div class="news-split">
    <a class="nfeat" href="news.html" data-reveal>
      <svg class="nfeat-deco" viewBox="0 0 600 400" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
        <g stroke="rgba(255,255,255,.1)" fill="none">
          <path d="M-20,300 C120,250 240,340 380,290 S560,240 640,300"/>
          <path d="M-20,340 C120,290 240,380 380,330 S560,280 640,340"/>
        </g>
      </svg>
      <span class="date">{feat_d}</span>
      <h3>{feat_t}</h3>
      <p>{feat_p}</p>
    </a>
    <div class="nlist">
{list_parts}
    </div>
  </div>
</div>

<!-- 研究方向 -->
<div class="section home-sec" id="research">
  <div class="sec-head" data-reveal>
    <span class="en">{res_head[1]}</span>
    <h2>{res_head[0]}</h2>
  </div>
  <div class="research home-research">
{tiles}
  </div>
  <p style="text-align:center;margin-top:44px" data-reveal><a class="btn btn-line" href="research.html">{res_more} →</a></p>
</div>

<!-- CESM-CoSiNE 横幅 -->
<div class="cosine-band">
  <div class="cosine-inner" data-reveal>
    <div class="cosine-txt">
      <span class="kicker">{cos[0]}</span>
      <h2>{cos[1]}</h2>
      <p>{cos[2]}</p>
    </div>
    <div class="cosine-btns">
      <a class="btn btn-gold" href="research.html#project">{cos[3]} →</a>
      <a class="btn btn-ghost" href="reports/CESM_CoSiNE16_Nature_style_draft_CN.html" target="_blank">{cos[4]} →</a>
    </div>
  </div>
</div>

<!-- 代表性论文 -->
<div class="section home-sec" id="pubs">
  <div class="sec-row" data-reveal>
    <div class="sec-title">
      <h2>{pub_head[0]}</h2>
      <span class="en">{pub_head[1]}</span>
    </div>
    <a class="more" href="papers.html">{pub_head[2]} ›</a>
  </div>
  <ul class="papers">
{pub_parts}
  </ul>
</div>

<!-- 招生招聘 / 合作交流 -->
<div class="join-band">
  <div class="join-grid">
{join_parts}
  </div>
</div>

<!-- 统计条 -->
<div class="stats-band">
  <div class="stats">
{stat_parts}
  </div>
</div>
</div><!-- /body-main -->

<button class="back-top" id="backTop" aria-label="back to top">↑</button>'''

def research_with_project(lang):
    tiles = tiles_body(lang, '#')
    proj = project_box(lang, full=True)
    if lang == EN:
        head1, head2 = 'Research Areas', 'CESM-CoSiNE Project'
        en1, en2 = 'RESEARCH AREAS', 'CESM-CoSiNE'
    else:
        head1, head2 = '研究方向', 'CESM-CoSiNE 项目'
        en1, en2 = 'RESEARCH AREAS', 'CESM-CoSiNE PROJECT'
    return f'''<div class="section">
  <div class="sec-head">
    <span class="en">{en1}</span>
    <h2>{head1}</h2>
  </div>
  <div class="research">
{tiles}
  </div>
</div>

<div class="section" id="project">
  <div class="sec-head">
    <span class="en">{en2}</span>
    <h2>{head2}</h2>
  </div>
  {proj}
</div>'''

def main():
    specs = {
        'about.html': ('课题组简介', 'ABOUT THE GROUP', ABOUT_BODY),
        'research.html': ('研究方向', 'RESEARCH AREAS', None),
        'project.html': ('CESM-CoSiNE', 'CESM-CoSiNE PROJECT', None),
        'papers.html': ('发表论文', 'PUBLICATIONS', None),
        'news.html': ('新闻动态', 'NEWS & UPDATES', None),
        'links.html': ('相关链接', 'RELATED LINKS', None),
    }
    specs_en = {
        'about.html': ('About the Group', 'ABOUT THE GROUP', ABOUT_BODY),
        'research.html': ('Research', 'RESEARCH AREAS', None),
        'project.html': ('CESM-CoSiNE', 'CESM-CoSiNE PROJECT', None),
        'papers.html': ('Publications', 'PUBLICATIONS', None),
        'news.html': ('News', 'NEWS & UPDATES', None),
        'links.html': ('Links', 'RELATED LINKS', None),
    }

    body_fn = {
        'research.html': research_tiles,
        'project.html': project_body,
        'papers.html': papers_body,
        'news.html': news_body,
        'links.html': links_body,
    }
    body_full = {
        'research.html': research_with_project,
        'project.html': lambda lang: project_box(lang, full=True),
    }

    # 中文版
    import os
    os.makedirs('en', exist_ok=True)
    for fname, (title, en_sub, about_body) in specs.items():
        if fname == 'about.html':
            body = about_body['zh']
        elif fname in body_full:
            body = body_full[fname](ZH)
        else:
            body = body_fn[fname](ZH)
        html = page(fname, title, en_sub, body, ZH)
        open(fname, 'w').write(html)
        print('生成', fname)

    # 英文版
    for fname, (title, en_sub, about_body) in specs_en.items():
        if fname == 'about.html':
            body = about_body['en']
        elif fname in body_full:
            body = body_full[fname](EN)
        else:
            body = body_fn[fname](EN)
        html = page(fname, title, en_sub, body, EN)
        open('en/' + fname, 'w').write(html)
        print('生成 en/' + fname)

    # 成员页
    open('members.html', 'w').write(page('members.html', '成员介绍', 'GROUP MEMBERS', members_body(ZH), ZH))
    open('en/members.html', 'w').write(page('members.html', 'Members', 'GROUP MEMBERS', members_body(EN), EN))
    print('生成 members.html / en/members.html')

    # 首页（无 page-banner，使用 home.js）
    open('index.html', 'w').write(page('index.html', '首页', 'HOME', home_body(ZH), ZH, banner=False, scripts='js/home.js'))
    open('en/index.html', 'w').write(page('index.html', 'Home', 'HOME', home_body(EN), EN, banner=False, scripts='../js/home.js'))
    print('生成 index.html / en/index.html')

if __name__ == '__main__':
    main()
