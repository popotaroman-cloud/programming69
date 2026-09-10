"""
Lab 07 — Exception — เฉลย
วิธีรัน: python lab_07_solution.py
"""

# ─── TODO 1: try/except ZeroDivisionError ─────────────────
a = 20
b = 0
try:
    result = a / b
    print(result)
except ZeroDivisionError:
    print("error: divide by zero")


# ─── TODO 2: try/except ValueError ────────────────────────
text_value = "25x"
try:
    number = int(text_value)
    print(number)
except ValueError:
    print("error: cannot convert")


# ─── TODO 3: Defensive function ───────────────────────────
def safe_get(items, index):
    try:
        return items[index]
    except IndexError:
        return None


nums = [10, 20, 30]
print(safe_get(nums, 1))
print(safe_get(nums, 9))
