# Approach Explanation

## Overview
This solution is designed to automatically extract a structured outline from PDF documents, identifying the document title and hierarchical headings (H1, H2, H3) along with their page numbers. The extracted information is output as a clean JSON file, enabling downstream tasks such as semantic search, recommendations, and document insights.

---

## Key Steps in the Approach

### 1. PDF Parsing
- **Library Used:** [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
- **Why:** PyMuPDF provides fast, reliable access to PDF text, font properties, and layout information, which are essential for heading detection.

### 2. Title Extraction
- The title is identified as the largest text span on the first page, assuming that the most prominent text is the document title.
- If no suitable candidate is found, the filename (without extension) is used as a fallback.

### 3. Heading Detection & Classification
- **Features Used:**
  - **Font Size:** Larger font sizes are more likely to be headings.
  - **Boldness:** Bold or black fonts are prioritized for headings.
  - **Numbering Patterns:** Text matching patterns like "1.", "1.1.", etc., are considered as headings.
  - **Capitalization:** All-uppercase text is considered for heading status.
- **Classification Logic:**
  - **H1:** Font size ≥ 18 and bold.
  - **H2:** Font size ≥ 15 and (bold or all-uppercase).
  - **H3:** Font size ≥ 11 or matches numbering pattern.

### 4. Multilingual Support
- **Library Used:** [langdetect](https://pypi.org/project/langdetect/)
- **How:** For each heading and the title, language detection is performed. This supports documents in various languages, including Japanese and other non-Latin scripts.
- **Fallback:** If language detection fails or is ambiguous, English is set as the default.

### 5. Output Formatting
- The extracted outline is structured as a list of dictionaries, each containing:
  - `level`: Heading level (H1, H2, H3)
  - `text`: The heading text
  - `page`: Page number where the heading appears
- The output is saved as a JSON file in the `/app/output` directory, matching the input PDF filename.

### 6. Dockerization
- The solution is containerized using a lightweight Python base image (`python:3.12-slim`), ensuring compatibility with AMD64 architecture and offline execution.
- All dependencies are installed within the container, and no internet access is required at runtime.

---

## Why This Approach?
- **Accuracy:** Combines multiple features (font size, boldness, numbering) for robust heading detection.
- **Performance:** Efficient parsing and processing, suitable for large PDFs (up to 50 pages) within the time constraints.
- **Generality:** Works across a wide range of document types and languages without hardcoded rules.
- **Extensibility:** Modular code structure allows for easy adaptation in future hackathon rounds.

---

## Libraries & Tools
- **PyMuPDF:** PDF parsing and text extraction
- **langdetect:** Multilingual language detection
- **Python 3.12:** Core runtime
- **Docker:** Containerization for reproducibility and portability

---

## Limitations & Future Improvements
- **Heading Detection:** Could be further improved by considering indentation, font family, or layout cues.
- **OCR:** Currently does not support scanned/image-based PDFs (no OCR).
- **Language Detection:** Short headings or names may be misclassified; fallback logic is used.

---

*This approach ensures a robust, scalable, and hackathon-compliant solution for PDF