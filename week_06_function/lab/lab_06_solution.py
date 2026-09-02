"""
Lab 06 — Function — เฉลย
วิธีรัน: python lab_06_solution.py
"""

# ─── TODO 1: function พื้นฐาน ──────────────────────────────
def multiply(a, b):
    return a * b


print(multiply(6, 7))


# ─── TODO 2: function คืนค่า boolean ───────────────────────
def is_even(n):
    if n % 2 == 0:
        return True
    return False


print(is_even(14))


# ─── TODO 3: Decomposition ─────────────────────────────────
def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi


def classify_bmi(bmi):
    if bmi < 18.5:
        return "ผอม"
    if bmi < 25:
        return "ปกติ"
    return "เกินมาตรฐาน"


w = 65
h = 1.7
bmi = calculate_bmi(w, h)
print(round(bmi, 1))
print(classify_bmi(bmi))
