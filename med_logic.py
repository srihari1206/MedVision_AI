import os
from google import genai 
from PIL import Image

def analyze_medicine(image:Image.Image) -> str:
    """
    Takes a PIL Image of a medicine, runs it through Gemini 2.5 Flash with strict
    medical guardrails, and returns the formatted safety analysis.
    """
    # 1. SETUP API KEY (Ensure your real key is here!)
    # In production, we read this from the environment for security
    api_key=os.environ.get("GOOGLE_API_KEY","AIzaSyBV2KXNAdOpj5qD4H3-w4ZcC2BlINudIoM")
    client=genai.Client(api_key=api_key)
    # 2. THE MEDICAL GUARDRAIL PROMPT
    prompt = """
    You are a highly precise pharmacological AI assistant. 
    Analyze the provided image of a medicine package.

    Task:
    1. Extract the exact brand name and active ingredients written on the package.
    2. Provide a brief, factual summary of what this medicine is typically used for.
    3. List 2 common side effects.

    STRICT RULES:
    - DO NOT guess. If the text is unreadable or the image is just a loose pill without packaging, reply ONLY with: 'WARNING: Cannot safely identify medicine from this image.'
    - Format your response cleanly.
    """
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt, image]

    )
    return response.text