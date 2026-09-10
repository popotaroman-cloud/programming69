"""
Lab 07 — Exception (สัปดาห์สุดท้าย)
วิธีรัน: python lab_07_starter.py
นโยบาย AI สัปดาห์นี้: เปิดเต็มที่ แต่ต้องอธิบายทุกบรรทัดได้ด้วยปากเปล่า (เตรียม oral defense)
"""

# ─── TODO 1: try/except ZeroDivisionError (Easy) ─────────
# สิ่งที่ต้องทำ: a = 20, b = 0
#              ใช้ try/except ดักหารด้วยศูนย์
#              ถ้าหารได้ พิมพ์ result
#              ถ้าหารด้วยศูนย์ พิมพ์ "error: divide by zero"
# Expected output: error: divide by zero
# ─────────────────────────────────────────────────────────
raise NotImplementedError("TODO 1: implement this")


# ─── TODO 2: try/except ValueError (Medium) ──────────────
# สิ่งที่ต้องทำ: text_value = "25x"
#              ใช้ try/except ดักการแปลง int() ที่ผิดพลาด
#              ถ้าแปลงได้ พิมพ์ number
#              ถ้าแปลงไม่ได้ พิมพ์ "error: cannot convert"
# Expected output: error: cannot convert
# ─────────────────────────────────────────────────────────
raise NotImplementedError("TODO 2: implement this")


# ─── TODO 3: Defensive function (Hard) ───────────────────
# สิ่งที่ต้องทำ: เขียน function safe_get(items, index)
#              ใน try: return items[index]
#              ใน except IndexError: return None
#              nums = [10, 20, 30]
#              พิมพ์ safe_get(nums, 1) บรรทัดแรก
#              พิมพ์ safe_get(nums, 9) บรรทัดสอง (index เกินขอบเขต)
# Pattern ที่ใช้: Defensive Input (Guard + try/except ผสมกัน)
# Expected output: 20
#                  None
# ─────────────────────────────────────────────────────────
raise NotImplementedError("TODO 3: implement this")
