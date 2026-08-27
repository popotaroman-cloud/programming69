# Slide Deck: Week 04 — Loop
> Week 4 | Topic: Loop | 12 slides

---

## Slide 1 — Title
**Key Message**: สัปดาห์นี้คือหัวใจของวิชา — trace ทุกตัวอย่างด้วยมือ

- Week 04 — Loop

---

## Slide 2 — while loop
**Key Message**: เช็คเงื่อนไขก่อนทำงานทุกรอบ

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

**Output:**
```
1
2
3
4
5
```

[FIGURE: loop diagram showing the back-edge arrow from end of loop body returning to the condition check]

---

## Slide 3 — while loop ก้าวกระโดด
**Key Message**: บวกกี่ก็ได้ ไม่จำเป็นต้องทีละ 1

```python
i = 2
while i < 10:
    print(i)
    i += 2
```

**Output:**
```
2
4
6
8
```

---

## Slide 4 — while loop เงื่อนไขผสม
**Key Message**: ใช้ and/or/not จาก Week 03 ผสมในเงื่อนไข while ได้

```python
nums = list(range(6))
target = 4
i = 0
found = False
while i < len(nums) and not found:
    if nums[i] == target:
        found = True
    i += 1
print(i)
```

**Output:**
```
5
```

- หยุดได้จากหลายเหตุผลพร้อมกัน (หลุดขอบเขต หรือ เจอแล้ว)

[FIGURE: flowchart showing a while loop condition combining an index bound check and a found flag with 'and not']

---

## Slide 5 — for loop + range()
**Key Message**: range(a, b) ไม่รวม b — จุดพลาดอันดับ 1

```python
for i in range(1, 6):
    print(i)
```

**Output:**
```
1
2
3
4
5
```

---

## Slide 6 — Accumulator Pattern
**Key Message**: ตั้งค่าเริ่มต้นก่อน loop แล้วสะสมค่าทีละรอบ

```python
total = 0
for i in range(1, 6):
    total = total + i
print(total)
```

**Output:**
```
15
```

[FIGURE: trace table showing i and total values changing across 5 loop iterations]

---

## Slide 7 — Max / Min Pattern
**Key Message**: ตั้งแชมป์ชั่วคราว แล้วเทียบทีละตัว (กลับทิศเทียบสำหรับ Min)

```python
nums = [12, 45, 7, 39, 21]
mx = nums[0]
for n in nums:
    if n > mx:
        mx = n
print(mx)
```

**Output:**
```
45
```

- Min pattern: เปลี่ยนแค่ `>` เป็น `<`

---

## Slide 8 — Count Pattern
**Key Message**: บวก 1 เมื่อเข้าเงื่อนไข ไม่ใช่บวกค่าตรง ๆ

```python
nums = [10, 27, 8, 39, 35]
count = 0
for n in nums:
    if n > 22:
        count += 1
print(count)
```

**Output:**
```
3
```

- ต่างจาก Accumulator ที่บวกค่า n เข้าไปตรง ๆ

---

## Slide 9 — Off-by-one
**Key Message**: "รอบสุดท้ายที่ทำงาน" ≠ "ค่าตัวแปรหลังจบ loop"

```python
i = 5
print("i during last iteration =", i)
i += 1
print("i right after while exits =", i)
```

**Output:**
```
i during last iteration = 5
i right after while exits = 6
```

---

## Slide 10 — Trace ตัวอย่างรวม
**Key Message**: ฝึก trace ให้คล่อง คือกุญแจของสัปดาห์นี้

[FIGURE: trace table combining while loop and accumulator pattern for a full worked example]

---

## Slide 11 — สรุป Pattern ทั้งหมดของสัปดาห์นี้
**Key Message**: 4 pattern หลักที่ต้องจำได้แม่น

| Pattern | ใช้ทำอะไร |
|---|---|
| Accumulator | สะสมผลรวม |
| Count | นับจำนวนที่ตรงเงื่อนไข |
| Max/Min | หาค่ามาก/น้อยสุด |
| while เงื่อนไขผสม | หยุดก่อนกำหนดจากหลายเหตุผล |

---

## Slide 12 — Summary + สัปดาห์ถัดไป
**Key Message**: สัปดาห์หน้าคือ Nested Loop — loop ซ้อน loop

- ทบทวน: while, step>1, เงื่อนไขผสม, for, accumulator, count, max/min, off-by-one
- สัปดาห์ 05: nested loop, search/flag, filter, break/continue
