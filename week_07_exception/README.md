# Week 07 — Exception
> Topic: Exception | สัปดาห์ที่ 7 จาก 7 (สัปดาห์สุดท้าย) | 3 ชั่วโมง
> 🤖 **นโยบาย AI สัปดาห์นี้:** เปิดเต็มที่ — ใช้ AI ช่วยเขียนได้เต็มที่ **แต่ต้องอธิบายทุกบรรทัดของโค้ดที่ส่งได้ด้วยปากเปล่า** (เตรียม oral defense ท้ายวิชา) ถ้าอธิบายไม่ได้ = ไม่ผ่าน แม้โค้ดจะรันได้ถูกต้องก็ตาม

## เป้าหมายของสัปดาห์นี้
เมื่อจบสัปดาห์นี้ นักศึกษาจะสามารถ:
- อธิบายว่า Exception (ข้อผิดพลาดขณะรันโปรแกรม) คืออะไร ต่างจาก syntax error อย่างไร
- ใช้ `try`/`except` ดักจับข้อผิดพลาดที่พบบ่อยได้
- แยกแยะ Exception type ที่พบบ่อย: `ValueError`, `ZeroDivisionError`, `TypeError`, `IndexError`
- เขียนโปรแกรมรับ input แบบทนทาน (Defensive Input) ที่ไม่ crash ง่าย ๆ
- อธิบายโค้ดของตัวเองได้ทุกบรรทัด (เตรียมสอบปากเปล่าปิดวิชา)

---

## ตารางเวลา

| ช่วง | เวลา | กิจกรรม |
|------|------|---------|
| 1 | 20 นาที | Retrieval quiz Week 06 + Live coding: try/except แรก |
| 2 | 40 นาที | Predict + Trace table: ZeroDivisionError, ValueError, IndexError (3 ตัวอย่าง) |
| 3 | 30 นาที | Peer Instruction: คำถามว่า except ตัวไหนจับ error อะไร |
| 4 | 40 นาที | Workshop: เขียนโปรแกรมรับ input แบบทนทาน (จับคู่ pair programming) |
| 5 | 30 นาที | **ซ้อม Oral Defense** — จับคู่ถามตอบอธิบายโค้ดของตัวเองให้เพื่อนฟัง |
| 6 | 20 นาที | สรุปทั้งวิชา + เตรียมสอบปากเปล่าจริง |

---

## 1. Exception คืออะไร

**Exception (ข้อผิดพลาดขณะรันโปรแกรม)** คือข้อผิดพลาดที่เกิด**ระหว่างโปรแกรมกำลังรัน** (ต่างจาก syntax error ที่ Python จับได้ตั้งแต่ก่อนรัน) เช่น หารด้วยศูนย์ หรือแปลงข้อความที่ไม่ใช่ตัวเลขเป็น `int`

ถ้าไม่จัดการ Exception โปรแกรมจะ **หยุดทำงานทันที (crash)**

---

## 2. try / except พื้นฐาน

```python
a = 10
b = 0
try:
    result = a / b
    print(result)
except ZeroDivisionError:
    print("หารด้วยศูนย์ไม่ได้")
```

Python จะทำโค้ดใน `try:` ก่อน ถ้า**เกิด error ตามชนิดที่ระบุใน `except`** จะกระโดดไปทำ block ใน `except:` ทันที (ไม่ทำบรรทัดที่เหลือใน try)

### Trace ตัวอย่างที่ 1

| ขั้น | เกิดอะไรขึ้น |
|---|---|
| 1 | เข้า `try:` เริ่มทำ `result = a / b` (10 / 0) |
| 2 | Python พบว่าหารด้วย 0 ไม่ได้ → เกิด `ZeroDivisionError` ทันที |
| 3 | บรรทัด `print(result)` **ไม่ถูกทำ** เพราะ error เกิดก่อนถึงบรรทัดนั้น |
| 4 | กระโดดไป `except ZeroDivisionError:` | พิมพ์ ? |

---

## 3. Exception Type ที่พบบ่อย

| Exception | เกิดตอนไหน | ตัวอย่าง |
|---|---|---|
| `ZeroDivisionError` | หารด้วยศูนย์ | `10 / 0` |
| `ValueError` | แปลงชนิดข้อมูลไม่ได้ | `int("abc")` |
| `TypeError` | ใช้ตัวดำเนินการผิดชนิดข้อมูล | `"5" + 3` |
| `IndexError` | เข้าถึง index ที่ไม่มีใน list | `nums[99]` เมื่อ `nums` มีแค่ 3 ตัว |

### Trace ตัวอย่างที่ 2 — ValueError

```python
text_value = "abc"
try:
    number = int(text_value)
    print(number)
except ValueError:
    print("แปลงเป็นตัวเลขไม่ได้")
```

| ขั้น | เกิดอะไรขึ้น |
|---|---|
| 1 | `int("abc")` → "abc" ไม่ใช่ตัวเลข → เกิด `ValueError` |
| 2 | บรรทัด `print(number)` ไม่ถูกทำ | — |
| 3 | กระโดดไป except | พิมพ์ ? |

### Trace ตัวอย่างที่ 3 — IndexError

```python
nums = [3, 7, 2]
try:
    print(nums[5])
except IndexError:
    print("index เกินขอบเขต")
```

| ขั้น | เกิดอะไรขึ้น |
|---|---|
| 1 | `nums` มีแค่ index 0, 1, 2 — `nums[5]` ไม่มีอยู่จริง → เกิด `IndexError` |
| 2 | กระโดดไป except | พิมพ์ ? |

---

## 4. Defensive Input — รับ input แบบทนทาน

รวม Guard pattern (Week 3) + try/except เข้าด้วยกัน เพื่อป้องกันโปรแกรม crash จาก input ที่ผู้ใช้พิมพ์ผิด:

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0

print(safe_divide(10, 2))
print(safe_divide(10, 0))
```

**สังเกต:** เขียน `try`/`except` ไว้**ใน function** ทำให้ function นี้ "ปลอดภัย" (safe) ไม่ว่าจะเรียกด้วยค่าอะไรก็ไม่ crash — เป็น pattern ที่ใช้บ่อยมากในโปรแกรมจริง

---

## แนวคิดสำคัญที่พบในสัปดาห์นี้

| แนวคิด | คำอธิบายสั้น |
|--------|------------|
| Exception (ข้อผิดพลาดขณะรัน) | ข้อผิดพลาดที่เกิดตอนโปรแกรมกำลังทำงาน ไม่ใช่ syntax error |
| try / except | ดักจับ Exception ไม่ให้โปรแกรม crash |
| ZeroDivisionError | หารด้วยศูนย์ |
| ValueError | แปลงชนิดข้อมูลไม่ได้ |
| IndexError | เข้าถึง index ที่ไม่มีจริง |
| Defensive Input | การเขียนโปรแกรมให้ทนทานต่อ input ที่ผิดพลาด |

---

## จบวิชา — เตรียม Oral Defense

วิชา Programming 1 จบที่สัปดาห์นี้ การประเมินท้ายวิชาจะเป็น**การสอบปากเปล่า (Oral Defense)** จากโค้ดที่เขียนไว้ในสัปดาห์ 6-7 คำถามที่ต้องตอบได้:

1. โค้ดส่วนนี้ทำอะไร (อธิบายเป็นประโยคเดียว ไม่ใช่ไล่ทีละบรรทัด)
2. ทำไมถึงเลือกวิธีนี้ (pattern ที่ใช้คืออะไร)
3. ถ้า input เป็นค่าที่ผิดปกติ (0, ค่าว่าง, ค่าติดลบ) จะเกิดอะไรขึ้น
4. ถ้าใช้ AI ช่วยเขียน — ใช้ตรงไหน และทำไมถึงเชื่อว่าโค้ดส่วนนั้นถูกต้อง

---

## Checklist ก่อนออกจากสัปดาห์นี้ (และก่อนจบวิชา)

```
□ อธิบายความต่างระหว่าง syntax error กับ exception ได้
□ ใช้ try/except ดักจับ ZeroDivisionError, ValueError, IndexError ได้
□ เขียน function แบบ defensive (ไม่ crash จาก input ผิดปกติ) ได้
□ อธิบายโค้ดของตัวเองทุกบรรทัดได้ด้วยปากเปล่า (ซ้อมกับเพื่อนแล้ว)
□ ทำ lab_07_starter.py ผ่านครบทุก TODO
```
