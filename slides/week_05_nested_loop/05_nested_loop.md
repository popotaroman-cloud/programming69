# Slide Deck: Week 05 — Nested Loop
> Week 5 | Topic: Nested Loop | 10 slides

---

## Slide 1 — Title
**Key Message**: loop ในทำงานครบก่อน loop นอกขยับ

- Week 05 — Nested Loop

---

## Slide 2 — Nested Loop
**Key Message**: 2 loop × 3 loop = 6 รอบทำงานรวม

```python
for i in range(1, 3):
    for j in range(1, 4):
        print(i, j)
```

**Output:**
```
1 1
1 2
1 3
2 1
2 2
2 3
```

[FIGURE: nested loop diagram showing outer loop i and inner loop j, inner completing all 3 rounds before outer advances]

---

## Slide 3 — Nested Loop จำนวนรอบไม่คงที่
**Key Message**: ขอบเขต loop ข้างในอ้างอิงค่า loop ข้างนอกได้

```python
rows = []
for i in range(1, 4):
    row_sum = 0
    for j in range(1, i + 1):
        row_sum += j
    rows.append(row_sum)
print(rows)
```

**Output:**
```
[1, 3, 6]
```

- `range(1, i + 1)` เปลี่ยนไปตาม i แต่ละรอบ

---

## Slide 4 — Matrix (List ซ้อน List)
**Key Message**: loop นอกวนแต่ละแถว loop ในวนแต่ละค่าในแถว

```python
matrix = [[8, 5, 7], [5, 7, 7], [7, 8, 4]]
total = 0
for row in matrix:
    for val in row:
        total += val
print(total)
```

**Output:**
```
58
```

[FIGURE: grid diagram showing a matrix with outer loop iterating rows and inner loop iterating values within each row]

---

## Slide 5 — Search/Flag Pattern
**Key Message**: ตั้ง found = False ก่อน แล้วเปลี่ยนเป็น True เมื่อเจอ

```python
nums = [15, 8, 42, 23, 4]
target = 23
found = False
for n in nums:
    if n == target:
        found = True
print(found)
```

**Output:**
```
True
```

---

## Slide 6 — Filter Pattern
**Key Message**: สร้าง list ว่าง แล้ว append ค่าที่ผ่านเงื่อนไข

```python
nums = [5, 18, 32, 7, 41, 9]
result = []
for n in nums:
    if n > 15:
        result.append(n)
print(result)
```

**Output:**
```
[18, 32, 41]
```

> ⚠️ ห้ามใช้ list comprehension เด็ดขาด

---

## Slide 7 — break vs continue
**Key Message**: break หยุดทั้ง loop — continue ข้ามแค่รอบนี้

| คำสั่ง | ผล |
|---|---|
| `break` | หยุด loop ทันที |
| `continue` | ข้ามไปรอบถัดไป |

```python
nums = [4, 9, 16, 25, 36]
collected = []
for n in nums:
    if n == 16:
        break
    collected.append(n)
print(collected)
```

**Output:**
```
[4, 9]
```

```python
nums = [3, 17, 9, 22, 6]
result = []
for n in nums:
    if n > 15:
        continue
    result.append(n)
print(result)
```

**Output:**
```
[3, 9, 6]
```

---

## Slide 8 — Search Index Pattern
**Key Message**: รวม Search + break เพื่อหา "ตำแหน่ง" ของตัวแรกที่เจอ

```python
nums = [6, 15, 35, 16, 17]
target = 15
idx = -1
for i in range(len(nums)):
    if nums[i] == target:
        idx = i
        break
print(idx)
```

**Output:**
```
1
```

- ไม่มี break = ได้ index ของตัว**สุดท้าย**ที่เจอแทน

---

## Slide 9 — Trace ตัวอย่างรวม
**Key Message**: ฝึก trace nested loop ให้คล่องก่อนไปสัปดาห์หน้า

[FIGURE: trace table for nested loop combined with a filter pattern worked example]

---

## Slide 10 — Summary + สัปดาห์ถัดไป
**Key Message**: สัปดาห์หน้าเริ่มเปิดให้ใช้ AI แบบมีเงื่อนไข — Function

- ทบทวน: nested loop (คงที่/ไม่คงที่/matrix), search/flag, filter, break/continue, search index
- สัปดาห์ 06: def, parameter, return, decomposition
