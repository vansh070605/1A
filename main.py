import os
import fitz  # PyMuPDF
import json

def classify_heading(size):
    """
    Simple font size-based heading classification.
    Tune thresholds as needed based on testing.
    """
    if size >= 17:
        return "H1"
    elif size >= 14:
        return "H2"
    elif size >= 11:
        return "H3"
    return None

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = os.path.basename(pdf_path).replace(".pdf", "")

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    font_size = span["size"]

                    level = classify_heading(font_size)
                    if level and text:
                        outline.append({
                            "level": level,
                            "text": text,
                            "page": page_num
                        })

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
