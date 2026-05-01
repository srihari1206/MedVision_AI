import os
from PIL import Image
import google.generativeai as genai #Old model 

os.environ["GOOGLE_API_KEY"]="AIzaSyBV2KXNAdOpj5qD4H3-w4ZcC2BlINudIoM"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model=genai.GenerativeModel("gemini-2.5-flash")

print("Loading medicine image...")
try:
    med_image = Image.open(r"C:\Users\Srihari\Downloads\MON1182_1.webp")
except FileNotFoundError:
    print("Error: Could not find 'medicine.jpg'. Please put an image in the folder.")
    exit()

# 4. THE MEDICAL GUARDRAIL PROMPT
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

# 5. EXECUTE THE VISION REQUEST
print("Analyzing image... (This acts as your camera capture)\n")
response = model.generate_content([prompt, med_image])

print("--- DIAGNOSIS REPORT ---")
print(response.text)