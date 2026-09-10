\
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import base64, io

plt.rcParams['font.family'] = 'Tahoma'

PRIMARY = '#1a237e'
ACCENT = '#1565c0'
LIGHT = '#e3f2fd'
MUTED = '#546e7a'
RED = '#c62828'
GREEN = '#2e7d32'
CODEBG = '#1e272e'
CODEFG = '#dfe6e9'

def save_b64(fig, path_png):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=170, bbox_inches='tight', facecolor='white')
    fig.savefig(path_png, dpi=170, bbox_inches='tight', facecolor='white')
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('ascii')

def box(ax, xy, w, h, text, fc=LIGHT, ec=PRIMARY, tc=PRIMARY, fontsize=12, weight='bold'):
    x, y = xy
    b = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.02,rounding_size=0.03', linewidth=2, edgecolor=ec, facecolor=fc)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=fontsize, color=tc, weight=weight, family='Tahoma')
    return b

def arrow(ax, xy1, xy2, color=ACCENT, style='-|>', lw=2.2, connectionstyle='arc3,rad=0', mutation_scale=17, ls='-'):
    a = FancyArrowPatch(xy1, xy2, arrowstyle=style, color=color, lw=lw,
                         connectionstyle=connectionstyle, mutation_scale=mutation_scale, linestyle=ls)
    ax.add_patch(a)

results = {}

# ============================================================
# Figure 1 (Slide 1.2): Syntax Error vs Exception timing
# ============================================================
fig, ax = plt.subplots(figsize=(10.5, 5.5))
ax.set_xlim(0, 10.5); ax.set_ylim(0, 5.5); ax.axis('off')

ax.text(5.25, 5.2, 'จังหวะเวลาที่ตรวจพบข้อผิดพลาด', ha='center', fontsize=14, color=PRIMARY, weight='bold', family='Tahoma')

# Syntax error row
ax.text(0.3, 4.1, 'Syntax\nError', ha='left', va='center', fontsize=12, color=PRIMARY, weight='bold', family='Tahoma')
box(ax, (2.2, 3.75), 2.0, 0.7, 'Parsing', fc='#eeeeee', ec=MUTED, tc='#333333', fontsize=11)
ax.text(5.3, 4.1, 'X', ha='center', va='center', fontsize=22, color=RED, weight='bold')
ax.text(6.6, 4.1, 'โปรแกรมไม่เริ่มทำงานเลย\nแม้แต่บรรทัดเดียว', ha='left', va='center', fontsize=10.5, color=RED, family='Tahoma')
arrow(ax, (4.2, 4.1), (5.05, 4.1), color=MUTED, lw=1.6)

# Exception row
ax.text(0.3, 1.7, 'Exception', ha='left', va='center', fontsize=12, color=PRIMARY, weight='bold', family='Tahoma')
xs = [2.2, 3.5, 4.8]
for x in xs:
    box(ax, (x, 1.35), 1.0, 0.7, 'OK', fc='#e8f5e9', ec=GREEN, tc=GREEN, fontsize=13)
ax.text(6.3, 1.7, 'X', ha='center', va='center', fontsize=22, color=RED, weight='bold')
ax.text(7.6, 1.7, 'โปรแกรมทำงานมาบางส่วน\nสำเร็จก่อนหยุดที่บรรทัดนี้', ha='left', va='center', fontsize=10.5, color=RED, family='Tahoma')
for i in range(len(xs) - 1):
    arrow(ax, (xs[i] + 1.0, 1.7), (xs[i+1], 1.7), color=MUTED, lw=1.6)
arrow(ax, (5.8, 1.7), (6.05, 1.7), color=MUTED, lw=1.6)

ax.text(3.2, 3.2, '(ยังไม่ทันรันบรรทัดใดเลย)', ha='center', fontsize=10, color=MUTED, style='italic', family='Tahoma')
ax.text(3.5, 0.85, '(บรรทัดก่อนหน้าทำงานสำเร็จแล้ว)', ha='center', fontsize=10, color=MUTED, style='italic', family='Tahoma')

results['fig1'] = save_b64(fig, r"E:\Temp\fig_w7_slide1_timing.png")
plt.close(fig)

# ============================================================
# Figure 2 (Slide 2.2): try/except control flow jump
# ============================================================
fig, ax = plt.subplots(figsize=(10.5, 5.8))
ax.set_xlim(0, 10.5); ax.set_ylim(0, 5.8); ax.axis('off')

box(ax, (0.4, 4.3), 3.2, 0.8, 'try: บรรทัด 1', fc=LIGHT, ec=PRIMARY, fontsize=11)
box(ax, (0.4, 3.2), 3.2, 0.8, 'try: บรรทัด 2 (เกิดปัญหา)', fc='#ffebee', ec=RED, tc=RED, fontsize=10.5)
box(ax, (0.4, 2.1), 3.2, 0.8, 'try: บรรทัด 3', fc='#eeeeee', ec=MUTED, tc=MUTED, fontsize=11)
ax.text(2.0, 1.75, '(ไม่ถูกรัน)', ha='center', fontsize=9.5, color=MUTED, style='italic', family='Tahoma')

box(ax, (5.5, 3.2), 3.0, 0.8, 'except: รับมือ', fc=ACCENT, ec=ACCENT, tc='white', fontsize=12)
box(ax, (5.5, 1.3), 3.0, 0.8, 'โค้ดหลัง try/except', fc='#e8f5e9', ec=GREEN, tc=GREEN, fontsize=11)

arrow(ax, (2.0, 4.3), (2.0, 4.0), color=MUTED, lw=1.6)
arrow(ax, (3.6, 3.6), (5.5, 3.6), color=RED, lw=2.4, mutation_scale=20)
ax.text(4.55, 3.85, 'กระโดดทันที', ha='center', fontsize=10, color=RED, family='Tahoma')
arrow(ax, (7.0, 3.2), (7.0, 2.1), color=ACCENT, lw=2.2)

ax.text(2.0, 5.3, 'บล็อก try (ทดลองรัน)', ha='center', fontsize=12, color=PRIMARY, weight='bold', family='Tahoma')
ax.text(7.0, 4.3, 'บล็อก except', ha='center', fontsize=12, color=PRIMARY, weight='bold', family='Tahoma')

results['fig2'] = save_b64(fig, r"E:\Temp\fig_w7_slide2_tryexcept.png")
plt.close(fig)

# ============================================================
# Figure 3 (Slide 6.5): try/except/else/finally branching
# ============================================================
fig, ax = plt.subplots(figsize=(10.5, 5.8))
ax.set_xlim(0, 10.5); ax.set_ylim(0, 5.8); ax.axis('off')

box(ax, (4.0, 4.5), 2.5, 0.9, 'try', fc=LIGHT, ec=PRIMARY, fontsize=13)
box(ax, (1.0, 3.0), 2.6, 0.9, 'except\n(เกิดข้อผิดพลาด)', fc='#ffebee', ec=RED, tc=RED, fontsize=11)
box(ax, (6.4, 3.0), 2.6, 0.9, 'else\n(สำเร็จ ไม่มีข้อผิดพลาด)', fc='#e8f5e9', ec=GREEN, tc=GREEN, fontsize=11)
box(ax, (3.75, 1.3), 3.0, 0.9, 'finally (รันเสมอ)', fc=ACCENT, ec=ACCENT, tc='white', fontsize=13)

arrow(ax, (4.6, 4.5), (2.6, 3.9), color=RED, lw=2.0, connectionstyle='arc3,rad=-0.15')
arrow(ax, (5.9, 4.5), (7.5, 3.9), color=GREEN, lw=2.0, connectionstyle='arc3,rad=0.15')
arrow(ax, (2.3, 3.0), (4.7, 2.2), color=MUTED, lw=2.0, connectionstyle='arc3,rad=-0.15')
arrow(ax, (7.7, 3.0), (5.7, 2.2), color=MUTED, lw=2.0, connectionstyle='arc3,rad=0.15')

ax.text(5.25, 0.55, 'ไม่ว่าจะผ่านทาง except หรือ else มาก็ตาม finally ทำงานเสมอเป็นลำดับสุดท้าย', ha='center',
        fontsize=11, color=MUTED, style='italic', family='Tahoma')

results['fig3'] = save_b64(fig, r"E:\Temp\fig_w7_slide6_elsefinally.png")
plt.close(fig)

# ============================================================
# Figure 4 (Slide 11.2): Exception hierarchy tree
# ============================================================
fig, ax = plt.subplots(figsize=(11.5, 6.5))
ax.set_xlim(0, 11.5); ax.set_ylim(0, 6.5); ax.axis('off')

box(ax, (4.6, 5.5), 2.3, 0.7, 'BaseException', fc=PRIMARY, ec=PRIMARY, tc='white', fontsize=11.5)

box(ax, (2.9, 4.2), 1.9, 0.7, 'Exception', fc=ACCENT, ec=ACCENT, tc='white', fontsize=11)
box(ax, (5.2, 4.2), 1.9, 0.65, 'SystemExit', fc='#eeeeee', ec=MUTED, tc='#333333', fontsize=10)
box(ax, (7.4, 4.2), 2.4, 0.65, 'KeyboardInterrupt', fc='#eeeeee', ec=MUTED, tc='#333333', fontsize=10)

box(ax, (0.5, 2.9), 2.3, 0.65, 'ArithmeticError', fc=LIGHT, ec=PRIMARY, tc=PRIMARY, fontsize=10)
box(ax, (3.1, 2.9), 1.9, 0.65, 'LookupError', fc=LIGHT, ec=PRIMARY, tc=PRIMARY, fontsize=10)

labels_arith = ['ZeroDivisionError', 'OverflowError', 'FloatingPointError']
for idx, lab in enumerate(labels_arith):
    box(ax, (0.1 + idx*2.05, 1.4), 1.9, 0.65, lab, fc='#f5f5f5', ec=MUTED, tc='#333333', fontsize=9)

labels_lookup = ['IndexError', 'KeyError']
for idx, lab in enumerate(labels_lookup):
    box(ax, (6.6 + idx*2.05, 1.4), 1.9, 0.65, lab, fc='#f5f5f5', ec=MUTED, tc='#333333', fontsize=9.5)

arrow(ax, (5.4, 5.5), (3.85, 4.9), color=MUTED, lw=1.8)
arrow(ax, (5.75, 5.5), (6.15, 4.85), color=MUTED, lw=1.8)
arrow(ax, (5.9, 5.5), (8.6, 4.85), color=MUTED, lw=1.8)

arrow(ax, (3.4, 4.2), (1.65, 3.55), color=MUTED, lw=1.6)
arrow(ax, (3.9, 4.2), (4.05, 3.55), color=MUTED, lw=1.6)

for idx in range(3):
    cx = 0.1 + idx*2.05 + 0.95
    arrow(ax, (1.65, 2.9), (cx, 2.05), color=MUTED, lw=1.4)

for idx in range(2):
    cx = 6.6 + idx*2.05 + 0.95
    arrow(ax, (4.05, 2.9), (cx, 2.05), color=MUTED, lw=1.4)

ax.text(9.6, 3.15, '(รากของทั้งหมด สืบทอด\nคุณสมบัติจากบนลงล่าง)', ha='left', fontsize=9.5, color=MUTED, style='italic', family='Tahoma')

results['fig4'] = save_b64(fig, r"E:\Temp\fig_w7_slide11_hierarchy.png")
plt.close(fig)

# ============================================================
# Figure 5 (Slide 13.2): nested try/except/finally flow
# ============================================================
fig, ax = plt.subplots(figsize=(10.5, 6.2))
ax.set_xlim(0, 10.5); ax.set_ylim(0, 6.2); ax.axis('off')

outer = FancyBboxPatch((0.4, 0.6), 9.7, 5.0, boxstyle='round,pad=0.02,rounding_size=0.04',
                        linewidth=2.2, edgecolor=PRIMARY, facecolor='none', linestyle=(0, (5, 3)))
ax.add_patch(outer)
ax.text(0.7, 5.3, 'try ชั้นนอก', fontsize=11.5, color=PRIMARY, weight='bold', family='Tahoma')

inner = FancyBboxPatch((1.0, 2.6), 5.0, 2.2, boxstyle='round,pad=0.02,rounding_size=0.04',
                        linewidth=2.0, edgecolor=ACCENT, facecolor=LIGHT, linestyle=(0, (4, 2)))
ax.add_patch(inner)
ax.text(1.3, 4.5, 'try ชั้นใน', fontsize=11, color=ACCENT, weight='bold', family='Tahoma')
box(ax, (1.4, 3.0), 3.2, 0.9, 'เกิดข้อผิดพลาด\n(ชนิดไม่ตรงกับ except ชั้นใน)', fc='#ffebee', ec=RED, tc=RED, fontsize=9.5)

box(ax, (6.5, 3.0), 3.0, 0.9, 'except ชั้นใน\n(ชนิดไม่ตรง — ไม่ทำงาน)', fc='#eeeeee', ec=MUTED, tc='#666666', fontsize=9.5)
box(ax, (6.5, 4.1), 3.0, 0.8, 'except ชั้นนอก\n(ชนิดตรง — ทำงาน)', fc=ACCENT, ec=ACCENT, tc='white', fontsize=10)

box(ax, (1.4, 1.8), 3.0, 0.65, 'finally ชั้นใน', fc='#fff3e0', ec='#e65100', tc='#e65100', fontsize=10)
box(ax, (6.5, 1.0), 3.0, 0.65, 'finally ชั้นนอก', fc='#fff3e0', ec='#e65100', tc='#e65100', fontsize=10)

arrow(ax, (4.6, 3.45), (6.5, 4.5), color=RED, lw=2.4, connectionstyle='arc3,rad=-0.2', mutation_scale=20)
ax.text(5.6, 4.1, 'ไหลออก\n(bypass)', ha='center', fontsize=9, color=RED, family='Tahoma')

arrow(ax, (2.9, 3.0), (2.9, 2.45), color=MUTED, lw=1.6)
arrow(ax, (8.0, 4.1), (8.0, 1.65), color=MUTED, lw=1.6, connectionstyle='arc3,rad=0.3')

results['fig5'] = save_b64(fig, r"E:\Temp\fig_w7_slide13_nested.png")
plt.close(fig)

# ============================================================
# Figure 6 (Slide 15.5): __cause__ vs __context__
# ============================================================
fig, ax = plt.subplots(figsize=(11.0, 6.5))
ax.set_xlim(0, 11.0); ax.set_ylim(0, 6.5); ax.axis('off')

box(ax, (3.9, 5.4), 3.2, 0.8, 'except ValueError as e:', fc=LIGHT, ec=PRIMARY, fontsize=11.5)

rows = [
    (4.6, 'raise NewErr(...) from e', '__cause__ = e', 'แสดงทั้งสอง error (เดิม + ใหม่)', '#e8f5e9', GREEN),
    (3.0, 'raise NewErr(...)  (ไม่มี from)', '__context__ = e (อัตโนมัติ)', 'แสดงทั้งสอง คั่นด้วย\n"During handling..."', '#fff3e0', '#e65100'),
    (1.4, 'raise NewErr(...) from None', '__cause__ = None (ตั้งใจ)', 'แสดงเฉพาะ NewErr เท่านั้น', '#ffebee', RED),
]
for y, path, attr, result, fc, tc in rows:
    box(ax, (0.3, y), 3.4, 0.8, path, fc=fc, ec=tc, tc=tc, fontsize=9.5)
    box(ax, (4.0, y), 3.1, 0.8, attr, fc='#f5f5f5', ec=MUTED, tc='#333333', fontsize=8.5)
    box(ax, (7.4, y), 3.3, 0.8, result, fc='#f5f5f5', ec=MUTED, tc='#333333', fontsize=8.5)
    arrow(ax, (5.5, 5.4), (2.0, y+0.8), color=MUTED, lw=1.3, connectionstyle='arc3,rad=0.1')

ax.text(5.5, 0.5, 'ข้อมูลต้นทางยังเข้าถึงได้ผ่าน __cause__/__context__ เสมอ ไม่ว่าจะเลือกรูปแบบใด', ha='center',
        fontsize=10.5, color=MUTED, style='italic', family='Tahoma')

results['fig6'] = save_b64(fig, r"E:\Temp\fig_w7_slide15_chaining.png")
plt.close(fig)

with open(r"E:\Temp\fig_w7_b64.txt", 'w', encoding='utf-8') as f:
    for k in ['fig1','fig2','fig3','fig4','fig5','fig6']:
        f.write(results[k] + '\n===SPLIT===\n')

for k in ['fig1','fig2','fig3','fig4','fig5','fig6']:
    print(k, len(results[k]))
