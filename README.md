# 📄 PDF Outline Extraction System
## 🏆 Adobe India Hackathon Challenge - "Connecting the Dots"

## 🎯 Overview
A smart solution for **Round 1A** of the Adobe India Hackathon that automatically extracts structured outlines from PDF documents! 📚 

✨ **What it does**: Converts messy PDF documents into clean, hierarchical outlines with headings (H1, H2, H3) and their page numbers in beautiful JSON format.

## 🚀 Key Features
- 📖 **Processes PDFs** up to 50 pages quickly
- 🏷️ **Extracts document titles** and heading hierarchy (H1, H2, H3) with page numbers
- 📊 **Outputs structured JSON** with page references in the required format
- ⚡ **Lightning fast** processing (≤10 seconds for 50 pages)
- 🔌 **Works offline** - no internet needed, no GPU required
- 🌍 **Multilingual support** (including Japanese 🇯🇵 and other non-Latin scripts)
- 🐳 **Dockerized** for easy deployment on AMD64 (x86_64) CPUs

## 📥 Input & 📤 Output

### 📥 **Input** 
PDF files placed in `/app/input` directory

### 📤 **Output** 
Clean JSON files in `/app/output` with this structure:
```json
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "Chapter 1: Introduction", "page": 1 },
    { "level": "H2", "text": "Overview", "page": 1 },
    { "level": "H3", "text": "Historical Background", "page": 2 }
  ]
}
```

## 🏃♂️ Quick Start Guide

### 🔨 Build the Container
```bash
docker build --platform linux/amd64 -t pdf-outline-extractor:latest .
```

### 🎯 Run the Extraction
```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-outline-extractor:latest
```

## 🧠 Smart Algorithm

### 📋 **Title Extraction**
🎯 Finds the largest font text on the first page as the document title

### 🏷️ **Heading Classification** 
Uses intelligent multi-factor detection:
- **H1**: ≥18pt **AND** bold 💪
- **H2**: ≥15pt **AND** (bold **OR** UPPERCASE) 📢
- **H3**: ≥11pt **OR** numbered patterns (e.g., "1.", "2.1.") 🔢

### 🌍 **Multilingual Detection**
Uses `langdetect` to support documents in various languages, including Japanese native script! 🇯🇵

### 🧹 **Smart Filtering**
Automatically removes duplicates and very short text for cleaner results

## ✅ Technical Requirements (All Met!)

| Requirement | Status |
|-------------|--------|
| 🖥️ AMD64 architecture compatible | ✅ |
| 🚫 CPU-only (no GPU needed) | ✅ |
| ⚡ ≤10 seconds for 50-page PDFs | ✅ |
| 🔌 No internet required | ✅ |
| 📦 Model size ≤200MB | ✅ |
| 🪶 Lightweight solution | ✅ |

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| 🔧 **PyMuPDF (fitz)** | PDF processing powerhouse |
| 🌍 **langdetect** | Multilingual language detection |
| 🐍 **Python 3.12** | Runtime environment |
| 📚 **Standard libraries** | os, json, re |

## 📁 Project Structure
```
📦 pdf-outline-extractor/
├── 🐍 main.py          # Core extraction magic ✨
├── 🐳 Dockerfile       # Container setup
├── 📥 input/           # Your PDF files go here
├── 📤 output/          # Generated JSON files
└── 📖 README.md        # This documentation
```

## 🧪 Sample Test Results

✅ **Successfully tested on:**
- 📚 **Academic reports** with formal structure
- 🏛️ **Government forms** with simple layouts  
- 🔬 **Technical documents** with multiple heading levels
- 🌍 **Multilingual documents** (Japanese 🇯🇵, French 🇫🇷, Hindi 🇮🇳, etc.)

## 🎖️ Challenge Compliance

| Criteria | Implementation |
|----------|----------------|
| ⚡ **Performance** | Fast, lightweight processing |
| 🎯 **Accuracy** | Multi-factor heading detection (font size, boldness, numbering) |
| 📋 **Format** | Perfect JSON structure as specified |
| 🔄 **Generalization** | Works across document types and languages |
| 🚫 **No hardcoding** | No file-specific logic or web/API calls |
| 🔌 **Offline ready** | All dependencies included, zero internet needed |

## 🏆 Built with ❤️ for Adobe India Hackathon 2025 - Round 1A

*Ready to connect the dots in your PDF documents! 🎯✨*