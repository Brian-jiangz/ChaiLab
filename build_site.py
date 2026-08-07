#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成课题组网站（中英双语，多页面结构）"""

ZH, EN = 'zh', 'en'

NAV_ZH = [
    ('index.html', '首页'), ('about.html', '课题组简介'), ('members.html', '成员介绍'),
    ('research.html', '研究方向'), ('project.html', 'CESM-CoSiNE'),
    ('papers.html', '发表论文'), ('news.html', '新闻动态'), ('links.html', '相关链接'),
]
NAV_EN = [
    ('index.html', 'Home'), ('about.html', 'About'), ('members.html', 'Members'),
    ('research.html', 'Research'), ('project.html', 'CESM-CoSiNE'),
    ('papers.html', 'Publications'), ('news.html', 'News'), ('links.html', 'Links'),
]

TXT = {
    'zh': {
        'site_name': '柴扉教授课题组',
        'site_sub': 'Chai Group · Xiamen University',
        'lang_switch': 'English',
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
        'footer_copy': '© 2026 柴扉教授课题组 · 厦门大学海洋生物地球化学全国重点实验室',
    },
    'en': {
        'site_name': 'Chai Group',
        'site_sub': 'Xiamen University · MEL',
        'lang_switch': '中文',
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
        'footer_copy': '© 2026 Chai Group · State Key Laboratory of Marine Environmental Science, Xiamen University',
    },
}

def nav(active, lang):
    items = NAV_EN if lang == EN else NAV_ZH
    t = TXT[lang]
    def _link(f, name):
        cls = ' class="active"' if f == active else ''
        return f'        <li><a href="{f}"{cls}>{name}</a></li>'
    lis = '\n'.join(_link(f, name) for f, name in items)
    return f'''<!-- 顶部导航 -->
<header class="g-head">
  <div class="inner">
    <a href="index.html" class="logo">
      <img src="images/xmu_logo.png" alt="Xiamen University" class="logo-xmu">
      <img src="images/mel_logo.svg" alt="MEL" class="logo-mel">
      <span class="logo-divider"></span>
      <div class="txt">
        <strong>{t['site_name']}</strong>
        <span>{t['site_sub']}</span>
      </div>
    </a>
    <nav class="g-nav">
      <ul>
{lis}
      </ul>
    </nav>
    <a class="lang-switch" href="{t['lang_url']}">{t['lang_switch']}</a>
    <button class="nav-toggle" onclick="document.querySelector('.g-nav').classList.toggle('open')">☰</button>
  </div>
</header>'''

def footer(lang):
    t = TXT[lang]
    return f'''<!-- 页脚 -->
<footer class="footer">
  <div class="inner">
    <div>
      <h5>{t['footer_name']}</h5>
      <p>{t['footer_org']}</p>
      <p>{t['footer_addr']}</p>
    </div>
    <div>
      <h5>{t['footer_contact']}</h5>
      <p>{t['footer_email']}</p>
      <p>{t['footer_zip']}</p>
    </div>
    <div>
      <h5>{t['footer_nav']}</h5>
      <p><a href="about.html">{t['footer_about']}</a> · <a href="members.html">{t['footer_members']}</a> · <a href="project.html">{t['footer_project']}</a></p>
    </div>
    <div class="copy">{t['footer_copy']}</div>
  </div>
</footer>'''

def page(fname, title, en_sub, body, lang, extra=''):
    t = TXT[lang]
    sitename = t['site_name']
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="images/favicon.svg" type="image/svg+xml">
<title>{title} | {sitename} · Xiamen University</title>
<link rel="stylesheet" href="css/style.css">
</head>
<body>

{nav(fname, lang)}

<div class="page-banner">
  <h1>{title}</h1>
  <p>{en_sub}</p>
</div>

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
      <p>课题组面向全球招聘博士后、博士生与硕士生，欢迎对海洋生物地球化学、气候模拟与计算海洋学感兴趣的同学加入。</p>
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
      <p>The group welcomes postdoctoral researchers and PhD/Master's students from around the world with interests in marine biogeochemistry, climate modeling, and computational oceanography.</p>
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
    if lang == EN:
        items = [
            (SVG_WAVE, 'Marine Ecosystem and Biogeochemical Modeling', 'Development and improvement of the CESM-CoSiNE coupled marine ecosystem\u2013biogeochemistry module to simulate the spatiotemporal evolution of phytoplankton, nutrients, and the carbon cycle.'),
            (SVG_GLOBE, 'Marine Carbon Cycle and Climate Feedbacks', 'Quantifying the ocean\u2019s role in regulating atmospheric CO\u2082, biological pump efficiency, and the response of the marine carbon cycle to future climate change.'),
            (SVG_BIO, 'Submesoscale Processes and Ecological Effects', 'Exploring how submesoscale physical processes (fronts, eddies) regulate planktonic ecosystems and carbon export fluxes.'),
            (SVG_TIME, 'Paleoclimate and Paleoceanography', 'Earth system modeling of key periods such as the Last Interglacial to understand the long-term evolution of the carbon cycle.'),
            (SVG_DIGI, 'Ocean Digital Twin', 'Building ocean digital twin systems to empower blue-economy innovation and integrated ocean observation\u2013simulation\u2013prediction.'),
            (SVG_SAT, 'Observation\u2013Model Integration', 'Combining in-situ observations, satellite remote sensing, and numerical models to quantify uncertainty and improve ecosystem model parameterizations.'),
        ]
    else:
        items = [
            (SVG_WAVE, '海洋生态系统与生物地球化学模拟', '发展并改进 CESM-CoSiNE 海洋生态系统—生物地球化学耦合模式，模拟浮游植物、营养盐与碳循环的时空演变。'),
            (SVG_GLOBE, '海洋碳循环与气候反馈', '研究海洋对大气 CO₂ 的调控作用、生物泵效率及海洋碳循环对未来气候变化的响应。'),
            (SVG_BIO, '海洋次中尺度过程与生态效应', '探索次中尺度物理过程（锋面、涡旋）对浮游生态系统与碳输出通量的调控机制。'),
            (SVG_TIME, '古气候与古海洋模拟', '利用地球系统模式开展末次间冰期等关键时期古气候模拟，理解碳循环的长期演化。'),
            (SVG_DIGI, '海洋数字孪生', '构建海洋数字孪生系统，赋能蓝色经济创新，服务海洋观测—模拟—预测一体化。'),
            (SVG_SAT, '观测—模拟融合', '结合现场观测、卫星遥感与数值模式，量化评估模式不确定性，改进生态模型参数化。'),
        ]
    tiles = '\n'.join(
        f'    <div class="rtile">\n      <div class="icon">{icon}</div>\n      <h3>{title}</h3>\n      <p>{desc}</p>\n    </div>'
        for icon, title, desc in items)
    return f'<div class="section">\n  <div class="research">\n{tiles}\n  </div>\n</div>'

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
        return '''<div class="section">
  <div class="news-grid">
    <div class="news">
      <span class="date">FEB 2026</span>
      <h4>Prof. Chai\u2019s team reveals ocean digital twins as a new engine for blue-economy innovation</h4>
      <p>The team systematically reviewed the core architecture of ocean digital twins, analyzed key application scenarios in blue-economy development, and provided forward-looking perspectives on challenges and prospects.</p>
    </div>
    <div class="news">
      <span class="date">NOV 2025</span>
      <h4>Lujiang Ocean Symposium concludes successfully</h4>
      <p>The ocean symposium co-hosted by Lujiang Innovation Laboratory and the State Key Laboratory of Marine Environmental Science (XMU) was held successfully.</p>
    </div>
    <div class="news">
      <span class="date">UPDATING</span>
      <h4>Group news continuously updated</h4>
      <p>Stay tuned for the latest research progress, recruitment, and academic exchange activities.</p>
    </div>
  </div>
</div>'''
    return '''<div class="section">
  <div class="news-grid">
    <div class="news">
      <span class="date">2026-02</span>
      <h4>柴扉教授团队揭示海洋数字孪生是赋能蓝色经济创新发展的新引擎</h4>
      <p>团队系统梳理海洋数字孪生核心架构，解析其在蓝色经济发展中的关键应用场景，并对该领域挑战与前景作出前瞻性研判。</p>
    </div>
    <div class="news">
      <span class="date">2025-11</span>
      <h4>鹭江海洋研讨会圆满落幕</h4>
      <p>由鹭江创新实验室与海洋生物地球化学全国重点实验室（厦门大学）联合主办的海洋研讨会成功举办。</p>
    </div>
    <div class="news">
      <span class="date">待更新</span>
      <h4>课题组新闻持续更新中</h4>
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
    """首页（轮播 + 分区摘要）"""
    if lang == EN:
        slides = [
            ('Marine Biogeochemistry', 'Marine Biogeochemistry and Climate Modeling', 'Ocean Biogeochemistry and Climate Modeling', 'MARINE BIOGEOCHEMISTRY · ECOSYSTEM MODELING · PALEOCLIMATE'),
            ('Earth System Modeling', 'The CESM-CoSiNE Marine Ecosystem Model', 'From coupled physics\u2013chemistry\u2013biology to understanding the marine carbon cycle', 'EMBEDDING CoSiNE IN THE COMMUNITY EARTH SYSTEM MODEL'),
            ('Paleoclimate & Digital Earth', 'Paleoclimate and the Digital Earth', 'Reconstruct the past, simulate the present, foresee the future', 'FROM PALEOCLIMATE RECONSTRUCTION TO DIGITAL EARTH'),
        ]
        about = ('About the Group', '''<p>Affiliated with the State Key Laboratory of Marine Environmental Science (MEL) at Xiamen University, our group studies coupled physical\u2013ecological\u2013biogeochemical oceanography, with a focus on the marine carbon cycle, nutrient cycles, and the response of marine ecosystems to climate change.</p>
      <p>Centered on the in-house CESM-CoSiNE module and combining observations with numerical simulation, we investigate planktonic ecosystems and the carbon cycle from the North Pacific to the global ocean, extending to paleoclimate reconstruction and ocean digital twins.</p>
      <p>The group welcomes postdoctoral researchers and PhD/Master's students with interests in marine biogeochemistry, climate modeling, and computational oceanography.</p>''')
        pi = ('Prof. Fei Chai', 'Tang Shifeng Chair Professor in Marine Sciences · PI', [
            ('Unit', 'State Key Laboratory of Marine Environmental Science (MEL), XMU'),
            ('Office', 'Zhoulongquan Building, Xiang\u2019an Campus, XMU'),
            ('Email', 'fchai@xmu.edu.cn'),
            ('Ph.D.', 'Biological Oceanography, Duke University (1991\u20131995)'),
            ('Career', 'Former Professor (tenured), University of Maine'),
        ])
        research = [
            ('Marine Ecosystem and Biogeochemical Modeling', 'Development and improvement of the CESM-CoSiNE coupled module to simulate phytoplankton, nutrients, and the carbon cycle.'),
            ('Marine Carbon Cycle and Climate Feedbacks', 'Quantifying the ocean\u2019s role in regulating atmospheric CO\u2082 and the response of the carbon cycle to climate change.'),
            ('Submesoscale Processes and Ecological Effects', 'How submesoscale physics (fronts, eddies) regulates planktonic ecosystems and carbon export.'),
            ('Paleoclimate and Paleoceanography', 'Earth system modeling of key periods such as the Last Interglacial.'),
            ('Ocean Digital Twin', 'Building ocean digital twins to empower blue-economy innovation.'),
            ('Observation\u2013Model Integration', 'Combining observations and models to quantify uncertainty and improve parameterizations.'),
        ]
        news = [
            ('FEB 2026', 'Prof. Chai\u2019s team reveals ocean digital twins as a new engine for blue-economy innovation', 'The team systematically reviewed the architecture of ocean digital twins and analyzed key application scenarios in blue-economy development.'),
            ('NOV 2025', 'Lujiang Ocean Symposium concludes successfully', 'The symposium co-hosted by Lujiang Innovation Laboratory and MEL (XMU) was held successfully.'),
            ('UPDATING', 'Group news continuously updated', 'Stay tuned for the latest research progress and recruitment.'),
        ]
    else:
        slides = [
            ('Marine Biogeochemistry', '海洋生物地球化学与气候模拟', 'Ocean Biogeochemistry and Climate Modeling', 'MARINE BIOGEOCHEMISTRY · ECOSYSTEM MODELING · PALEOCLIMATE'),
            ('Earth System Modeling', 'CESM-CoSiNE 海洋生态系统模式', '从物理—化学—生物耦合出发，理解海洋碳循环', 'EMBEDDING CoSiNE IN THE COMMUNITY EARTH SYSTEM MODEL'),
            ('Paleoclimate & Digital Earth', '古气候与数字地球', '重建过去，模拟现在，预见未来', 'FROM PALEOCLIMATE RECONSTRUCTION TO DIGITAL EARTH'),
        ]
        about = ('课题组简介', '''<p>本课题组依托厦门大学海洋生物地球化学全国重点实验室，长期从事海洋物理—生态—生物地球化学耦合研究，聚焦海洋碳循环、营养盐循环与生态系统对气候变化的响应与反馈。</p>
      <p>课题组以自主发展的 CESM-CoSiNE 海洋生态系统—生物地球化学模块为核心工具，结合观测资料与数值模拟，研究北太平洋、南海及全球大洋中浮游生态系统与碳循环的调控机制，并拓展至古气候重建与海洋数字孪生等前沿方向。</p>
      <p>课题组面向全球招聘博士后、博士生与硕士生，欢迎对海洋生物地球化学、气候模拟与计算海洋学感兴趣的同学加入。</p>''')
        pi = ('柴扉 教授', '"唐世凤"海洋学科讲席教授 · PI', [
            ('单位', '海洋生物地球化学全国重点实验室（厦门大学）'),
            ('地址', '厦门大学翔安校区周隆泉楼'),
            ('邮箱', 'fchai@xmu.edu.cn'),
            ('学历', '杜克大学 生物海洋学博士（1991–1995）'),
            ('经历', '曾任美国缅因大学海洋学院教授（终身教职）'),
        ])
        research = [
            ('海洋生态系统与生物地球化学模拟', '发展并改进 CESM-CoSiNE 海洋生态系统—生物地球化学耦合模式，模拟浮游植物、营养盐与碳循环的时空演变。'),
            ('海洋碳循环与气候反馈', '研究海洋对大气 CO₂ 的调控作用、生物泵效率及海洋碳循环对未来气候变化的响应。'),
            ('海洋次中尺度过程与生态效应', '探索次中尺度物理过程（锋面、涡旋）对浮游生态系统与碳输出通量的调控机制。'),
            ('古气候与古海洋模拟', '利用地球系统模式开展末次间冰期等关键时期古气候模拟，理解碳循环的长期演化。'),
            ('海洋数字孪生', '构建海洋数字孪生系统，赋能蓝色经济创新，服务海洋观测—模拟—预测一体化。'),
            ('观测—模拟融合', '结合现场观测、卫星遥感与数值模式，量化评估模式不确定性，改进生态模型参数化。'),
        ]
        news = [
            ('2026-02', '柴扉教授团队揭示海洋数字孪生是赋能蓝色经济创新发展的新引擎', '团队系统梳理海洋数字孪生核心架构，解析其在蓝色经济发展中的关键应用场景，并对该领域挑战与前景作出前瞻性研判。'),
            ('2025-11', '鹭江海洋研讨会圆满落幕', '由鹭江创新实验室与海洋生物地球化学全国重点实验室（厦门大学）联合主办的海洋研讨会成功举办。'),
            ('待更新', '课题组新闻持续更新中', '欢迎关注课题组最新科研进展、招生与学术交流动态。'),
        ]

    svg_deco = '''      <svg class="bg-svg" viewBox="0 0 1440 520" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
        <g stroke="rgba(255,255,255,.05)" fill="none">
          <path d="M-40,420 C200,360 400,470 640,410 S1080,350 1480,420"/>
          <path d="M-40,455 C200,395 400,505 640,445 S1080,385 1480,455"/>
          <path d="M-40,490 C200,430 400,540 640,480 S1080,420 1480,490"/>
        </g>
        <g stroke="rgba(255,255,255,.03)">
          <line x1="0" y1="130" x2="1440" y2="130"/><line x1="0" y1="260" x2="1440" y2="260"/>
          <line x1="360" y1="0" x2="360" y2="520"/><line x1="720" y1="0" x2="720" y2="520"/><line x1="1080" y1="0" x2="1080" y2="520"/>
        </g>
      </svg>'''

    slide_html = []
    for i, (kicker, h1, p, en) in enumerate(slides):
        slide_html.append(f'''    <div class="slide s{i+1}{' on' if i == 0 else ''}">
{svg_deco}
      <div class="inner-txt">
        <div class="kicker">{kicker}</div>
        <h1>{h1}</h1>
        <p>{p}</p>
        <p class="en">{en}</p>
      </div>
    </div>''')

    sec_head = lambda en_txt, zh_txt: f'''  <div class="sec-head">
    <span class="en">{en_txt}</span>
    <h2>{zh_txt}</h2>
  </div>'''

    about_title, about_paras = about
    pi_name, pi_title, pi_info = pi
    pi_lis = '\n'.join(f'        <li><b>{k}：</b>{v}</li>' if lang == ZH else f'        <li><b>{k}:</b> {v}</li>' for k, v in pi_info)

    rtiles = '\n'.join(
        f'''    <div class="rtile">
      <div class="icon">{ic}</div>
      <h3>{t}</h3>
      <p>{d}</p>
    </div>''' for (ic, t, d) in [
        (SVG_WAVE, research[0][0], research[0][1]),
        (SVG_GLOBE, research[1][0], research[1][1]),
        (SVG_BIO, research[2][0], research[2][1]),
        (SVG_TIME, research[3][0], research[3][1]),
        (SVG_DIGI, research[4][0], research[4][1]),
        (SVG_SAT, research[5][0], research[5][1]),
    ])

    news_cards = '\n'.join(
        f'''    <div class="news">
      <span class="date">{d}</span>
      <h4>{t}</h4>
      <p>{c}</p>
    </div>''' for d, t, c in news)

    if lang == EN:
        more = {'about': 'Learn more →', 'research': 'More about our research →', 'project': 'View Project Details →', 'news': 'More news →'}
        secs = {
            'about': ('ABOUT THE GROUP', 'About the Group'),
            'research': ('RESEARCH AREAS', 'Research Areas'),
            'project': ('CESM-CoSiNE PROJECT', 'CESM-CoSiNE Project'),
            'news': ('NEWS & UPDATES', 'News & Updates'),
        }
        lang_kw = 'EN'
    else:
        more = {'about': '了解课题组 →', 'research': '了解更多 →', 'project': '查看项目详情 →', 'news': '更多新闻 →'}
        secs = {
            'about': ('ABOUT THE GROUP', '课题组简介'),
            'research': ('RESEARCH AREAS', '研究方向'),
            'project': ('CESM-CoSiNE PROJECT', 'CESM-CoSiNE 项目'),
            'news': ('NEWS & UPDATES', '新闻动态'),
        }
        lang_kw = 'ZH'

    if lang == EN:
        proj_title = 'CESM-CoSiNE: An Ocean Ecosystem\u2013Biogeochemistry Module Embedded in CESM'
        proj_desc = ('CoSiNE (Carbon, Silicon, Nitrogen Ecosystem) is developed and maintained by our group '
                     'and has been embedded in the CESM Earth System Model (POP2 ocean component) to study '
                     'planktonic ecosystems and the marine carbon cycle at global and regional scales.')
    else:
        proj_title = 'CESM-CoSiNE：嵌入 CESM 的海洋生态—生物地球化学模块'
        proj_desc = ('CoSiNE（Carbon, Silicon, Nitrogen Ecosystem）由本课题组维护发展，已嵌入 CESM 地球系统模式'
                     '（POP2 海洋分量），用于研究浮游生态系统与海洋碳循环在全球及区域尺度上的演变。')

    body = f'''<!-- 轮播 -->
<div class="banner">
  <div class="slides">
{chr(10).join(slide_html)}
  </div>
  <div class="dots">
    <span class="on"></span>
    <span></span>
    <span></span>
  </div>
</div>

<!-- 课题组简介 -->
<div class="section" id="intro">
  <div class="sec-head">
    <span class="en">{secs['about'][0]}</span>
    <h2>{secs['about'][1]}</h2>
  </div>
  <div class="intro-grid">
    <div class="intro-card">
      {about_paras}
      <p style="margin-top:28px"><a class="btn btn-solid" href="about.html">{more['about']}</a></p>
    </div>
    <div class="pi-card">
      <div class="pi-avatar"><img src="images/chai_fei.jpg" alt=""></div>
      <h3>{pi_name}</h3>
      <div class="title">{pi_title}</div>
      <ul class="info">
{pi_lis}
      </ul>
    </div>
  </div>
</div>

<!-- 研究方向 -->
<div class="section" id="research">
  <div class="sec-head">
    <span class="en">{secs['research'][0]}</span>
    <h2>{secs['research'][1]}</h2>
  </div>
  <div class="research">
{rtiles}
  </div>
  <p style="text-align:center;margin-top:40px"><a class="btn btn-line" href="research.html">{more['research']}</a></p>
</div>

<!-- CESM-CoSiNE 项目 -->
<div class="section" id="project">
  <div class="sec-head">
    <span class="en">{secs['project'][0]}</span>
    <h2>{secs['project'][1]}</h2>
  </div>
  <div class="project-box">
    <div class="project-hero">
      <div class="kicker">CESM-CoSiNE</div>
      <h3>{proj_title}</h3>
      <p>{proj_desc}</p>
    </div>
    <div class="project-body">
      <div class="project-links" style="margin-top:0">
        <a class="btn btn-solid" href="project.html">{more['project']}</a>
      </div>
    </div>
  </div>
</div>

<!-- 新闻动态 -->
<div class="section" id="news">
  <div class="sec-head">
    <span class="en">{secs['news'][0]}</span>
    <h2>{secs['news'][1]}</h2>
  </div>
  <div class="news-grid">
{news_cards}
  </div>
  <p style="text-align:center;margin-top:40px"><a class="btn btn-line" href="news.html">{more['news']}</a></p>
</div>'''

    js = '''
<script>
var cur = 0;
var timer = null;
var slides = document.querySelectorAll('.slide');
var dots = document.querySelectorAll('.banner .dots span');

function goSlide(i) {
  cur = i;
  slides.forEach(function (s, k) { s.classList.toggle('on', k === i); });
  dots.forEach(function (d, k) { d.classList.toggle('on', k === i); });
}
function auto() {
  timer = setInterval(function () { goSlide((cur + 1) % slides.length); }, 5000);
}
goSlide(0);
auto();
</script>'''
    return body, js

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

    # 中文版
    import os
    os.makedirs('en', exist_ok=True)
    for fname, (title, en_sub, about_body) in specs.items():
        body = about_body['zh'] if fname == 'about.html' else body_fn[fname](ZH)
        html = page(fname, title, en_sub, body, ZH)
        open(fname, 'w').write(html)
        print('生成', fname)

    # 英文版
    for fname, (title, en_sub, about_body) in specs_en.items():
        body = about_body['en'] if fname == 'about.html' else body_fn[fname](EN)
        html = page(fname, title, en_sub, body, EN)
        open('en/' + fname, 'w').write(html)
        print('生成 en/' + fname)

    # 成员页
    open('members.html', 'w').write(page('members.html', '成员介绍', 'GROUP MEMBERS', members_body(ZH), ZH))
    open('en/members.html', 'w').write(page('members.html', 'Members', 'GROUP MEMBERS', members_body(EN), EN))
    print('生成 members.html / en/members.html')

    # 首页
    body_zh, js_zh = home_body(ZH)
    open('index.html', 'w').write(page('index.html', '首页', 'HOME', body_zh, ZH, extra=js_zh))
    body_en, js_en = home_body(EN)
    open('en/index.html', 'w').write(page('index.html', 'Home', 'HOME', body_en, EN, extra=js_en))
    print('生成 index.html / en/index.html')

if __name__ == '__main__':
    main()
