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
CODEBG = '#1e272e'
CODEFG = '#dfe6e9'

def save_b64(fig, path_png):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=170, bbox_inches='tight', facecolor='white')
    fig.savefig(path_png, dpi=170, bbox_inches='tight', facecolor='white')
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('ascii')

def box(ax, xy, w, h, text, fc=LIGHT, ec=PRIMARY, tc=PRIMARY, fontsize=13, weight='bold'):
    x, y = xy
    b = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.02,rounding_size=0.03', linewidth=2, edgecolor=ec, facecolor=fc)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=fontsize, color=tc, weight=weight, family='Tahoma')
    return b

def arrow(ax, xy1, xy2, color=ACCENT, style='-|>', lw=2.2, connectionstyle='arc3,rad=0', mutation_scale=18, ls='-'):
    a = FancyArrowPatch(xy1, xy2, arrowstyle=style, color=color, lw=lw,
                         connectionstyle=connectionstyle, mutation_scale=mutation_scale, linestyle=ls)
    ax.add_patch(a)

# ============================================================
# Figure 1 — Slide 7: def (declaration) vs call (execution)
# ============================================================
fig, ax = plt.subplots(figsize=(10.5, 6.4))
ax.set_xlim(0, 10.5)
ax.set_ylim(0, 6.4)
ax.axis('off')

ax.text(5.25, 6.15, 'นิยาม (Definition) เพียงแค่ "ประกาศไว้" — ยังไม่รันคำสั่งข้างในจนกว่าจะถูกเรียกใช้',
        ha='center', fontsize=12.5, color=MUTED, style='italic', family='Tahoma')

def_box = FancyBboxPatch((2.6, 4.7), 5.3, 1.2, boxstyle='round,pad=0.02,rounding_size=0.03',
                          linewidth=2.2, edgecolor=MUTED, facecolor='#f5f5f5', linestyle=(0, (6, 3)))
ax.add_patch(def_box)
ax.text(5.25, 5.6, 'def greet():', ha='center', va='center', fontsize=14, color=PRIMARY, weight='bold', family='Consolas')
ax.text(5.25, 5.05, 'print("สวัสดี")', ha='center', va='center', fontsize=12, color=MUTED, family='Tahoma')

# Timeline of calls
y0 = 1.15
labels = ['print(\n"ก่อนเรียก")', 'greet()\n(ครั้งที่ 1)', 'greet()\n(ครั้งที่ 2)', 'print(\n"หลังเรียก")']
xs = [0.4, 3.05, 5.7, 8.35]
w = 1.9
for x, lab in zip(xs, labels):
    is_call = 'greet' in lab
    box(ax, (x, y0), w, 0.9, lab, fc=ACCENT if is_call else '#eeeeee',
        ec=ACCENT if is_call else MUTED, tc='white' if is_call else '#333333', fontsize=11.5)

for i in range(len(xs) - 1):
    arrow(ax, (xs[i] + w, y0 + 0.45), (xs[i+1], y0 + 0.45), color=MUTED, lw=1.6)

ax.text(5.25, y0 + 1.75, 'ลำดับที่ทำงานจริง (runtime) — เรียงจากซ้ายไปขวาตามเวลา', ha='center', fontsize=12,
        color=PRIMARY, weight='bold', family='Tahoma')

# One clear loop for call 1 only: up into def box, down back to call site
call1_top = (3.05 + w/2, y0 + 0.9)
arrow(ax, call1_top, (4.3, 4.7), color=PRIMARY, lw=2.2, connectionstyle='arc3,rad=-0.25', mutation_scale=17)
arrow(ax, (5.4, 4.7), (call1_top[0] + 0.35, y0 + 0.9), color=PRIMARY, lw=2.2,
      connectionstyle='arc3,rad=-0.3', mutation_scale=17, ls=(0, (3, 2)))
ax.text(2.55, 3.35, 'เข้าไปรัน body\nของฟังก์ชัน', ha='center', fontsize=10.5, color=PRIMARY, family='Tahoma')
ax.text(6.85, 3.35, 'กลับมาทำงานต่อ\n(return to caller)', ha='center', fontsize=10.5, color=PRIMARY, family='Tahoma')

ax.text(5.25, y0 + 1.35, '(ครั้งที่ 2 ก็ทำงานแบบเดียวกัน — เข้าไปรัน แล้วกลับออกมา)', ha='center', fontsize=10.5,
        color=MUTED, style='italic', family='Tahoma')

b64_1 = save_b64(fig, r"E:\Temp\fig_slide7_def_vs_call.png")
plt.close(fig)

# ============================================================
# Figure 2 — Slide 12: parameter (empty slot) vs argument (real value) binding
# ============================================================
fig, ax = plt.subplots(figsize=(10.5, 5.6))
ax.set_xlim(0, 10.5)
ax.set_ylim(0, 5.6)
ax.axis('off')

ax.text(5.25, 5.35, 'def introduce(name, age):', ha='center', fontsize=15, color=PRIMARY, weight='bold', family='Consolas')

box(ax, (2.3, 3.9), 2.1, 0.9, 'name', fc='#f5f5f5', ec=MUTED, tc=MUTED, fontsize=13)
box(ax, (5.5, 3.9), 2.1, 0.9, 'age', fc='#f5f5f5', ec=MUTED, tc=MUTED, fontsize=13)
ax.text(5.25, 3.55, 'parameter = ช่องว่างรอรับค่า', ha='center', fontsize=11.5,
        color=MUTED, style='italic', family='Tahoma')

ax.text(5.25, 2.55, 'introduce("Aom", 20)', ha='center', fontsize=15, color=PRIMARY, weight='bold', family='Consolas')

box(ax, (2.3, 1.0), 2.1, 0.8, '"Aom"', fc=ACCENT, ec=ACCENT, tc='white', fontsize=13)
box(ax, (5.5, 1.0), 2.1, 0.8, '20', fc=ACCENT, ec=ACCENT, tc='white', fontsize=13)
ax.text(5.25, 0.55, 'argument = ค่าจริงที่ส่งเข้าไป', ha='center', fontsize=11.5,
        color=ACCENT, style='italic', family='Tahoma')

arrow(ax, (3.35, 1.8), (3.35, 3.9), color=ACCENT, lw=2.4, mutation_scale=20)
arrow(ax, (6.55, 1.8), (6.55, 3.9), color=ACCENT, lw=2.4, mutation_scale=20)

ax.text(1.05, 2.85, 'ตำแหน่งที่ 1', fontsize=10.5, color=ACCENT, family='Tahoma', rotation=90, va='center', ha='center')
ax.text(9.45, 2.85, 'ตำแหน่งที่ 2', fontsize=10.5, color=ACCENT, family='Tahoma', rotation=90, va='center', ha='center')

b64_2 = save_b64(fig, r"E:\Temp\fig_slide12_param_arg.png")
plt.close(fig)

with open(r"E:\Temp\fig_b64.txt", 'w', encoding='utf-8') as f:
    f.write(b64_1 + '\n===SPLIT===\n' + b64_2)

print('fig1 bytes:', len(b64_1))
print('fig2 bytes:', len(b64_2))
