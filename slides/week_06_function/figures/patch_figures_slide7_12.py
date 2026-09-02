\
# -*- coding: utf-8 -*-
import re

b64_text = open(r"E:\Temp\fig_b64.txt", encoding='utf-8').read()
b64_1, b64_2 = b64_text.split('\n===SPLIT===\n')
b64_1 = b64_1.strip()
b64_2 = b64_2.strip()

PLACEHOLDER_1 = '<div class="placeholder">\U0001F4CA <em>diagram contrasting a "def" block (declaration only, body not executed) with a "call site" line (jumps into the function, executes the body, returns control) — arrows showing control flow only happens at the call</em></div>'
PLACEHOLDER_2 = '<div class="placeholder">\U0001F4CA <em>diagram of <code>def introduce(name, age):</code> showing name and age as empty labeled slots, connected by arrows from <code>introduce("Aom", 20)</code> showing "Aom" binding to the name slot and 20 binding to the age slot by position</em></div>'

FIG_1 = '<div class="slide-figure"><img src="data:image/png;base64,%s" alt="def vs call diagram"></div>' % b64_1
FIG_2 = '<div class="slide-figure"><img src="data:image/png;base64,%s" alt="parameter vs argument diagram"></div>' % b64_2

for path in [
    r"E:\2569\programming\.claude\worktrees\session-aedcf8\week_06_function\slides\06_function.html",
    r"E:\2569\programming\.claude\worktrees\session-aedcf8\week_06_function\slides\index.html",
]:
    text = open(path, encoding='utf-8').read()
    n1 = text.count(PLACEHOLDER_1)
    n2 = text.count(PLACEHOLDER_2)
    if n1 != 1 or n2 != 1:
        raise SystemExit("MISMATCH in %s: n1=%d n2=%d" % (path, n1, n2))
    text = text.replace(PLACEHOLDER_1, FIG_1)
    text = text.replace(PLACEHOLDER_2, FIG_2)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    print(path, 'patched OK')
