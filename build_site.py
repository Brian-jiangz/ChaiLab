#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成课题组网站（中英双语，多页面结构）"""

ZH, EN = 'zh', 'en'

NAV_ZH = [
    ('index.html', '首页'), ('about.html', '成员介绍'),
    ('research.html', '研究方向'),
    ('papers.html', '学术论文'), ('news.html', '课题组动态'), ('links.html', '相关链接'),
]
NAV_EN = [
    ('index.html', 'Home'), ('about.html', 'Members'),
    ('research.html', 'Research'),
    ('papers.html', 'Academic Papers'), ('news.html', 'Group News'), ('links.html', 'Links'),
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
    'about': [
        ('about-group.html', '课题组简介'),
        ('about-chai.html', '柴扉教授'),
        ('members.html', '成员介绍'),
    ],
    'papers': [
        ('papers-journal.html', '期刊论文'),
        ('papers-digital-twin.html', '数字孪生'),
        ('papers-data.html', '科研数据'),
        ('papers-model.html', '数值模式'),
    ],
    'research': [
        ('research-r0.html', '生态系统与生物地球化学模拟'),
        ('research-r1.html', '碳循环与气候反馈'),
        ('research-r2.html', '次中尺度过程与生态效应'),
        ('research-r3.html', '古气候与古海洋模拟'),
        ('research-r4.html', '海洋数字孪生'),
        ('research-r5.html', '观测—模拟融合'),
        ('research-project.html', 'CESM-CoSiNE 项目'),
    ],
    'links': [
        ('https://coeoa.xmu.edu.cn/t/CF/', '柴扉教授个人主页', '_blank'),
        ('https://mel.xmu.edu.cn/', 'MEL 实验室官网', '_blank'),
        ('links.html', '全部相关链接', ''),
    ],
}
DD_EN = {
    'about': [
        ('about-group.html', 'About the Group'),
        ('about-chai.html', 'Prof. Fei Chai'),
        ('members.html', 'Members'),
    ],
    'papers': [
        ('papers-journal.html', 'Journal Papers'),
        ('papers-digital-twin.html', 'Digital Twin'),
        ('papers-data.html', 'Research Data'),
        ('papers-model.html', 'Numerical Models'),
    ],
    'research': [
        ('research-r0.html', 'Ecosystem & Biogeochemical Modeling'),
        ('research-r1.html', 'Carbon Cycle & Climate Feedbacks'),
        ('research-r2.html', 'Submesoscale Processes'),
        ('research-r3.html', 'Paleoclimate Modeling'),
        ('research-r4.html', 'Ocean Digital Twin'),
        ('research-r5.html', 'Observation\u2013Model Integration'),
        ('research-project.html', 'CESM-CoSiNE Project'),
    ],
    'links': [
        ('https://coeoa.xmu.edu.cn/t/CF/', "Prof. Chai's Homepage", '_blank'),
        ('https://mel.xmu.edu.cn/', 'MEL Official Site', '_blank'),
        ('links.html', 'All Related Links', ''),
    ],
}

def nav(active, lang, subpage=False):
    items = NAV_EN if lang == EN else NAV_ZH
    dd = DD_EN if lang == EN else DD_ZH
    t = TXT[lang]
    parts = []
    for f, name in items:
        cls = ' class="active"' if f == active else ''
        if f == 'about.html':
            subs = '\n'.join(f'          <dd><a href="{u}">{n}</a></dd>' for u, n in dd['about'])
            parts.append(f'''        <li class="has-sub"><a href="{f}"{cls}>{name}</a>
          <div class="sub"><dl>
{subs}
          </dl></div>
        </li>''')
        elif f == 'papers.html':
            subs = '\n'.join(f'          <dd><a href="{u}">{n}</a></dd>' for u, n in dd['papers'])
            parts.append(f'''        <li class="has-sub"><a href="{f}"{cls}>{name}</a>
          <div class="sub"><dl>
{subs}
          </dl></div>
        </li>''')
        elif f == 'research.html':
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
    head_cls = 'g-head subpage' if subpage else 'g-head'
    return f'''<!-- 顶部导航 -->
<header class="{head_cls}" id="g-head">
  <div class="inner main">
    <a href="index.html" class="logo">
      <span class="logo-marks">
        <img src="images/xmu_logo.png" alt="Xiamen University" class="logo-xmu">
        <img src="images/mel_logo.png" alt="MEL" class="logo-mel">
      </span>
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
    <button class="nav-toggle" id="navToggle" aria-label="menu">☰</button>
    <a class="lang-switch" href="{t['lang_url']}">{t['lang_short']}</a>
  </div>
</header>'''

def footer(lang):
    t = TXT[lang]
    if lang == EN:
        qlinks = [
            ('about.html', 'About'), ('members.html', 'Members'), ('research.html', 'Research'),
            ('papers.html', 'Academic Papers'), ('news.html', 'Group News'), ('links.html', 'Links'),
        ]
        rlinks = [
            ('https://coeoa.xmu.edu.cn/t/CF/', "Prof. Chai's Homepage", ' target="_blank"'),
            ('https://mel.xmu.edu.cn/', 'MEL, Xiamen University', ' target="_blank"'),
            ('https://www.xmu.edu.cn/', 'Xiamen University', ' target="_blank"'),
        ]
    else:
        qlinks = [
            ('about.html', '课题组简介'), ('members.html', '成员介绍'), ('research.html', '研究方向'),
            ('papers.html', '学术论文'), ('news.html', '课题组动态'), ('links.html', '相关链接'),
        ]
        rlinks = [
            ('https://coeoa.xmu.edu.cn/t/CF/', '柴扉教授个人主页', ' target="_blank"'),
            ('https://mel.xmu.edu.cn/', '海洋生物地球化学全国重点实验室', ' target="_blank"'),
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
    prefix = '../' if lang == EN else ''
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="icon" href="{prefix}images/favicon.svg" type="image/svg+xml">
<title>{title} | {sitename} · Xiamen University</title>
<link rel="stylesheet" href="{prefix}css/style.css">
{scripts_html}
</head>
<body>

{nav(fname, lang, subpage=banner)}
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
'zh': '''<div class="section" id="about-group">
  <div class="intro-card intro-full">
    <p>本课题组依托厦门大学海洋生物地球化学全国重点实验室，长期从事海洋物理—生态—生物地球化学耦合研究，聚焦海洋碳循环、营养盐循环与生态系统对气候变化的响应与反馈。</p>
    <p>课题组以自主发展的 CESM-CoSiNE 海洋生态系统—生物地球化学模块为核心工具，结合观测资料与数值模拟，研究北太平洋、南海及全球大洋中浮游生态系统与碳循环的调控机制，并拓展至古气候重建与海洋数字孪生等前沿方向。</p>
    <p id="join">课题组面向全球招聘博士后、博士生与硕士生，欢迎对海洋生物地球化学、气候模拟与计算海洋学感兴趣的同学加入。</p>
    <p style="margin-top:28px"><a class="btn btn-solid" href="members.html">了解课题组成员 →</a></p>
  </div>
</div>''',
'en': '''<div class="section" id="about-group">
  <div class="intro-card intro-full">
    <p>Affiliated with the State Key Laboratory of Marine Environmental Science (MEL) at Xiamen University, our group conducts research on coupled physical\u2013ecological\u2013biogeochemical oceanography, with a focus on the marine carbon cycle, nutrient cycles, and the response and feedback of marine ecosystems to climate change.</p>
    <p>Centered on the CESM-CoSiNE marine ecosystem\u2013biogeochemistry module, which we develop in-house, and combining observations with numerical simulation, the group studies the controls of planktonic ecosystems and the carbon cycle in the North Pacific, the South China Sea, and the global ocean, extending to paleoclimate reconstruction and ocean digital twins.</p>
    <p id="join">The group welcomes postdoctoral researchers and PhD/Master's students from around the world with interests in marine biogeochemistry, climate modeling, and computational oceanography.</p>
    <p style="margin-top:28px"><a class="btn btn-solid" href="members.html">Meet the Team →</a></p>
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
            ('Faculty', [('Fei Chai', 'Chair Professor / PI', 'Marine biogeochemistry, physics-ecology coupling, climate modeling', 'fchai@xmu.edu.cn', 'about.html#chai', 'chai_fei.jpg'),
                          ('Xiaoyi Wang', 'Research Assistant', '\u2014', '\u2014', '', ''),
                          ('Wang Qian', 'Postdoctoral Researcher', '\u2014', '\u2014', '', ''),
                          ('Yang Kai', 'Postdoctoral Researcher', '\u2014', '\u2014', '', '')]),
            ('PhD Students', [('Zhao Kewei', 'PhD Student', '\u2014', '\u2014', '', ''),
                              ('Jiang Zheng', 'PhD Student', '\u2014', '\u2014', '', '')]),
            ("Master's Students", [('Lin Jianchun', "Master's Student", '\u2014', '\u2014', '', ''),
                                   ('Xie Xianyu', "Master's Student", '\u2014', '\u2014', '', ''),
                                   ('Li Peimin', "Master's Student", '\u2014', '\u2014', '', '')]),
            ('Alumni', [('Wang Qian', 'PhD Graduate (2025)', '\u2014', '\u2014', '', ''),
                        ('Wang Yin', "Master's Graduate (2026)", '\u2014', '\u2014', '', '')]),
        ]
    else:
        groups = [
            ('教职工', [('柴扉', '讲席教授 / PI', '海洋生物地球化学、物理—生态耦合、气候模拟', 'fchai@xmu.edu.cn', 'about.html#chai', 'chai_fei.jpg'),
                      ('王晓依', '科研助理', '—', '—', '', ''),
                      ('王谦', '博士后', '—', '—', '', ''),
                      ('杨凯', '博士后', '—', '—', '', '')]),
            ('博士研究生', [('赵柯崴', '博士研究生', '—', '—', '', ''),
                          ('姜正', '博士研究生', '—', '—', '', '')]),
            ('硕士研究生', [('林剑纯', '硕士研究生', '—', '—', '', ''),
                          ('谢娴予', '硕士研究生', '—', '—', '', ''),
                          ('李沛珉', '硕士研究生', '—', '—', '', '')]),
            ('已毕业成员', [('王谦', '博士毕业（2025）', '—', '—', '', ''),
                          ('王胤', '硕士毕业（2026）', '—', '—', '', '')]),
        ]
    out = ['<div class="section">']
    for i, (gtitle, members) in enumerate(groups):
        style = ' style="margin-top:72px"' if i > 0 else ''
        out.append(f'  <div class="sec-head"{style}>\n    <h2>{gtitle}</h2>\n  </div>')
        def _card(name, role, dir_, email, link, photo):
            home_zh, home_en, soon_zh, soon_en = '个人主页 →', 'Personal Page →', '个人主页 · 待配置', 'Personal page · TBD'
            if lang == EN:
                home_zh, home_en, soon_zh, soon_en = home_en, home_en, soon_en, soon_en
            if photo:
                face = f'<div class="m-avatar"><img src="images/{photo}" alt="{name}"></div>'
            else:
                face = f'<div class="m-avatar"><span class="m-initial">{name[0]}</span></div>'
            if link:
                ext = ' target="_blank"' if link.startswith('http') else ''
                return f'''    <a class="member m-link" href="{link}"{ext}>
      {face}
      <h4>{name}</h4>
      <div class="role">{role}</div>
      <div class="dir">{dir_}</div>
      <div class="email">{email}</div>
      <div class="m-home">{home_zh}<span class="m-arrow">›</span></div>
    </a>'''
            return f'''    <div class="member">
      {face}
      <h4>{name}</h4>
      <div class="role">{role}</div>
      <div class="dir">{dir_}</div>
      <div class="email">{email}</div>
      <div class="m-home soon">{soon_zh}</div>
    </div>'''
        cards = '\n'.join(_card(name, role, dir_, email, link, photo) for name, role, dir_, email, link, photo in members)
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

MONTHS_EN = ['', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

# 二级页面左侧竖排导航（href, 中文, 英文）
RESEARCH_ITEMS_ZH = [
    ('海洋生态系统与生物地球化学模拟', '发展并改进 CESM-CoSiNE 海洋生态系统—生物地球化学耦合模式，模拟浮游植物、营养盐与碳循环在全球大洋与边缘海的时空演变。'),
    ('海洋碳循环与气候反馈', '研究海洋对大气 CO₂ 的调控作用、生物泵效率及海洋碳循环对未来气候变化的响应。'),
    ('海洋次中尺度过程与生态效应', '探索次中尺度物理过程（锋面、涡旋）对浮游生态系统与碳输出通量的调控机制。'),
    ('古气候与古海洋模拟', '利用地球系统模式开展末次间冰期等关键时期古气候模拟，理解碳循环的长期演化。'),
    ('海洋数字孪生', '构建海洋数字孪生系统，赋能蓝色经济创新，服务海洋观测—模拟—预测一体化。'),
    ('观测—模拟融合', '结合现场观测、卫星遥感与数值模式，量化评估模式不确定性，改进生态模型参数化。'),
]
RESEARCH_ITEMS_EN = [
    ('Marine Ecosystem and Biogeochemical Modeling', 'Development and improvement of the CESM-CoSiNE coupled marine ecosystem-biogeochemistry module to simulate the spatiotemporal evolution of phytoplankton, nutrients, and the carbon cycle across the global ocean and marginal seas.'),
    ('Marine Carbon Cycle and Climate Feedbacks', 'Quantifying the ocean role in regulating atmospheric CO2, biological pump efficiency, and the response of the marine carbon cycle to future climate change.'),
    ('Submesoscale Processes and Ecological Effects', 'Exploring how submesoscale physical processes (fronts, eddies) regulate planktonic ecosystems and carbon export fluxes.'),
    ('Paleoclimate and Paleoceanography', 'Earth system modeling of key periods such as the Last Interglacial to understand the long-term evolution of the carbon cycle.'),
    ('Ocean Digital Twin', 'Building ocean digital twin systems to empower blue-economy innovation and integrated ocean observation-simulation-prediction.'),
    ('Observation-Model Integration', 'Combining in-situ observations, satellite remote sensing, and numerical models to quantify uncertainty and improve ecosystem model parameterizations.'),
]

SUB_MENUS = {
    'about': [
        ('about-group.html', '课题组简介', 'About the Group'),
        ('about-chai.html', '柴扉教授', 'Prof. Fei Chai'),
        ('members.html', '成员介绍', 'Members'),
    ],
    'papers': [
        ('papers-journal.html', '期刊论文', 'Journal Papers'),
        ('papers-digital-twin.html', '数字孪生', 'Digital Twin'),
        ('papers-data.html', '科研数据', 'Data'),
        ('papers-model.html', '数值模式', 'Models'),
    ],
    'research': [
        ('research-r0.html', '生态系统与生物地球化学模拟', 'Ecosystem & Biogeochemistry Modeling'),
        ('research-r1.html', '碳循环与气候反馈', 'Carbon Cycle & Climate Feedback'),
        ('research-r2.html', '次中尺度过程与生态效应', 'Submesoscale Processes & Ecology'),
        ('research-r3.html', '古气候与古海洋模拟', 'Paleoclimate & Paleoceanography'),
        ('research-r4.html', '海洋数字孪生', 'Ocean Digital Twin'),
        ('research-r5.html', '观测—模拟融合', 'Observation\u2013Model Fusion'),
        ('research-project.html', 'CESM-CoSiNE 项目', 'CESM-CoSiNE Project'),
    ],
    'links': [
        ('https://coeoa.xmu.edu.cn/t/CF/', '柴扉教授个人主页', "Prof. Chai's Homepage"),
        ('https://mel.xmu.edu.cn/', 'MEL 实验室官网', 'MEL Official Website'),
        ('links.html', '全部相关链接', 'All Links'),
    ],
}

def subnav_html(page, lang):
    items = SUB_MENUS[page]
    lis = []
    for href, zh, en in items:
        label = en if lang == EN else zh
        tgt = ' target="_blank"' if href.startswith('http') else ''
        lis.append(f'      <a href="{href}"{tgt}>{label}</a>')
    return '<nav class="sub-nav" id="subNav" aria-label="sub navigation">\n' + '\n'.join(lis) + '\n    </nav>'

def with_subnav(page, body, lang):
    return f'''<div class="page-wrap">
{subnav_html(page, lang)}
  <div class="sub-content">
{body}
  </div>
</div>'''


def paper_timeline(rows, lang, reveal=False):
    """论文时间线：同年份只显示一次，竖线 + 月份刻度"""
    groups = {}
    for year, month, title, authors, journal, doi in rows:
        groups.setdefault(year, []).append((month, title, authors, journal, doi))
    out = ['<ul class="papers tl">']
    for gi, year in enumerate(sorted(groups, reverse=True)):
        rev = f' data-reveal style="--d:{gi * 80}ms"' if reveal else ''
        out.append(f'  <li class="tl-group"{rev}>')
        out.append(f'    <div class="tl-year">{year}</div>')
        out.append('    <ul class="tl-items">')
        for month, title, authors, journal, doi in sorted(groups[year], key=lambda x: -x[0]):
            m = f'{month}月' if lang == ZH else MONTHS_EN[month]
            out.append(f'''      <li class="tl-item">
        <div class="tl-month">{m}</div>
        <div class="t">{title}</div>
        <div class="a">{authors}</div>
        <div class="j">{journal}. DOI: <a href="https://doi.org/{doi}" target="_blank" style="color:var(--navy-3)">{doi}</a></div>
      </li>''')
        out.append('    </ul>')
        out.append('  </li>')
    out.append('</ul>')
    return '\n'.join(out)

PAPERS = [
    ('2026', 2, 'Digital twin of the ocean as a catalyst for blue economy innovation',
     'Chai F., Deng Q., Dai M., Wang X., Staneva J., Behera S. K., Tonani M., Liu J., Yu Z., Peng Z.',
     'National Science Review, 13(3): nwag012', '10.1093/nsr/nwag012'),
    ('2025', 6, 'Rising trends in winter phytoplankton blooms in the northern Arabian Sea over the last two decades',
     'Song Z., Kang D., Chai F.',
     'Geophysical Research Letters, 52', '10.1029/2025GL116509'),
    ('2025', 3, 'Arctic warming as a potential trigger for the warm blob in the northeast Pacific',
     'Chen H.-H., Wang Y., Li X., Wan L., Yuan Y., Yan Y., Hannah C., Chai F.',
     'npj Climate and Atmospheric Science, 8', '10.1038/s41612-025-00900-9'),
    ('2024', 9, 'Development of a total variation diminishing (TVD) sea ice transport scheme for the ocean model',
     'Wang Q., Zhang Y., Chai F., Zhang Y. J., Zampieri L.',
     'Geoscientific Model Development, 17: 7067-7086', '10.5194/gmd-17-7067-2024'),
]

def papers_body(lang):
    if lang == EN:
        content = f'''<div class="section" id="journal">
  <div class="sec-head">
    <span class="en">JOURNAL PAPERS</span>
    <h2>Journal Papers</h2>
  </div>
  {paper_timeline(PAPERS, lang)}
</div>

<div class="section" id="digital-twin">
  <div class="sec-head">
    <span class="en">DIGITAL TWIN</span>
    <h2>Ocean Digital Twin</h2>
  </div>
  <div class="project-box">
    <div class="project-hero">
      <div class="kicker">DIGITAL TWIN</div>
      <h3>Digital twin of the ocean as a catalyst for blue economy innovation</h3>
      <p>Prof. Chai and international experts systematically reviewed the core architecture of ocean digital twins and key application scenarios in blue-economy development. Published in National Science Review (2026).</p>
    </div>
    <div class="project-body">
      <div class="project-links" style="margin-top:0">
        <a class="btn btn-solid" href="https://mel.xmu.edu.cn/info/1012/61071.htm" target="_blank">Read the Original Report →</a>
        <a class="btn btn-line" href="https://doi.org/10.1093/nsr/nwag012" target="_blank">Paper DOI →</a>
      </div>
    </div>
  </div>
</div>

<div class="section" id="data">
  <div class="sec-head">
    <span class="en">RESEARCH DATA</span>
    <h2>Research Data</h2>
  </div>
  <div class="project-box">
    <div class="project-body">
      <h4>BGC-Argo Observations</h4>
      <p>Biogeochemical-Argo float observations in the western North Pacific and the South China Sea, including high-frequency profiles of oxygen, nitrate, chlorophyll, pH, and particulate organic carbon flux.</p>
      <h4>Model Outputs</h4>
      <p>CESM-CoSiNE simulation outputs covering the global ocean, the North Pacific, and the South China Sea (data sharing under preparation).</p>
    </div>
  </div>
</div>

<div class="section" id="model">
  <div class="sec-head">
    <span class="en">NUMERICAL MODELS</span>
    <h2>Numerical Models</h2>
  </div>
  <div class="project-box">
    <div class="project-hero">
      <div class="kicker">CESM-CoSiNE</div>
      <h3>CESM-CoSiNE: An Ocean Ecosystem\u2013Biogeochemistry Module Embedded in CESM</h3>
      <p>Developed and maintained by our group, embedded in the CESM Earth System Model (POP2 ocean component) to study planktonic ecosystems and the marine carbon cycle at global and regional scales.</p>
    </div>
    <div class="project-body">
      <div class="project-links" style="margin-top:0">
        <a class="btn btn-solid" href="reports/CESM_CoSiNE16_Nature_style_draft_CN.html" target="_blank">Project Report (Nature Style)</a>
        <a class="btn btn-line" href="reports/CESM_CoSiNE16_v2_Process_Manual.html" target="_blank">V2 Coupling Manual</a>
      </div>
    </div>
  </div>
</div>'''
        return with_subnav('papers', content, lang)
    content = f'''<div class="section" id="journal">
  <div class="sec-head">
    <span class="en">JOURNAL PAPERS</span>
    <h2>期刊论文</h2>
  </div>
  {paper_timeline(PAPERS, lang)}
</div>

<div class="section" id="digital-twin">
  <div class="sec-head">
    <span class="en">DIGITAL TWIN</span>
    <h2>海洋数字孪生</h2>
  </div>
  <div class="project-box">
    <div class="project-hero">
      <div class="kicker">DIGITAL TWIN</div>
      <h3>Digital twin of the ocean as a catalyst for blue economy innovation</h3>
      <p>柴扉教授与国际专家系统梳理海洋数字孪生核心架构，解析其在蓝色经济发展中的关键应用场景。综述发表于 National Science Review（2026）。</p>
    </div>
    <div class="project-body">
      <div class="project-links" style="margin-top:0">
        <a class="btn btn-solid" href="https://mel.xmu.edu.cn/info/1012/61071.htm" target="_blank">阅读原报道 →</a>
        <a class="btn btn-line" href="https://doi.org/10.1093/nsr/nwag012" target="_blank">论文 DOI →</a>
      </div>
    </div>
  </div>
</div>

<div class="section" id="data">
  <div class="sec-head">
    <span class="en">RESEARCH DATA</span>
    <h2>科研数据</h2>
  </div>
  <div class="project-box">
    <div class="project-body">
      <h4>BGC-Argo 观测</h4>
      <p>西北太平洋与南海 Biogeochemical-Argo 浮标观测：溶解氧、硝酸盐、叶绿素、pH 与颗粒有机碳通量的高频剖面数据。</p>
      <h4>模式输出</h4>
      <p>CESM-CoSiNE 全球海洋、北太平洋与南海模拟输出（数据共享整理中）。</p>
    </div>
  </div>
</div>

<div class="section" id="model">
  <div class="sec-head">
    <span class="en">NUMERICAL MODELS</span>
    <h2>数值模式</h2>
  </div>
  <div class="project-box">
    <div class="project-hero">
      <div class="kicker">CESM-CoSiNE</div>
      <h3>CESM-CoSiNE：嵌入 CESM 的海洋生态—生物地球化学模块</h3>
      <p>由本课题组自主发展并维护，已嵌入 CESM 地球系统模式（POP2 海洋分量），研究全球及区域尺度浮游生态系统与海洋碳循环的演变。</p>
    </div>
    <div class="project-body">
      <div class="project-links" style="margin-top:0">
        <a class="btn btn-solid" href="reports/CESM_CoSiNE16_Nature_style_draft_CN.html" target="_blank">项目报告（Nature 风格）</a>
        <a class="btn btn-line" href="reports/CESM_CoSiNE16_v2_Process_Manual.html" target="_blank">V2 耦合说明书</a>
      </div>
    </div>
  </div>
</div>'''
    return with_subnav('papers', content, lang)

def news_body(lang):
    if lang == EN:
        return '''<div class="section news-page">
  <div class="news-feat">
    <div class="nf-head">
      <span class="date">FEB 2026</span>
      <h2>Prof. Chai\u2019s team reveals ocean digital twins as a new engine for blue-economy innovation</h2>
      <p>The team systematically reviewed the core architecture of ocean digital twins, analyzed key application scenarios in blue-economy development, and provided forward-looking perspectives on challenges and prospects. The review, titled \u201cDigital twin of the ocean as a catalyst for blue economy innovation\u201d, was published in National Science Review.</p>
      <a class="btn btn-gold" href="https://mel.xmu.edu.cn/info/1012/61071.htm" target="_blank" style="margin-top:22px">Read the Original Report →</a>
    </div>
  </div>
  <div class="news-list">
    <div class="news-item">
      <span class="date">JUL 2026</span>
      <h3>Profiling floats reveal deep-sea carbon pulses in the marginal sea</h3>
      <p>Using Biogeochemical-Argo floats deployed in the southwestern South China Sea, the team achieved three years of high-frequency observations of particulate organic carbon flux at 1000 m depth, revealing how seasonal cyclonic eddies and coastal jets drive deep-sea carbon flux pulses. The study was published in Limnology and Oceanography, with Prof. Fei Chai as a co-author.<a href="https://mel.xmu.edu.cn/info/1012/63211.htm" target="_blank" style="color:var(--navy-3)">Read the Original Report →</a></p>
    </div>
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
      <p>团队系统梳理了海洋数字孪生的核心架构，深度解析其在蓝色经济发展中的关键应用场景，并对该领域当前挑战与未来前景作出前瞻性研判。相关综述以\u201cDigital twin of the ocean as a catalyst for blue economy innovation\u201d为题发表于 National Science Review。</p>
      <a class="btn btn-gold" href="https://mel.xmu.edu.cn/info/1012/61071.htm" target="_blank" style="margin-top:22px">阅读原报道 →</a>
    </div>
  </div>
  <div class="news-list">
    <div class="news-item">
      <span class="date">2026-07</span>
      <h3>剖面浮标揭秘边缘海深海碳脉冲</h3>
      <p>利用南海西南部布放的生物地球化学剖面浮标实现1000米深颗粒有机碳通量连续三年高频观测，揭示季节性气旋涡与沿岸急流驱动深海碳通量脉冲的机制。相关成果发表于 Limnology and Oceanography，柴扉教授为共同作者。<a href="https://mel.xmu.edu.cn/info/1012/63211.htm" target="_blank" style="color:var(--navy-3)">阅读原报道 →</a></p>
    </div>
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
        content = '''<div class="section" id="links">
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
    <a class="link-card" href="https://mel.xmu.edu.cn/" target="_blank">
      <div class="icon">''' + SVG_LAB + '''</div>
      <h4>State Key Laboratory of Marine Environmental Science</h4>
      <p>Official website of MEL, Xiamen University</p>
      <div class="ext">mel.xmu.edu.cn →</div>
    </a>
  </div>
</div>'''
        return with_subnav('links', content, lang)
    content = '''<div class="section" id="links">
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
    <a class="link-card" href="https://mel.xmu.edu.cn/" target="_blank">
      <div class="icon">''' + SVG_LAB + '''</div>
      <h4>海洋生物地球化学全国重点实验室</h4>
      <p>厦门大学海洋生物地球化学全国重点实验室官网</p>
      <div class="ext">mel.xmu.edu.cn →</div>
    </a>
  </div>
</div>'''
    return with_subnav('links', content, lang)

def pi_detail_html(pi, lang):
    """柴教授完整个人介绍（头像头区 + 学术经历 + 研究领域 + 代表性论文）"""
    timeline = '\n'.join(
        f'''        <li>
          <span class="tl-dot"></span>
          <span class="tl-y">{y}</span>
          <span class="tl-t">{t}</span>
        </li>'''
        for y, t in pi['timeline'])
    interests = '\n'.join(f'        <li>{x}</li>' for x in pi['interests'])
    pubs = '\n'.join(
        f'''        <li>
          <span class="pub-y">{y}</span>
          <span class="pub-t"><b>{t}</b> <i>— {j}</i></span>
        </li>'''
        for y, t, j in pi['pubs'])
    L = lambda zh, en: en if lang == EN else zh
    if lang == EN:
        _unit = 'State Key Laboratory of Marine Environmental Science (MEL), XMU'
        _office = 'Zhoulongquan Building, Xiang\u2019an Campus, XMU'
    else:
        _unit = '海洋生物地球化学全国重点实验室（厦门大学）'
        _office = '厦门大学翔安校区周隆泉楼'
    return f'''<div class="section chai-sec" id="chai">
  <div class="sec-head">
    <span class="en">{L('PRINCIPAL INVESTIGATOR', 'PRINCIPAL INVESTIGATOR')}</span>
    <h2>{pi['name']}</h2>
  </div>
  <div class="chai-head" data-reveal>
    <div class="chai-photo">
      <img src="images/chai_fei.jpg" alt="{pi['name']}">
    </div>
    <div class="chai-meta">
      <div class="chai-title">{pi['title']}</div>
      <p class="chai-bio">{pi['bio']}</p>
      <ul class="chai-info">
        <li><b>{L('单位', 'Unit')}：</b>{_unit}</li>
        <li><b>{L('地址', 'Office')}：</b>{_office}</li>
        <li><b>{L('邮箱', 'Email')}：</b>fchai@xmu.edu.cn</li>
      </ul>
      <div class="chai-actions">
        <a class="btn btn-solid btn-sm" href="{pi['homepage']}" target="_blank">{L('个人主页', 'Personal Homepage')} →</a>
        <a class="btn btn-line btn-sm" href="members.html">{L('课题组成员', 'Group Members')} →</a>
      </div>
    </div>
  </div>
  <div class="chai-grid" data-reveal>
    <div class="chai-col">
      <h3>{L('学术经历', 'Career Timeline')}</h3>
      <ul class="chai-timeline">
{timeline}
      </ul>
    </div>
    <div class="chai-col">
      <h3>{L('主要研究领域', 'Research Interests')}</h3>
      <ul class="chai-interests">
{interests}
      </ul>
      <h3>{L('代表性论文', 'Selected Publications')}</h3>
      <ul class="chai-pubs">
{pubs}
      </ul>
    </div>
  </div>
</div>'''

PI_EN = {
    'name': 'Prof. Fei Chai',
    'en': 'PRINCIPAL INVESTIGATOR',
    'title': 'Tang Shifeng Chair Professor in Marine Sciences · PI',
    'bio': 'Marine biogeochemistry, ocean carbon cycle, and physical\u2013biogeochemical modeling. Ph.D. in Biological Oceanography, Duke University; former Professor and Dean at the School of Marine Sciences, University of Maine; currently Tang Shifeng Chair Professor at Xiamen University.',
    'btn1': 'About the Group',
    'btn2': 'Our Team',
    'homepage': 'https://coeoa.xmu.edu.cn/t/CF/',
    'timeline': [
        ('1980\u20131987', 'B.S./M.S. in Physical Oceanography, Ocean University of China'),
        ('1988\u20131991', 'M.S. in Ocean & Atmospheric Sciences, Princeton University'),
        ('1991\u20131995', 'Ph.D. in Biological Oceanography, Duke University'),
        ('1996\u20132008', 'Assistant then Associate (tenured) Professor, University of Maine'),
        ('2008\u20132021', 'Professor, School of Marine Sciences, University of Maine (Dean 2012\u20132015)'),
        ('2016\u20132022', 'Professor & Director, State Key Laboratory of Satellite Ocean Environment Dynamics, Second Institute of Oceanography, MNR'),
        ('2022\u2013now', 'Tang Shifeng Chair Professor, State Key Laboratory of Marine Environmental Science (MEL), Xiamen University'),
    ],
    'interests': [
        'Marine carbon cycle', 'Physical\u2013biogeochemical ecosystem modeling',
        'Marine ecosystem dynamics', 'Fisheries resources', 'BGC-Argo observations',
        'Ocean digital twin',
    ],
    'pubs': [
        ('2026', 'Digital twin of the ocean as a catalyst for blue economy innovation', 'National Science Review'),
        ('2021', 'A limited effect of sub-tropical typhoons on phytoplankton dynamics', 'Biogeosciences'),
        ('2020', 'Monitoring ocean biogeochemistry with autonomous platforms', 'Nature Reviews Earth & Environment'),
        ('2020', 'Enhanced winter carbon export observed by BGC-Argo in the Northwest Pacific Ocean', 'Geophysical Research Letters'),
    ],
}

PI_ZH = {
    'name': '柴扉 教授',
    'en': 'PRINCIPAL INVESTIGATOR',
    'title': '"唐世凤"海洋学科讲席教授 · PI',
    'bio': '长期从事海洋生物地球化学、海洋碳循环与物理—生物地球化学模型研究。美国杜克大学生物海洋学博士，曾任美国缅因大学海洋学院教授、院长，现任厦门大学海洋生物地球化学全国重点实验室"唐世凤"海洋学科讲席教授。',
    'btn1': '了解课题组',
    'btn2': '我们的团队',
    'homepage': 'https://coeoa.xmu.edu.cn/t/CF/',
    'timeline': [
        ('1980–1987', '中国海洋大学 物理海洋学 本科、硕士'),
        ('1988–1991', '美国普林斯顿大学 海洋和大气科学 硕士'),
        ('1991–1995', '美国杜克大学 生物海洋学 博士'),
        ('1996–2008', '美国缅因大学海洋学院 助理教授、副教授（终身教职）'),
        ('2008–2021', '美国缅因大学海洋学院 教授（2012–2015 任院长）'),
        ('2016–2022', '自然资源部第二海洋研究所研究员、卫星海洋环境动力学国家重点实验室主任'),
        ('2022–至今', '厦门大学 "唐世凤"海洋学科讲席教授'),
    ],
    'interests': [
        '海洋碳循环', '物理—生物地球化学模型', '海洋生态系统',
        '渔业资源', 'BGC-Argo 观测', '海洋数字孪生',
    ],
    'pubs': [
        ('2026', 'Digital twin of the ocean as a catalyst for blue economy innovation', 'National Science Review'),
        ('2021', 'A limited effect of sub-tropical typhoons on phytoplankton dynamics', 'Biogeosciences'),
        ('2020', 'Monitoring ocean biogeochemistry with autonomous platforms', 'Nature Reviews Earth & Environment'),
        ('2020', 'Enhanced winter carbon export observed by BGC-Argo in the Northwest Pacific Ocean', 'Geophysical Research Letters'),
    ],
}

def home_body(lang):
    """首页：清华式布局（Hero轮播+统计条+新闻分栏+研究方向+项目横幅+论文+招生合作）"""
    import os
    if lang == EN:
        slides = [
            ('Ocean Digital Twin', 'Ocean digital twin as a catalyst for blue-economy innovation',
             'Prof. Chai and international experts published a review in National Science Review',
             [('Read More', 'news.html'), ('Research', 'research.html')]),
            ('Earth System Modeling', 'The CESM-CoSiNE Marine Ecosystem Model', 'From coupled physics\u2013chemistry\u2013biology to understanding the marine carbon cycle',
             [('CESM-CoSiNE Details', 'research.html#project'), ('Project Report', 'reports/CESM_CoSiNE16_Nature_style_draft_CN.html')]),
            ('Paleoclimate & Digital Earth', 'Paleoclimate and the Digital Earth', 'Reconstruct the past, simulate the present, foresee the future',
             [('Research Areas', 'research.html'), ('About Us', 'about.html')]),
        ]
        stats = [(4, '', 'Faculty'), (6, '', 'Research Areas'), (5, '', 'Graduate Students'), (100, '+', 'Publications')]
        news_head = ('Group News', 'GROUP NEWS', 'Learn More')
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
        aca = {
            'title': 'Research Progress',
            'en': 'RESEARCH PROGRESS',
            'more': 'Learn More',
            'slider': ['images/mel_digital_twin.png', 'images/cosine_bg.png'],
            'feat_img': 'images/mel_digital_twin.png',
            'feat_h': 'Ocean digital twin as a catalyst for blue-economy innovation',
            'feat_p': 'Prof. Chai and international experts published a review in National Science Review, systematically reviewing the core architecture of ocean digital twins and key application scenarios in blue-economy development.',
            'feat_date': 'FEB 2026 · National Science Review',
             'block1': 'Research Progress',
             'block1_items': [
                 ('JUL 2026', 'Profiling floats reveal deep-sea carbon pulses in the marginal sea',
                  'images/cosine_bg.png', 'https://mel.xmu.edu.cn/info/1012/63211.htm'),
                 ('MAR 2026', 'CESM-CoSiNE module development and validation',
                  'images/cosine_bg.png', 'research.html#project'),
                 ('FEB 2026', 'Ocean digital twin review published in National Science Review',
                  'images/mel_digital_twin.png', 'https://mel.xmu.edu.cn/info/1012/61071.htm'),
                 ('NOV 2025', 'Lujiang Ocean Symposium concludes successfully',
                  'images/cosine_bg.png', 'news.html'),
                 ('SEP 2025', 'Group website officially launched',
                  'images/cosine_bg.png', 'news.html'),
                 ('JUN 2025', 'Rising winter phytoplankton blooms in the northern Arabian Sea',
                  'images/cosine_bg.png', 'papers.html'),
                 ('MAR 2025', 'Arctic warming as a potential trigger for the warm blob in the northeast Pacific',
                  'images/cosine_bg.png', 'papers.html'),
                 ('SEP 2024', 'TVD sea ice transport scheme published in Geoscientific Model Development',
                  'images/cosine_bg.png', 'papers.html'),
             ],
            'block2': 'Selected Work',
            'block2_items': [
                ('CESM-CoSiNE16', 'An ocean ecosystem\u2013biogeochemistry module embedded in CESM', 'reports/CESM_CoSiNE16_Nature_style_draft_CN.html'),
                ('CoSiNE22 (V2)', 'Coupling manual with carbon isotope tracers', 'reports/CESM_CoSiNE16_v2_Process_Manual.html'),
            ],
            'link_news': 'news.html',
        }
        pub_head = ('Academic Papers', 'ACADEMIC PAPERS', 'Learn More')
        pubs = [
            ('2026', 2, 'Digital twin of the ocean as a catalyst for blue economy innovation', 'Chai F., Deng Q., Dai M., et al.', 'National Science Review, 13(3): nwag012', '10.1093/nsr/nwag012'),
            ('2025', 6, 'Rising trends in winter phytoplankton blooms in the northern Arabian Sea over the last two decades', 'Song Z., Kang D., Chai F.', 'Geophysical Research Letters, 52', '10.1029/2025GL116509'),
            ('2025', 3, 'Arctic warming as a potential trigger for the warm blob in the northeast Pacific', 'Chen H.-H., Wang Y., Li X., et al.', 'npj Climate and Atmospheric Science, 8', '10.1038/s41612-025-00900-9'),
            ('2024', 9, 'Development of a total variation diminishing (TVD) sea ice transport scheme', 'Wang Q., Zhang Y., Chai F., et al.', 'Geoscientific Model Development, 17', '10.5194/gmd-17-7067-2024'),
        ]
        join = [
            ('Recruitment', 'We recruit PhD and Master\u2019s students year-round and welcome postdoctoral applicants from around the world with interests in marine biogeochemistry, climate modeling, and computational oceanography.', 'mailto:fchai@xmu.edu.cn', 'Send an Application'),
            ('Collaboration', 'The group maintains close collaborations with universities and research institutes at home and abroad. We welcome academic visits, joint training, and project cooperation.', 'links.html', 'Related Links'),
        ]
        scroll_hint = 'Scroll'
        pi = PI_EN
    else:
        slides = [
            ('Ocean Digital Twin', '海洋数字孪生：赋能蓝色经济创新', '柴扉教授团队综述发表于 National Science Review',
             [('了解更多', 'news.html'), ('研究方向', 'research.html')]),
            ('Earth System Modeling', 'CESM-CoSiNE 海洋生态系统模式', '从物理—化学—生物耦合出发，理解海洋碳循环',
             [('模式详情', 'research.html#project'), ('项目报告', 'reports/CESM_CoSiNE16_Nature_style_draft_CN.html')]),
            ('Paleoclimate & Digital Earth', '古气候与数字地球', '重建过去，模拟现在，预见未来',
             [('研究方向', 'research.html'), ('了解课题组', 'about.html')]),
        ]
        stats = [(4, '', '教职工'), (6, '', '研究方向'), (5, '', '在读研究生'), (100, '+', '发表论文')]
        news_head = ('课题组动态', 'GROUP NEWS', '了解更多')
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
        aca = {
            'title': '科研进展',
            'en': 'RESEARCH PROGRESS',
            'more': '了解更多',
            'slider': ['images/mel_digital_twin.png', 'images/cosine_bg.png'],
            'feat_img': 'images/mel_digital_twin.png',
            'feat_h': '海洋数字孪生综述发表于 National Science Review',
            'feat_p': '柴扉教授团队系统梳理海洋数字孪生核心架构，解析其在蓝色经济发展中的关键应用场景，并对该领域挑战与前景作出前瞻性研判。',
            'feat_date': '2026-02 · National Science Review',
             'block1': '科研进展',
             'block1_items': [
                 ('2026-07', '剖面浮标揭秘边缘海深海碳脉冲',
                  'images/cosine_bg.png', 'https://mel.xmu.edu.cn/info/1012/63211.htm'),
                 ('2026-03', 'CESM-CoSiNE 模式研发与验证进展',
                  'images/cosine_bg.png', 'research.html#project'),
                 ('2026-02', '海洋数字孪生综述发表于 National Science Review',
                  'images/mel_digital_twin.png', 'https://mel.xmu.edu.cn/info/1012/61071.htm'),
                 ('2025-11', '鹭江海洋研讨会圆满落幕',
                  'images/cosine_bg.png', 'news.html'),
                 ('2025-09', '课题组网站全新上线',
                  'images/cosine_bg.png', 'news.html'),
                 ('2025-06', '阿拉伯海冬季浮游植物水华呈上升趋势',
                  'images/cosine_bg.png', 'papers.html'),
                 ('2025-03', '北极增暖或触发东北太平洋暖斑',
                  'images/cosine_bg.png', 'papers.html'),
                 ('2024-09', 'TVD 海冰输运方案发表于 Geoscientific Model Development',
                  'images/cosine_bg.png', 'papers.html'),
             ],
            'block2': '代表性工作',
            'block2_items': [
                ('CESM-CoSiNE16', '嵌入 CESM 的海洋生态—生物地球化学模块', 'reports/CESM_CoSiNE16_Nature_style_draft_CN.html'),
                ('CoSiNE22 (V2)', '含碳同位素示踪物的耦合说明书', 'reports/CESM_CoSiNE16_v2_Process_Manual.html'),
            ],
            'link_news': 'news.html',
        }
        pub_head = ('学术论文', 'ACADEMIC PAPERS', '了解更多')
        pubs = [
            ('2026', 2, 'Digital twin of the ocean as a catalyst for blue economy innovation', 'Chai F., Deng Q., Dai M., 等.', 'National Science Review, 13(3): nwag012', '10.1093/nsr/nwag012'),
            ('2025', 6, 'Rising trends in winter phytoplankton blooms in the northern Arabian Sea over the last two decades', 'Song Z., Kang D., Chai F.', 'Geophysical Research Letters, 52', '10.1029/2025GL116509'),
            ('2025', 3, 'Arctic warming as a potential trigger for the warm blob in the northeast Pacific', 'Chen H.-H., Wang Y., Li X., 等.', 'npj Climate and Atmospheric Science, 8', '10.1038/s41612-025-00900-9'),
            ('2024', 9, 'Development of a total variation diminishing (TVD) sea ice transport scheme', 'Wang Q., Zhang Y., Chai F., 等.', 'Geoscientific Model Development, 17', '10.5194/gmd-17-7067-2024'),
        ]
        join = [
            ('招生招聘', '课题组长期招收博士研究生、硕士研究生，并面向全球招聘博士后。欢迎对海洋生物地球化学、气候模拟与计算海洋学感兴趣的同学与我们联系。', 'mailto:fchai@xmu.edu.cn', '发送申请邮件'),
            ('合作交流', '课题组与国内外多所高校及研究机构保持紧密合作，欢迎就学术访问、联合培养与项目合作事宜洽谈。', 'links.html', '查看相关链接'),
        ]
        scroll_hint = '向下滚动'
        pi = PI_ZH

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
        if i == 0:
            photo = 'images/mel_digital_twin.png'
        if i == 1:
            photo = 'images/cosine_bg.png'
        bg_style = f' style="background-image:linear-gradient(rgba(7,24,42,.5),rgba(7,24,42,.5)),url({photo});background-size:cover;background-position:center"' if photo else ''
        def _cta(j, t, u):
            cls = ' cta-solid' if j == 0 else ''
            ext = ' target="_blank"' if 'reports/' in u else ''
            return f'          <a class="hero-cta{cls}" href="{u}"{ext}>{t} →</a>'
        cta_html = '\n'.join(_cta(j, t, u) for j, (t, u) in enumerate(ctas))
        # 第三屏（古气候与数字地球）：视频背景
        video_html = ''
        if i == 2:
            video_html = '''      <video class="hvideo" autoplay muted loop playsinline preload="metadata" aria-hidden="true">
        <source src="videos/paleo_hero.mp4" type="video/mp4">
        <source src="videos/paleo_hero.webm" type="video/webm">
      </video>'''
        slide_parts.append(f'''    <div class="hslide{' hs' + str(i+1) if not photo and not video_html else ''}{' on' if i == 0 else ''}"{bg_style}>
{video_html}
{'' if video_html else decos[i]}
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
    pi_name = pi['name']; pi_en = pi['en']; pi_title = pi['title']
    pi_bio = pi['bio']; pi_btn1 = pi['btn1']; pi_btn2 = pi['btn2']
    pi_timeline = '\n'.join(
        f'''          <li><span class="tl-y">{y}</span><span class="tl-t">{t}</span></li>'''
        for y, t in pi['timeline'])
    pi_interests = '\n'.join(f'          <li>{x}</li>' for x in pi['interests'])
    pi_pubs = '\n'.join(
        f'''          <li><span class="pub-y">{y}</span><span class="pub-t">{t} <i>— {j}</i></span></li>'''
        for y, t, j in pi['pubs'])
    list_parts = '\n'.join(
        f'''      <a class="nitem" href="news.html" data-reveal style="--d:{i*100}ms">
        <span class="date">{d}</span>
        <h4>{t}</h4>
        <span class="arr">→</span>
      </a>''' for i, (d, t, p) in enumerate(news[1:]))

    pub_parts = paper_timeline(pubs, lang, reveal=True)

    join_parts = '\n'.join(
        f'''    <div class="join-cell" data-reveal style="--d:{i*120}ms">
      <h3>{t}</h3>
      <p>{p}</p>
      <a class="btn btn-ghost" href="{u}">{b} →</a>
    </div>''' for i, (t, p, u, b) in enumerate(join))

    tiles = tiles_body(lang, 'research.html#')

    aca_index = '\n'.join(
        f'''        <li data-img="{img}" data-link="{link}" class="{"on" if i == 0 else ""}">
          <span class="d">{d}</span>
          <span class="t">{t}</span>
          <span class="arr">→</span>
        </li>''' for i, (d, t, img, link) in enumerate(aca['block1_items']))
    aca_stage = '\n'.join(
        f'''      <div class="aca-stage-img{" on" if i == 0 else ""}" style="background-image:url({img})"></div>'''
        for i, (d, t, img, link) in enumerate(aca['block1_items']))

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
        <a class="btn btn-line" href="{pi['homepage']}" target="_blank">{'Personal Homepage' if lang == EN else '个人主页'} →</a>
      </div>
    </div>
  </div>
</div>

<!-- 课题组动态 -->
<div class="section home-sec" id="news">
  <div class="sec-head" data-reveal>
    <span class="en">{news_head[1]}</span>
    <h2>{news_head[0]}</h2>
  </div>
  <div class="news-split">
    <a class="nfeat" href="https://mel.xmu.edu.cn/info/1012/61071.htm" target="_blank" data-reveal>
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
  <p style="text-align:center;margin-top:40px" data-reveal><a class="btn btn-sm btn-line" href="news.html">{news_head[2]} →</a></p>
</div>

<!-- 统计条 -->
<div class="stats-band">
  <div class="stats">
{stat_parts}
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
  <p style="text-align:center;margin-top:40px" data-reveal><a class="btn btn-sm btn-line" href="research.html">{res_more} →</a></p>
</div>

<!-- 学术·科研面板（左侧索引 / 右侧大图，hover 切换） -->
<div class="section home-sec academic-sec" id="academic">
  <div class="sec-head" data-reveal>
    <span class="en">{aca['en']}</span>
    <h2>{aca['title']}</h2>
  </div>
  <div class="aca-wrap" data-reveal>
    <div class="aca-index">
      <ul>
{aca_index}
      </ul>
    </div>
    <div class="aca-stage">
{aca_stage}
      <div class="aca-stage-cap">
        <span class="cap-t">{aca['block1_items'][0][1]}</span>
        <span class="cap-d">{aca['block1_items'][0][0]}</span>
      </div>
    </div>
  </div>
  <p style="text-align:center;margin-top:40px" data-reveal><a class="btn btn-sm btn-line" href="{aca['link_news']}">{aca['more']} →</a></p>
</div>

<!-- 代表性论文 -->
<div class="section home-sec" id="pubs">
  <div class="sec-head" data-reveal>
    <span class="en">{pub_head[1]}</span>
    <h2>{pub_head[0]}</h2>
  </div>
  <ul class="papers">
{pub_parts}
  </ul>
  <p style="text-align:center;margin-top:40px" data-reveal><a class="btn btn-sm btn-line" href="papers.html">{pub_head[2]} →</a></p>
</div>

<!-- 招生招聘 / 合作交流 -->
<div class="join-band">
  <div class="join-grid">
{join_parts}
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
    return with_subnav('research', f'''<div class="section">
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
</div>''', lang)

# ============ 二级滑动视图（Hero 式顺序切换） ============

def research_slides(lang):
    """研究方向二级内容：Hero 式垂直全屏滑动（每屏一个方向）"""
    if lang == EN:
        items = [
            ('Marine Ecosystem and Biogeochemical Modeling', 'Development and improvement of the CESM-CoSiNE coupled marine ecosystem-biogeochemistry module to simulate the spatiotemporal evolution of phytoplankton, nutrients, and the carbon cycle across the global ocean and marginal seas.', 'images/cosine_bg.png'),
            ('Marine Carbon Cycle and Climate Feedbacks', 'Quantifying the ocean role in regulating atmospheric CO2, biological pump efficiency, and the response of the marine carbon cycle to future climate change.', 'images/mel_digital_twin.png'),
            ('Submesoscale Processes and Ecological Effects', 'Exploring how submesoscale physical processes (fronts, eddies) regulate planktonic ecosystems and carbon export fluxes.', 'images/cosine_bg.png'),
            ('Paleoclimate and Paleoceanography', 'Earth system modeling of key periods such as the Last Interglacial to understand the long-term evolution of the carbon cycle.', 'images/cosine_bg.png'),
            ('Ocean Digital Twin', 'Building ocean digital twin systems to empower blue-economy innovation and integrated ocean observation-simulation-prediction.', 'images/mel_digital_twin.png'),
            ('Observation-Model Integration', 'Combining in-situ observations, satellite remote sensing, and numerical models to quantify uncertainty and improve ecosystem model parameterizations.', 'images/cosine_bg.png'),
        ]
    else:
        items = [
            ('海洋生态系统与生物地球化学模拟', '发展并改进 CESM-CoSiNE 海洋生态系统—生物地球化学耦合模式，模拟浮游植物、营养盐与碳循环在全球大洋与边缘海的时空演变。', 'images/cosine_bg.png'),
            ('海洋碳循环与气候反馈', '研究海洋对大气 CO₂ 的调控作用、生物泵效率及海洋碳循环对未来气候变化的响应。', 'images/mel_digital_twin.png'),
            ('海洋次中尺度过程与生态效应', '探索次中尺度物理过程（锋面、涡旋）对浮游生态系统与碳输出通量的调控机制。', 'images/cosine_bg.png'),
            ('古气候与古海洋模拟', '利用地球系统模式开展末次间冰期等关键时期古气候模拟，理解碳循环的长期演化。', 'images/cosine_bg.png'),
            ('海洋数字孪生', '构建海洋数字孪生系统，赋能蓝色经济创新，服务海洋观测—模拟—预测一体化。', 'images/mel_digital_twin.png'),
            ('观测—模拟融合', '结合现场观测、卫星遥感与数值模式，量化评估模式不确定性，改进生态模型参数化。', 'images/cosine_bg.png'),
        ]
    panels = []
    for i, (title, desc, img) in enumerate(items):
        num = '%02d' % (i + 1)
        panels.append('''<section class="vs-panel">
      <div class="vs-bg" style="background-image:linear-gradient(rgba(7,24,42,.72),rgba(7,24,42,.72)),url(%s)"></div>
      <div class="vs-inner">
        <span class="vs-num">%s</span>
        <h2>%s</h2>
        <p>%s</p>
        <span class="vs-line"></span>
      </div>
    </section>''' % (img, num, title, desc))
    proj = project_box(lang, full=True)
    panels.append('''<section class="vs-panel">
      <div class="vs-bg" style="background-image:linear-gradient(rgba(7,24,42,.8),rgba(7,24,42,.8)),url(images/cosine_bg.png)"></div>
      <div class="vs-inner vs-scroll">
        <span class="vs-num">CESM-CoSiNE</span>
        <h2>%s</h2>
        <span class="vs-line"></span>
        %s
      </div>
    </section>''' % ('CESM-CoSiNE Project' if lang == EN else 'CESM-CoSiNE 项目', proj))
    return '\n'.join(panels)

def papers_slides(lang):
    """学术论文二级内容：Hero 式垂直全屏滑动"""
    if lang == EN:
        blocks = [
            ('Journal Papers', 'Peer-reviewed journal publications of the group.', 'images/mel_digital_twin.png', paper_timeline(PAPERS, lang)),
            ('Ocean Digital Twin', 'The ocean digital twin framework and its applications in blue-economy innovation.', 'images/mel_digital_twin.png', project_box(lang, full=True)),
            ('Research Data', 'BGC-Argo observations and model outputs for the North Pacific and the South China Sea.', 'images/cosine_bg.png', '<p class="vs-p">BGC-Argo float observations in the western North Pacific and the South China Sea; CESM-CoSiNE simulation outputs (data sharing under preparation).</p>'),
            ('Numerical Models', 'The CESM-CoSiNE marine ecosystem-biogeochemistry module embedded in CESM.', 'images/cosine_bg.png', project_box(lang, full=True)),
        ]
    else:
        blocks = [
            ('期刊论文', '课题组发表的同行评审期刊论文。', 'images/mel_digital_twin.png', paper_timeline(PAPERS, lang)),
            ('海洋数字孪生', '海洋数字孪生框架及其在蓝色经济创新中的应用。', 'images/mel_digital_twin.png', project_box(lang, full=True)),
            ('科研数据', '北太平洋与南海 BGC-Argo 观测及模式输出数据。', 'images/cosine_bg.png', '<p class="vs-p">西北太平洋与南海 Biogeochemical-Argo 浮标观测；CESM-CoSiNE 全球海洋、北太平洋与南海模拟输出（数据共享整理中）。</p>'),
            ('数值模式', '嵌入 CESM 的 CESM-CoSiNE 海洋生态—生物地球化学模块。', 'images/cosine_bg.png', project_box(lang, full=True)),
        ]
    panels = []
    for i, (title, desc, img, content) in enumerate(blocks):
        num = '%02d' % (i + 1)
        panels.append('''<section class="vs-panel">
      <div class="vs-bg" style="background-image:linear-gradient(rgba(7,24,42,.78),rgba(7,24,42,.78)),url(%s)"></div>
      <div class="vs-inner vs-scroll">
        <span class="vs-num">%s</span>
        <h2>%s</h2>
        <p class="vs-p">%s</p>
        <span class="vs-line"></span>
        %s
      </div>
    </section>''' % (img, num, title, desc, content))
    return '\n'.join(panels)

def about_slides(lang):
    """成员介绍二级内容：Hero 式垂直全屏滑动"""
    if lang == EN:
        blocks = [
            ('About the Group', ABOUT_BODY['en']),
            ('Prof. Fei Chai', pi_detail_html(PI_EN, EN)),
            ('Members', members_body(EN)),
        ]
    else:
        blocks = [
            ('课题组简介', ABOUT_BODY['zh']),
            ('柴扉教授', pi_detail_html(PI_ZH, ZH)),
            ('成员介绍', members_body(ZH)),
        ]
    panels = []
    for i, (title, content) in enumerate(blocks):
        num = '%02d' % (i + 1)
        panels.append('''<section class="vs-panel">
      <div class="vs-bg" style="background-image:linear-gradient(rgba(7,24,42,.8),rgba(7,24,42,.8)),url(images/cosine_bg.png)"></div>
      <div class="vs-inner vs-scroll">
        <span class="vs-num">%s</span>
        <h2>%s</h2>
        <span class="vs-line"></span>
        %s
      </div>
    </section>''' % (num, title, content))
    return '\n'.join(panels)

def slides_page(key, lang, title, en_sub):
    """二级内容页：Hero 式垂直全屏滑动（vs-view）"""
    if key == 'research':
        panels = research_slides(lang)
    elif key == 'papers':
        panels = papers_slides(lang)
    else:
        panels = about_slides(lang)
    n = panels.count('<section class="vs-panel"')
    steps = '\n'.join('<span%s></span>' % (' class="on"' if i == 0 else '') for i in range(n))
    body = '''<div class="vs-view" id="vsView">
  <div class="vs-track" id="vsTrack">
%s
  </div>
  <button class="vs-arrow up" id="vsUp" aria-label="prev">↑</button>
  <button class="vs-arrow down" id="vsDown" aria-label="next">↓</button>
  <div class="vs-steps" id="vsSteps">
%s
  </div>
  <div class="vs-counter" id="vsCounter">1 / %d</div>
</div>''' % (panels, steps, n)
    fname = key + '-slides.html'
    return page(fname, title, en_sub, body, lang, banner=False,
                scripts='../js/home.js' if lang == EN else 'js/home.js')

def apple_page(key, lang, title, en_sub, hero_sub, items):
    """一级页面：Apple iPhone 风格（Hero + sticky 横向二级导航 + 大 section + 保留左侧纵向 sub-nav）"""
    # Hero 区
    hero = '''<div class="apple-hero">
  <div class="apple-hero-inner">
    <span class="en">%s</span>
    <h1>%s</h1>
    <p>%s</p>
  </div>
</div>''' % (en_sub, title, hero_sub)

    # sticky 横向二级导航条（Apple 机型条样式）
    nav_links = '\n'.join(
        '<a href="#%s">%s</a>' % (aid, t) for aid, t in [(x[0], x[1]) for x in items])
    apple_nav = '''<nav class="apple-nav" id="appleNav">
  <div class="apple-nav-inner">
%s
  </div>
</nav>''' % nav_links

    # 各二级内容大 section（Apple 式）
    sections = []
    for i, (aid, t, d, img, content) in enumerate(items):
        num = '%02d' % (i + 1)
        if img:
            bg = ' style="background-image:linear-gradient(rgba(7,24,42,.86),rgba(7,24,42,.86)),url(%s)"' % img
        else:
            bg = ''
        sections.append('''<div class="apple-section" id="%s"%s>
  <div class="apple-sec-inner">
    <span class="as-num">%s</span>
    <h2>%s</h2>
    <p class="as-desc">%s</p>
    %s
  </div>
</div>''' % (aid, bg, num, t, d, content))

    body = hero + apple_nav + '''
<div class="page-wrap">
%s
  <div class="sub-content">
%s
  </div>
</div>''' % (subnav_html(key, lang), '\n'.join(sections))
    return body

def main():
    specs = {
        'about.html': ('课题组简介', 'ABOUT THE GROUP', ABOUT_BODY),
        'research.html': ('研究方向', 'RESEARCH AREAS', None),
        'project.html': ('CESM-CoSiNE', 'CESM-CoSiNE PROJECT', None),
        'papers.html': ('学术论文', 'ACADEMIC PAPERS', None),
        'news.html': ('课题组动态', 'GROUP NEWS', None),
        'links.html': ('相关链接', 'RELATED LINKS', None),
    }
    specs_en = {
        'about.html': ('About the Group', 'ABOUT THE GROUP', ABOUT_BODY),
        'research.html': ('Research', 'RESEARCH AREAS', None),
        'project.html': ('CESM-CoSiNE', 'CESM-CoSiNE PROJECT', None),
        'papers.html': ('Academic Papers', 'ACADEMIC PAPERS', None),
        'news.html': ('Group News', 'GROUP NEWS', None),
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

    # ---- 二级独立页面 ----
    def sub_pages_zh():
        pages = []
        # 成员介绍栏
        pages.append(('about-group.html', '课题组简介', 'ABOUT THE GROUP',
                      with_subnav('about', ABOUT_BODY['zh'], ZH)))
        pages.append(('about-chai.html', '柴扉教授', 'PROF. FEI CHAI',
                      with_subnav('about', pi_detail_html(PI_ZH, ZH), ZH)))
        # 学术论文栏
        pages.append(('papers-journal.html', '期刊论文', 'JOURNAL PAPERS',
                      with_subnav('papers', '<div class="section" id="journal">' + paper_timeline(PAPERS, ZH) + '</div>', ZH)))
        pages.append(('papers-digital-twin.html', '数字孪生', 'DIGITAL TWIN',
                      with_subnav('papers', '<div class="section" id="digital-twin">' + project_box(ZH, full=True) + '</div>', ZH)))
        pages.append(('papers-data.html', '科研数据', 'RESEARCH DATA',
                      with_subnav('papers', '''<div class="section" id="data">
  <div class="sec-head"><span class="en">RESEARCH DATA</span><h2>科研数据</h2></div>
  <div class="ov-desc"><p>西北太平洋与南海 Biogeochemical-Argo 浮标观测；CESM-CoSiNE 全球海洋、北太平洋与南海模拟输出（数据共享整理中）。</p></div>
</div>''', ZH)))
        pages.append(('papers-model.html', '数值模式', 'NUMERICAL MODELS',
                      with_subnav('papers', '<div class="section" id="model">' + project_box(ZH, full=True) + '</div>', ZH)))
        # 研究方向栏
        for i in range(6):
            aid = 'r%d' % i
            num = '%02d' % (i + 1)
            title, desc = RESEARCH_ITEMS_ZH[i]
            pages.append(('research-%s.html' % aid, title, 'RESEARCH AREA %s' % num,
                          with_subnav('research', '''<div class="section" id="%s">
  <div class="sec-head"><span class="en">%s · 研究方向</span><h2>%s</h2></div>
  <div class="ov-desc"><p>%s</p></div>
</div>''' % (aid, num, title, desc), ZH)))
        pages.append(('research-project.html', 'CESM-CoSiNE 项目', 'CESM-CoSiNE PROJECT',
                      with_subnav('research', '<div class="section" id="project">' + project_box(ZH, full=True) + '</div>', ZH)))
        for fname, title, en_sub, body in pages:
            html = page(fname, title, en_sub, body, ZH, scripts='js/home.js')
            open(fname, 'w').write(html)
            print('生成二级页', fname)

    sub_pages_zh()

    # ---- 一级总览页（二级入口卡片） ----
    def overview_zh():
        groups = [
            ('成员介绍', 'GROUP OVERVIEW', [
                ('课题组简介', '课题组研究概况与招生信息。', 'about-group.html'),
                ('柴扉教授', '个人档案：学术经历、研究领域与代表性论文。', 'about-chai.html'),
                ('成员介绍', '教职工、博士后与研究生名单。', 'members.html'),
            ]),
            ('研究方向', 'RESEARCH AREAS', [
                ('海洋生态系统与生物地球化学模拟', RESEARCH_ITEMS_ZH[0][1], 'research-r0.html'),
                ('海洋碳循环与气候反馈', RESEARCH_ITEMS_ZH[1][1], 'research-r1.html'),
                ('海洋次中尺度过程与生态效应', RESEARCH_ITEMS_ZH[2][1], 'research-r2.html'),
                ('古气候与古海洋模拟', RESEARCH_ITEMS_ZH[3][1], 'research-r3.html'),
                ('海洋数字孪生', RESEARCH_ITEMS_ZH[4][1], 'research-r4.html'),
                ('观测—模拟融合', RESEARCH_ITEMS_ZH[5][1], 'research-r5.html'),
                ('CESM-CoSiNE 项目', '嵌入 CESM 的海洋生态—生物地球化学模块。', 'research-project.html'),
            ]),
            ('学术论文', 'ACADEMIC PAPERS', [
                ('期刊论文', '课题组发表的同行评审期刊论文。', 'papers-journal.html'),
                ('数字孪生', '海洋数字孪生框架及其应用。', 'papers-digital-twin.html'),
                ('科研数据', 'BGC-Argo 观测与模式输出数据。', 'papers-data.html'),
                ('数值模式', 'CESM-CoSiNE 模式与报告。', 'papers-model.html'),
            ]),
        ]
        for title, en_sub, items in groups:
            cards = '\n'.join(
                '''      <a class="ov-card" href="%s">
        <span class="ov-go">%s →</span>
        <h3>%s</h3>
        <p>%s</p>
      </a>''' % (link, '进入', t, d) for t, d, link in items)
            body = '''<div class="section ov-sec">
  <div class="sec-head">
    <span class="en">%s</span>
    <h2>%s</h2>
  </div>
  <div class="ov-grid">
%s
  </div>
</div>''' % (en_sub, title, cards)
            fname = 'about.html' if title == '成员介绍' else ('research.html' if title == '研究方向' else 'papers.html')
            html = page(fname, title, en_sub, body, ZH, scripts='js/home.js')
            open(fname, 'w').write(html)
            print('生成一级页', fname)

    overview_zh()

    for fname, (title, en_sub, about_body) in specs.items():
        if fname in ('about.html', 'research.html', 'papers.html'):
            continue
        if fname == 'project.html':
            body = project_box(ZH, full=True)
        else:
            body = body_fn[fname](ZH)
        html = page(fname, title, en_sub, body, ZH, scripts='js/home.js')
        open(fname, 'w').write(html)
        print('生成', fname)

    # 英文版（en/ 子目录：body 内相对资源加 ../ 前缀）
    def _en(html):
        return (html.replace('href="images/', 'href="../images/')
                    .replace('src="images/', 'src="../images/')
                    .replace('href="reports/', 'href="../reports/')
                    .replace('src="videos/', 'src="../videos/')
                    .replace('url(images/', 'url(../images/'))
    # ---- 英文版二级独立页面 ----
    def sub_pages_en():
        pages = []
        pages.append(('about-group.html', 'About the Group', 'ABOUT THE GROUP',
                      with_subnav('about', ABOUT_BODY['en'], EN)))
        pages.append(('about-chai.html', 'Prof. Fei Chai', 'PROF. FEI CHAI',
                      with_subnav('about', pi_detail_html(PI_EN, EN), EN)))
        pages.append(('papers-journal.html', 'Journal Papers', 'JOURNAL PAPERS',
                      with_subnav('papers', '<div class="section" id="journal">' + paper_timeline(PAPERS, EN) + '</div>', EN)))
        pages.append(('papers-digital-twin.html', 'Digital Twin', 'DIGITAL TWIN',
                      with_subnav('papers', '<div class="section" id="digital-twin">' + project_box(EN, full=True) + '</div>', EN)))
        pages.append(('papers-data.html', 'Research Data', 'RESEARCH DATA',
                      with_subnav('papers', '''<div class="section" id="data">
  <div class="sec-head"><span class="en">RESEARCH DATA</span><h2>Research Data</h2></div>
  <div class="ov-desc"><p>BGC-Argo float observations in the western North Pacific and the South China Sea; CESM-CoSiNE simulation outputs (data sharing under preparation).</p></div>
</div>''', EN)))
        pages.append(('papers-model.html', 'Numerical Models', 'NUMERICAL MODELS',
                      with_subnav('papers', '<div class="section" id="model">' + project_box(EN, full=True) + '</div>', EN)))
        for i in range(6):
            aid = 'r%d' % i
            num = '%02d' % (i + 1)
            title, desc = RESEARCH_ITEMS_EN[i]
            pages.append(('research-%s.html' % aid, title, 'RESEARCH AREA %s' % num,
                          with_subnav('research', '''<div class="section" id="%s">
  <div class="sec-head"><span class="en">%s · RESEARCH AREA</span><h2>%s</h2></div>
  <div class="ov-desc"><p>%s</p></div>
</div>''' % (aid, num, title, desc), EN)))
        pages.append(('research-project.html', 'CESM-CoSiNE Project', 'CESM-CoSiNE PROJECT',
                      with_subnav('research', '<div class="section" id="project">' + project_box(EN, full=True) + '</div>', EN)))
        for fname, title, en_sub, body in pages:
            html = _en(page(fname, title, en_sub, body, EN, scripts='../js/home.js'))
            open('en/' + fname, 'w').write(html)
            print('生成二级页 en/' + fname)

    # ---- 英文一级总览页 ----
    def overview_en():
        groups = [
            ('Members', 'GROUP OVERVIEW', [
                ('About the Group', 'Overview of the group research and recruitment.', 'about-group.html'),
                ('Prof. Fei Chai', 'Profile: career, research interests, selected publications.', 'about-chai.html'),
                ('Members', 'Faculty, postdocs, and graduate students.', 'members.html'),
            ]),
            ('Research', 'RESEARCH AREAS', [
                ('Ecosystem & Biogeochemical Modeling', RESEARCH_ITEMS_EN[0][1], 'research-r0.html'),
                ('Carbon Cycle & Climate Feedbacks', RESEARCH_ITEMS_EN[1][1], 'research-r1.html'),
                ('Submesoscale Processes', RESEARCH_ITEMS_EN[2][1], 'research-r2.html'),
                ('Paleoclimate Modeling', RESEARCH_ITEMS_EN[3][1], 'research-r3.html'),
                ('Ocean Digital Twin', RESEARCH_ITEMS_EN[4][1], 'research-r4.html'),
                ('Observation\u2013Model Integration', RESEARCH_ITEMS_EN[5][1], 'research-r5.html'),
                ('CESM-CoSiNE Project', 'An ocean ecosystem-biogeochemistry module embedded in CESM.', 'research-project.html'),
            ]),
            ('Academic Papers', 'ACADEMIC PAPERS', [
                ('Journal Papers', 'Peer-reviewed journal publications of the group.', 'papers-journal.html'),
                ('Digital Twin', 'Ocean digital twin framework and applications.', 'papers-digital-twin.html'),
                ('Research Data', 'BGC-Argo observations and model outputs.', 'papers-data.html'),
                ('Numerical Models', 'CESM-CoSiNE model and reports.', 'papers-model.html'),
            ]),
        ]
        for title, en_sub, items in groups:
            cards = '\n'.join(
                '''      <a class="ov-card" href="%s">
        <span class="ov-go">%s →</span>
        <h3>%s</h3>
        <p>%s</p>
      </a>''' % (link, 'Enter', t, d) for t, d, link in items)
            body = '''<div class="section ov-sec">
  <div class="sec-head">
    <span class="en">%s</span>
    <h2>%s</h2>
  </div>
  <div class="ov-grid">
%s
  </div>
</div>''' % (en_sub, title, cards)
            fname = 'about.html' if title == 'Members' else ('research.html' if title == 'Research' else 'papers.html')
            html = _en(page(fname, title, en_sub, body, EN, scripts='../js/home.js'))
            open('en/' + fname, 'w').write(html)
            print('生成一级页 en/' + fname)

    overview_en()

    sub_pages_en()

    for fname, (title, en_sub, about_body) in specs_en.items():
        if fname in ('about.html', 'research.html', 'papers.html'):
            continue
        if fname == 'project.html':
            body = project_box(EN, full=True)
        else:
            body = body_fn[fname](EN)
        html = _en(page(fname, title, en_sub, body, EN, scripts='../js/home.js'))
        open('en/' + fname, 'w').write(html)
        print('生成 en/' + fname)

    # 成员页
    open('members.html', 'w').write(page('members.html', '成员介绍', 'GROUP MEMBERS', members_body(ZH), ZH, scripts='js/home.js'))
    open('en/members.html', 'w').write(_en(page('members.html', 'Members', 'GROUP MEMBERS', members_body(EN), EN, scripts='../js/home.js')))
    print('生成 members.html / en/members.html')

    # 首页（无 page-banner，使用 home.js）
    open('index.html', 'w').write(page('index.html', '首页', 'HOME', home_body(ZH), ZH, banner=False, scripts='js/home.js'))
    open('en/index.html', 'w').write(_en(page('index.html', 'Home', 'HOME', home_body(EN), EN, banner=False, scripts='../js/home.js')))
    print('生成 index.html / en/index.html')

if __name__ == '__main__':
    main()
