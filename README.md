# 🩺 MedVision AI: Pharmacological Identification Agent

MedVision AI is an end-to-end application designed to safely identify and analyze medical packaging using Generative AI. By utilizing the Gemini 2.5 Flash vision model, the system extracts critical pharmacological data (brand names, active ingredients, usage, and side effects) directly from images of medication boxes or blister packs.

**Crucially, this application implements strict medical guardrails.** The AI is instructed to refuse analysis if the image is unreadable or if it depicts a loose pill without packaging, prioritizing patient safety over hallucinated answers.

## 🚀 Features
*   **Multimodal AI Integration:** Uses the `google-genai` SDK to process images alongside complex pharmacological prompts.
*   **Safety Guardrails:** Strict prompt engineering prevents the AI from guessing or diagnosing based on insufficient visual evidence.
*   **Dual Interface Deployment:**
    *   **Backend API:** A robust REST API built with **FastAPI**, ready for integration into mobile apps or hospital systems.
    *   **Frontend UI:** An interactive web interface built with **Streamlit**, featuring direct camera capture capabilities.

## 🛠️ Tech Stack
*   **Language:** Python 3.11+
*   **AI Model:** Google Gemini 2.5 Flash
*   **Backend Server:** FastAPI, Uvicorn
*   **Frontend Web App:** Streamlit
*   **Image Processing:** Pillow (PIL)

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/MedVision-AI.git](https://github.com/YOUR_USERNAME/MedVision-AI.git)
cd MedVision-AI
