# Week 06 — Function
> Topic: Function | สัปดาห์ที่ 6 จาก 7 | 3 ชั่วโมง
> 🤖 **นโยบาย AI สัปดาห์นี้:** เปิดแบบมีเงื่อนไข — ใช้ได้เฉพาะช่วยอธิบาย/debug เท่านั้น **ต้อง disclose ว่าใช้ AI ตรงไหน และต้องอธิบายทุกบรรทัดของโค้ดที่ส่งได้ด้วยตัวเอง** ถ้าอธิบายไม่ได้ถือว่าไม่เข้าใจ ให้กลับไปเขียนเอง

## เป้าหมายของสัปดาห์นี้
เมื่อจบสัปดาห์นี้ นักศึกษาจะสามารถ:
- ประกาศ function ด้วย `def` และเรียกใช้ได้
- ใช้ parameter ส่งค่าเข้า function และใช้ `return` ส่งค่าออกได้
- แตกปัญหาใหญ่เป็นฟังก์ชันย่อย (decomposition) ได้
- อธิบาย scope เบื้องต้น (ตัวแปรใน function เข้าถึงข้างนอกไม่ได้)

---

## ตารางเวลา

| ช่วง | เวลา | กิจกรรม |
|------|------|---------|
| 1 | 20 นาที | Retrieval quiz Week 05 + Live coding: function แรก |
| 2 | 40 นาที | Predict + Trace table: def/parameter/return, call stack (3 ตัวอย่าง) |
| 3 | 30 นาที | Peer Instruction: คำถาม scope (ตัวแปรใน function เห็นข้างนอกไหม) |
| 4 | 40 นาที | Workshop: แตกโปรแกรมยาวเป็นฟังก์ชันย่อย (จับคู่ pair programming) |
| 5 | 30 นาที | Explain in Plain English + fix bug (return ผิดตำแหน่ง/ไม่มี return) |
| 6 | 20 นาที | สรุป + แจกโจทย์กลับบ้าน |

---

## 1. def / parameter / return พื้นฐาน

```python
def add(x, y):
    result = x + y
    return result

answer = add(3, 5)
print(answer)
```

**Function (ฟังก์ชัน)** คือ "คำสั่งชุดหนึ่งที่ตั้งชื่อไว้ เรียกใช้ซ้ำได้" — `x`, `y` คือ **Parameter (พารามิเตอร์)** ค่าที่รับเข้ามา ส่วน `return` คือคำสั่งที่ **ส่งค่าออกจาก function กลับไปให้ผู้เรียก**

> **กฎของวิชานี้:** function ทุกตัวใน 7 สัปดาห์นี้ **`return` ค่าเดียวเสมอ** ไม่ return หลายค่าพร้อมกัน (เพื่อไม่ต้องเรียนเรื่อง tuple unpacking ก่อนเวลา)

### Trace ตัวอย่างที่ 1 — call stack (การเรียกใช้ function)

| ขั้น | เกิดอะไรขึ้น |
|---|---|
| 1 | โปรแกรมเรียก `add(3, 5)` |
| 2 | เข้าไปใน function: `x = 3`, `y = 5` (ตั้งจาก parameter) |
| 3 | คำนวณ `result = x + y` → result = ? |
| 4 | `return result` → ส่งค่ากลับออกมา |
| 5 | ค่าที่ return มาถูกเก็บใน `answer` | answer = ? |
| 6 | `print(answer)` | พิมพ์ ? |

---

## 2. return หยุด function ทันที

```python
def bigger(x, y):
    if x > y:
        return x
    return y

print(bigger(12, 7))
```

**ข้อสำคัญ:** เมื่อเจอ `return` function จะ**จบทันที** บรรทัดหลังจากนั้นในrun นั้นจะไม่ทำงาน — ในตัวอย่างนี้ถ้า `x > y` เป็นจริง จะ `return x` แล้วจบเลย ไม่ไปแตะบรรทัด `return y`

### Trace ตัวอย่างที่ 2

| ขั้น | เช็ค | ผล |
|---|---|---|
| 1 | เรียก `bigger(12, 7)` → x=12, y=7 | — |
| 2 | `if x > y:` (12 > 7) | ? |
| 3 | ถ้าจริง → `return x` (จบ function ทันที) | ผลลัพธ์ = ? |

---

## 3. Decomposition — แตกปัญหาใหญ่เป็นฟังก์ชันย่อย

```python
def calculate_area(width, height):
    area = width * height
    return area

def calculate_perimeter(width, height):
    perimeter = 2 * (width + height)
    return perimeter

w = 5
h = 3
print(calculate_area(w, h))
print(calculate_perimeter(w, h))
```

**Decomposition (การแตกปัญหา)** คือหลักการเขียนโปรแกรมที่สำคัญที่สุดของสัปดาห์นี้ — แทนที่จะเขียนทุกอย่างในบล็อกเดียวยาว ๆ ให้**แยกงานย่อยแต่ละอย่างเป็น function ของตัวเอง** ทำให้โค้ดอ่านง่าย แก้ง่าย และเทสได้ทีละส่วน

---

## 4. Scope — ตัวแปรใน function มองไม่เห็นจากข้างนอก

```python
count = 0

def increase():
    local_count = count + 1
    return local_count

print(increase())
print(count)
```

**Scope (ขอบเขตของตัวแปร)** — ตัวแปรที่สร้างข้างใน function (`local_count`) เป็นของ function นั้นเท่านั้น เมื่อ function จบ ตัวแปรนั้นก็หายไป **ตัวแปรข้างนอก (`count`) จะไม่ถูกแก้ไข** แม้จะมีการคำนวณโดยอิงค่ามันในฟังก์ชันก็ตาม

### Trace ตัวอย่างที่ 3

| บรรทัด | เกิดอะไรขึ้น | ค่า `count` (ตัวแปรข้างนอก) |
|---|---|---|
| `count = 0` | สร้างตัวแปรข้างนอก | ? |
| `print(increase())` | เข้า function, คำนวณ local_count = count+1 = ?, return ค่านั้น, พิมพ์ ? | ? (เปลี่ยนไหม) |
| `print(count)` | พิมพ์ค่า count ข้างนอกอีกครั้ง | พิมพ์ ? |

---

## แนวคิดสำคัญที่พบในสัปดาห์นี้

| แนวคิด | คำอธิบายสั้น |
|--------|------------|
| Function (ฟังก์ชัน) | คำสั่งชุดหนึ่งที่ตั้งชื่อไว้ เรียกใช้ซ้ำได้ |
| Parameter (พารามิเตอร์) | ค่าที่รับเข้ามาตอนเรียก function |
| return | ส่งค่าออกจาก function และจบ function ทันที |
| Decomposition (การแตกปัญหา) | แยกงานใหญ่เป็นฟังก์ชันย่อยที่อ่านง่ายกว่า |
| Scope (ขอบเขตตัวแปร) | ตัวแปรใน function ไม่กระทบตัวแปรข้างนอก |

---

## สัปดาห์ถัดไป

**Week 07 — Exception**

จะเรียนรู้:
- `try`/`except` จัดการข้อผิดพลาดขณะรันโปรแกรม
- Exception type ที่พบบ่อย
- **สัปดาห์สุดท้าย — เปิดใช้ AI เต็มที่ แต่ต้องอธิบายทุกบรรทัดได้ (เตรียม oral defense)**

---

## Checklist ก่อนออกจากสัปดาห์นี้

```
□ ประกาศและเรียกใช้ function ที่มี parameter + return ได้
□ อธิบายได้ว่า return ทำให้ function จบทันที
□ แตกโปรแกรมยาว ๆ เป็นฟังก์ชันย่อยได้อย่างสมเหตุสมผล
□ อธิบาย scope ได้ว่าทำไมตัวแปรข้างนอกไม่ถูกแก้ไขจากใน function
□ ทำ lab_06_starter.py ผ่านครบทุก TODO
```
