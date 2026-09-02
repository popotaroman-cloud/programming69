# -*- coding: utf-8 -*-
import re

with open(r"E:\Temp\fig2_b64.txt", 'r', encoding='utf-8') as f:
    raw = f.read()

parts = raw.split('\n===SPLIT===\n')
b64 = {}
for p in parts:
    k, v = p.split('|||', 1)
    b64[k] = v

print('keys:', list(b64.keys()))
for k, v in b64.items():
    print(k, len(v))

HTML_PATH = r"E:\2569\programming\.claude\worktrees\session-aedcf8\week_06_function\slides\06_function.html"
INDEX_PATH = r"E:\2569\programming\.claude\worktrees\session-aedcf8\week_06_function\slides\index.html"

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

def img_div(key, alt):
    return f'<div class="slide-figure"><img src="data:image/png;base64,{b64[key]}" alt="{alt}"></div>'

replacements = []

# Slide 17
old = '<div class="placeholder">📊 <em>call stack diagram showing add(3, 5) call, parameters bound, and return value flowing back to caller</em></div>'
new = img_div('slide17', 'call stack diagram: add(3, 5) call, x and y parameters bound to 3 and 5, return value 8 flowing back to the caller')
replacements.append((old, new))

# Slide 22
old = '<div class="placeholder">📊 <em>box diagram showing outer scope variable count separate from the function\'s local_count box</em></div>'
new = img_div('slide22', 'box diagram: global scope variable count clearly separate from the function\'s local scope variable local_count')
replacements.append((old, new))

# Slide 32
old = ('<div class="placeholder">📊 <em>two side-by-side memory-reference diagrams. Left (immutable): variable num and parameter x both start pointing to '
       'the same int object 5; after x = x + 10 inside the function, x is rebound to point to a brand-new object 15 while num still points to the original '
       'object 5. Right (mutable): variable my_list and parameter items both point to the same list object the whole time; after items.append("B") the shared '
       "object itself is mutated in place, so both names still point to it and both now see ['A', 'B'].</em></div>")
new = img_div('slide32', 'memory-reference diagrams: immutable int (num, x rebinds to a new object) vs mutable list (my_list, items share and mutate the same object)')
replacements.append((old, new))

# Slide 36
old = ("<div class=\"placeholder\">📊 <em>diagram showing the def statement executing once and creating a single shared empty-list object bound into "
       "add_item_bad's default-argument slot; every call to add_item_bad() without an explicit basket argument reuses that exact same list object, so items "
       "pile up across calls — contrasted with add_item_good(), where basket=None is the fixed default and a brand-new empty list object is created fresh "
       "inside the function body on every call.</em></div>")
new = img_div('slide36', 'diagram: add_item_bad shares one default list object across calls (bug) vs add_item_good creating a fresh list each call (fix)')
replacements.append((old, new))

# Slide 43
old = ('<div class="placeholder">📊 <em>call stack diagram showing factorial(4) calling factorial(3) calling factorial(2) calling factorial(1) calling '
       "factorial(0), each frame stacked on top of the previous one with its own local variable n, growing upward until the base case n=0 is reached at the "
       'top.</em></div>')
new = img_div('slide43', 'call stack diagram: factorial(4) calling factorial(3), factorial(2), factorial(1), factorial(0), stacked upward to the base case')
replacements.append((old, new))

# Slide 46
old = ('<div class="placeholder">📊 <em>recursion unwind diagram for factorial(4). Downward chain of calls: factorial(4) calls factorial(3) calls factorial(2) '
       "calls factorial(1) calls factorial(0), reaching the base case. Then an upward chain of returns back through each waiting frame: factorial(0) returns 1, "
       "factorial(1) returns 1*1=1, factorial(2) returns 2*1=2, factorial(3) returns 3*2=6, factorial(4) returns 4*6=24 — each pending call multiplying by its "
       'own local n before returning to its caller.</em></div>')
new = img_div('slide46', 'recursion unwind diagram for factorial(4): calls go down to the base case, then returns unwind back up multiplying at each frame')
replacements.append((old, new))

# Slide 49 -> TABLE
old = ('<div class="placeholder">📊 <em>diagram showing a function object sitting alongside int/str/list values, with arrows showing it can be assigned to a '
       'variable, passed as an argument, stored in a data structure, and returned from another function</em></div>')
new = ('<div class="table-wrap"><table><thead><tr><th>ความสามารถ</th><th>ตัวอย่าง</th></tr></thead><tbody>'
       '<tr><td>เก็บไว้ในตัวแปรได้</td><td><code>f = greet</code></td></tr>'
       '<tr><td>ส่งเป็นอาร์กิวเมนต์ให้ฟังก์ชันอื่นได้</td><td><code>apply(greet)</code></td></tr>'
       '<tr><td>เก็บไว้ในโครงสร้างข้อมูลได้</td><td><code>ops = {"a": greet}</code></td></tr>'
       '<tr><td>ส่งกลับออกมาจากฟังก์ชันอื่นได้</td><td><code>return greet</code></td></tr>'
       '</tbody></table></div>')
replacements.append((old, new))

# Slide 59
old = ('<div class="placeholder">📊 <em>diagram showing a higher-order function box with an arrow pointing IN labeled "function as argument" and an arrow '
       'pointing OUT labeled "function as return value"</em></div>')
new = img_div('slide59', 'higher-order function box with an arrow pointing in labeled function as argument and an arrow pointing out labeled function as return value')
replacements.append((old, new))

# Slide 62
old = ('<div class="placeholder">📊 <em>diagram showing three lambda closures in a loop all pointing to the same shared variable <code>i</code> box (which ends '
       'up holding 3), versus three lambdas each with their own bound <code>factor</code> value (1, 2, 3) captured at creation time</em></div>')
new = img_div('slide62', 'diagram: three lambda closures sharing one variable i (late binding bug) vs three lambdas each with their own bound factor value 1, 2, 3')
replacements.append((old, new))

missing = []
for i, (old, new) in enumerate(replacements, 1):
    cnt = html.count(old)
    if cnt != 1:
        missing.append((i, cnt))
    else:
        html = html.replace(old, new)

print('missing (index, count):', missing)

if not missing:
    with open(HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    print('WROTE BOTH FILES')
else:
    print('ABORTED - fix placeholder text matches first')
