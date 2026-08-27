# Slide Deck: Week 06 — Function
> Week 6 | Topic: Function | 7 slides

---

## Slide 1 — Title
**Key Message**: แตกปัญหาใหญ่เป็นฟังก์ชันย่อยที่อ่านง่ายกว่า

- Week 06 — Function
- 🤖 สัปดาห์นี้เริ่มเปิด AI แบบมีเงื่อนไข (ต้อง disclose + อธิบายได้)

---

## Slide 2 — def / parameter / return
**Key Message**: parameter รับค่าเข้า, return ส่งค่าออก

```python
def add(x, y):
    result = x + y
    return result

print(add(3, 5))
```

**Output:**
```
8
```

[FIGURE: call stack diagram showing add(3, 5) call, parameters bound, and return value flowing back to caller]

---

## Slide 3 — return หยุด function ทันที
**Key Message**: เจอ return ที่ไหน function จบตรงนั้น

```python
def bigger(x, y):
    if x > y:
        return x
    return y

print(bigger(12, 7))
```

**Output:**
```
12
```

---

## Slide 4 — Decomposition
**Key Message**: แยกงานย่อยเป็น function ของตัวเอง

```python
def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

w = 5
h = 3
print(calculate_area(w, h))
print(calculate_perimeter(w, h))
```

**Output:**
```
15
16
```

---

## Slide 5 — Scope
**Key Message**: ตัวแปรใน function ไม่กระทบตัวแปรข้างนอก

```python
count = 0

def increase():
    local_count = count + 1
    return local_count

print(increase())
print(count)
```

**Output:**
```
1
0
```

[FIGURE: box diagram showing outer scope variable count separate from the function's local_count box]

---

## Slide 6 — กฎวิชานี้: return ค่าเดียวเสมอ
**Key Message**: ไม่ return หลายค่าพร้อมกัน — ลดภาระจำ syntax

- ยังไม่เรียน tuple unpacking ใน 7 สัปดาห์นี้
- ถ้าต้องส่งหลายค่า ให้แยกเป็นหลาย function

---

## Slide 7 — Summary + สัปดาห์ถัดไป
**Key Message**: สัปดาห์สุดท้าย — Exception + เตรียม oral defense

- ทบทวน: def, parameter, return, decomposition, scope
- สัปดาห์ 07: try/except, defensive input, oral defense
