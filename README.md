# PDF Outline Extraction System
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

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/71583922/ada3bc55-b888-4ff5-ba04-26f79ba45fe1/sample_test_ai.json
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/71583922/6808ca14-a355-4c29-a867-452192e1a63a/file01.json
[3] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/71583922/4cb0efa2-a5a9-4422-b9c1-e6791a6f6a18/Community-Connect-Report-Shashwat_Sharma.json
[4] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/71583922/e1288742-11da-4432-a497-367e9176de04/6874ef2e50a4a_adobe_india_hackathon_challenge_doc.json
[5] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/71583922/94f73948-a6d2-4b15-a793-4b6f6d5240e7/main.py
[6] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/71583922/bdad8271-8721-410e-aa90-1fdc9358986c/file01.pdf
[7] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/71583922/099e73b6-9c9f-4d0d-8640-90104e36633c/Dockerfile
