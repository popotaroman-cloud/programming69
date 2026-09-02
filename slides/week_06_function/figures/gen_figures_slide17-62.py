# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Circle
import base64, io

plt.rcParams['font.family'] = 'Tahoma'

PRIMARY = '#1a237e'
ACCENT = '#1565c0'
LIGHT = '#e3f2fd'
MUTED = '#546e7a'
CODEBG = '#1e272e'
CODEFG = '#dfe6e9'
GOOD = '#2e7d32'
BAD = '#c62828'
GOODLIGHT = '#e8f5e9'
BADLIGHT = '#ffebee'

results = {}

def save_b64(fig, key, path_png):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=170, bbox_inches='tight', facecolor='white')
    fig.savefig(path_png, dpi=170, bbox_inches='tight', facecolor='white')
    buf.seek(0)
    results[key] = base64.b64encode(buf.read()).decode('ascii')

def box(ax, xy, w, h, text, fc=LIGHT, ec=PRIMARY, tc=PRIMARY, fontsize=13, weight='bold', family='Tahoma', ls='-', lw=2):
    x, y = xy
    b = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.02,rounding_size=0.03', linewidth=lw, edgecolor=ec, facecolor=fc, linestyle=ls)
    ax.add_patch(b)
    if text:
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=fontsize, color=tc, weight=weight, family=family)
    return b

def arrow(ax, xy1, xy2, color=ACCENT, style='-|>', lw=2.2, connectionstyle='arc3,rad=0', mutation_scale=18, ls='-'):
    a = FancyArrowPatch(xy1, xy2, arrowstyle=style, color=color, lw=lw,
                         connectionstyle=connectionstyle, mutation_scale=mutation_scale, linestyle=ls)
    ax.add_patch(a)

# ============================================================
# Figure A — Slide 17: call stack, add(3, 5) -> params bound -> return 8
# ============================================================
fig, ax = plt.subplots(figsize=(11.5, 6.0))
ax.set_xlim(0, 11.5)
ax.set_ylim(0, 6.0)
ax.axis('off')

# caller frame (bottom)
box(ax, (0.6, 0.3), 4.6, 1.15, 'โปรแกรมหลัก (caller)\nresult1 = add(3, 5)', fc='#f5f5f5', ec=MUTED, tc='#333333', fontsize=12)

# callee frame (top) - the add() stack frame
box(ax, (0.6, 3.15), 4.6, 2.35, '', fc=LIGHT, ec=PRIMARY, lw=2.4)
ax.text(2.9, 5.15, 'add(3, 5)  — stack frame', ha='center', fontsize=13, color=PRIMARY, weight='bold', family='Tahoma')
box(ax, (0.95, 3.9), 1.75, 0.75, 'x = 3', fc='white', ec=ACCENT, tc=ACCENT, fontsize=12.5)
box(ax, (2.95, 3.9), 1.9, 0.75, 'y = 5', fc='white', ec=ACCENT, tc=ACCENT, fontsize=12.5)
ax.text(2.9, 3.45, 'return x + y', ha='center', fontsize=12, color=MUTED, family='Consolas')

# call arrow: caller -> callee (left side, going up)
arrow(ax, (1.15, 1.45), (1.15, 3.15), color=PRIMARY, lw=2.4, mutation_scale=20)
ax.text(0.35, 2.3, 'เรียก', ha='center', fontsize=11.5, color=PRIMARY, weight='bold', family='Tahoma', rotation=90)

# return arrow: callee -> caller (right side, going down), value 8 flows back
arrow(ax, (4.05, 3.15), (4.05, 1.45), color=ACCENT, lw=2.6, mutation_scale=20)
ax.text(4.85, 2.3, 'return 8', ha='center', fontsize=11.5, color=ACCENT, weight='bold', family='Tahoma', rotation=90)

# right side: what happens to the returned value
box(ax, (6.3, 0.55), 4.6, 0.9, 'result1 = 8', fc=ACCENT, ec=ACCENT, tc='white', fontsize=14, weight='bold', family='Consolas')
arrow(ax, (5.2, 1.0), (6.3, 1.0), color=ACCENT, lw=2.2, mutation_scale=18)

ax.text(8.6, 4.3, 'เมื่อ return ทำงาน:\nฟังก์ชันหยุดทันที\nส่งค่ากลับไปยัง\nจุดที่เรียกใช้', ha='center', fontsize=11.5,
        color=MUTED, family='Tahoma', style='italic')

save_b64(fig, 'slide17', r"E:\Temp\fig_slide17_callstack_return.png")
plt.close(fig)

# ============================================================
# Figure B — Slide 22: global scope box vs local scope box (no shared border)
# ============================================================
fig, ax = plt.subplots(figsize=(11.5, 5.6))
ax.set_xlim(0, 11.5)
ax.set_ylim(0, 5.6)
ax.axis('off')

# Global scope box (left, big)
box(ax, (0.4, 0.6), 4.6, 4.3, '', fc='#f5f5f5', ec=MUTED, lw=2.2, ls=(0, (6, 3)))
ax.text(2.7, 4.25, 'Global Scope\n(ทั้งโปรแกรม)', ha='center', fontsize=13.5, color=MUTED, weight='bold', family='Tahoma')
box(ax, (1.15, 2.5), 3.1, 0.95, 'count = 100', fc=LIGHT, ec=PRIMARY, tc=PRIMARY, fontsize=13.5)
ax.text(2.7, 1.7, 'อ่านได้จากทุกจุด\nแก้ไขต้องมี global', ha='center', fontsize=10.5, color=MUTED, family='Tahoma', style='italic')

# Local scope box (right, inside a function outline) - clearly separate, no shared border
box(ax, (6.5, 0.9), 4.6, 3.7, '', fc='white', ec=ACCENT, lw=2.2)
ax.text(8.8, 4.25, 'def some_function():', ha='center', fontsize=12.5, color=ACCENT, weight='bold', family='Consolas')
box(ax, (7.0, 2.2), 3.6, 1.5, '', fc=LIGHT, ec=PRIMARY, lw=1.8)
ax.text(8.8, 3.35, 'Local Scope', ha='center', fontsize=12, color=PRIMARY, weight='bold', family='Tahoma')
ax.text(8.8, 2.75, 'local_count = 0', ha='center', fontsize=13, color=PRIMARY, weight='bold', family='Consolas')
ax.text(8.8, 1.35, 'มีชีวิตอยู่เฉพาะ\nขณะฟังก์ชันทำงาน', ha='center', fontsize=10.5, color=MUTED, family='Tahoma', style='italic')

# gap note between the two — no shared border, explicitly separate
ax.text(5.65, 3.0, 'ไม่เชื่อมถึงกัน\nคนละตัวแปรกัน', ha='center', fontsize=10.5, color=BAD, weight='bold', family='Tahoma')
arrow(ax, (5.15, 3.5), (6.35, 3.9), color=BAD, lw=1.6, style='-', connectionstyle='arc3,rad=0.15')
arrow(ax, (6.35, 2.5), (5.15, 2.1), color=BAD, lw=1.6, style='-', connectionstyle='arc3,rad=0.15')

save_b64(fig, 'slide22', r"E:\Temp\fig_slide22_scope.png")
plt.close(fig)

# ============================================================
# Figure C — Slide 32: immutable vs mutable reference diagrams (before/after)
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.8))

# ---- Left: Immutable (int) ----
ax = axes[0]
ax.set_xlim(0, 6.4)
ax.set_ylim(0, 6.3)
ax.axis('off')
ax.set_xlim(0, 6.4)
ax.set_ylim(-0.9, 6.3)
ax.axis('off')
ax.text(3.2, 6.05, 'Immutable — int', ha='center', fontsize=14.5, color=PRIMARY, weight='bold', family='Tahoma')

ax.text(1.55, 5.45, 'ก่อนเรียกฟังก์ชัน', ha='center', fontsize=11.5, color=MUTED, style='italic', family='Tahoma')
box(ax, (0.2, 4.5), 1.3, 0.7, 'num', fc='white', ec=MUTED, tc='#333333', fontsize=12)
box(ax, (1.9, 4.5), 1.1, 0.7, 'x', fc='white', ec=MUTED, tc='#333333', fontsize=12)
c1 = Circle((3.35, 3.4), 0.6, facecolor=LIGHT, edgecolor=PRIMARY, linewidth=2.2)
ax.add_patch(c1)
ax.text(3.35, 3.4, '5', ha='center', va='center', fontsize=15, color=PRIMARY, weight='bold', family='Consolas')
arrow(ax, (0.85, 4.5), (2.95, 3.75), color=MUTED, lw=1.8, mutation_scale=15)
arrow(ax, (2.45, 4.5), (3.2, 3.9), color=MUTED, lw=1.8, mutation_scale=15)

ax.text(3.2, 2.55, 'ในฟังก์ชัน:  x = x + 10', ha='center', fontsize=12, color=ACCENT, weight='bold', family='Tahoma')

ax.text(1.55, 1.95, 'หลังฟังก์ชันทำงานเสร็จ', ha='center', fontsize=11.5, color=MUTED, style='italic', family='Tahoma')
box(ax, (0.2, 1.0), 1.3, 0.7, 'num', fc='white', ec=PRIMARY, tc=PRIMARY, fontsize=12, weight='bold')
box(ax, (1.9, 1.0), 1.1, 0.7, 'x', fc='white', ec=ACCENT, tc=ACCENT, fontsize=12, weight='bold')
# original object 5 stays where num points (below num)
o5 = Circle((0.85, -0.15), 0.55, facecolor='#f5f5f5', edgecolor=MUTED, linewidth=1.8)
ax.add_patch(o5)
ax.text(0.85, -0.15, '5', ha='center', va='center', fontsize=13.5, color=MUTED, weight='bold', family='Consolas')
n15 = Circle((3.35, -0.15), 0.6, facecolor=ACCENT, edgecolor=ACCENT, linewidth=2.2)
ax.add_patch(n15)
ax.text(3.35, -0.15, '15', ha='center', va='center', fontsize=15, color='white', weight='bold', family='Consolas')
arrow(ax, (0.85, 1.0), (0.85, 0.4), color=PRIMARY, lw=2.0, mutation_scale=15)
arrow(ax, (2.45, 1.0), (3.15, 0.45), color=ACCENT, lw=2.0, mutation_scale=15)
ax.text(4.55, 0.9, 'x ผูกกับ\nอ็อบเจกต์ใหม่\n(num ไม่เปลี่ยน)', ha='center', fontsize=10, color=ACCENT, family='Tahoma')
ax.set_ylim(-0.9, 6.3)

# ---- Right: Mutable (list) ----
ax = axes[1]
ax.set_xlim(0, 6.4)
ax.set_ylim(-0.9, 6.3)
ax.axis('off')
ax.text(3.2, 6.05, 'Mutable — list', ha='center', fontsize=14.5, color=PRIMARY, weight='bold', family='Tahoma')

ax.text(1.55, 5.45, 'ก่อนเรียกฟังก์ชัน', ha='center', fontsize=11.5, color=MUTED, style='italic', family='Tahoma')
box(ax, (0.1, 4.5), 1.7, 0.7, 'my_list', fc='white', ec=MUTED, tc='#333333', fontsize=11.5)
box(ax, (2.1, 4.5), 1.5, 0.7, 'items', fc='white', ec=MUTED, tc='#333333', fontsize=11.5)
box(ax, (2.55, 3.15), 2.0, 0.75, "['A']", fc=LIGHT, ec=PRIMARY, tc=PRIMARY, fontsize=13, family='Consolas')
arrow(ax, (0.95, 4.5), (3.0, 3.9), color=MUTED, lw=1.8, mutation_scale=15)
arrow(ax, (2.85, 4.5), (3.4, 3.9), color=MUTED, lw=1.8, mutation_scale=15)

ax.text(3.2, 2.55, 'ในฟังก์ชัน:  items.append("B")', ha='center', fontsize=12, color=ACCENT, weight='bold', family='Tahoma')

ax.text(1.55, 1.95, 'หลังฟังก์ชันทำงานเสร็จ', ha='center', fontsize=11.5, color=MUTED, style='italic', family='Tahoma')
box(ax, (0.1, 1.0), 1.7, 0.7, 'my_list', fc='white', ec=PRIMARY, tc=PRIMARY, fontsize=11.5, weight='bold')
box(ax, (2.1, 1.0), 1.5, 0.7, 'items', fc='white', ec=PRIMARY, tc=PRIMARY, fontsize=11.5, weight='bold')
box(ax, (2.35, -0.45), 2.4, 0.75, "['A', 'B']", fc=PRIMARY, ec=PRIMARY, tc='white', fontsize=13, family='Consolas')
arrow(ax, (0.95, 1.0), (3.1, -0.05), color=PRIMARY, lw=2.0, mutation_scale=15)
arrow(ax, (2.85, 1.0), (3.5, -0.05), color=PRIMARY, lw=2.0, mutation_scale=15)
ax.text(5.15, 0.4, 'ทั้งสองชื่อ\nยังชี้อ็อบเจกต์เดิม\n(อ็อบเจกต์ถูกแก้ไข)', ha='center', fontsize=10, color=PRIMARY, family='Tahoma')

save_b64(fig, 'slide32', r"E:\Temp\fig_slide32_mutability.png")
plt.close(fig)

print('C done')

# ============================================================
# Figure D — Slide 36: mutable default argument bug vs fix
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(13.5, 6.0))

# ---- Left: BAD ----
ax = axes[0]
ax.set_xlim(0, 6.4)
ax.set_ylim(-0.55, 6.4)
ax.axis('off')
ax.text(3.2, 6.15, 'add_item_bad(item, basket=[])', ha='center', fontsize=12.5, color=BAD, weight='bold', family='Consolas')
box(ax, (1.35, 5.1), 3.7, 0.75, 'def รันครั้งเดียว -> สร้าง [ ] เก็บไว้', fc='#fdecea', ec=BAD, tc=BAD, fontsize=10.5)
box(ax, (2.05, 3.85), 2.3, 0.85, 'default basket\n(อ็อบเจกต์เดียว)', fc=BADLIGHT, ec=BAD, tc=BAD, fontsize=11)
arrow(ax, (3.2, 5.1), (3.2, 4.7), color=BAD, lw=2.0, mutation_scale=16)

box(ax, (0.1, 2.45), 2.7, 0.95, 'เรียกครั้งที่ 1:\nadd_item_bad("แอปเปิล")', fc='white', ec=MUTED, tc='#333333', fontsize=9.3)
box(ax, (3.35, 2.45), 3.0, 0.95, 'เรียกครั้งที่ 2:\nadd_item_bad("กล้วย")', fc='white', ec=MUTED, tc='#333333', fontsize=9.3)
arrow(ax, (1.45, 3.4), (2.7, 3.85), color=BAD, lw=1.8, mutation_scale=14, connectionstyle='arc3,rad=-0.2')
arrow(ax, (4.85, 3.4), (3.7, 3.85), color=BAD, lw=1.8, mutation_scale=14, connectionstyle='arc3,rad=0.2')
ax.text(3.2, 1.65, 'ทั้งสองครั้งใช้อ็อบเจกต์เดียวกัน\n-> สินค้าสะสมข้ามการเรียก', ha='center', fontsize=10.5, color=BAD, weight='bold', family='Tahoma')
box(ax, (1.5, 0.05), 3.4, 0.85, "['แอปเปิล', 'กล้วย']", fc=BAD, ec=BAD, tc='white', fontsize=13, family='Tahoma')
arrow(ax, (3.2, 1.15), (3.2, 0.9), color=BAD, lw=2.0, mutation_scale=16)

# ---- Right: GOOD ----
ax = axes[1]
ax.set_xlim(0, 6.4)
ax.set_ylim(-0.55, 6.4)
ax.axis('off')
ax.text(3.2, 6.15, 'add_item_good(item, basket=None)', ha='center', fontsize=12.5, color=GOOD, weight='bold', family='Consolas')
box(ax, (1.35, 5.1), 3.7, 0.75, 'def รันครั้งเดียว -> ค่าเริ่มต้นคือ None', fc='#e8f5e9', ec=GOOD, tc=GOOD, fontsize=10.5)
box(ax, (2.05, 3.85), 2.3, 0.85, 'default = None\n(ไม่ใช่ list)', fc=GOODLIGHT, ec=GOOD, tc=GOOD, fontsize=11)
arrow(ax, (3.2, 5.1), (3.2, 4.7), color=GOOD, lw=2.0, mutation_scale=16)

box(ax, (0.1, 2.45), 2.7, 0.95, 'เรียกครั้งที่ 1:\nadd_item_good("แอปเปิล")', fc='white', ec=MUTED, tc='#333333', fontsize=8.8)
box(ax, (3.35, 2.45), 3.0, 0.95, 'เรียกครั้งที่ 2:\nadd_item_good("กล้วย")', fc='white', ec=MUTED, tc='#333333', fontsize=8.8)
ax.text(1.45, 1.65, 'if basket is None:\n    basket = []\n(ลิสต์ใหม่ทุกครั้ง)', ha='center', fontsize=9.0, color=GOOD, family='Tahoma')
ax.text(4.85, 1.65, 'if basket is None:\n    basket = []\n(ลิสต์ใหม่ทุกครั้ง)', ha='center', fontsize=9.0, color=GOOD, family='Tahoma')
box(ax, (0.1, 0.05), 2.7, 0.85, "['แอปเปิล']", fc=GOOD, ec=GOOD, tc='white', fontsize=13, family='Tahoma')
box(ax, (3.35, 0.05), 3.0, 0.85, "['กล้วย']", fc=GOOD, ec=GOOD, tc='white', fontsize=13, family='Tahoma')
ax.text(3.2, -0.35, 'แต่ละครั้งได้ลิสต์คนละอ็อบเจกต์ -> ไม่สะสมข้ามการเรียก', ha='center', fontsize=10, color=GOOD, weight='bold', family='Tahoma')

save_b64(fig, 'slide36', r"E:\Temp\fig_slide36_mutable_default.png")
plt.close(fig)

print('D done')

# ============================================================
# Figure E — Slide 43: call stack for factorial(4)..factorial(0), growing upward
# ============================================================
fig, ax = plt.subplots(figsize=(8.6, 7.6))
ax.set_xlim(0, 8.6)
ax.set_ylim(0, 7.6)
ax.axis('off')

frames = [(4, 'n * factorial(3)'), (3, 'n * factorial(2)'), (2, 'n * factorial(1)'),
          (1, 'n * factorial(0)'), (0, 'return 1   (base case)')]
y0 = 0.35
fh = 1.35
fw = 5.4
fx = 1.6
for i, (n, body) in enumerate(frames):
    y = y0 + i * fh
    is_base = (n == 0)
    box(ax, (fx, y), fw, fh - 0.18, '', fc=LIGHT if not is_base else '#fff3e0', ec=PRIMARY if not is_base else '#e65100', lw=2.2)
    ax.text(fx + 0.25, y + (fh - 0.18) - 0.32, f'factorial({n})', ha='left', fontsize=12.5,
            color=PRIMARY if not is_base else '#e65100', weight='bold', family='Consolas')
    ax.text(fx + 0.25, y + 0.32, f'n = {n}   {body}', ha='left', fontsize=10.5, color=MUTED, family='Consolas')
    if i < len(frames) - 1:
        arrow(ax, (fx + fw + 0.15, y + (fh-0.18)/2), (fx + fw + 0.15, y + fh + (fh-0.18)/2),
              color=ACCENT, lw=2.0, mutation_scale=15)

ax.text(fx + fw + 1.35, y0 + 2.5 * fh, 'เรียกลึกขึ้นเรื่อย ๆ\n(stack โตขึ้น)', ha='center', fontsize=11,
        color=ACCENT, weight='bold', family='Tahoma', rotation=90)
ax.text(fx + fw/2, y0 + len(frames)*fh + 0.15, 'base case: n = 0 อยู่บนสุดของ stack', ha='center', fontsize=11.5,
        color='#e65100', weight='bold', family='Tahoma')

save_b64(fig, 'slide43', r"E:\Temp\fig_slide43_callstack_factorial.png")
plt.close(fig)

print('E done')

# ============================================================
# Figure F — Slide 46: recursion unwind for factorial(4)
# ============================================================
fig, ax = plt.subplots(figsize=(10.8, 7.8))
ax.set_xlim(0, 10.8)
ax.set_ylim(0, 7.8)
ax.axis('off')

frames = [4, 3, 2, 1, 0]
returns = {0: '1 (base case)', 1: '1 * 1 = 1', 2: '2 * 1 = 2', 3: '3 * 2 = 6', 4: '4 * 6 = 24'}
y0 = 0.3
fh = 1.35
fw = 4.6
fx = 3.0
for i, n in enumerate(frames):
    y = y0 + i * fh
    is_base = (n == 0)
    box(ax, (fx, y), fw, fh - 0.2, f'factorial({n})   n = {n}', fc=LIGHT if not is_base else '#fff3e0',
        ec=PRIMARY if not is_base else '#e65100', tc=PRIMARY if not is_base else '#e65100', fontsize=12.5, family='Consolas')

# downward-to-upward call arrows (left side): call goes from bottom frame up to top (deeper)
for i in range(len(frames) - 1):
    y = y0 + i * fh
    arrow(ax, (fx - 0.35, y + (fh-0.2)/2), (fx - 0.35, y + fh + (fh-0.2)/2), color=ACCENT, lw=2.0, mutation_scale=15)
ax.text(fx - 1.15, y0 + 2.5*fh, 'เรียก (call)\nลงลึกขึ้น', ha='center', fontsize=10.5, color=ACCENT,
        weight='bold', family='Tahoma', rotation=90)

# upward-to-downward return arrows (right side): return goes from top frame back down, with value label
for i in range(len(frames) - 1, 0, -1):
    y = y0 + i * fh
    arrow(ax, (fx + fw + 0.35, y + (fh-0.2)/2), (fx + fw + 0.35, y - fh + (fh-0.2)/2), color=GOOD, lw=2.2, mutation_scale=16)
    ax.text(fx + fw + 1.55, y - fh/2 + (fh-0.2)/2, f'return {returns[frames[i]]}', ha='left', fontsize=10.3,
            color=GOOD, weight='bold', family='Tahoma')

ax.text(fx + fw/2, y0 + len(frames)*fh + 0.15, 'base case n = 0 -> เริ่มคืนค่ากลับ (unwind)', ha='center', fontsize=11.5,
        color='#e65100', weight='bold', family='Tahoma')

save_b64(fig, 'slide46', r"E:\Temp\fig_slide46_unwind.png")
plt.close(fig)

print('F done')

# ============================================================
# Figure G — Slide 59: higher-order function box, in/out arrows
# ============================================================
fig, ax = plt.subplots(figsize=(11.0, 4.6))
ax.set_xlim(0, 11.0)
ax.set_ylim(0, 4.6)
ax.axis('off')

box(ax, (3.9, 1.3), 3.2, 2.0, 'Higher-order\nFunction', fc=PRIMARY, ec=PRIMARY, tc='white', fontsize=15)

box(ax, (0.3, 1.7), 2.4, 1.1, 'ฟังก์ชันอื่น\n(f)', fc=LIGHT, ec=ACCENT, tc=ACCENT, fontsize=12)
arrow(ax, (2.7, 2.25), (3.9, 2.25), color=ACCENT, lw=2.6, mutation_scale=20)
ax.text(3.3, 3.0, 'function\nas argument', ha='center', fontsize=10.8, color=ACCENT, weight='bold', family='Tahoma')

box(ax, (8.3, 1.7), 2.4, 1.1, 'ฟังก์ชันใหม่\n(g)', fc=LIGHT, ec=GOOD, tc=GOOD, fontsize=12)
arrow(ax, (7.1, 2.25), (8.3, 2.25), color=GOOD, lw=2.6, mutation_scale=20)
ax.text(7.7, 3.0, 'function\nas return value', ha='center', fontsize=10.8, color=GOOD, weight='bold', family='Tahoma')

ax.text(5.5, 0.65, 'เข้าเงื่อนไขได้ทั้งสอง หรือเพียงข้อใดข้อหนึ่งก็เพียงพอ', ha='center', fontsize=10.5,
        color=MUTED, style='italic', family='Tahoma')

save_b64(fig, 'slide59', r"E:\Temp\fig_slide59_hof.png")
plt.close(fig)

print('G done')

# ============================================================
# Figure H — Slide 62: closure late binding (shared i vs bound factor)
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.8))

# ---- Left: buggy shared i ----
ax = axes[0]
ax.set_xlim(0, 6.4)
ax.set_ylim(0, 6.2)
ax.axis('off')
ax.text(3.2, 5.95, 'ผิด — closure late binding', ha='center', fontsize=13, color=BAD, weight='bold', family='Tahoma')
ax.text(3.2, 5.4, 'for i in [1, 2, 3]:\n    funcs.append(lambda x: x * i)', ha='center', fontsize=10.5, color='#333333', family='Consolas')

box(ax, (2.15, 3.5), 2.1, 0.85, 'i = 3\n(ค่าสุดท้าย)', fc=BADLIGHT, ec=BAD, tc=BAD, fontsize=12, weight='bold')

lam_y = 1.5
lam_w = 1.6
lam_xs = [0.25, 2.4, 4.55]
for lx in lam_xs:
    cx = lx + lam_w / 2
    box(ax, (lx, lam_y), lam_w, 0.9, 'lambda x:\nx * i', fc='white', ec=MUTED, tc='#333333', fontsize=10, family='Consolas')
    arrow(ax, (cx, lam_y + 0.9), (3.2, 3.5), color=BAD, lw=1.8, mutation_scale=13,
          connectionstyle=f'arc3,rad={(lx-3.2)/16}')
ax.text(3.2, 0.75, 'ทุก lambda ชี้ไปที่ตัวแปร i ตัวเดียวกัน\n-> ได้ผลลัพธ์ 30, 30, 30', ha='center', fontsize=10.3,
        color=BAD, weight='bold', family='Tahoma')

# ---- Right: fixed bound factor ----
ax = axes[1]
ax.set_xlim(0, 6.4)
ax.set_ylim(0, 6.2)
ax.axis('off')
ax.text(3.2, 5.95, 'ถูก — ผูกค่าไว้ทันที', ha='center', fontsize=13, color=GOOD, weight='bold', family='Tahoma')
ax.text(3.2, 5.4, 'for i in [1, 2, 3]:\n    funcs_fixed.append(lambda x, factor=i: x*factor)', ha='center', fontsize=9.3, color='#333333', family='Consolas')

lam_w2 = 1.75
lam_xs2 = [0.2, 2.35, 4.5]
vals = [1, 2, 3]
for lx, v in zip(lam_xs2, vals):
    cx = lx + lam_w2 / 2
    box(ax, (lx, 3.35), lam_w2, 1.0, f'lambda x,\nfactor={v}:\nx * factor', fc=GOODLIGHT, ec=GOOD, tc=GOOD, fontsize=9.3, family='Consolas')
    box(ax, (cx - 0.4, 1.75), 0.8, 0.7, f'{v}', fc=GOOD, ec=GOOD, tc='white', fontsize=13, family='Consolas')
    arrow(ax, (cx, 3.35), (cx, 2.45), color=GOOD, lw=1.8, mutation_scale=13)

ax.text(3.2, 0.9, 'แต่ละ lambda มี factor เป็นของตัวเอง\n-> ได้ผลลัพธ์ 10, 20, 30', ha='center', fontsize=10.3,
        color=GOOD, weight='bold', family='Tahoma')

save_b64(fig, 'slide62', r"E:\Temp\fig_slide62_closure.png")
plt.close(fig)

print('H done')

with open(r"E:\Temp\fig2_b64.txt", 'w', encoding='utf-8') as f:
    f.write('\n===SPLIT===\n'.join(f'{k}|||{v}' for k, v in results.items()))

for k, v in results.items():
    print(k, 'bytes:', len(v))

