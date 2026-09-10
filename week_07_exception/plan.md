# Plan: Week 07 Exception — Lecture Note + Lab + Slide + Notebook (ครอบคลุม 15 หัวข้อ)

> เอกสารนี้จำลอง workflow เดียวกับที่ใช้กับ Week 06 Function ทั้งหมด (ดู `../week_06_function/plan.md` เป็นตัวอย่างอ้างอิง)
> ปรับให้เข้ากับหัวข้อ Exception ของสัปดาห์ 7 — **หยุดรอตรวจสอบหลังทำแต่ละขั้นตอนใหญ่เสร็จ ตามที่ผู้ใช้ระบุไว้**

## เป้าหมาย
สร้างชุดเอกสารประกอบการสอนสำหรับ Week 07 — Exception ครอบคลุมแนวคิดการจัดการข้อผิดพลาดแบบ
**language-agnostic** ทั้ง 15 หัวข้อ (พื้นฐาน/กลาง/สูง) อ้างอิงจาก 3 แหล่งเดียวกับที่ใช้ทำ Week 06:
- W3Schools — https://www.w3schools.com/python/python_try_except.asp
- GeeksforGeeks — https://www.geeksforgeeks.org/python/python-exception-handling/
- TutorialsPoint — https://www.tutorialspoint.com/python/python_exceptions.htm (+ หน้าย่อย try-except, try-finally, raising exceptions, user-defined exception, assertions, built-in exceptions)

ตัวอย่างโค้ดเป็น Python ล้วน คำอธิบายแนวคิดเขียนแบบทั่วไปก่อนแล้วค่อยลง syntax

## ไม่จำกัดความยาว (อัปเดต — ใช้กับทุกไฟล์ในชุดนี้ ไม่ใช่แค่ slide outline)
**ทุกไฟล์ที่สร้างในแผนนี้ (lecture note, lab, slide outline, สไลด์, notebook) ไม่จำกัดจำนวนหน้า/บรรทัด/สไลด์**
ให้ความครบถ้วนของเนื้อหาและความชัดเจนของคำอธิบายมาก่อนความกระชับเสมอ ห้ามตัดทอนเนื้อหาเพียงเพื่อให้ไฟล์สั้นลง

## Output — ไฟล์ที่จะสร้าง (ทำทีละกลุ่ม หยุดตรวจก่อนไปขั้นถัดไป)
- `week_07_exception/lecture_note_basic.md` — หัวข้อ 1–5 (ตรงกับขอบเขตสอบจริงใน `slides/07_exception.md`)
- `week_07_exception/lecture_note_intermediate.md` — หัวข้อ 6–9 (เสริม นอกขอบเขตสอบ)
- `week_07_exception/lecture_note_advanced.md` — หัวข้อ 10–15 (เสริม นอกขอบเขตสอบ พร้อม banner แจ้งขอบเขตเนื้อหาแบบเป็นกลาง ไม่ใช้ถ้อยคำเชิงเตือน)
- `week_07_exception/lab_pseudocode_to_python.md` — lab 12 ข้อ (3 ระดับ x 4 ข้อ ตามโครงสร้าง scaffold ที่ปรับปรุงแล้วจาก week 6)
- `week_07_exception/slide_content_outline.md` — สกัดเนื้อหาเตรียมทำสไลด์ (ไม่จำกัดจำนวนหน้า)
- `slides/07_exception.md` + `.html` + `index.html` — สไลด์ฉบับเต็มครอบคลุม 15 หัวข้อ (แทนที่ 8 สไลด์เดิม)
- `week_07_exception/notebooks/*.ipynb` — notebook คู่ขนานของทุกไฟล์ (คำถาม + เฉลยแยกไฟล์)

## Mapping: 15 หัวข้อ → แหล่งอ้างอิง

**ระดับพื้นฐาน (ตรงกับขอบเขตสอบ — `slides/07_exception.md` เดิม)**
1. Exception คืออะไร ต่างจาก Syntax Error อย่างไร — W3: intro / GfG: Errors vs Exceptions / TP: intro
2. `try`/`except` พื้นฐาน (จับ exception ประเภทเดียว) — W3: Exception Handling / GfG: Catching Exceptions / TP: try-except Block
3. Exception types ที่พบบ่อย: `ZeroDivisionError`, `ValueError`, `TypeError`, `IndexError` — GfG: Built-in Exceptions / TP: Built-in Exceptions (29 ชนิด)
4. จับหลาย exception ในฟังก์ชันเดียว (multiple except blocks) — W3: Multiple Exception Blocks / GfG: Multiple Exceptions / TP: multiple except statements
5. Defensive Input/Function — เขียนฟังก์ชันให้ทนทานต่อ error (ต่อยอดจาก slide 5 เดิม `safe_divide`)

**ระดับกลาง (เสริม นอกขอบเขตสอบ)**
6. `else` clause — รันเมื่อไม่มี error เกิดใน try — W3: Else / GfG: (มีใน syntax overview) / TP: try-except-else
7. `finally` clause — รันเสมอไม่ว่าจะเกิด error หรือไม่ (cleanup) — W3: Finally / TP: try-finally Block
8. จับ exception object เป็นตัวแปร (`except X as e`) + พิมพ์ข้อความ error จริง — TP: Exception Arguments
9. `raise` — โยน exception เองจากเงื่อนไข validation — W3: Raise / GfG: Raise an Exception / TP: Raising Exceptions

**ระดับสูง (เสริม นอกขอบเขตสอบ)**
10. Custom Exception — สร้าง exception ชนิดของตัวเองโดย subclass จาก `Exception` — TP: User-defined Exception
11. Exception Hierarchy — ลำดับชั้น built-in exceptions อธิบายว่าทำไม `except Exception` จับได้ทุกอย่าง — GfG: Built-in Exceptions / TP: Built-in Exceptions
12. `assert` / `AssertionError` — sanity check ระหว่างพัฒนา — TP: Assertions
13. Nested try/except/finally — TP: nested try-except-finally
14. Bare `except:` (catch-all) และความเสี่ยง — anti-pattern — GfG: "Catch-All Handlers and Their Risks"
15. Re-raise / exception chaining (`raise ... from ...`) — เสริมเอง (ไม่มีหน้าตรงในสามแหล่ง ระบุชัดในเอกสาร)

## กฎขั้นต่ำ: จำนวนตัวอย่างโค้ดต่อหัวข้อ (เหมือน week 6 ฉบับล่าสุด)
**3 ตัวอย่างทุกระดับ ทุกหัวข้อ** และต้องคนละโดเมนปัญหากัน (ห้ามใช้สถานการณ์ซ้ำกันทั้ง 3 ตัวอย่างในหัวข้อเดียว):
- พื้นฐาน/กลาง: 1) ตัวอย่างหลัก 2) ตัวอย่างบริบทอื่นที่ต่างโดเมน 3) ตัวอย่าง edge case/ข้อผิดพลาดที่พบบ่อย
- สูง: 1) ตัวอย่างพื้นฐานของแนวคิด 2) ตัวอย่างการใช้งานจริง 3) ตัวอย่าง anti-pattern/ข้อควรระวัง

## องค์ประกอบของ "1 ตัวอย่าง" (อัปเดต — เพิ่มเป็น 5 ส่วน จากเดิม 4 ส่วนของ week 6)
ทุกตัวอย่างต้องมีครบ 5 ส่วนนี้เสมอ ขาดส่วนใดถือว่าไม่สมบูรณ์:

1. **โค้ดพร้อมเลขบรรทัดกำกับ** (`01  ...`)
2. **Output ที่รันจริงยืนยันแล้ว** — กำกับทุกตัวอย่าง ไม่มีข้อยกเว้น แม้ตัวอย่างจะสั้นหรือดูชัดเจนอยู่แล้วก็ตาม
3. **ตารางการเปลี่ยนแปลงค่า (trace table)** — บรรทัดที่ / คำสั่งที่ทำงาน / ตัวแปร-ค่า / หมายเหตุ
4. **คำอธิบายภาพรวม** — อธิบายโค้ดทั้งบล็อกทุกครั้ง (บังคับ ไม่ใช่ทางเลือก) อ้างอิงช่วงบรรทัดที่เกี่ยวข้อง
5. **จุดสังเกต** (ส่วนใหม่) — ระบุสิ่งที่ผู้เรียนควรสังเกตเป็นพิเศษจากตัวอย่างนี้โดยเฉพาะ (เช่น พฤติกรรมที่ไม่ตรงสัญชาตญาณ, ผลลัพธ์ที่เปลี่ยนไปเมื่อเงื่อนไขเปลี่ยน, จุดที่มักเข้าใจผิด) เขียนแยกเป็นหัวข้อของตัวเอง ไม่ปนกับคำอธิบายภาพรวม

## การทดสอบตัวอย่างโค้ด (Verification) — บังคับทุกตัวอย่าง เหมือนเดิมทุกประการ
รันจริงด้วย Python ผ่าน scratch file ก่อนใส่ Output เสมอ ห้ามเดา ห้ามคัดลอก output จากเว็บต้นทางโดยไม่รันซ้ำ

## มาตรฐานภาษาและศัพท์เทคนิค (เพิ่มคำศัพท์เฉพาะของ Exception)
ใช้ภาษาไทยทางการ ต่อยอดตารางศัพท์เดิมจาก week 6 (`plan.md` ของ week 6) เพิ่มคำใหม่:

| English | ใช้คำว่า |
|---|---|
| exception | ข้อผิดพลาดขณะรัน (exception) |
| syntax error | ข้อผิดพลาดทางไวยากรณ์ (syntax error) |
| raise | โยนข้อผิดพลาด (raise) |
| try block | บล็อกทดลองรัน (try) |
| except block | บล็อกดักข้อผิดพลาด (except) |
| else clause (try) | ส่วน else (เมื่อไม่มีข้อผิดพลาด) |
| finally clause | ส่วน finally (รันเสมอ) |
| custom exception | ข้อผิดพลาดที่ผู้ใช้กำหนดเอง (custom exception) |
| assertion | การยืนยันเงื่อนไข (assert) |
| exception hierarchy | ลำดับชั้นของข้อผิดพลาด |
| bare except / catch-all | การดักข้อผิดพลาดแบบไม่ระบุชนิด (bare except) |
| defensive programming | การเขียนโปรแกรมเชิงป้องกัน (defensive programming) |
| traceback | ข้อความแสดงลำดับข้อผิดพลาด (traceback) |

## การรีวิวภาษาเชิงวิชาการ (Academic Language Review) — ขั้นตอนใหม่ บังคับทุกไฟล์
หลังเขียนเนื้อหาแต่ละไฟล์เสร็จ ต้องไล่รีวิวอีกรอบเพื่อ:
- แทนที่คำที่ไม่เป็นทางการ/ภาษาพูด/ภาษาปาก ด้วยคำศัพท์ทางวิชาการที่ตรงตามตารางศัพท์มาตรฐานข้างต้น
- ตรวจรูปประโยคให้เป็นรูปแบบเอกสารวิชาการ (เลี่ยงคำลงท้ายแบบสนทนา, เลี่ยงการใช้สรรพนามที่ไม่เป็นทางการ)
- ตรวจสอบว่าคำศัพท์เดียวกันถูกแปล/ใช้สม่ำเสมอกันตลอดทั้งไฟล์และข้ามไฟล์ (basic/intermediate/advanced/lab ต้องใช้คำเดียวกัน)

## นโยบายใหม่: ห้ามใส่คำเตือนเรื่อง "ขัดกฎ" ไว้ในเนื้อหา — ให้บันทึกลง log แทน
**เปลี่ยนจากแนวทางเดิมของ week 6** (ที่ใส่ ⚠️/หมายเหตุ/ข้อควรระวัง/คำแนะนำ ไว้ในเนื้อหาโดยตรงเมื่อพบตัวอย่างที่อาจขัดกับกฎของสไลด์) เป็นดังนี้:

- **ห้าม**ใช้คำว่า "หมายเหตุ", "ข้อควรระวัง", "คำแนะนำ", "remark", "note", "recommend" หรือคำอื่นที่มีนัยยะสื่อว่า "สิ่งนี้ขัดกับกฎ/ไม่ควรทำ/เป็นข้อยกเว้น" ปะปนอยู่ในเนื้อหาที่ส่งมอบ (lecture note, lab, slide, notebook) ไม่ว่าจะเป็นหัวข้อย่อยหรือประโยคแทรก
- เมื่อพบระหว่างเขียนเนื้อหาว่าตัวอย่างใดอาจขัดกับกฎที่ตั้งไว้ก่อนหน้า (เช่น กฎ "return ค่าเดียวเสมอ" ที่สืบทอดจาก week 6) **ให้บันทึกจุดนั้นแยกไว้ใน log ต่างหาก** — ไฟล์ `week_07_exception/conflict_log.md` — โดยระบุ: ไฟล์/หัวข้อ/ตัวอย่างที่พบ, อธิบายว่าขัดกับกฎอะไร, และเนื้อหาจริงของตัวอย่างนั้น (ไม่ต้องเสนอทางแก้ ไม่ต้องตัดสินว่าควรทำอย่างไร — รายงานข้อเท็จจริงแล้วปล่อยให้ผู้ใช้พิจารณาเอง)
- เนื้อหาที่ส่งมอบจริงจึงมีแต่การอธิบายแนวคิด/ตัวอย่าง/จุดสังเกตแบบเป็นกลาง ไม่มีการตัดสินแทนผู้อ่านว่าอะไรผิดหรือไม่ควรทำ

## Audit Checklist ต่อหัวข้อ (อัปเดต — 8 ข้อ ปรับข้อสุดท้าย)
Source coverage / Example count (3 ตัวอย่าง คนละโดเมน) / Verified output / Academic language (ผ่านการรีวิวภาษาเชิงวิชาการแล้ว) / Language-agnostic framing / Scope note (ตรงขอบเขตสอบหรือเสริม) / Cross-link / **Rule-conflict scan** (ตรวจแล้วว่าไม่มีคำเตือนเรื่องขัดกฎหลงเหลือในเนื้อหา — ประเด็นที่พบทั้งหมดถูกย้ายไป `conflict_log.md` แล้ว)

## Lab: 12 ข้อ (3 ระดับ x 4 ข้อ) — ใช้โครงสร้าง scaffold แบบเดียวกับ week 6 ฉบับแก้ไขล่าสุด
ต่อระดับ: ข้อ 1 = pseudocode, ข้อ 2–3 = คำอธิบายขั้นตอนเป็นข้อความ, ข้อ 4 = โจทย์/pain point ล้วน (ไม่มี scaffold)
**สำคัญ**: ต้องออกแบบสถานการณ์ให้ไม่ซ้ำกับตัวอย่างใน lecture note/สไลด์ (ตรวจสอบก่อนสรุปเหมือนที่ทำกับ week 6)

## Practice ท้ายบท ≥20 ข้อ/ไฟล์ (เหมือน week 6)
ผสม 4 ประเภท: อธิบายแนวคิด / ทายผลลัพธ์ / หาข้อผิดพลาด / เขียนโค้ด — มีเฉลยรันจริงแยกหมวดท้ายไฟล์

## จุดอ้างอิงเรื่องขอบเขตของ slide เดิม (ข้อเท็จจริง ไม่ใช่คำเตือน)
`slides/07_exception.md` (8 สไลด์เดิม) มีฟังก์ชัน `safe_divide` ใน Slide 5 ที่ return ค่าเดียวเสมอ (ตามธรรมเนียมที่สืบทอดจาก week 6)
ระหว่างเขียนหัวข้อ 6–15 หากพบตัวอย่างที่มีรูปแบบการ return ต่างจากนี้ ให้บันทึกลง `conflict_log.md` ตามนโยบายด้านบน
แทนการติดคำเตือนไว้ในเนื้อหา

## Workflow (หยุดตรวจสอบหลังทำแต่ละ Step ใหญ่เสร็จ — ตามที่ผู้ใช้ระบุ)

```
Step 0   ยืนยัน plan.md นี้กับผู้ใช้                                    ✅ เสร็จแล้ว
Step 1   เขียน lecture_note_basic.md (หัวข้อ 1–5)                      ✅ เสร็จแล้ว (1591 บรรทัด)
Step 2   เขียน lecture_note_intermediate.md (หัวข้อ 6–9)               ✅ เสร็จแล้ว (1371 บรรทัด)
Step 3   เขียน lecture_note_advanced.md (หัวข้อ 10–15)                 ✅ เสร็จแล้ว (1672 บรรทัด)
Step 4   เขียน lab_pseudocode_to_python.md (12 ข้อ) + ตรวจไม่ให้ซ้ำ    ✅ เสร็จแล้ว (715 บรรทัด)
Step 5   สกัด slide_content_outline.md (ครบ 15 หัวข้อ ไม่จำกัดหน้า)    ✅ เสร็จแล้ว (427 บรรทัด)
Step 6   สร้างสไลด์เต็ม (slides/07_exception.md/html/index.html)      ✅ เสร็จแล้ว (84 สไลด์ + 6 diagram)
Step 7   สร้าง notebooks (คำถาม+เฉลยแยกไฟล์ ทุกไฟล์) + รันจริงยืนยัน  ✅ เสร็จแล้ว (8 ไฟล์)
Step 8   ตรวจสอบรวม (terminology, rule-conflict scan, dedup กับ lab)   ✅ เสร็จแล้ว
```

**ยกเลิกการหยุดรอตรวจระหว่างทาง** ตามคำสั่งของผู้ใช้ ("ทำทั้งหมดให้เสร็จที่เหลือ โดยไม่ต้องให้ตรวจสอบอีก") — ทำ Step 1–8 ต่อเนื่องจนจบ

## ผลการดำเนินงาน (เสร็จสิ้น 2026-09-03)

**ไฟล์ที่สร้างจริง:**
- `lecture_note_basic.md` / `lecture_note_intermediate.md` / `lecture_note_advanced.md` — รวม 15 หัวข้อ, 36+ ตัวอย่างรันจริง (แต่ละตัวอย่างครบ 5 ส่วน: โค้ด+เลขบรรทัด, output จริง, trace table, คำอธิบายภาพรวม, จุดสังเกต), ทุกไฟล์มีแบบฝึกหัดท้ายบท ≥20 ข้อ
- `lab_pseudocode_to_python.md` — 12 ข้อ (3 ระดับ x 4 ข้อ scaffold) ตรวจสอบแล้วไม่ซ้ำโดเมนกับ lecture note
- `slide_content_outline.md` — สกัดครบ 15 หัวข้อ ไม่จำกัดความยาว
- `slides/07_exception.{md,html}` + `index.html` — 84 สไลด์ (จากเดิม 8 สไลด์) + 6 diagram (matplotlib → base64 PNG ฝังใน HTML) เก็บสคริปต์ต้นฉบับไว้ที่ `slides/figures/`
- `notebooks/*.ipynb` — 8 ไฟล์ (คำถาม + เฉลยแยกไฟล์ ครบทุกเอกสาร) รันจริงยืนยันทุกเซลล์ (error ที่ปรากฏคือ traceback จริงที่ตั้งใจสาธิต ระบุด้วย tag `raises-exception` ชัดเจน)
- `conflict_log.md` — 1 รายการ (หัวข้อ 14 ตัวอย่างที่ 2 `process_batch` return เป็น tuple สองค่า ขัดกับกฎ "return ค่าเดียวเสมอ")

### ผลตรวจสอบ Step 8
- **Rule-conflict scan**: สแกนคำต้องห้าม (หมายเหตุ/ข้อควรระวัง/คำแนะนำ/remark/note/recommend) ทั้ง 4 ไฟล์ `.md` และ 8 ไฟล์ `.ipynb` แล้ว — พบหลงเหลือเฉพาะในส่วน audit-report ที่รายงานผลการสแกนเอง (ไม่ใช่การใช้งานจริง) ยกเว้นจุดเดียวที่แก้ไขแล้ว: cross-reference note ในสมุดบันทึก 6 ไฟล์ที่ใช้คำว่า "หมายเหตุ" สำหรับชี้ไปยังไฟล์เฉลย (เป็นการนำทาง ไม่ใช่คำเตือนเรื่องขัดกฎ แต่แก้เป็น "ข้อมูลเพิ่มเติม" เพื่อความสอดคล้องกับนโยบาย)
- **Terminology**: ตรวจศัพท์เทคนิคหลัก (ข้อผิดพลาดขณะรัน, บล็อกทดลองรัน, บล็อกดักข้อผิดพลาด) ใช้ตรงกันทั้ง 4 ไฟล์ `.md`
- **Dedup**: lab ตรวจสอบแล้วไม่ใช้โดเมนซ้ำกับ lecture note (12 โดเมนใหม่ทั้งหมด)
- **Notebook execution**: ทุกไฟล์รันจริงผ่าน `nbclient` ยืนยันแล้วว่าไม่มี error ที่ไม่คาดคิดหลงเหลือ (พบและแก้บั๊ก 1 จุดระหว่างทำ — ตัวแปรรั่วข้าม cell ในไฟล์ advanced ทำให้ topic 14 ตัวอย่างที่ NameError ไม่เกิดจริง แก้ด้วย `%reset -f` ต่อ cell)
