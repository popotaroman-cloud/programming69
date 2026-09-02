# Slide Deck: Week 03 — Selection
> Week 3 | Topic: Selection | 8 slides

---

## Slide 1 — Title
**Key Message**: เลือกทำ block เดียวตามเงื่อนไข ไม่ใช่ทำทั้งคู่

- Week 03 — Selection

---

## Slide 2 — if / else
**Key Message**: จริงทำ block บน เท็จทำ block ล่าง เลือกได้แค่ 1 block

```python
score = 65
if score >= 50:
    result = "ผ่าน"
else:
    result = "ไม่ผ่าน"
print(result)
```

**Output:**
```
ผ่าน
```

---

## Slide 3 — if / elif / else
**Key Message**: เช็คบนลงล่าง เจอจริงก่อนหยุดทันที

```python
score = 72
if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
else:
    grade = "F"
print(grade)
```

**Output:**
```
B
```

[FIGURE: flowchart decision tree showing if/elif/else checking conditions top to bottom and stopping at first true condition]

---

## Slide 4 — Boolean: and / or / not
**Key Message**: and ต้องจริงทั้งคู่ — or จริงข้างใดข้างหนึ่งพอ

| ตัวดำเนินการ | ต้องจริงกี่ข้าง |
|---|---|
| `and` | ทั้งคู่ |
| `or` | ข้างใดข้างหนึ่ง |

---

## Slide 5 — Chained Comparison
**Key Message**: `a < x < b` เช็คช่วงค่าในนิพจน์เดียว อ่านง่ายเหมือนคณิตศาสตร์

```python
x = 19
if 4 < x < 36:
    result = "อยู่ในช่วง"
else:
    result = "อยู่นอกช่วง"
print(result)
```

**Output:**
```
อยู่ในช่วง
```

- เทียบเท่ากับ `x > 4 and x < 36`
- ใช้ได้ในวิชานี้ (ไม่ใช่ shorthand ที่ต้องเลี่ยง — ต่างจาก ternary)

---

## Slide 6 — Guard Pattern
**Key Message**: เช็คเงื่อนไขอันตรายก่อนทำงานจริงเสมอ

```python
a = 10
b = 0
if b != 0:
    result = a / b
    print(result)
else:
    print("หารด้วยศูนย์ไม่ได้")
```

**Output:**
```
หารด้วยศูนย์ไม่ได้
```

---

## Slide 7 — Nested if
**Key Message**: if ข้างในทำงานก็ต่อเมื่อ if ข้างนอกเป็นจริง

[FIGURE: nested box diagram showing an inner if condition only evaluated when the outer if is true]

---

## Slide 8 — Summary + สัปดาห์ถัดไป
**Key Message**: สัปดาห์หน้าคือหัวใจของวิชา — Loop

- ทบทวน: if/elif/else, and/or, chained comparison, guard
- สัปดาห์ 04: while loop, for loop, accumulator pattern
