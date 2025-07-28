import os
import fitz  # PyMuPDF
import json
import re

def classify_heading(text, size, is_bold):
    """
    Improved heading classification based on font size, boldness, and numbering pattern.
    """
    numbered_heading = re.match(r"^\d+\.", text)  # matches patterns like "1.", "2.", etc.

    if size >= 18 and is_bold:
        return "H1"
    elif size >= 15 and (is_bold or text.isupper()):
        return "H2"
    elif size >= 11 or numbered_heading:
        return "H3"
    return None

def extract_title(doc):
    """
    Extracts the most prominent title from the top of the first page.
    """
    title_candidates = []
    first_page = doc[0]
    blocks = first_page.get_text("dict")["blocks"]
    
    for block in blocks:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text = span["text"].strip()
                size = span["size"]
                font = span.get("font", "").lower()

                if len(text.split()) >= 3 and size >= 15:
                    title_candidates.append((size, text))

    # Return the largest font size candidate
    if title_candidates:
        return sorted(title_candidates, reverse=True)[0][1]
    else:
        return os.path.basename(doc.name).replace(".pdf", "")

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = extract_title(doc)
    seen = set()

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    size = span["size"]
                    font = span.get("font", "").lower()
                    is_bold = "bold" in font or "black" in font  # handles different font naming conventions

                    if not text or text in seen or len(text) < 3:
                        continue

                    level = classify_heading(text, size, is_bold)
                    if level:
                        outline.append({
                            "level": level,
                            "text": text,
                            "page": page_num
                        })
                        seen.add(text)

    return {
        "title": title,
        "outline": outline
    }

def main():
    input_dir = "input"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            print(f"Processing: {filename}")
            output_data = extract_outline(pdf_path)

            json_filename = filename.replace(".pdf", ".json")
            output_path = os.path.join(output_dir, json_filename)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(output_data, f, indent=2, ensure_ascii=False)

    print("All PDFs processed.")

if __name__ == "__main__":
    main()
