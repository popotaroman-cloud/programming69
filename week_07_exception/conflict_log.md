# Conflict Log — Week 07 Exception

บันทึกจุดที่ตัวอย่างโค้ดในเอกสารประกอบการสอน (lecture note / lab / slide / notebook) ของสัปดาห์ 7 มีรูปแบบต่างจากกฎ/ธรรมเนียม
ที่หลักสูตรกำหนดไว้ก่อนหน้า (สืบทอดจาก Week 06 Function) ไฟล์นี้ใช้ร่วมกันโดยหลายกระบวนการ (agent) ที่ทำงานคนละไฟล์ในชุดเอกสารนี้
แต่ละรายการด้านล่างเป็นบล็อกที่บันทึกโดยอิสระ ระบุข้อเท็จจริงล้วน ไม่มีข้อเสนอแนะหรือการตัดสินว่าควรแก้ไขอย่างไร

---

## รายการที่ 1

- **ไฟล์**: `week_07_exception/lecture_note_advanced.md`
- **หัวข้อ**: 14 — การดักข้อผิดพลาดแบบไม่ระบุชนิด (Bare `except`)
- **ตัวอย่างที่พบ**: ตัวอย่างที่ 2 (การใช้งานจริง — ประมวลผลชุดข้อมูลโดยไม่ให้รายการที่มีปัญหาทำให้ทั้งชุดหยุดทำงาน)
- **กฎที่เกี่ยวข้อง**: กฎ "ฟังก์ชัน return ค่าเดียวเสมอ" ที่สืบทอดจาก Week 06 Function และปรากฏเป็นธรรมเนียมของฟังก์ชัน
  `safe_divide` ใน `week_07_exception/slides/07_exception.md` (Slide 5) ซึ่งเป็นขอบเขตสอบจริงของสัปดาห์ 7
- **สิ่งที่ขัดกัน**: ฟังก์ชัน `process_batch` ในตัวอย่างนี้จบด้วย `return total, error_count` ซึ่งคืนค่าสองค่าพร้อมกัน
  เป็น tuple (ไม่ใช่ค่าเดียว) และโค้ดฝั่งเรียกใช้ tuple unpacking (`total, error_count = process_batch(records)`) เพื่อแยกรับ
  ค่าทั้งสอง
- **โค้ดจริงที่พบ**:
```python
def process_batch(records):
    total = 0
    error_count = 0
    for text in records:
        try:
            total += int(text)
        except:
            error_count += 1
    return total, error_count

total, error_count = process_batch(records)
```

---
