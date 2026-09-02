# Slide Deck: Week 07 — Exception
> Week 7 | Topic: Exception | 8 slides

---

## Slide 1 — Title
**Key Message**: สัปดาห์สุดท้าย — เตรียมอธิบายโค้ดของตัวเองให้ได้ทุกบรรทัด

- Week 07 — Exception
- 🤖 AI เปิดเต็มที่ แต่ต้องอธิบายได้ (Oral Defense)

---

## Slide 2 — Exception คืออะไร
**Key Message**: ข้อผิดพลาดที่เกิดตอนโปรแกรม "กำลังรัน" ไม่ใช่ syntax error

- ถ้าไม่จัดการ โปรแกรม crash ทันที

---

## Slide 3 — try / except
**Key Message**: error เกิดที่ไหน กระโดดไป except ทันที บรรทัดที่เหลือใน try ไม่ทำ

```python
a = 10
b = 0
try:
    result = a / b
    print(result)
except ZeroDivisionError:
    print("หารด้วยศูนย์ไม่ได้")
```

**Output:**
```
หารด้วยศูนย์ไม่ได้
```

[FIGURE: flowchart showing try block execution jumping to except block the moment an exception is raised]

---

## Slide 4 — Exception Type ที่พบบ่อย
**Key Message**: แต่ละ error มีชื่อเฉพาะ ต้องจำ 4 ตัวนี้

| Exception | เกิดตอนไหน |
|---|---|
| ZeroDivisionError | หารด้วยศูนย์ |
| ValueError | แปลงชนิดข้อมูลไม่ได้ |
| TypeError | ใช้ตัวดำเนินการผิดชนิด |
| IndexError | index ไม่มีจริงใน list |

---

## Slide 5 — Defensive Function
**Key Message**: try/except ใน function ทำให้ function ปลอดภัยเสมอ

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0

print(safe_divide(10, 2))
print(safe_divide(10, 0))
```

**Output:**
```
5.0
0
```

---

## Slide 6 — Oral Defense คืออะไร
**Key Message**: คะแนนสุดท้ายมาจากการอธิบายโค้ด ไม่ใช่แค่โค้ดรันผ่าน

1. โค้ดนี้ทำอะไร
2. ทำไมเลือกวิธีนี้
3. ถ้า input ผิดปกติจะเกิดอะไรขึ้น
4. ถ้าใช้ AI ช่วย — อธิบายได้ไหมว่าทำไมถูก

---

## Slide 7 — ทบทวนทั้งวิชา 7 สัปดาห์
**Key Message**: จาก "ตัวแปร" ถึง "โปรแกรมที่ทนทานต่อ error"

| Week | Topic |
|:---:|---|
| 1 | In |
| 2 | Out |
| 3 | Selection |
| 4 | Loop |
| 5 | Nested Loop |
| 6 | Function |
| 7 | Exception |

---

## Slide 8 — Summary
**Key Message**: จบวิชา Programming 1 — พร้อมสอบปากเปล่า

- ทบทวน: try/except, exception types, defensive input
- เตรียมตัวสอบ Oral Defense ตามวันที่กำหนด
