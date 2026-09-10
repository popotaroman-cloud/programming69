\
# -*- coding: utf-8 -*-
b64_text = open(r"E:\Temp\fig_w7_b64.txt", encoding='utf-8').read()
parts = [p.strip() for p in b64_text.split('\n===SPLIT===\n') if p.strip()]
assert len(parts) == 6, len(parts)
b64 = dict(zip(['fig1','fig2','fig3','fig4','fig5','fig6'], parts))

PLACEHOLDERS = [
    ('fig1', '<div class="placeholder">\U0001F4CA <em>timeline diagram comparing syntax error (detected during parsing, before any line runs, program never starts) versus exception (detected mid-execution after some lines have already run successfully, program stops at that line)</em></div>'),
    ('fig2', '<div class="placeholder">\U0001F4CA <em>flowchart showing execution flowing top-to-bottom through the try block, jumping immediately to the matching except block the moment an exception is raised, skipping all remaining try statements, then continuing to code after the whole try/except structure</em></div>'),
    ('fig3', '<div class="placeholder">\U0001F4CA <em>flowchart showing try block execution branching to except block on error or else block on success, with finally block always executing last on every path regardless of which branch was taken</em></div>'),
    ('fig4', '<div class="placeholder">\U0001F4CA <em>tree diagram — BaseException at root, branching to Exception and SystemExit/KeyboardInterrupt; under Exception show ArithmeticError branching to ZeroDivisionError/OverflowError/FloatingPointError, and LookupError branching to IndexError/KeyError</em></div>'),
    ('fig5', '<div class="placeholder">\U0001F4CA <em>call-stack diagram showing an outer try/except/finally wrapping an inner try/except/finally, with an arrow showing an exception raised inside the inner try bypassing the inner except (type mismatch) and flowing up to the outer except, passing through both finally blocks along the way</em></div>'),
    ('fig6', '<div class="placeholder">\U0001F4CA <em>diagram showing an except block catching an original exception (ValueError), then raising a new exception (ConfigError/SignupError); one path labeled "raise NewErr(...) from e" pointing to __cause__ set + shown in traceback; another path labeled "raise NewErr(...) from None" pointing to __cause__ = None, __context__ still recorded but suppressed in traceback; a third path labeled "raise NewErr(...) with no from" pointing to __context__ recorded and shown in traceback with the "During handling..." separator line</em></div>'),
]

ALTS = {
    'fig1': 'syntax error vs exception timing diagram',
    'fig2': 'try except control flow diagram',
    'fig3': 'try except else finally flowchart',
    'fig4': 'exception hierarchy tree diagram',
    'fig5': 'nested try except finally flow diagram',
    'fig6': 'exception chaining cause context diagram',
}

for path in [
    r"E:\2569\programming\.claude\worktrees\session-aedcf8\week_07_exception\slides\07_exception.html",
    r"E:\2569\programming\.claude\worktrees\session-aedcf8\week_07_exception\slides\index.html",
]:
    text = open(path, encoding='utf-8').read()
    for key, placeholder in PLACEHOLDERS:
        n = text.count(placeholder)
        if n != 1:
            raise SystemExit("MISMATCH %s in %s: count=%d" % (key, path, n))
        fig_html = '<div class="slide-figure"><img src="data:image/png;base64,%s" alt="%s"></div>' % (b64[key], ALTS[key])
        text = text.replace(placeholder, fig_html)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    print(path, 'patched OK')
