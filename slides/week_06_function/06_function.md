# Slide Deck: Week 06 — Function
> Week 6 | Topic: Function | 79 slides

---

## Slide 1 — Title
**Key Message**: จากแนวคิดพื้นฐานของฟังก์ชัน สู่การออกแบบโปรแกรมระดับมืออาชีพ

- Week 06 — Function (ฉบับเต็ม 15 หัวข้อ: พื้นฐาน / กลาง / สูง)
- ส่วนที่ 1 (หัวข้อ 1–5): เนื้อหาหลัก อยู่ในขอบเขตสอบของวิชานี้
- ส่วนที่ 2–3 (หัวข้อ 6–15): เนื้อหาเสริม นอกขอบเขตสอบ สำหรับผู้ที่อยากเข้าใจลึกขึ้น
- 🤖 สัปดาห์นี้เริ่มเปิด AI แบบมีเงื่อนไข (ต้อง disclose + อธิบายได้)

---

## Slide 2 — จุดประสงค์ของฟังก์ชัน: DRY และ Decomposition
**Key Message**: แตกปัญหาใหญ่เป็นฟังก์ชันย่อยที่อ่านง่ายกว่า

- ฟังก์ชัน = กลุ่มคำสั่งที่ตั้งชื่อไว้ เรียกใช้ซ้ำได้หลายครั้งโดยไม่ต้องเขียนคำสั่งเดิมซ้ำใหม่ทุกครั้ง
- หลักการ **DRY (Don't Repeat Yourself)**: เขียนตรรกะไว้ที่เดียว แล้วเรียกใช้ซ้ำ แทนการคัดลอกวางหลายจุด
- **Decomposition**: แตกปัญหาใหญ่ที่ซับซ้อนให้กลายเป็นปัญหาย่อย แต่ละส่วนเขียนเป็นฟังก์ชันของตัวเอง
- ผลลัพธ์: โปรแกรมอ่านง่ายขึ้น ทดสอบแยกส่วนได้ ดูแลรักษาง่ายขึ้นในระยะยาว
- ไวยากรณ์ Python: สร้างฟังก์ชันด้วย `def ชื่อฟังก์ชัน(...):`

---

## Slide 3 — ตัวอย่าง: คำนวณพื้นที่สี่เหลี่ยม (DRY กับตัวเลข)
**Key Message**: ฟังก์ชันเดียว เรียกซ้ำได้หลายครั้งด้วยค่าต่างกัน

```python
def calculate_area(width, height):
    return width * height

print(calculate_area(4, 5))
print(calculate_area(6, 2))
print(calculate_area(3, 3))
```

**Output:**
```
20
12
9
```

- ฟังก์ชันเดียวถูกเรียกซ้ำ 3 ครั้งด้วยอาร์กิวเมนต์ต่างกัน — ตัวอย่าง DRY ที่ชัดเจนที่สุด

---

## Slide 4 — ตัวอย่าง: จัดรูปแบบรายการใบเสร็จ (DRY กับข้อความ)
**Key Message**: DRY ใช้ได้กับงานข้อความ ไม่ได้จำกัดแค่การคำนวณ

```python
def format_receipt_line(item, price):
    return f"{item} ราคา {price} บาท"

print(format_receipt_line("กาแฟ", 45))
print(format_receipt_line("ขนมปัง", 30))
print(format_receipt_line("นม", 25))
```

**Output:**
```
กาแฟ ราคา 45 บาท
ขนมปัง ราคา 30 บาท
นม ราคา 25 บาท
```

- ตรรกะการจัดรูปแบบข้อความถูกเขียนไว้ที่เดียว แล้วเรียกใช้ซ้ำกับสินค้าหลายรายการ

---

## Slide 5 — ตัวอย่าง: ไม่ทำ DRY แล้วพิมพ์สูตรผิด
**Key Message**: คัดลอกสูตรซ้ำ = เสี่ยงพิมพ์ผิดโดยไม่รู้ตัว

```python
def celsius_to_fahrenheit_v1(celsius):
    return celsius * 9 / 5 + 32

def celsius_to_fahrenheit_v2(celsius):
    return celsius * 9 / 5 + 3   # คัดลอกสูตรมาเขียนใหม่ พิมพ์ผิด: ลืมเลข 2

print(celsius_to_fahrenheit_v1(20))
print(celsius_to_fahrenheit_v2(20))
```

**Output:**
```
68.0
39.0
```

- ตั้งใจให้สองฟังก์ชันคำนวณเหมือนกัน แต่การคัดลอกสูตรแทนการเรียกใช้ฟังก์ชันเดิมซ้ำทำให้พิมพ์ผิด ผลลัพธ์จึงไม่ตรงกัน

---

## Slide 6 — สรุป: ทำไม DRY ถึงสำคัญ
**Key Message**: แก้สูตรที่จุดเดียว ปลอดภัยกว่าคัดลอกวางหลายจุด

- เขียนตรรกะการคำนวณไว้ที่เดียว หากภายหลังต้องแก้สูตร ก็แก้เพียงจุดเดียว
- ถ้าคัดลอกวางตรรกะเดียวกันไว้หลายแห่ง การแก้ไขหรือพิมพ์ผิดที่จุดหนึ่งจะไม่ส่งผลไปยังจุดอื่นโดยอัตโนมัติ ทำให้โปรแกรมไม่สอดคล้องกัน
- DRY ใช้ได้ผลทั้งกับโดเมนตัวเลข (เรขาคณิต) และโดเมนข้อความ (การจัดรูปแบบ)

---

## Slide 7 — Function Definition กับ Function Call
**Key Message**: นิยามฟังก์ชันแค่ประกาศไว้ ยังไม่รันจนกว่าจะถูกเรียกใช้

- การใช้งานฟังก์ชันแบ่งเป็น 2 ขั้นตอนที่แยกจากกันชัดเจน: **definition** (นิยาม) กับ **call** (เรียกใช้)
- Definition: บอกชื่อฟังก์ชัน รับข้อมูลอะไร มีคำสั่งอะไรภายใน — เป็นเพียงการ "ประกาศ" ไว้ คำสั่งภายในยังไม่ถูกรัน
- Call: จุดที่โปรแกรมกระโดดเข้าไปรันคำสั่งภายในฟังก์ชันนั้นจริง ๆ
- นิยามฟังก์ชันได้เพียงครั้งเดียว แต่เรียกใช้ได้หลายครั้งตามต้องการ
- ไวยากรณ์: นิยามด้วย `def ชื่อฟังก์ชัน():` ตามด้วยบล็อกเยื้อง; เรียกใช้ด้วย `ชื่อฟังก์ชัน()`

[FIGURE: diagram contrasting a "def" block (declaration only, body not executed) with a "call site" line (jumps into the function, executes the body, returns control) — arrows showing control flow only happens at the call]

---

## Slide 8 — ตัวอย่าง: ทักทายซ้ำสองครั้ง
**Key Message**: นิยามครั้งเดียว แต่เรียกใช้ได้หลายครั้ง แต่ละครั้งรันจริง

```python
def greet():
    print("สวัสดี")

print("ก่อนเรียก")
greet()
greet()
print("หลังเรียก")
```

**Output:**
```
ก่อนเรียก
สวัสดี
สวัสดี
หลังเรียก
```

- บรรทัด `def` ไม่รันคำสั่งใด ๆ ทันที การเรียก `greet()` แต่ละครั้งต่างหากที่ทำให้ `print("สวัสดี")` ทำงาน

---

## Slide 9 — ตัวอย่าง: เรียกซ้ำอัตโนมัติผ่านลูป
**Key Message**: เรียกฟังก์ชันเดิมซ้ำได้อัตโนมัติผ่าน for loop

```python
def square(number):
    return number * number

numbers = [2, 3, 4]
for n in numbers:
    print(square(n))
```

**Output:**
```
4
9
16
```

- ไม่ต้องพิมพ์เรียกฟังก์ชันด้วยมือทีละครั้ง — `for` loop เรียก `square(n)` ซ้ำให้อัตโนมัติ

---

## Slide 10 — ตัวอย่าง: นิยามฟังก์ชันแล้วลืมเรียกใช้
**Key Message**: นิยามฟังก์ชันไม่ทำให้โค้ดข้างในรันเอง

```python
def show_message():
    print("ทำงานแล้ว")

print("เริ่มโปรแกรม")
print("จบโปรแกรม")
```

**Output:**
```
เริ่มโปรแกรม
จบโปรแกรม
```

- ไม่มีบรรทัด `show_message()` ปรากฏในโปรแกรม จึงไม่มีข้อความ "ทำงานแล้ว" ใน output เลย — และไม่มี error แจ้งเตือนด้วย

---

## Slide 11 — ข้อผิดพลาดที่พบบ่อย: def ไม่ใช่การรัน
**Key Message**: def ไม่ใช่การรัน ต้องมีวงเล็บเรียกใช้เสมอ

- ผู้เริ่มต้นมักเข้าใจผิดว่านิยามฟังก์ชัน (`def`) เพียงอย่างเดียวจะทำให้โค้ดภายในทำงานทันที — ความจริงต้องมีการเรียกใช้ (call) ด้วยเสมอ
- ต้องแยกให้ออก: บรรทัดที่มี `def` คือการนิยาม ส่วนบรรทัดที่เรียกชื่อฟังก์ชันตามด้วยวงเล็บคือการเรียกใช้
- ตัวอย่าง: ฟังก์ชัน `add` นิยามด้วย `def` แล้วเรียกใช้ด้วย `add(3, 5)`

---

## Slide 12 — Parameter กับ Argument
**Key Message**: parameter คือช่องรอรับค่า argument คือค่าจริงที่ถูกส่งเข้าไป

- **Parameter**: ชื่อตัวแปรในวงเล็บตอน "นิยาม" ฟังก์ชัน ทำหน้าที่เป็นช่องว่างรอรับค่า ยังไม่มีค่าจริง
- **Argument**: ค่าจริงที่ถูกส่งเข้าไปตอน "เรียกใช้" ฟังก์ชัน ถูกผูก (bind) กับพารามิเตอร์ตามลำดับตำแหน่ง (positional)
- **Keyword argument**: ระบุชื่อพารามิเตอร์กำกับตอนเรียกใช้ ทำให้สลับลำดับเขียนได้โดยไม่เปลี่ยนความหมาย เพราะ Python ผูกค่าตามชื่อแทนตำแหน่ง
- Python ไม่ตรวจสอบว่าค่าที่ส่งเข้ามาตรงกับความหมายที่พารามิเตอร์ต้องการหรือไม่

[FIGURE: diagram of `def introduce(name, age):` showing name and age as empty labeled slots, connected by arrows from `introduce("Aom", 20)` showing "Aom" binding to the name slot and 20 binding to the age slot by position]

---

## Slide 13 — ตัวอย่าง: แนะนำตัวบุคคล
**Key Message**: argument ผูกกับ parameter ตามลำดับตำแหน่งที่ส่งเข้าไป

```python
def introduce(name, age):
    print(f"ฉันชื่อ {name} อายุ {age} ปี")

introduce("Aom", 20)
introduce("Beam", 22)
```

**Output:**
```
ฉันชื่อ Aom อายุ 20 ปี
ฉันชื่อ Beam อายุ 22 ปี
```

- `name`, `age` คือพารามิเตอร์ (ช่องรอรับค่า) ส่วน `"Aom"`, `20` คืออาร์กิวเมนต์ (ค่าจริง) ที่ผูกตามลำดับตำแหน่ง

---

## Slide 14 — ตัวอย่าง: Positional vs Keyword Argument
**Key Message**: keyword argument สลับลำดับเขียนได้โดยไม่เปลี่ยนความหมาย

```python
def calculate_total(price, quantity):
    return price * quantity

print(calculate_total(50, 3))
print(calculate_total(quantity=3, price=50))
```

**Output:**
```
150
150
```

- แบบแรกส่งตามตำแหน่ง (positional) แบบที่สองระบุชื่อกำกับ (keyword) แล้วสลับลำดับได้ เพราะ Python ผูกค่าตามชื่อแทนตำแหน่ง

---

## Slide 15 — ข้อผิดพลาด: ส่งอาร์กิวเมนต์ผิดลำดับ
**Key Message**: สลับตำแหน่ง argument = ผูกค่าผิดโดยไม่มี error เตือน

```python
def introduce(name, age):
    print(f"ฉันชื่อ {name} อายุ {age} ปี")

introduce("Aom", 20)
introduce(20, "Aom")
```

**Output:**
```
ฉันชื่อ Aom อายุ 20 ปี
ฉันชื่อ 20 อายุ Aom ปี
```

- สลับตำแหน่งอาร์กิวเมนต์ทำให้ค่าผูกผิดพารามิเตอร์โดยไม่มี error แจ้งเตือน — เป็นข้อผิดพลาดเชิงตรรกะที่ตรวจพบยาก

---

## Slide 16 — สรุป: Python ผูกค่าตามตำแหน่งเสมอ
**Key Message**: Python ไม่ตรวจสอบความหมาย มีแต่ผูกค่าตามตำแหน่ง

- Python จะไม่แจ้งข้อผิดพลาดใด ๆ เมื่อสลับลำดับ positional argument เพราะภาษาไม่ตรวจสอบชนิด/ความหมายของพารามิเตอร์ แต่ผูกค่าตามตำแหน่งเสมอ
- Keyword argument คือทางป้องกันความผิดพลาดนี้ โดยเฉพาะเมื่อฟังก์ชันมีพารามิเตอร์หลายตัว
- เชื่อมโยง: ฟังก์ชัน `add(x, y)` มี `x`, `y` เป็นพารามิเตอร์ ส่วน `3`, `5` ใน `add(3, 5)` คืออาร์กิวเมนต์

---

## Slide 17 — Return Value กับ Procedure (Void Function)
**Key Message**: return หยุด function ทันทีและส่งค่ากลับ ไม่มี return ได้ None เสมอ

- ฟังก์ชันที่มีค่าส่งกลับ (**return value**): ประมวลผลแล้ว `return` ค่ากลับไปให้จุดที่เรียกใช้ นำไปเก็บในตัวแปรหรือใช้ในนิพจน์ต่อได้ทันที
- `return` เมื่อถูกรัน จะหยุดการทำงานของฟังก์ชันทันทีและส่งค่าที่ระบุกลับไป
- ฟังก์ชันแบบ **procedure** (void function): ทำงานบางอย่าง (เช่น `print`) แต่ไม่มี `return` ที่ส่งค่ากลับให้ใช้ต่อ — ถูกเรียกเพื่อ "ผลข้างเคียง" (side effect)
- ถ้าฟังก์ชันไม่มี `return` หรือมี `return` โดยไม่ระบุค่า จะคืนค่าพิเศษ `None` โดยอัตโนมัติเสมอ
- กฎของวิชานี้: **return ค่าเดียวเสมอ** (ยังไม่สอน tuple unpacking / return หลายค่า)

[FIGURE: call stack diagram showing add(3, 5) call, parameters bound, and return value flowing back to caller]

---

## Slide 18 — ตัวอย่าง: add (มี return) กับ show_greeting (procedure)
**Key Message**: return ได้ค่ามาใช้ต่อ ไม่มี return ได้ None

```python
def add(x, y):
    return x + y

def show_greeting(name):
    print(f"สวัสดี {name}")

result1 = add(3, 5)
result2 = show_greeting("Beam")

print(result1)
print(result2)
```

**Output:**
```
สวัสดี Beam
8
None
```

- เก็บผลจาก `add` ได้ค่า 8 ใช้ต่อได้จริง ส่วนเก็บผลจาก `show_greeting` ได้ `None` เพราะไม่มี `return`

---

## Slide 19 — ตัวอย่าง: find_max (มี return) กับ print_list (procedure)
**Key Message**: หลักการเดียวกันในบริบทลิสต์ — return ได้ค่า ไม่มี return ได้ None

```python
def find_max(numbers):
    return max(numbers)

def print_list(items):
    for item in items:
        print(item)

scores = [88, 95, 72, 90]

best = find_max(scores)
nothing = print_list(scores)

print(best)
print(nothing)
```

**Output:**
```
88
95
72
90
95
None
```

- `find_max` คืนค่ากลับใช้ต่อได้ (95) ส่วน `print_list` แค่พิมพ์ค่าออกจอ แต่ตัวแปร `nothing` ที่เก็บผลลัพธ์ยังเป็น `None`

---

## Slide 20 — ข้อผิดพลาด: เข้าใจผิดว่า procedure ส่งค่ากลับด้วย
**Key Message**: เอาผลจาก procedure ไปใช้ต่อ = ได้ None แทนค่าที่ต้องการ

```python
def show_greeting(name):
    print(f"สวัสดี {name}")

message = show_greeting("Beam")
print("ข้อความคือ: " + message)
```

**Output:**
```
สวัสดี Beam
Traceback (most recent call last):
  File "main.py", line 5, in <module>
    print("ข้อความคือ: " + message)
TypeError: can only concatenate str (not "NoneType") to str
```

- นำผลจากฟังก์ชัน procedure (ได้ `None`) ไปต่อกับ string เกิด `TypeError` ทันที

---

## Slide 21 — สรุป: print ไม่ใช่ return
**Key Message**: print แสดงผลบนจอ แต่ไม่ส่งค่ากลับให้ใช้ต่อ

- ข้อผิดพลาดที่พบบ่อยที่สุด: เข้าใจผิดว่าฟังก์ชันที่ `print` ข้อความออกหน้าจอจะ "ส่งค่ากลับ" ให้ใช้งานต่อได้ด้วย — ความจริงคือ `print` ไม่ใช่ `return`
- ระวังสับสนระหว่าง "สิ่งที่พิมพ์ออกจอ" กับ "ค่าที่ return" — ค่าที่ถูกเก็บในตัวแปรปลายทางยังเป็น `None` อยู่ดี แม้หน้าจอจะแสดงข้อความออกมาแล้วก็ตาม
- กฎวิชานี้: **return ค่าเดียวเสมอ**

---

## Slide 22 — ขอบเขตตัวแปร (Scope): Local กับ Global
**Key Message**: ตัวแปรใน function ไม่กระทบตัวแปรข้างนอก เว้นแต่ประกาศ global

- **Scope** (ขอบเขต): บริเวณของโปรแกรมที่ตัวแปรนั้นสามารถถูกอ้างถึงและใช้งานได้
- ตัวแปรเฉพาะที่ (**local**): สร้างขึ้นภายในฟังก์ชัน ใช้ได้เฉพาะภายในฟังก์ชันนั้น ถูกทำลายเมื่อฟังก์ชันทำงานเสร็จ
- ตัวแปรส่วนกลาง (**global**): สร้างขึ้นภายนอกฟังก์ชันทั้งหมด ครอบคลุมทั้งโปรแกรม อ่านค่าได้จากทุกจุดรวมถึงจากภายในฟังก์ชัน
- **อ่าน** ค่า global จากในฟังก์ชัน: ทำได้โดยตรงโดยไม่ต้องประกาศเพิ่มเติม
- **แก้ไข** ค่า global จากในฟังก์ชัน: ต้องประกาศชื่อตัวแปรด้วย `global` ก่อนเสมอ มิฉะนั้น Python จะตีความว่ากำลังสร้างตัวแปร local ใหม่แทน
- พารามิเตอร์ทุกตัวก็เป็นตัวแปรเฉพาะที่ (local) ชนิดหนึ่งเสมอ

[FIGURE: box diagram showing outer scope variable count separate from the function's local_count box]

---

## Slide 23 — ตัวอย่าง: ยอดเงินคงเหลือ (อ่านและแก้ไข global)
**Key Message**: อ่าน global ได้อิสระ แต่แก้ไขต้องประกาศ global ก่อน

```python
balance = 1000

def deposit(amount):
    global balance
    balance = balance + amount

def show_balance():
    print(f"ยอดคงเหลือ: {balance}")

show_balance()
deposit(500)
show_balance()
```

**Output:**
```
ยอดคงเหลือ: 1000
ยอดคงเหลือ: 1500
```

- `show_balance` อ่านค่า `balance` ได้โดยตรง ส่วน `deposit` ต้องประกาศ `global balance` ก่อนจึงจะแก้ไขค่าได้จริง

---

## Slide 24 — ตัวอย่าง: สถานะเกม (scope กับข้อความ)
**Key Message**: แนวคิด scope ใช้ได้กับข้อความเช่นเดียวกับตัวเลข

```python
game_status = "กำลังเล่น"

def update_status(new_status):
    global game_status
    game_status = new_status

def show_status():
    print(f"สถานะ: {game_status}")

show_status()
update_status("จบเกม")
show_status()
```

**Output:**
```
สถานะ: กำลังเล่น
สถานะ: จบเกม
```

- หลักการเดียวกับตัวอย่างยอดเงิน แต่แสดงว่า scope ใช้ได้กับตัวแปรชนิดข้อความ (string) เช่นเดียวกับตัวเลข

---

## Slide 25 — ข้อผิดพลาด: ลืมประกาศ global ก่อนแก้ไข
**Key Message**: ลืม global = Python สร้างตัวแปร local ใหม่ทันที ไม่ใช่แก้ตัวเดิม

```python
balance = 1000

def deposit_wrong(amount):
    balance = balance + amount
    print(balance)

deposit_wrong(500)
```

**Output:**
```
Traceback (most recent call last):
  File "main.py", line 4, in deposit_wrong
    balance = balance + amount
UnboundLocalError: cannot access local variable 'balance' where it is not associated with a value
```

- ไม่ประกาศ `global` ทำให้ Python ตีความว่า `balance` ในฟังก์ชันเป็นตัวแปร local ใหม่ทั้งฟังก์ชัน จึงอ่านค่าฝั่งขวาของ `=` ไม่ได้เลย

---

## Slide 26 — Trick สำคัญที่สุด: assign จุดเดียวทำให้ทั้งฟังก์ชันเป็น local
**Key Message**: มี assign แม้จุดเดียวในฟังก์ชัน = ชื่อนั้นเป็น local ตลอดทั้งฟังก์ชัน

- แม้จะมีการกำหนดค่า (assign) ให้ชื่อตัวแปรใด ๆ ภายในฟังก์ชันเพียงจุดเดียว Python จะถือว่าชื่อนั้นเป็นตัวแปรเฉพาะที่ (local) ตลอดทั้งฟังก์ชัน ไม่ใช่แค่หลังจุดที่ assign
- ผลคือแม้แต่ตอนอ่านค่าฝั่งขวาของเครื่องหมาย `=` (เช่น `balance + amount`) ก็ยังไม่มีค่า `balance` แบบ local ให้อ่าน จึงเกิด `UnboundLocalError`
- ตัวแปร global ที่พยายามแก้ไขโดยไม่ประกาศ `global` จะไม่ถูกแก้ไขจริง เพราะฟังก์ชันหยุดทำงานด้วย error ก่อนถึงบรรทัดถัดไป
- หมายเหตุ: ข้อความ error นี้เป็นรูปแบบของ Python 3.11 ขึ้นไป เวอร์ชันเก่ากว่าจะขึ้น `local variable 'balance' referenced before assignment` แต่เป็น `UnboundLocalError` เหมือนกัน

---

## Slide 27 — เนื้อหาเสริม: ระดับกลาง (นอกขอบเขตสอบ)
**Key Message**: หัวข้อ 6–9 ต่อไปนี้เป็นเนื้อหาเสริมนอกขอบเขตสอบของวิชานี้ — เจาะลึกกลไกเบื้องหลังของฟังก์ชันใน Python

- หัวข้อ 6–9 ไม่ปรากฏในสไลด์ตัวสอบจริงของสัปดาห์นี้ (ไม่ออกสอบ)
- เหมาะสำหรับผู้ที่อยากเข้าใจกลไกเบื้องหลังของ Python ให้ลึกขึ้น หรือเตรียมเขียนโปรแกรมจริงในอนาคต
- ครอบคลุม 4 เรื่อง: กลไกส่งอาร์กิวเมนต์ (by value/reference), default parameters, `*args`/`**kwargs`, และ recursion (การเรียกซ้ำ)

---

## Slide 28 — By Value vs By Reference: กลไกการส่งค่าให้ฟังก์ชันของ Python
**Key Message**: Python ส่งอาร์กิวเมนต์แบบ "pass-by-object-reference" เสมอ — พฤติกรรมที่เห็นต่างกันเพราะชนิดอ็อบเจกต์ mutable/immutable ต่างกัน ไม่ใช่เพราะกลไกต่างกัน

- ภาษาโปรแกรมทั่วไปแบ่งกลไกส่งอาร์กิวเมนต์เป็น pass by value กับ pass by reference
- Python ใช้กลไกเฉพาะตัว: พารามิเตอร์ได้รับ "การอ้างอิง" ไปยังอ็อบเจกต์เดียวกับตัวแปรต้นทาง ไม่ใช่สำเนาข้อมูลทั้งก้อน
- immutable types (int, str, tuple): กำหนดค่าใหม่ให้พารามิเตอร์จะสร้างอ็อบเจกต์ใหม่ ไม่กระทบตัวแปรต้นทาง (พฤติกรรมคล้าย pass by value)
- mutable types (list, dict, set): เมธอดที่แก้ไขแบบ in-place (เช่น append) กระทบตัวแปรต้นทางด้วย เพราะชี้อ็อบเจกต์เดียวกันในหน่วยความจำ
- ตัวแปร local ในฟังก์ชันเป็นเพียง "ชื่อ" ที่ชี้ไปยังอ็อบเจกต์ ไม่ใช่ช่องความจำแยกต่างหากเสมอไป — กฎเรื่อง scope ยังจริงอยู่เสมอ

---

## Slide 29 — ตัวอย่าง: ส่งค่าชนิด immutable (int)
**Key Message**: ตัวเลข (immutable) — กำหนดค่าใหม่ให้พารามิเตอร์ภายในฟังก์ชันไม่กระทบตัวแปรต้นฉบับภายนอก

```python
def change_value(x):
    x = x + 10
    print("ค่าภายในฟังก์ชัน:", x)

num = 5
change_value(num)
print("ค่านอกฟังก์ชัน:", num)
```

**Output:**
```
ค่าภายในฟังก์ชัน: 15
ค่านอกฟังก์ชัน: 5
```

- `x = x + 10` สร้างอ็อบเจกต์ใหม่ (15) แล้วผูกชื่อ `x` กับมัน เฉพาะภายในฟังก์ชัน — `num` ยังชี้อ็อบเจกต์เดิม (5)

---

## Slide 30 — ตัวอย่าง: ส่งค่าชนิด mutable (list)
**Key Message**: ลิสต์ (mutable) — เมธอด in-place ที่เรียกในฟังก์ชันกระทบตัวแปรต้นฉบับจริง

```python
def add_item(items):
    items.append("B")
    print("ภายในฟังก์ชัน:", items)

my_list = ["A"]
add_item(my_list)
print("นอกฟังก์ชัน:", my_list)
```

**Output:**
```
ภายในฟังก์ชัน: ['A', 'B']
นอกฟังก์ชัน: ['A', 'B']
```

- พารามิเตอร์ `items` กับตัวแปร `my_list` ชี้ไปยังอ็อบเจกต์ลิสต์เดียวกัน `.append()` จึงกระทบทั้งคู่พร้อมกัน

---

## Slide 31 — ตัวอย่าง: ส่งค่าชนิดข้อความ (str)
**Key Message**: ข้อความ (str) เป็น immutable เช่นเดียวกับ int — พฤติกรรม "คล้าย pass by value" ครอบคลุมทุกชนิด immutable

```python
def shout(message):
    message = message.upper()
    print("ภายในฟังก์ชัน:", message)

greeting_text = "hello world"
shout(greeting_text)
print("นอกฟังก์ชัน:", greeting_text)
```

**Output:**
```
ภายในฟังก์ชัน: HELLO WORLD
นอกฟังก์ชัน: hello world
```

- `message.upper()` คืนอ็อบเจกต์ string ใหม่เสมอ — str ไม่มีเมธอดใดแก้ไขข้อมูลเดิมแบบ in-place ได้เลย

---

## Slide 32 — สรุป: จำแบบไหน กระทบต้นฉบับหรือไม่
**Key Message**: "กำหนดค่าใหม่ตรง ๆ" ไม่กระทบต้นฉบับ แต่ "เรียกเมธอด in-place" กระทบต้นฉบับเสมอ

| ชนิดอ็อบเจกต์ | ตัวอย่าง type | กำหนดค่าใหม่ (`x = ...`) | เมธอด in-place (เช่น `.append()`) |
|---|---|---|---|
| Immutable | int, str, tuple | สร้างอ็อบเจกต์ใหม่ ไม่กระทบต้นฉบับ | ไม่มีเมธอดแก้ไขแบบ in-place |
| Mutable | list, dict, set | ผูกชื่อใหม่เฉพาะในฟังก์ชัน ไม่กระทบต้นฉบับ | กระทบต้นฉบับ เพราะชี้อ็อบเจกต์เดียวกัน |

[FIGURE: two side-by-side memory-reference diagrams. Left (immutable): variable num and parameter x both start pointing to the same int object 5; after x = x + 10 inside the function, x is rebound to point to a brand-new object 15 while num still points to the original object 5. Right (mutable): variable my_list and parameter items both point to the same list object the whole time; after items.append("B") the shared object itself is mutated in place, so both names still point to it and both now see ['A', 'B'].]

- กลไกเบื้องหลังเป็น pass-by-object-reference แบบเดียวกันเสมอ — ความต่างที่สังเกตเห็นอยู่ที่ mutable/immutable ไม่ใช่กลไกส่งค่าที่ต่างกัน
- หัวข้อนี้ไม่อยู่ในขอบเขตสอบของวิชานี้

---

## Slide 33 — อาร์กิวเมนต์ค่าเริ่มต้น (Default Parameters)
**Key Message**: default argument ทำให้พารามิเตอร์กลายเป็น "ทางเลือก" — แต่ค่าเริ่มต้นถูกสร้างเพียงครั้งเดียวตอน `def` เท่านั้น

- default argument: ค่าที่กำหนดไว้ล่วงหน้าให้พารามิเตอร์ตอนนิยามฟังก์ชัน ทำให้เรียกฟังก์ชันได้โดยไม่ต้องระบุอาร์กิวเมนต์ตัวนั้นก็ได้
- ไม่ส่งค่ามา → ใช้ค่าเริ่มต้นอัตโนมัติ / ส่งค่ามา → ค่านั้นแทนที่ค่าเริ่มต้นทันที
- กฎการนิยาม: พารามิเตอร์ที่ไม่มีค่าเริ่มต้นต้องมาก่อนพารามิเตอร์ที่มีค่าเริ่มต้นเสมอ
- ข้อควรระวังเฉพาะของ Python: ค่าเริ่มต้นถูกสร้างขึ้น "เพียงครั้งเดียว" ตอนประมวลผลคำสั่ง `def` ไม่ใช่ทุกครั้งที่ฟังก์ชันถูกเรียก
- Python รักษาชนิดข้อมูล (type) ตามอาร์กิวเมนต์ที่ส่งเข้ามาจริง ไม่ได้ยึดตามชนิดของค่าเริ่มต้นเสมอไป

---

## Slide 34 — ตัวอย่าง: พารามิเตอร์พร้อมค่าเริ่มต้น
**Key Message**: ไม่ระบุอาร์กิวเมนต์ = ใช้ค่าเริ่มต้น ระบุมา = ทับค่าเริ่มต้นทันที

```python
def greet(name, greeting="สวัสดี"):
    print(f"{greeting} {name}")

greet("อาทิตย์")
greet("จันทร์", "หวัดดี")
```

**Output:**
```
สวัสดี อาทิตย์
หวัดดี จันทร์
```

- `greeting` เป็น optional parameter เพราะมีค่าเริ่มต้นกำกับไว้ ส่วน `name` ยังคงเป็น required parameter เสมอ

---

## Slide 35 — ตัวอย่าง: ค่าเริ่มต้นแบบ mutable ที่ก่อปัญหา
**Key Message**: ค่าเริ่มต้นแบบ mutable (list ว่าง) จะ "ค้าง" ข้ามการเรียกฟังก์ชันแต่ละครั้งโดยไม่ตั้งใจ

```python
def add_item_bad(item, basket=[]):
    basket.append(item)
    return basket

print(add_item_bad("แอปเปิล"))
print(add_item_bad("กล้วย"))
```

**Output:**
```
['แอปเปิล']
['แอปเปิล', 'กล้วย']
```

- คาดว่าแต่ละครั้งจะได้ตะกร้าใหม่ที่มีสินค้าชิ้นเดียว แต่ `basket=[]` ถูกสร้างครั้งเดียวตอน `def` แล้วผูกกับตัวฟังก์ชันไปตลอด ไม่ใช่ลิสต์ว่างใหม่ทุกครั้งที่เรียก

---

## Slide 36 — Trick: ทำไมเกิดบั๊ก และวิธีแก้มาตรฐาน
**Key Message**: วิธีแก้มาตรฐาน — ตั้งค่าเริ่มต้นเป็น `None` แล้วค่อยสร้างอ็อบเจกต์ mutable ใหม่ภายในฟังก์ชัน

```python
def add_item_good(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print(add_item_good("แอปเปิล"))
print(add_item_good("กล้วย"))
```

**Output:**
```
['แอปเปิล']
['กล้วย']
```

[FIGURE: diagram showing the def statement executing once and creating a single shared empty-list object bound into add_item_bad's default-argument slot; every call to add_item_bad() without an explicit basket argument reuses that exact same list object, so items pile up across calls — contrasted with add_item_good(), where basket=None is the fixed default and a brand-new empty list object is created fresh inside the function body on every call.]

- **Trick สำคัญที่สุด**: ค่าเริ่มต้นถูกสร้าง "ครั้งเดียว" ตอน `def` ประมวลผล ไม่ใช่ทุกครั้งที่เรียกฟังก์ชัน — เป็นต้นตอของบั๊ก mutable default argument
- อย่าใช้ list/dict/set เป็นค่าเริ่มต้นโดยตรง — ให้ใช้ `None` แล้วเช็ค `if basket is None:` ภายในฟังก์ชันแทนเสมอ
- เป็นบั๊กที่พบบ่อยแม้ในโค้ดของโปรแกรมเมอร์มีประสบการณ์ ควรจำรูปแบบการแก้นี้ให้ขึ้นใจ

---

## Slide 37 — ตัวอย่าง: คำนวณราคารวมพร้อมภาษี
**Key Message**: default argument ส่งได้ทั้งแบบไม่ระบุ ตามตำแหน่ง หรือ keyword — type ของผลลัพธ์ขึ้นกับอาร์กิวเมนต์จริงที่ส่งเข้ามา

```python
def calculate_total(price, tax_rate=0.07):
    return price + price * tax_rate

print(round(calculate_total(200), 2))
print(round(calculate_total(200, 0.10), 2))
print(calculate_total(200, tax_rate=0))
print(type(calculate_total(200)))
print(type(calculate_total(200, tax_rate=0)))
```

**Output:**
```
214.0
220.0
200
<class 'float'>
<class 'int'>
```

- `calculate_total(200)` ใช้ `tax_rate` เริ่มต้น (float) จึงได้ผลลัพธ์เป็น float แต่ `calculate_total(200, tax_rate=0)` ส่ง `int` เข้ามาแทนที่ จึงได้ผลลัพธ์เป็น `int` — type ยึดตามอาร์กิวเมนต์จริง ไม่ใช่ type ของค่า default

---

## Slide 38 — อาร์กิวเมนต์จำนวนไม่จำกัด (`*args` / `**kwargs`)
**Key Message**: `*args` รวบรวมอาร์กิวเมนต์ตามตำแหน่งที่ไม่จำกัดจำนวนเป็น tuple ส่วน `**kwargs` รวบรวมอาร์กิวเมนต์แบบระบุชื่อเป็น dict

- ปัญหาที่แก้: บางครั้งผู้ออกแบบฟังก์ชันไม่ทราบล่วงหน้าว่าผู้เรียกจะส่งอาร์กิวเมนต์เข้ามากี่ตัว
- `*args`: อาร์กิวเมนต์ตามตำแหน่งจำนวนไม่จำกัด รวบรวมเป็น tuple ผ่านสัญลักษณ์ `*`
- `**kwargs`: อาร์กิวเมนต์แบบระบุชื่อจำนวนไม่จำกัด รวบรวมเป็น dict ผ่านสัญลักษณ์ `**`
- ธรรมเนียมการตั้งชื่อคือ `args`/`kwargs` แต่ตั้งชื่ออื่นได้ — สัญลักษณ์ `*`/`**` ต่างหากที่กำหนดพฤติกรรม
- กฎการเรียงลำดับพารามิเตอร์เมื่อใช้ร่วมกัน: พารามิเตอร์ปกติ → `*args` → `**kwargs` เป็นลำดับสุดท้ายเสมอ

---

## Slide 39 — ตัวอย่าง: `*args` รวบรวมอาร์กิวเมนต์จำนวนไม่จำกัด
**Key Message**: ฟังก์ชันเดียวเรียกด้วยจำนวนอาร์กิวเมนต์ต่างกันกี่ตัวก็ได้ ผ่าน `*args`

```python
def total(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result

print(total(1, 2, 3))
print(total(10, 20))
print(total())
```

**Output:**
```
6
30
0
```

- ภายในฟังก์ชัน `numbers` คือ tuple เช่น `(1, 2, 3)` — วนลูปได้เหมือน list ทั่วไป แม้ไม่ส่งอาร์กิวเมนต์เลยก็ได้ tuple ว่าง

---

## Slide 40 — ตัวอย่าง: ผสม `*args` กับ `**kwargs` ในฟังก์ชันเดียว
**Key Message**: พารามิเตอร์ปกติ, `*args`, และ `**kwargs` ใช้ร่วมกันในฟังก์ชันเดียวได้ตามลำดับที่กำหนด

```python
def student_report(name, *subjects, **details):
    print(f"นักเรียน: {name}")
    print("วิชาที่ลงทะเบียน:", subjects)
    print("รายละเอียดเพิ่มเติม:", details)

student_report("มานะ", "คณิต", "วิทย์", room="6/1", advisor="ครูสมชาย")
```

**Output:**
```
นักเรียน: มานะ
วิชาที่ลงทะเบียน: ('คณิต', 'วิทย์')
รายละเอียดเพิ่มเติม: {'room': '6/1', 'advisor': 'ครูสมชาย'}
```

- `name` รับค่าตามปกติ, อาร์กิวเมนต์ตามตำแหน่งที่เหลือรวบเข้า `subjects` (tuple), อาร์กิวเมนต์ระบุชื่อทั้งหมดรวบเข้า `details` (dict)

---

## Slide 41 — ตัวอย่าง: ใบเสร็จร้านอาหารด้วย `*args` และ `**kwargs`
**Key Message**: อ่านค่าจาก `**kwargs` ด้วย `.items()` เพื่อวนลูปทั้งชื่อคีย์และค่าไปพร้อมกัน

```python
def print_receipt(customer, *items, **options):
    print(f"ลูกค้า: {customer}")
    for item in items:
        print("-", item)
    for key, value in options.items():
        print(f"{key}: {value}")

print_receipt("สมหญิง", "ข้าวผัด", "ต้มยำ", table=5, discount="10%")
```

**Output:**
```
ลูกค้า: สมหญิง
- ข้าวผัด
- ต้มยำ
table: 5
discount: 10%
```

- จำลองสถานการณ์จริงที่จำนวนรายการอาหารและตัวเลือกเสริมของแต่ละออเดอร์ไม่แน่นอน ฟังก์ชันเดียวรองรับได้ทุกแบบ

---

## Slide 42 — สรุป: กฎการเรียงลำดับพารามิเตอร์
**Key Message**: ลำดับพารามิเตอร์ต้องเป็น พารามิเตอร์ปกติ → `*args` → `**kwargs` เสมอ ห้ามสลับ

| รูปแบบ | สัญลักษณ์ | เก็บเป็น | ตัวอย่างการเรียก |
|---|---|---|---|
| อาร์กิวเมนต์ตามตำแหน่งไม่จำกัด | `*args` | tuple | `total(1, 2, 3)` |
| อาร์กิวเมนต์ระบุชื่อไม่จำกัด | `**kwargs` | dict | `f(a=1, b=2)` |

- ชื่อ `args`/`kwargs` เปลี่ยนได้ตามใจ (เช่น `*numbers`, `**details`) เพราะสัญลักษณ์ `*`/`**` ต่างหากที่กำหนดพฤติกรรม ไม่ใช่ตัวชื่อตัวแปร
- อาร์กิวเมนต์ตามตำแหน่งที่เกินจากพารามิเตอร์ปกติจะถูกจัดสรรเข้า `*args` โดยอัตโนมัติ ส่วน keyword ทั้งหมดเข้า `**kwargs` โดยอัตโนมัติ
- หัวข้อนี้ไม่อยู่ในขอบเขตสอบของวิชานี้

---

## Slide 43 — การเรียกซ้ำ (Recursion)
**Key Message**: recursion ต้องมี "กรณีฐาน" (base case) เสมอ ไม่งั้นฟังก์ชันจะเรียกตัวเองไม่มีที่สิ้นสุด

- recursion: เทคนิคที่ฟังก์ชันหนึ่งเรียกใช้ตัวเองภายในนิยามของมันเอง เพื่อแก้ปัญหาที่แบ่งย่อยเป็นปัญหาย่อยลักษณะเดียวกันแต่ขนาดเล็กลงเรื่อย ๆ — เป็นทางเลือกหนึ่งของการวนลูป
- องค์ประกอบสำคัญที่ต้องมีเสมอ 2 ส่วน: (1) กรณีฐาน (base case) (2) กรณีเรียกซ้ำ (recursive case)
- ขาดกรณีฐาน → ฟังก์ชันเรียกตัวเองไม่มีที่สิ้นสุด
- call stack มีขีดจำกัด — ลึกเกินไปเกิด `RecursionError: maximum recursion depth exceeded` (ขีดจำกัดเริ่มต้นประมาณ 1000 ระดับ)
- แต่ละ call มีตัวแปร local ของตัวเองแยก scope กัน แม้เป็นฟังก์ชันเดียวกันที่เรียกซ้ำหลายรอบ

[FIGURE: call stack diagram showing factorial(4) calling factorial(3) calling factorial(2) calling factorial(1) calling factorial(0), each frame stacked on top of the previous one with its own local variable n, growing upward until the base case n=0 is reached at the top.]

---

## Slide 44 — ตัวอย่าง: แฟกทอเรียลด้วยการเรียกซ้ำ
**Key Message**: แฟกทอเรียลคือรูปแบบมาตรฐานของ recursion — base case ชัดเจน, recursive case ลดขนาดปัญหาลงทุกครั้งที่เรียก

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))
```

**Output:**
```
24
```

- `n == 0` คือ base case (คืนค่า 1 ทันทีโดยไม่เรียกตัวเองต่อ) ส่วน `n * factorial(n - 1)` คือ recursive case ที่เรียกตัวเองด้วยปัญหาที่เล็กลงทุกครั้ง

---

## Slide 45 — ตัวอย่าง: ขาดกรณีฐาน แล้วแก้ไข
**Key Message**: ฟังก์ชันเรียกซ้ำที่ไม่มี base case จะเกิด `RecursionError` เสมอ ไม่ว่าตรรกะส่วนอื่นจะถูกต้องแค่ไหน

```python
def countdown_broken(n):
    print(n)
    countdown_broken(n - 1)

countdown_broken(3)
```

**Output:**
```
3
2
1
0
-1
...
RecursionError: maximum recursion depth exceeded
```

```python
def countdown_fixed(n):
    if n == 0:
        print("หมดเวลา!")
        return
    print(n)
    countdown_fixed(n - 1)

countdown_fixed(3)
```

**Output:**
```
3
2
1
หมดเวลา!
```

- `countdown_fixed` เพิ่ม base case `if n == 0: return` เข้าไป ทำให้การเรียกซ้ำหยุดได้จริงแทนที่จะไล่ลงไปติดลบไม่มีที่สิ้นสุด

---

## Slide 46 — Trick: RecursionError และการคลี่ (unwind) call stack
**Key Message**: การคืนค่ากลับ (unwind) เกิดขึ้นตามลำดับย้อนกลับ — call ที่เรียกทีหลังสุดจะคืนค่าก่อนเป็นอันดับแรก

[FIGURE: recursion unwind diagram for factorial(4). Downward chain of calls: factorial(4) calls factorial(3) calls factorial(2) calls factorial(1) calls factorial(0), reaching the base case. Then an upward chain of returns back through each waiting frame: factorial(0) returns 1, factorial(1) returns 1*1=1, factorial(2) returns 2*1=2, factorial(3) returns 3*2=6, factorial(4) returns 4*6=24 — each pending call multiplying by its own local n before returning to its caller.]

- **"กรณีฐานไม่ใช่ทางเลือก แต่เป็นส่วนที่ขาดไม่ได้"** — ไม่มี base case = เรียกตัวเองไม่มีที่สิ้นสุดจนเกินขีดจำกัดของ call stack
- แต่ละ call ที่ค้างอยู่ (เช่น `factorial(3)` รอผลจาก `factorial(2)`) จะทยอยคืนค่ากลับตามลำดับย้อนกลับ หลังจากไปถึง base case แล้วเท่านั้น
- แต่ละ call มีตัวแปร parameter `n` ของตัวเองแยก scope กัน แม้เรียกฟังก์ชันเดียวกันซ้ำหลายรอบ
- ข้อความ error เต็มของ Python: `RecursionError: maximum recursion depth exceeded while calling a Python object`

---

## Slide 47 — ตัวอย่าง: กลับข้อความด้วยการเรียกซ้ำ
**Key Message**: recursion ใช้ได้กับโดเมนข้อมูลประเภทข้อความเช่นกัน ไม่ได้จำกัดอยู่แค่ตัวเลข

```python
def reverse_text(text):
    if len(text) == 0:
        return text
    else:
        return reverse_text(text[1:]) + text[0]

print(reverse_text("Python"))
```

**Output:**
```
nohtyP
```

- base case คือ string ว่าง (`len(text) == 0`) ส่วน recursive case ตัดตัวอักษรแรกออกไปเรื่อย ๆ แล้วนำตัวอักษรนั้นมาต่อท้ายตอนคืนค่ากลับ (unwind)

---

## Slide 48 — เนื้อหาเสริม — นอกขอบเขตสอบ (ขั้นสูง)
**Key Message**: จากนี้คือเนื้อหาเสริมระดับสูง (functional programming) — นอกขอบเขตสอบทั้งหมด เรียนเพื่อความเข้าใจกว้างขึ้น ไม่ใช่เพื่อสอบ

- หัวข้อ 10–15: First-class functions, Lambda, Higher-order functions, Pure function vs Side effect, Function signature/Contract, Single Responsibility Principle
- เนื้อหาทั้งหมดในส่วนนี้อยู่นอกขอบเขตสอบของวิชานี้ (ต่อยอดจากหัวข้อ 1–9)
- ข้อยกเว้นสำคัญที่ต้องระวัง: มีตัวอย่างหนึ่งจุด (หัวข้อ 11) ที่ขัดกับกฎหลักของวิชานี้ "return ค่าเดียวเสมอ" โดยเจตนา — จะมีคำเตือน ⚠️ กำกับไว้ชัดเจนเมื่อถึงจุดนั้น

---

## Slide 49 — First-class Functions คืออะไร
**Key Message**: ใน Python ฟังก์ชันถูกปฏิบัติเหมือนค่าข้อมูลชนิดอื่นทุกประการ

- ภาษาที่ถือว่าฟังก์ชันเป็น "ชั้นหนึ่ง" (first-class) คือฟังก์ชันถูกปฏิบัติเหมือนค่าข้อมูลชนิดอื่นทุกประการ
- คุณสมบัติ 4 อย่างที่ตามมา: เก็บไว้ในตัวแปรได้ / ส่งเป็นอาร์กิวเมนต์ให้ฟังก์ชันอื่นได้ / เก็บไว้ในโครงสร้างข้อมูลได้ (list, dict) / ส่งกลับออกมาจากฟังก์ชันอื่นได้
- ตรงข้ามกับภาษาที่ฟังก์ชันเป็นเพียง "หน่วยคำสั่ง" เรียกได้อย่างเดียว
- เป็นรากฐานของ higher-order function (หัวข้อ 12)
- ใน Python ฟังก์ชันทุกตัวคือ `function` object โดยธรรมชาติ ไม่ต้องเปิดใช้งานพิเศษ

[FIGURE: diagram showing a function object sitting alongside int/str/list values, with arrows showing it can be assigned to a variable, passed as an argument, stored in a data structure, and returned from another function]

---

## Slide 50 — ตัวอย่าง: กำหนดฟังก์ชันให้ตัวแปร
**Key Message**: เขียนชื่อฟังก์ชันโดยไม่มีวงเล็บ = คัดลอกตัวอ้างอิงฟังก์ชัน ไม่ใช่เรียกใช้งาน

```python
def greet(name):
    return f"สวัสดี {name}"

say_hello = greet          # ไม่มีวงเล็บ -> คัดลอกตัวอ้างอิง ไม่ได้เรียกใช้
print(say_hello("มานะ"))
print(say_hello == greet)
```

**Output:**
```
สวัสดี มานะ
True
```

- `say_hello` กับ `greet` ชี้ไปยังฟังก์ชันเดียวกัน เรียกผ่านชื่อไหนก็ได้ผลเหมือนกัน

---

## Slide 51 — ตัวอย่าง: Dispatch Table
**Key Message**: เก็บฟังก์ชันเป็นค่าใน dict แล้วค้นหา-เรียกใช้ตาม key แทนการเขียน if/elif ยาว ๆ

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

operations = {"+": add, "-": subtract, "*": multiply}

def calculate(a, op, b):
    func = operations[op]
    return func(a, b)

print(calculate(4, "+", 5))
print(calculate(4, "*", 5))
```

**Output:**
```
9
20
```

- `operations` เก็บฟังก์ชันเป็น value ของ dict ได้ เพราะฟังก์ชันเป็น first-class

---

## Slide 52 — ตัวอย่าง: อ้างอิงฟังก์ชัน vs เรียกฟังก์ชัน
**Key Message**: ลืมหรือใส่วงเล็บผิดจุด โปรแกรมทำงานไม่ตรงใจโดยไม่มี error แจ้งเตือน

```python
def get_score():
    print("กำลังคำนวณคะแนน...")
    return 95

correct_ref = get_score     # ไม่เรียกใช้ ยังเป็นฟังก์ชัน
wrong_ref = get_score()     # เรียกใช้ทันที ได้ค่าที่ return

print(type(correct_ref))
print(type(wrong_ref))
```

**Output:**
```
กำลังคำนวณคะแนน...
<class 'function'>
<class 'int'>
```

- `get_score()` มี side effect (print) และจะรันทันทีตอนบรรทัด `wrong_ref = get_score()` ถูกประมวลผล ไม่ใช่ตอน print
- ใช้ `type()` เป็นเครื่องมือพิสูจน์ความแตกต่างระหว่างตัวอ้างอิงฟังก์ชันกับค่าที่ถูกเรียกไปแล้ว

---

## Slide 53 — สรุป: วงเล็บคือตัวชี้ขาด
**Key Message**: "ไม่มีวงเล็บ" = คัดลอกตัวอ้างอิง ยังไม่ทำงาน — "มีวงเล็บ" = เรียกใช้ทันทีและเก็บเฉพาะค่าที่ return

| รูปแบบ | ความหมาย | ผลลัพธ์ที่ได้ |
|---|---|---|
| `x = get_score` | คัดลอกตัวอ้างอิงฟังก์ชัน | `function` object |
| `x = get_score()` | เรียกใช้งานทันที | ค่าที่ `return` กลับมา (เช่น `int`) |

- ถ้าเขียนผิดพลาดโดยลืมหรือใส่วงเล็บผิดจุด โปรแกรมจะทำงานไม่ตรงกับที่ตั้งใจ **โดยไม่มี error แจ้งเตือนชัดเจน** — ดีบักยาก
- dispatch table (Slide 10.3) คือการใช้ประโยชน์จริงของ first-class function เพื่อลดโค้ด if/elif ซ้ำซ้อน

---

## Slide 54 — Lambda คืออะไร
**Key Message**: lambda คือฟังก์ชันไม่มีชื่อ เขียนสั้น ๆ ได้เพียงนิพจน์เดียว คืนค่าอัตโนมัติโดยไม่ต้องเขียน `return`

- lambda คือฟังก์ชันขนาดเล็กที่ไม่มีชื่อในตัวเอง ใช้งานแบบสั้น ๆ โดยไม่ต้องประกาศแบบเต็มรูปแบบด้วย `def`
- ข้อจำกัดสำคัญ: บรรจุได้เพียง "นิพจน์เดียว" (single expression) เท่านั้น ค่าของนิพจน์นั้นถูกคืนกลับโดยอัตโนมัติ ไม่ต้องเขียน `return`
- ความแตกต่างจาก `def` เป็นเรื่อง "รูปแบบการเขียน" เท่านั้น — ในทางความหมายและการทำงาน lambda ก็คือฟังก์ชันชนิดหนึ่งเช่นเดียวกับ `def`
- นิยมใช้เมื่อฟังก์ชันมีตรรกะสั้นมาก ใช้ครั้งเดียวหรือไม่กี่ครั้ง โดยเฉพาะเมื่อส่งเป็นอาร์กิวเมนต์ให้ฟังก์ชันอันดับสูง เช่น `sorted()`, `map()`, `filter()`

---

## Slide 55 — ตัวอย่าง: lambda เทียบกับฟังก์ชันมีชื่อ
**Key Message**: lambda กับ `def` ให้ผลลัพธ์เหมือนกันทุกประการ ต่างกันแค่รูปแบบการเขียน

```python
def square_def(x):
    return x ** 2

square = lambda x: x ** 2

print(square_def(5))
print(square(5))
print(type(square))
```

**Output:**
```
25
25
<class 'function'>
```

- `type(square)` ยืนยันว่า lambda เป็น `function` object ชนิดเดียวกับที่นิยามด้วย `def`

---

## Slide 56 — ตัวอย่าง: lambda เป็นเกณฑ์จัดเรียงข้อมูล
**Key Message**: กรณีใช้งานจริงที่พบบ่อยที่สุดของ lambda คือเป็น "ฟังก์ชันเกณฑ์" สั้น ๆ ที่ส่งเป็นอาร์กิวเมนต์ `key=`

```python
students = [("Aom", 88), ("Beam", 95), ("Ken", 72)]

ranked = sorted(students, key=lambda record: record[1], reverse=True)
print(ranked)
```

**Output:**
```
[('Beam', 95), ('Aom', 88), ('Ken', 72)]
```

- จงใจใช้การเข้าถึงด้วยดัชนี `record[1]` แทน tuple unpacking เพื่อไม่ให้พึ่งพา syntax ที่ยังไม่สอนในคอร์สนี้
- `sorted(..., key=...)` คือ higher-order function ที่รับ lambda เป็นอาร์กิวเมนต์

---

## Slide 57 — ⚠️ ข้อควรระวัง: lambda คืนค่าหลายค่า (ขัดกับกฎวิชานี้โดยเจตนา)
**Key Message**: ⚠️ ตัวอย่างนี้ขัดกับกฎ "return ค่าเดียวเสมอ" ของวิชานี้โดยเจตนา — แสดงเพื่อเป็น "ข้อสังเกต" เท่านั้น ไม่ใช่แนวปฏิบัติที่แนะนำให้ใช้ในคอร์สนี้

```python
# ⚠️ ตัวอย่างนี้ขัดกับกฎ "return ค่าเดียวเสมอ" ของวิชานี้โดยเจตนา
calc_both = lambda a, b: (a + b, a * b)

total, product = calc_both(3, 4)   # ต้องใช้ tuple unpacking แยกค่า
print(total, product)
```

**Output:**
```
7 12
```

- lambda คืนค่าเป็น tuple ได้เหมือนฟังก์ชันปกติ แต่ผู้เรียกต้องใช้ **tuple unpacking** ซึ่งยังไม่สอนในสัปดาห์ 1–7 ของคอร์สนี้
- ⚠️ **แม้ทำงานได้ถูกต้องจริง แต่ขัดกับกฎ "return ค่าเดียวเสมอ" ของ `slides/06_function.md` (Slide 6) โดยตรง** — ต้องมองเป็น "ข้อควรระวัง/สิ่งที่พบเจอได้ในโลกจริง" ไม่ใช่แนวทางที่แนะนำให้ทำตามในคอร์สนี้
- หากต้องการผลลัพธ์สองค่าจริงและสอดคล้องกับกฎวิชานี้ ให้แยกเป็นสองฟังก์ชันแทน เช่น `calc_sum(a, b)` และ `calc_product(a, b)` แยกกัน

---

## Slide 58 — สรุป: เมื่อไรควรใช้ lambda
**Key Message**: lambda ไม่ใช่ฟังก์ชันชนิดพิเศษ แค่เขียนสั้นกว่า — ใช้ให้ถูกที่ ไม่ใช่ใช้แทน `def` ทุกกรณี

| ใช้ lambda เมื่อ | ใช้ `def` เมื่อ |
|---|---|
| ตรรกะสั้นมาก นิพจน์เดียว | ตรรกะซับซ้อนหลายบรรทัด |
| ใช้ครั้งเดียว/ไม่กี่ครั้ง เช่น `key=` ของ `sorted` | ต้องเรียกซ้ำหลายที่ทั่วโปรแกรม |
| ไม่จำเป็นต้องตั้งชื่อ | ต้องการชื่อที่สื่อความหมายเพื่ออ่านง่าย |

- lambda ≠ ฟังก์ชันชนิดพิเศษ — Python มองว่าเป็น "ฟังก์ชัน" ชนิดเดียวกับที่นิยามด้วย `def` ต่างกันแค่รูปแบบการเขียน
- ⚠️ ทบทวนอีกครั้ง: ตัวอย่าง Slide 11.4 คือจุดเดียวในเนื้อหาทั้งหมดของ Week 6 ที่ขัดกับกฎ "return ค่าเดียวเสมอ" — อย่าจำสับสนว่าเป็นแนวทางมาตรฐานของคอร์สนี้

---

## Slide 59 — Higher-order Functions คืออะไร
**Key Message**: higher-order function คือฟังก์ชันที่รับฟังก์ชันอื่นเป็นอาร์กิวเมนต์ หรือคืนค่าเป็นฟังก์ชัน (หรือทั้งสองอย่าง)

- นิยาม: มีคุณสมบัติอย่างน้อยหนึ่งใน 2 อย่าง: (1) รับฟังก์ชันอื่นเป็นอาร์กิวเมนต์ หรือ (2) คืนค่าเป็นฟังก์ชันออกมา
- เป็นไปได้เพราะภาษาถือว่าฟังก์ชันเป็น first-class (หัวข้อ 10)
- เป็นเครื่องมือสำคัญของ functional programming — แยก "ตรรกะที่ทำซ้ำ" ออกจาก "การกระทำเฉพาะจุด" ทำให้โค้ดนำกลับมาใช้ซ้ำได้มากขึ้น
- Python มี built-in higher-order function ที่ใช้บ่อย: `map()` (แปลงทุกสมาชิก) และ `filter()` (คัดกรองสมาชิกที่ผ่านเงื่อนไข) — มักใช้ร่วมกับ lambda (หัวข้อ 11)

[FIGURE: diagram showing a higher-order function box with an arrow pointing IN labeled "function as argument" and an arrow pointing OUT labeled "function as return value"]

---

## Slide 60 — ตัวอย่าง: ฟังก์ชันรับฟังก์ชันเป็นอาร์กิวเมนต์
**Key Message**: ฟังก์ชันหนึ่งรับ "ฟังก์ชัน" เป็นพารามิเตอร์แล้วเรียกซ้อนกันได้ โดยไม่ต้องรู้ล่วงหน้าว่าฟังก์ชันนั้นทำอะไร

```python
def apply_twice(func, value):
    return func(func(value))

def add_ten(x):
    return x + 10

result = apply_twice(add_ten, 5)
print(result)
```

**Output:**
```
25
```

- `apply_twice` เป็น higher-order function เพราะรับฟังก์ชันอื่นเป็นอาร์กิวเมนต์ — ตัวมันเองไม่จำเป็นต้องรู้ล่วงหน้าว่าฟังก์ชันที่ส่งเข้ามาทำอะไร

---

## Slide 61 — ตัวอย่าง: filter และ map
**Key Message**: `filter`/`map` เป็น built-in higher-order function ที่รับ lambda เป็นอาร์กิวเมนต์ ช่วยให้ไม่ต้องเขียน loop เอง

```python
scores = [45, 62, 78, 30, 91, 55]

passed = list(filter(lambda s: s >= 50, scores))
bonus = list(map(lambda s: s + 5, passed))

print(passed)
print(bonus)
```

**Output:**
```
[62, 78, 91, 55]
[67, 83, 96, 60]
```

- `filter(...)` คัดกรองเฉพาะคะแนนที่ผ่าน (>= 50) ส่วน `map(...)` แปลงทุกสมาชิกในลิสต์ที่ผ่านการกรองแล้วให้บวกคะแนนพิเศษ

---

## Slide 62 — ⚠️ ข้อควรระวัง: Closure Late Binding
**Key Message**: closure ของ Python จำ "ตัวแปร" ไม่ใช่ "ค่า ณ ขณะนั้น" — lambda ที่สร้างในลูปเดียวกันจะใช้ค่าตัวแปรลูปตัวสุดท้ายเหมือนกันหมด

```python
# ผิด — closure late binding
funcs = []
for i in [1, 2, 3]:
    funcs.append(lambda x: x * i)

print([f(10) for f in funcs])   # คาดหวัง [10, 20, 30]

# ถูก — ผูกค่าปัจจุบันไว้เป็นค่าเริ่มต้นของพารามิเตอร์
funcs_fixed = []
for i in [1, 2, 3]:
    funcs_fixed.append(lambda x, factor=i: x * factor)

print([f(10) for f in funcs_fixed])
```

**Output:**
```
[30, 30, 30]
[10, 20, 30]
```

- ทุก lambda ในลูปแรก "จำ" ตัวแปร `i` ตัวเดียวกัน เมื่อลูปจบ `i` มีค่าสุดท้ายคือ 3 ทุกฟังก์ชันจึงใช้ค่า 3 เหมือนกันหมด (`[30, 30, 30]`)
- วิธีแก้: กำหนดค่าปัจจุบันของตัวแปรลูปเป็น "ค่าเริ่มต้นของพารามิเตอร์" อีกตัว (`factor=i`) ซึ่งจะถูกประเมินและผูกไว้ทันทีตอนสร้างฟังก์ชันแต่ละตัว ไม่ใช่ตอนเรียกใช้ภายหลัง

[FIGURE: diagram showing three lambda closures in a loop all pointing to the same shared variable `i` box (which ends up holding 3), versus three lambdas each with their own bound `factor` value (1, 2, 3) captured at creation time]

---

## Slide 63 — สรุป Higher-order Functions
**Key Message**: Trick สำคัญที่สุดของหัวข้อนี้คือ closure late binding — จำตัวแปร ไม่ใช่ค่า

- `apply_twice` และ `filter`/`map` แสดงประโยชน์ของ higher-order function ในการลดโค้ดซ้ำซ้อน
- **Trick สำคัญที่สุด (closure late binding)**: closure ของ Python อ้างอิงถึง **"ตัวแปร"** ไม่ใช่ **"ค่า ณ ขณะนั้น"**
- เชื่อมโยงโดยตรงกับแนวคิด scope (local vs global) ในหัวข้อ 5 — ตัวแปรลูป `i` มี scope ครอบคลุมทุก lambda ที่สร้างขึ้นในลูปนั้น
- จำไว้: ถ้าต้อง "แช่แข็ง" ค่าตัวแปรลูป ณ ขณะสร้างฟังก์ชัน ให้ใช้ default parameter ผูกค่าไว้ทันที

---

## Slide 64 — Pure Function กับ Side Effect
**Key Message**: pure function เรียกด้วยอาร์กิวเมนต์ชุดเดียวกันแล้วได้ผลลัพธ์เดียวกันเสมอ และไม่เปลี่ยนแปลงสิ่งใดนอกขอบเขตของตัวเอง

- นิยาม pure function: (1) เรียกด้วยอาร์กิวเมนต์ชุดเดียวกันแล้วได้ผลลัพธ์เดียวกันเสมอ (2) การทำงานไม่ก่อให้เกิดการเปลี่ยนแปลงใด ๆ ที่มองเห็นได้จากภายนอกขอบเขตของตัวเอง
- ตัวอย่างของ side effect: แก้ไขตัวแปรส่วนกลาง, แก้ไขข้อมูลที่รับเข้ามาเป็นอาร์กิวเมนต์, พิมพ์ข้อความ, เขียนไฟล์, ติดต่อแหล่งข้อมูลภายนอก
- ฟังก์ชันมี side effect ไม่ได้ผิดหรือใช้งานไม่ได้ — โปรแกรมจริงต้องมีส่วนแสดงผล/บันทึกข้อมูล/แก้ไขสถานะ
- ประโยชน์ของการแยก "ส่วนคำนวณบริสุทธิ์" ออกจาก "ส่วนมี side effect": ทดสอบง่ายขึ้น คาดเดาพฤติกรรมง่ายขึ้น นำกลับไปใช้ซ้ำได้ปลอดภัยกว่า

---

## Slide 65 — ตัวอย่าง: Pure vs Impure
**Key Message**: pure function ให้ผลเดิมทุกครั้งที่เรียกด้วยอาร์กิวเมนต์เดิม impure function อาจแก้ตัวแปร global หรือพิมพ์ผลข้างเคียงไปด้วย

```python
total_calls = 0

def add_pure(a, b):
    return a + b

def add_impure(a, b):
    global total_calls
    total_calls += 1
    print(f"เรียกครั้งที่ {total_calls}")
    return a + b

print(add_pure(2, 3))
print(add_pure(2, 3))
print(add_impure(2, 3))
print(add_impure(2, 3))
```

**Output:**
```
5
5
เรียกครั้งที่ 1
5
เรียกครั้งที่ 2
5
```

- `add_pure` คืนค่า 5 เสมอโดยไม่มีผลกระทบอื่นใด ส่วน `add_impure` แก้ไข `total_calls` (global) และ print ควบคู่ไปกับการคืนค่าทุกครั้งที่เรียก

---

## Slide 66 — ตัวอย่าง: Pure Function ทดสอบง่ายกว่า
**Key Message**: pure function ทดสอบด้วย `assert` ได้ตรง ๆ ทันที โดยไม่ต้องกังวลข้อความที่พิมพ์ออกหน้าจอ

```python
def calculate_discount(price, percent):
    return price - (price * percent / 100)

assert calculate_discount(100, 10) == 90
assert calculate_discount(200, 50) == 100
print("ผ่านการทดสอบทั้งหมด")
```

**Output:**
```
ผ่านการทดสอบทั้งหมด
```

- เหตุผลเชิงปฏิบัติที่นิยมแยกฟังก์ชัน "คำนวณ" ออกจากฟังก์ชัน "แสดงผล": ทดสอบด้วย `assert` ได้ทันทีโดยไม่ต้องดักจับข้อความที่พิมพ์ออกหน้าจอ

---

## Slide 67 — ตัวอย่าง: ฟังก์ชันแก้ไขข้อมูลผู้เรียกโดยไม่ตั้งใจ
**Key Message**: ส่ง mutable object เป็นอาร์กิวเมนต์แล้วแก้ไขในฟังก์ชัน จะกระทบตัวแปรต้นฉบับของผู้เรียกด้วยเสมอ

```python
def add_bonus_item(cart):
    cart.append("ของแถม")   # แก้ไข object เดิมโดยตรง (in-place)
    return cart

shopping_cart = ["เสื้อ", "กางเกง"]
new_cart = add_bonus_item(shopping_cart)

print(shopping_cart)
print(new_cart is shopping_cart)
```

**Output:**
```
['เสื้อ', 'กางเกง', 'ของแถม']
True
```

- การส่ง list เข้าฟังก์ชันทำให้พารามิเตอร์ชี้ไปยัง object เดียวกันกับอาร์กิวเมนต์ (เชื่อมโยงหัวข้อ 6) — เมื่อฟังก์ชันเรียก `.append(...)` จึงแก้ไข object ต้นฉบับโดยตรง
- หากไม่ต้องการผลข้างเคียงแบบนี้ ควรสร้างลิสต์ใหม่ภายในฟังก์ชันแทน เช่น `return cart + ["ของแถม"]`

---

## Slide 68 — สรุป Pure Function vs Side Effect
**Key Message**: แยก "ส่วนคำนวณบริสุทธิ์" ออกจาก "ส่วนมี side effect" ทำให้โปรแกรมทดสอบง่าย คาดเดาได้ และนำกลับมาใช้ซ้ำได้ปลอดภัยกว่า

| ลักษณะ | Pure Function | Impure Function (มี Side Effect) |
|---|---|---|
| ผลลัพธ์เมื่อเรียกซ้ำด้วย argument เดิม | เหมือนเดิมเสมอ | อาจไม่เหมือนเดิม |
| กระทบตัวแปร/ข้อมูลภายนอก | ไม่กระทบ | อาจกระทบ (global, mutable argument, print, ไฟล์) |
| ทดสอบด้วย `assert` | ง่าย ตรงไปตรงมา | ยาก ต้องจัดการผลข้างเคียงด้วย |

- pure function เรียกกี่ครั้งด้วยอาร์กิวเมนต์ชุดเดิมก็ได้ผลลัพธ์เดิมเสมอ ส่วน impure function ทำให้ "ผลลัพธ์โดยรวมของโปรแกรมขึ้นกับลำดับการเรียกฟังก์ชัน"
- Trick สำคัญ (mutable argument aliasing): การส่ง list เข้าฟังก์ชันทำให้พารามิเตอร์ชี้ไปยัง object เดียวกัน — นี่คือสาเหตุที่พบบ่อยที่สุดของ side effect ที่ไม่ตั้งใจ

---

## Slide 69 — Function Signature คืออะไร
**Key Message**: signature คือ "สัญญา" ระหว่างผู้เขียนฟังก์ชันกับผู้เรียกใช้ — บอกว่ารับอะไรเข้าและคืนอะไรออก โดยไม่ต้องอ่านโค้ดภายใน

- นิยาม signature: ส่วนหัวของฟังก์ชันที่ระบุชื่อฟังก์ชัน จำนวน/ชื่อพารามิเตอร์ที่รับเข้ามา และ (ถ้ามี) ชนิดของค่าที่คาดว่าจะส่งกลับ
- signature ทำหน้าที่เป็น "สัญญา" (contract) ระหว่างผู้เขียนฟังก์ชันกับผู้เรียกใช้ — ผู้เรียกทราบได้จาก signature อย่างเดียวว่าต้องส่งอาร์กิวเมนต์กี่ตัว ชนิดใด และควรได้รับอะไรกลับมา
- สัญญาครอบคลุมมากกว่าชื่อพารามิเตอร์ — รวมถึง "ชนิด/ลักษณะของค่าที่ส่งกลับในทุกเส้นทางการทำงาน" ด้วย
- function annotation ใน Python: ระบุชนิดข้อมูลของพารามิเตอร์และค่าที่คืนไว้ใน signature ได้ แต่เพราะ Python เป็น dynamically typed จึงเป็นเพียง "เอกสารประกอบ" ไม่ได้ถูกบังคับตรวจสอบขณะรันจริง

---

## Slide 70 — ตัวอย่าง: Signature เป็นสัญญาที่พึ่งพาได้
**Key Message**: ไม่ว่าจะเรียกแบบ positional หรือ keyword argument ผลลัพธ์ตรงตาม signature เสมอ

```python
def calculate_area(width, height):
    return width * height

print(calculate_area(5, 3))
print(calculate_area(height=3, width=5))
```

**Output:**
```
15
15
```

- ผู้เรียกทราบจาก signature `calculate_area(width, height)` อย่างเดียวว่าต้องส่งค่าอะไรเข้าไป โดยไม่ต้องอ่านโค้ดภายในฟังก์ชันเลย

---

## Slide 71 — ตัวอย่าง: Function Annotation
**Key Message**: annotation ไม่ใช่กลไกบังคับชนิดข้อมูล เป็นเพียงเอกสารประกอบที่มีประโยชน์ต่อผู้พัฒนาและ IDE/type-checker ภายนอก

```python
def calculate_area(width: float, height: float) -> float:
    return width * height

print(calculate_area(5, 3))
print(calculate_area.__annotations__)
```

**Output:**
```
15
{'width': <class 'float'>, 'height': <class 'float'>, 'return': <class 'float'>}
```

- แม้ส่ง `int` เข้าไป (5, 3 ไม่ใช่ float) Python ก็ไม่บังคับหรือแจ้ง error ใด ๆ — annotation เก็บไว้ใน `__annotations__` เพื่อเป็นเอกสารประกอบเท่านั้น

---

## Slide 72 — ⚠️ ข้อควรระวัง: ละเมิดสัญญาโดยปริยาย (Implicit None Return)
**Key Message**: ฟังก์ชันที่มี `return` เฉพาะกรณีเจอ (ไม่มี return ท้ายฟังก์ชัน) จะคืน `None` โดยปริยายโดยไม่มีคำเตือนใด ๆ

```python
records = [{"id": 1, "name": "Aom"}, {"id": 2, "name": "Beam"}]

def find_student(student_id):
    for record in records:
        if record["id"] == student_id:
            return record["name"]
    # ไม่มี return ท้ายฟังก์ชัน -> คืน None โดยปริยายถ้าไม่เจอ

name = find_student(2)
print(name.upper())

missing = find_student(99)
print(missing.upper())
```

**Output:**
```
BEAM
Traceback (most recent call last):
  ...
AttributeError: 'NoneType' object has no attribute 'upper'
```

- **Trick สำคัญที่สุด**: การวนลูปค้นหาแล้วมี `return` เฉพาะกรณีเจอ (ไม่มี return ท้ายฟังก์ชัน) จะคืนค่า `None` โดยปริยาย (implicit return) — ผู้เรียกที่สมมติว่าได้ชนิดข้อมูลเดิมเสมอจะพบ error ทันทีที่รันจริง เช่น `AttributeError: 'NoneType' object has no attribute 'upper'`
- นี่คือการละเมิดสัญญาโดยปริยาย: signature ดูเหมือนจะคืนชื่อ (string) เสมอ แต่จริง ๆ แล้วมีเส้นทางหนึ่งที่คืน `None`

---

## Slide 73 — สรุป Function Signature / Contract
**Key Message**: "สัญญา" ของฟังก์ชันไม่ได้มีแค่ชื่อพารามิเตอร์ แต่รวมถึงชนิด/ลักษณะของค่าที่ส่งกลับในทุกเส้นทางการทำงานด้วย

- signature กำหนดว่าฟังก์ชัน "รับอะไรเข้า และคืนอะไรออก" โดยไม่ต้องอ่านโค้ดภายในฟังก์ชันเลย
- annotation ช่วยด้านเอกสารและเครื่องมือภายนอก แต่ไม่ใช่การรับประกันพฤติกรรมขณะรันจริง
- ฟังก์ชันที่ดีควรคืนค่าชนิดเดียวกันในทุกเส้นทางการทำงาน (ทุก branch) เพื่อรักษาสัญญาไว้ให้ผู้เรียกใช้ไว้วางใจได้

---

## Slide 74 — Single Responsibility Principle (SRP) คืออะไร
**Key Message**: ฟังก์ชันหนึ่งฟังก์ชันควรทำหน้าที่เดียวให้ดี ไม่ควรรวมงานหลายอย่างที่ไม่เกี่ยวข้องกันไว้ในที่เดียว

- นิยาม SRP: หน่วยของโค้ดหนึ่งหน่วย (ระดับฟังก์ชัน) ควรมี "เหตุผลให้ต้องเปลี่ยนแปลง" เพียงเหตุผลเดียวเท่านั้น
- เชื่อมโยงโดยตรงกับ decomposition (หัวข้อ 1) — SRP ให้ "เกณฑ์" ที่ชัดเจนขึ้นว่าควรแบ่งฟังก์ชันตรงไหน
- ประโยชน์: ทดสอบได้ง่ายขึ้น แก้ไขส่วนหนึ่งโดยไม่กระทบอีกส่วนหนึ่ง นำกลับไปใช้ซ้ำในบริบทอื่นได้สะดวกขึ้น

---

## Slide 75 — ตัวอย่าง: แยกการคำนวณออกจากการแสดงผล
**Key Message**: ฟังก์ชันเดียวที่ทำสองหน้าที่ ทดสอบและนำผลไปใช้ต่อไม่ได้ — แยกตาม SRP แล้วนำกลับมาใช้ซ้ำได้

```python
# ไม่ทำตาม SRP — คำนวณและแสดงผลปนกัน
def process_order_bad(price, qty):
    total = price * qty
    print(f"ยอดรวม: {total} บาท")

# ทำตาม SRP — แยกหน้าที่ชัดเจน
def calculate_total(price, qty):
    return price * qty

def display_total(total):
    print(f"ยอดรวม: {total} บาท")

total = calculate_total(50, 3)
display_total(total)
```

**Output:**
```
ยอดรวม: 150 บาท
```

- `calculate_total` คืนค่าไปใช้ต่อได้ (เช่นบันทึกลงฐานข้อมูล) ในขณะที่ `process_order_bad` ทำได้แค่พิมพ์อย่างเดียว ดึงค่าไปใช้ต่อไม่ได้

---

## Slide 76 — ตัวอย่าง: แยกความรับผิดชอบ 3 หน้าที่
**Key Message**: แยกเป็นฟังก์ชันคนละหน้าที่ ทำให้แต่ละส่วนแก้ไข ทดสอบ และนำกลับมาใช้ซ้ำได้อย่างอิสระจากกัน

```python
def calculate_bonus(sales_amount):
    return sales_amount * 0.05

def record_sale(sales_amount):
    print(f"บันทึกยอดขาย: {sales_amount} บาท")

def format_bonus_message(bonus):
    return f"โบนัสที่ได้รับ: {bonus:.2f} บาท"

sales = 12000
bonus = calculate_bonus(sales)
record_sale(sales)
print(format_bonus_message(bonus))
```

**Output:**
```
บันทึกยอดขาย: 12000 บาท
โบนัสที่ได้รับ: 600.00 บาท
```

- สามฟังก์ชันแยกกันคนละหน้าที่: คำนวณ (`calculate_bonus`), บันทึกข้อมูล (`record_sale`), จัดรูปแบบข้อความ (`format_bonus_message`)

---

## Slide 77 — ตัวอย่าง: ผลกระทบเชิงปฏิบัติของการละเมิด SRP
**Key Message**: ฟังก์ชันที่รวมตรรกะตัดสินใจ + แสดงผลไว้ด้วยกัน ใช้กับ list comprehension ไม่ได้โดยไม่มีข้อความแทรกออกมา

```python
def calculate_and_show_grade(score):
    grade = "A" if score >= 80 else "B" if score >= 70 else "C"
    print(f"คะแนน {score} ได้เกรด {grade}")
    return grade

def calculate_grade(score):
    return "A" if score >= 80 else "B" if score >= 70 else "C"

grades = [calculate_grade(s) for s in [85, 72, 60]]
print(grades)
```

**Output:**
```
['A', 'B', 'C']
```

- ถ้าใช้ `calculate_and_show_grade` แทนใน list comprehension จะได้ข้อความ "คะแนน ... ได้เกรด ..." พิมพ์แทรกออกมาสามบรรทัดก่อนเห็นผลลัพธ์ลิสต์ — ผลข้างเคียงที่ไม่ต้องการ
- `calculate_grade` (ตาม SRP) ทำหน้าที่เดียวคือคำนวณ จึงใช้ใน list comprehension ได้อย่างสะอาด

---

## Slide 78 — สรุป SRP
**Key Message**: ฟังก์ชันที่รวมสองหน้าที่ไว้ด้วยกันมี "เหตุผลให้ต้องแก้ไขมากกว่าหนึ่งอย่าง" และนำส่วนคำนวณไปใช้ซ้ำโดยไม่พิมพ์ผลลัพธ์ออกมาด้วยไม่ได้

- แนวทางที่แยกฟังก์ชันมีความยืดหยุ่นในการนำไปใช้ซ้ำและทดสอบมากกว่า แม้ผลลัพธ์ที่ผู้ใช้เห็นจะเหมือนกันก็ตาม
- เชื่อมโยงกับหัวข้อ 13 (pure function vs side effect) — ฟังก์ชันที่คำนวณอย่างเดียวไม่มีผลข้างเคียงใด ๆ จึงนำไปใช้ซ้ำได้อย่างปลอดภัย
- SRP คือเกณฑ์ปฏิบัติที่ทำให้หลักการ decomposition (หัวข้อ 1) ชัดเจนขึ้น: "ควรแบ่งฟังก์ชันตรงไหน" — คำตอบคือแบ่งตามจำนวนเหตุผลที่ต้องเปลี่ยนแปลง

---

## Slide 79 — Summary — ทบทวนภาพรวมทั้ง 15 หัวข้อ
**Key Message**: พื้นฐานคือสิ่งที่ต้องสอบ ส่วนที่เหลือคือการมองเห็นภาพกว้างของฟังก์ชันใน Python

| ระดับ | หัวข้อ | อยู่ในขอบเขตสอบ? |
|---|---|---|
| พื้นฐาน | 1. DRY/Decomposition · 2. Definition vs Call · 3. Parameter vs Argument · 4. Return vs Procedure · 5. Scope | ใช่ |
| กลาง | 6. By value/reference · 7. Default parameters · 8. `*args`/`**kwargs` · 9. Recursion | ไม่ (เสริม) |
| สูง | 10. First-class · 11. Lambda · 12. Higher-order · 13. Pure/Side effect · 14. Signature/Contract · 15. SRP | ไม่ (เสริม) |

- กฎหลักของวิชานี้ที่ต้องจำ: **return ค่าเดียวเสมอ** (มีข้อยกเว้นที่ตั้งใจแสดงไว้จุดเดียวคือ Lambda ตัวอย่างที่ 3 ⚠️)
- สัปดาห์ 07: try/except, defensive input, oral defense
