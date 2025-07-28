import os
import fitz  # PyMuPDF
import json
import re
from langdetect import detect_langs, DetectorFactory

DetectorFactory.seed = 0  # For consistent language detection

def classify_heading(text, size, is_bold):
    """Classifies headings based on font size, boldness, and numbering patterns."""
    if not text or len(text) < 3:
        return None
    if size >= 18 and is_bold:
        return "H1"
    if size >= 15 and (is_bold or text.isupper()):
        return "H2"
    if size >= 11 or re.match(r"^\d+\.", text):
        return "H3"
    return None

def detect_language(text):
    if len(text) >= 5:
        try:
            langs = detect_langs(text)
            lang_list = [{"lang": str(l.lang), "prob": round(l.prob, 2)} for l in langs]
        except Exception:
            lang_list = [{"lang": "en", "prob": 1.0}]
    else:
        lang_list = [{"lang": "en", "prob": 1.0}]
    return lang_list

def extract_title_and_outline(doc):
    outline = []
    seen = set()
    # Title: largest text on first page
    largest_span = {"text": "", "size": 0}
    for block in doc[0].get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text = span["text"].strip()
                size = span["size"]
                if len(text) >= 3 and size > largest_span["size"]:
                    largest_span = {"text": text, "size": size}
    title = largest_span["text"] if largest_span["text"] else os.path.basename(doc.name).replace(".pdf", "")
    outline.append({
        "level": "H1",
        "text": title,
        "page": 1,
        "langs": detect_language(title)
    })
    seen.add(title)
    # Headings from all pages
    for page_num, page in enumerate(doc, start=1):
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    size = span["size"]
                    font = span.get("font", "").lower()
                    is_bold = "bold" in font or "black" in font
                    if not text or text in seen or len(text) < 3:
                        continue
                    level = classify_heading(text, size, is_bold)
                    if level:
                        outline.append({
                            "level": level,
                            "text": text,
                            "page": page_num,
                            "langs": detect_language(text)
                        })
                        seen.add(text)
    return title, outline

def main():
    input_dir = "input"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            print(f"Processing: {filename}")
            doc = fitz.open(pdf_path)
            title, outline = extract_title_and_outline(doc)
            output_data = {
                "title": title,
                "outline": outline
            }
            json_filename = filename.replace(".pdf", ".json")
            output_path = os.path.join(output_dir, json_filename)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(output_data, f, indent=2, ensure_ascii=False)
    print("All PDFs processed.")

if __name__ == "__main__":
    main()
