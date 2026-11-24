# -*- coding: utf-8 -*-
import os
from docx import Document
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = r"C:\Users\User\OneDrive\Документи\лаби\LABA-10.2a"
IMG_DIR = os.path.join(BASE_DIR, "images")
OUT_DOCX = os.path.join(BASE_DIR, "АП_РІ-13_Шах_ЛР-10.2а.docx")

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex="F8F9FA"):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._element.get_or_add_tcPr().append(shading_elm)

def add_p(doc, text="", bold=False, italic=False, size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, space_before=0):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.line_spacing = 1.15
    if text:
        r = p.add_run(text)
        r.bold = bold
        r.italic = italic
        r.font.name = 'Times New Roman'
        r.font.size = Pt(size)
        r.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_h(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_code_block(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_shading(cell, "F8F9FA")
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
    tcPr = cell._element.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:left w:val="single" w:sz="12" w:space="0" w:color="333333"/>\n'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    r = p.add_run(code_text)
    r.font.name = 'Courier New'
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(0, 0, 0)
    add_p(doc, "", space_after=4)

def add_img(doc, path, caption):
    if os.path.exists(path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        p.add_run().add_picture(path, width=Inches(5.5))
        add_p(doc, caption, italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)

def read_txt(rel_path):
    with open(os.path.join(BASE_DIR, rel_path), "r", encoding="utf-8") as f:
        return f.read().rstrip()

def generate_report():
    doc = Document()
    for section in doc.sections:
        section.top_margin = Cm(2)
        section.bottom_margin = Cm(2)
        section.left_margin = Cm(2)
        section.right_margin = Cm(2)

    add_p(doc, "", space_after=60)
    title_text = (
        "ЗВІТ\n"
        "про виконання лабораторної роботи № 10.2a\n"
        "«Масиви структур та об'єднань»\n"
        "з дисципліни\n"
        "«Алгоритмізація та програмування»\n\n"
        "студента групи РІ-13\n"
        "Шаха Владислава Ігоровича"
    )
    add_p(doc, title_text, bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    add_p(doc, "", space_after=60)
    add_p(doc, "Варіант № 32", bold=True, size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    doc.add_page_break()

    add_h(doc, "1. Мета роботи")
    add_p(doc, "Метою лабораторної роботи є набуття практичних навичок визначення і використання структур даних (struct), переліків (enum) та об'єднань (union) у мові програмування С++. Вивчення способів оголошення масивів структур, звернення до полів структур, а також реалізації підпрограм обробки масивів структур.")

    add_h(doc, "2. Завдання")
    add_img(doc, os.path.join(IMG_DIR, "task.png"), "Рис. 1. Умова лабораторної роботи № 10.2а (Варіант 32)")

    add_h(doc, "3. Алгоритм розв'язання")
    add_p(doc, "1. Використано структуру Student рівня А з полями prizv, kurs, spec, physics, math, it та перелік Specialnist.")
    add_p(doc, "2. Реалізовано компаратор compareStudents(a, b), який задає багатоключовий порядок впорядкування: спершу за оцінкою з фізики (за зростанням), далі за курсом (за зростанням), і за прізвищем (за спаданням — у зворотному до алфавітного порядку).")
    add_p(doc, "3. Підпрограма PhysicalSort(p, N) фізично переставляє елементи масиву структур у пам'яті відповідно до compareStudents().")
    add_p(doc, "4. Підпрограма BuildIndexArray(p, N, idx) формує масив індексів idx[0..N-1], сортуючи індекси за значеннями елементів p[idx[j]] без зміни вихідного масиву p, а PrintWithIndex(p, N, idx) виводить таблицю за індексним порядком.")
    add_p(doc, "5. Підпрограма BinarySearch(p, N, prizv, kurs, physics) виконує двійковий пошук у фізично впорядкованому масиві за складеним ключем (фізика, курс, прізвище за спаданням) за O(log N) та повертає індекс знайденого студента або -1.")
    add_p(doc, "6. У функції main() організовано циклічне текстове меню з перевіркою коректності введення даних.")

    add_h(doc, "4. Лістинг програми")
    add_p(doc, "Головний файл програми LABA-10.2a.cpp:", bold=True, space_after=4)
    add_code_block(doc, read_txt(r"LABA-10.2a\LABA-10.2a.cpp"))
    add_p(doc, "Заголовний файл student2a.h:", bold=True, space_after=4)
    add_code_block(doc, read_txt(r"LABA-10.2a\student2a.h"))
    add_p(doc, "Файл реалізації student2a.cpp:", bold=True, space_after=4)
    add_code_block(doc, read_txt(r"LABA-10.2a\student2a.cpp"))

    add_h(doc, "5. Схема програми")
    add_img(doc, os.path.join(IMG_DIR, "struct.png"), "Рис. 2. Структурна схема програми LABA-10.2a")

    add_h(doc, "6. Результати виконання програми")
    add_img(doc, os.path.join(IMG_DIR, "console_main.png"), "Рис. 3. Результат роботи основної програми у консолі")
    add_img(doc, os.path.join(IMG_DIR, "console_test.png"), "Рис. 4. Результат виконання модульних тестів (vstest.console.exe)")

    add_h(doc, "7. Контрольні запитання")
    qa = [
        ("1. Чим відрізняється фізичне впорядкування масиву структур від індексного?",
         "Під час фізичного впорядкування переміщуються самі об'єкти структур у пам'яті, тоді як при індексному формується окремий масив цілих індексів idx[], а початковий масив структур залишається незмінним."),
        ("2. Які переваги має індексне сортування для масивів великих структур?",
         "Замість копіювання великих структур під час обмінів переставляються лише 4-байтові індекси, крім того, зберігається вихідний порядок елементів і можна підтримувати кілька різних індексних масивів одночасно."),
        ("3. Як працює багатоключове порівняння двох структур?",
         "Спочатку порівнюються первинні ключі (physics). Якщо вони рівні, перевіряється вторинний ключ (kurs), а в разі рівності — третинний ключ (prizv за спаданням)."),
        ("4. Яка головна передумова коректної роботи алгоритму бінарного пошуку?",
         "Масив структур обов'язково має бути попередньо фізично впорядкований за тими самими ключами і в тому ж напрямку (зростання/спадання), за якими виконується порівняння у бінарному пошуку."),
        ("5. Яку часову складність має бінарний пошук порівняно з лінійним?",
         "Бінарний пошук має логарифмічну складність O(log N), тоді як лінійний пошук — O(N), тому на великих масивах бінарний пошук працює значно швидше.")
    ]
    for q, a in qa:
        add_p(doc, q, bold=True, size=12, space_before=4, space_after=2)
        add_p(doc, a, bold=False, size=12, space_before=0, space_after=6)

    add_h(doc, "8. Висновки")
    add_p(doc, "У процесі виконання лабораторної роботи № 10.2a було реалізовано фізичне та індексне багатоключове впорядкування масиву структур Student і бінарний пошук за складеним ключем (оцінка з фізики, курс, прізвище). Розроблено консольне меню з контролем коректності введення та перевірено всі алгоритми в модульних тестах UnitTest10.2a.")

    doc.save(OUT_DOCX)
    print("Saved:", OUT_DOCX)

if __name__ == "__main__":
    generate_report()
