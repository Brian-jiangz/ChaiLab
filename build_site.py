#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成课题组网站子页面（导航/页脚保持一致）"""
import re

NAV = [
    ('index.html', '首页'), ('about.html', '课题组简介'), ('members.html', '成员介绍'),
    ('research.html', '研究方向'), ('project.html', 'CESM-CoSiNE'),
    ('papers.html', '发表论文'), ('news.html', '新闻动态'), ('links.html', '相关链接'),
]

def nav(active):
    def _link(f, t):
        cls = ' class="active"' if f == active else ''
        return f'        <li><a href="{f}"{cls}>{t}</a></li>'
    lis = '\n'.join(_link(f, t) for f, t in NAV)
    return f'''<!-- 顶部导航 -->
<header class="g-head">
  <div class="inner">
    <a href="index.html" class="logo">
      <img src="images/xmu_logo.png" alt="厦门大学" class="logo-xmu">
      <img src="images/mel_logo.svg" alt="海洋生物地球化学全国重点实验室" class="logo-mel">
      <span class="logo-divider"></span>
      <div class="txt">
        <strong>柴扉教授课题组</strong>
        <span>Chai Group · Xiamen University</span>
      </div>
    </a>
    <button class="nav-toggle" onclick="document.querySelector('.g-nav').classList.toggle('open')">☰</button>
    <nav class="g-nav">
      <ul>
{lis}
      </ul>
    </nav>
  </div>
</header>'''

FOOTER = '''<!-- 页脚 -->
<footer class="footer">
  <div class="inner">
    <div>
      <h5>柴扉教授课题组</h5>
      <p>海洋生物地球化学全国重点实验室（厦门大学）</p>
      <p>厦门大学翔安校区周隆泉楼</p>
    </div>
    <div>
      <h5>联系方式</h5>
      <p>邮箱：fchai@xmu.edu.cn</p>
      <p>邮编：361102</p>
    </div>
    <div>
      <h5>快速导航</h5>
      <p><a href="about.html" style="color:rgba(255,255,255,.75)">课题组简介</a> · <a href="members.html" style="color:rgba(255,255,255,.75)">成员介绍</a> · <a href="project.html" style="color:rgba(255,255,255,.75)">CESM-CoSiNE</a></p>
    </div>
    <div class="copy">© 2026 柴扉教授课题组 · 厦门大学海洋生物地球化学全国重点实验室</div>
  </div>
</footer>'''

def page(fname, title, en, body, extra=''):
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | 柴扉教授课题组 · 厦门大学</title>
<link rel="stylesheet" href="css/style.css">
</head>
<body>

{nav(fname)}

<div class="page-banner">
  <h1>{title}</h1>
  <p>{en}</p>
</div>

{body}
{FOOTER}
{extra}
</body>
</html>
'''

pages = {}

# ============ 课题组简介 ============
pages['about.html'] = page('about.html', '课题组简介', 'ABOUT THE GROUP', '''
<div class="section">
  <div class="intro-grid">
    <div class="intro-card">
      <p>本课题组依托厦门大学海洋生物地球化学全国重点实验室，长期从事海洋物理—生态—生物地球化学耦合研究，聚焦海洋碳循环、营养盐循环与生态系统对气候变化的响应与反馈。</p>
      <p>课题组以自主发展的 CESM-CoSiNE 海洋生态系统—生物地球化学模块为核心工具，结合观测资料与数值模拟，研究北太平洋、南海及全球大洋中浮游生态系统与碳循环的调控机制，并拓展至古气候重建与海洋数字孪生等前沿方向。</p>
      <p>课题组面向全球招聘博士后、博士生与硕士生，欢迎对海洋生物地球化学、气候模拟与计算海洋学感兴趣的同学加入。</p>
      <p style="margin-top:20px"><a class="btn btn-red" href="members.html">了解课题组成员 →</a></p>
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
</div>''')

# ============ 成员介绍 ============
members = '''<div class="section">
  <div class="sec-head">
    <h2>教授 / 研究员</h2>
  </div>
  <div class="members">'''
for name, role, dir_, email in [
    ('柴扉', '讲席教授 / PI', '海洋生物地球化学、物理—生态耦合、气候模拟', 'fchai@xmu.edu.cn'),
    ('（待补充）', '副教授 / 研究员', '成员信息整理中……', '—'),
]:
    members += f'''
    <div class="member">
      <div class="m-avatar">{name[0]}</div>
      <h4>{name}</h4>
      <div class="role">{role}</div>
      <div class="dir">{dir_}</div>
      <div class="email">{email}</div>
    </div>'''
members += '''</div>
  <div class="sec-head" style="margin-top:56px">
    <h2>博士后</h2>
  </div>
  <div class="members">'''
for name, role, dir_, email in [
    ('（待补充）', '博士后', '成员信息整理中……', '—'),
]:
    members += f'''
    <div class="member">
      <div class="m-avatar">{name[0]}</div>
      <h4>{name}</h4>
      <div class="role">{role}</div>
      <div class="dir">{dir_}</div>
      <div class="email">{email}</div>
    </div>'''
members += '''</div>
  <div class="sec-head" style="margin-top:56px">
    <h2>研究生</h2>
  </div>
  <div class="members">'''
for name, role, dir_, email in [
    ('（待补充）', '博士研究生', '成员信息整理中……', '—'),
    ('（待补充）', '博士研究生', '成员信息整理中……', '—'),
    ('（待补充）', '硕士研究生', '成员信息整理中……', '—'),
    ('（待补充）', '硕士研究生', '成员信息整理中……', '—'),
]:
    members += f'''
    <div class="member">
      <div class="m-avatar">{name[0]}</div>
      <h4>{name}</h4>
      <div class="role">{role}</div>
      <div class="dir">{dir_}</div>
      <div class="email">{email}</div>
    </div>'''
members += '''</div>
</div>'''
pages['members.html'] = page('members.html', '成员介绍', 'GROUP MEMBERS', members)

# ============ 研究方向 ============
pages['research.html'] = page('research.html', '研究方向', 'RESEARCH AREAS', '''
<div class="section">
  <div class="research">
    <div class="rtile">
      <div class="icon">🌊</div>
      <h3>海洋生态系统与生物地球化学模拟</h3>
      <p>发展并改进 CESM-CoSiNE 海洋生态系统—生物地球化学耦合模式，模拟浮游植物、营养盐与碳循环的时空演变。</p>
    </div>
    <div class="rtile">
      <div class="icon">🌍</div>
      <h3>海洋碳循环与气候反馈</h3>
      <p>研究海洋对大气 CO₂ 的调控作用、生物泵效率及海洋碳循环对未来气候变化的响应。</p>
    </div>
    <div class="rtile">
      <div class="icon">🦠</div>
      <h3>海洋次中尺度过程与生态效应</h3>
      <p>探索次中尺度物理过程（锋面、涡旋）对浮游生态系统与碳输出通量的调控机制。</p>
    </div>
    <div class="rtile">
      <div class="icon">⏳</div>
      <h3>古气候与古海洋模拟</h3>
      <p>利用地球系统模式开展末次间冰期等关键时期古气候模拟，理解碳循环的长期演化。</p>
    </div>
    <div class="rtile">
      <div class="icon">🖥️</div>
      <h3>海洋数字孪生</h3>
      <p>构建海洋数字孪生系统，赋能蓝色经济创新，服务海洋观测—模拟—预测一体化。</p>
    </div>
    <div class="rtile">
      <div class="icon">📡</div>
      <h3>观测—模拟融合</h3>
      <p>结合现场观测、卫星遥感与数值模式，量化评估模式不确定性，改进生态模型参数化。</p>
    </div>
  </div>
</div>''')

# ============ CESM-CoSiNE ============
pages['project.html'] = page('project.html', 'CESM-CoSiNE 项目', 'CESM-CoSiNE PROJECT', '''
<div class="section">
  <div class="project-box">
    <div class="project-hero">
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
        <a class="btn btn-red" href="reports/CESM_CoSiNE16_Nature_style_draft_CN.html" target="_blank">📄 阅读项目报告（Nature 风格）</a>
        <a class="btn btn-outline" href="reports/CESM_CoSiNE16_v2_Process_Manual.html" target="_blank">🔧 V2 耦合说明书</a>
      </div>
    </div>
  </div>
</div>''')

# ============ 发表论文 ============
pages['papers.html'] = page('papers.html', '发表论文', 'PUBLICATIONS', '''
<div class="section">
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
        <div class="j"><a href="https://coeoa.xmu.edu.cn/t/CF/" target="_blank" style="color:var(--blue)">coeoa.xmu.edu.cn/t/CF/ →</a></div>
      </div>
    </li>
  </ul>
</div>''')

# ============ 新闻动态 ============
pages['news.html'] = page('news.html', '新闻动态', 'NEWS & UPDATES', '''
<div class="section">
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
</div>''')

# ============ 相关链接 ============
pages['links.html'] = page('links.html', '相关链接', 'RELATED LINKS', '''
<div class="section">
  <div class="links">
    <a class="link-card" href="#" onclick="return false" title="链接待补充">
      <div class="icon">🌏</div>
      <h4>厦门大学古气候数字地球系统</h4>
      <p>古气候模拟与数字地球平台（链接待补充）</p>
      <div class="ext">敬请期待 →</div>
    </a>
    <a class="link-card" href="https://coeoa.xmu.edu.cn/t/CF/" target="_blank">
      <div class="icon">👤</div>
      <h4>柴扉教授个人主页</h4>
      <p>厦门大学海洋生物地球化学全国重点实验室</p>
      <div class="ext">coeoa.xmu.edu.cn →</div>
    </a>
    <a class="link-card" href="https://meli.xmu.edu.cn/" target="_blank">
      <div class="icon">🔬</div>
      <h4>海洋生物地球化学全国重点实验室</h4>
      <p>厦门大学海洋生物地球化学全国重点实验室官网</p>
      <div class="ext">meli.xmu.edu.cn →</div>
    </a>
  </div>
</div>''')

for fname, html in pages.items():
    with open(fname, 'w') as f:
        f.write(html)
    print('生成', fname)
