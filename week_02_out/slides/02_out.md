# Slide Deck: Week 02 — Out (แสดงผลออก)
> Week 2 | Topic: Out | 6 slides

---

## Slide 1 — Title
**Key Message**: การแสดงผลที่อ่านง่าย เริ่มจาก f-string

- Week 02 — Out (แสดงผลออก)

---

## Slide 2 — print() หลายค่า
**Key Message**: คั่นด้วยจุลภาค Python เว้นวรรคให้อัตโนมัติ

```python
name = "Nan"
score = 85
print(name, score)
```

**Output:**
```
Nan 85
```

---

## Slide 3 — f-string
**Key Message**: `f"...{ตัวแปร}..."` คือวิธีเดียวที่วิชานี้ใช้แทรกค่าตัวแปร

```python
name = "Nan"
score = 85
print(f"{name} ได้ {score} คะแนน")
```

**Output:**
```
Nan ได้ 85 คะแนน
```

- สังเกต: template `{name}`/`{score}` ถูกแทนที่ด้วยค่าจริงในผลลัพธ์

---

## Slide 4 — round() จัดรูปแบบทศนิยม
**Key Message**: ปัดเศษก่อนแสดงผลให้อ่านง่าย

```python
score = 88
total = 120
percent = score / total * 100
print(round(percent, 1))
```

**Output:**
```
73.3
```

---

## Slide 5 — Trace ตัวอย่าง
**Key Message**: ไล่ทีละบรรทัดก่อนรันเสมอ

[FIGURE: trace table showing variable state after each line for the receipt example]

---

## Slide 6 — Summary + สัปดาห์ถัดไป
**Key Message**: สัปดาห์หน้าเรียนเรื่อง Selection — การเลือกทำตามเงื่อนไข

- ทบทวน: print หลายค่า, f-string, round()
- สัปดาห์ 03: if/elif/else, boolean, guard pattern
