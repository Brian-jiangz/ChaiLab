#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""替换 emoji 图标为 SVG 线性图标"""
import re, sys

ICONS = {
    '🌊': '''<svg class="icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><path d="M2 12c1.8-2.5 3.6-2.5 5.4 0s3.6 2.5 5.4 0 3.6-2.5 5.4 0 3.6 2.5 5.4 0"/><path d="M2 17c1.8-2.5 3.6-2.5 5.4 0s3.6 2.5 5.4 0 3.6-2.5 5.4 0 3.6 2.5 5.4 0"/><path d="M2 7c1.8-2.5 3.6-2.5 5.4 0s3.6 2.5 5.4 0 3.6-2.5 5.4 0 3.6 2.5 5.4 0"/></svg>''',
    '🌍': '''<svg class="icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18a14 14 0 0 1 0-18"/></svg>''',
    '🦠': '''<svg class="icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><path d="M12 12m-4.5 0a4.5 4.5 0 1 0 9 0a4.5 4.5 0 1 0-9 0"/><path d="M12 12l6-5"/><path d="M12 12l-7-2"/><path d="M12 12l3 6"/><path d="M12 12l-4 5"/></svg>''',
    '⏳': '''<svg class="icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/><path d="M7 3.5C8.5 4.8 10.2 5.5 12 5.5s3.5-.7 5-2"/></svg>''',
    '🖥️': '''<svg class="icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><rect x="3" y="4" width="18" height="12" rx="1"/><path d="M8 20h8"/><path d="M12 16v4"/></svg>''',
    '📡': '''<svg class="icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><circle cx="12" cy="12" r="1.5" fill="currentColor"/><path d="M9 9a4.2 4.2 0 0 1 6 0"/><path d="M6.8 6.8a8 8 0 0 1 10.4 0"/><path d="M15 15a4.2 4.2 0 0 1-6 0"/><path d="M17.2 17.2a8 8 0 0 0-10.4 0"/></svg>''',
    '🌏': '''<svg class="icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18a14 14 0 0 1 0-18"/><path d="M5.5 6c1.6 1 3 2.4 3.9 4M18.5 6c-1.6 1-3 2.4-3.9 4"/></svg>''',
    '👤': '''<svg class="icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.6-6 8-6s6.5 2 8 6"/></svg>''',
    '🔬': '''<svg class="icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><path d="M10 2v6l-6.5 11A2.2 2.2 0 0 0 5.3 22h13.4a2.2 2.2 0 0 0 1.8-3L14 8V2"/><path d="M7.5 14h9"/><path d="M10 2h4"/></svg>''',
}

def replace_icons(text):
    for emoji, svg in ICONS.items():
        text = text.replace(emoji, svg)
    return text

if __name__ == '__main__':
    for fname in sys.argv[1:]:
        s = open(fname).read()
        s2 = replace_icons(s)
        if s2 != s:
            open(fname, 'w').write(s2)
            print('更新', fname)
