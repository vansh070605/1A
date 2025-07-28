# PDF Outline Extraction System
## Adobe India Hackathon Challenge - "Connecting the Dots"

### Overview
A solution for **Round 1A** of the Adobe India Hackathon that extracts structured outlines from PDF documents, generating hierarchical headings (H1, H2, H3) with page numbers in JSON format.

### Features
- Processes PDFs up to 50 pages
- Extracts document titles and heading hierarchy (H1, H2, H3) with page numbers
- Outputs structured JSON with page references in the required format
- Fast, lightweight processing (≤10 seconds for 50 pages)
- Works offline without GPU dependencies
- Multilingual support (including Japanese and other non-Latin scripts)
- Dockerized for easy deployment on AMD64 (x86_64) CPUs

### Input/Output
**Input**: PDF files in `/app/input`  
**Output**: JSON files in `/app/output` with structure:
```json
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "Chapter 1", "page": 1 },
    { "level": "H2", "text": "Overview", "page": 1 },
    { "level": "H3", "text": "History", "page": 2 }
  ]
}
```

### Quick Start
```bash
# Build
docker build --platform linux/amd64 -t pdf-outline-extractor:latest .

# Run
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-outline-extractor:latest
```

### Algorithm
- **Title Extraction**: Identifies the largest font text on the first page as the document title.
- **Heading Classification**: Uses font size, boldness, and numbering patterns:
  - H1: ≥18pt and bold
  - H2: ≥15pt and (bold or uppercase)
  - H3: ≥11pt or matches numbering pattern (e.g., "1.", "2.1.")
- **Multilingual Detection**: Uses `langdetect` to support documents in various languages, including Japanese (native script).
- **Filtering**: Removes duplicates and very short text.

### Technical Requirements ✅
- AMD64 architecture compatible (linux/amd64)
- CPU-only processing (no GPU)
- Execution time ≤10 seconds for 50-page PDFs
- No internet connectivity required
- Model size ≤200MB (if any)
- Lightweight solution

### Dependencies
- PyMuPDF (fitz) - PDF processing
- langdetect - Multilingual language detection
- Python 3.12 runtime
- Standard libraries (os, json, re)

### Project Structure
```
├── main.py         # Core extraction logic
├── Dockerfile      # Container setup
├── input/          # PDF input directory
├── output/         # JSON output directory
└── README.md       # Documentation
```

### Sample Results
Tested on various document types:
- Academic reports with formal structure
- Government forms with simple layouts
- Technical documents with multiple heading levels
- Multilingual documents (including Japanese, French, Hindi, etc.)

### Challenge Compliance
- **Performance**: Fast, lightweight processing
- **Accuracy**: Multi-factor heading detection (font size, boldness, numbering)
- **Format**: Proper JSON structure as specified in the challenge
- **Generalization**: Works across document types and languages
- **No hardcoding**: No file-specific logic or web/API calls
- **Offline**: All dependencies included, no internet required

---

*Built for Adobe India Hackathon 2025 - Round# PDF Outline Extraction System
## Adobe India Hackathon Challenge - "Connecting the Dots"

### Overview
A solution for **Round 1A** of the Adobe India Hackathon that extracts structured outlines from PDF documents, generating hierarchical headings (H1, H2, H3) with page numbers in JSON format.

### Features
- Processes PDFs up to 50 pages
- Extracts document titles and heading hierarchy
- Outputs structured JSON with page references
- Fast, lightweight processing (≤10 seconds)
- Works offline without GPU dependencies

### Input/Output
**Input**: PDF files in `/app/input`
**Output**: JSON files in `/app/output` with structure:
```json
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "Chapter 1", "page": 1 },
    { "level": "H2", "text": "Overview", "page": 1 }
  ]
}
```

### Quick Start
```bash
# Build
docker build --platform linux/amd64 -t pdf-outline-extractor:latest .

# Run
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-outline-extractor:latest
```

### Algorithm
- **Title Extraction**: Identifies largest font text on first page
- **Heading Classification**: Uses font size, boldness, and numbering patterns
  - H1: ≥18pt + bold
  - H2: ≥15pt + (bold or uppercase)
  - H3: ≥11pt or numbered patterns
- **Filtering**: Removes duplicates and very short text

### Technical Requirements ✅
- AMD64 architecture compatible
- CPU-only processing (no GPU)
- Execution time ≤10 seconds for 50-page PDFs
- No internet connectivity required
- Lightweight solution

### Dependencies
- PyMuPDF (fitz) - PDF processing
- Python 3.12 runtime
- Standard libraries (os, json, re)

### Project Structure
```
├── main.py         # Core extraction logic
├── Dockerfile      # Container setup
├── input/          # PDF input directory
├── output/         # JSON output directory
└── README.md       # Documentation
```

### Sample Results
Tested on various document types:
- Academic reports with formal structure
- Government forms with simple layouts  
- Technical documents with multiple heading levels

### Challenge Compliance
- **Performance**: Fast, lightweight processing
- **Accuracy**: Multi-factor heading detection
- **Format**: Proper JSON structure as specified
- **Generalization**: Works across document types

*Built for Adobe India Hackathon 2025 - Round 1A*
