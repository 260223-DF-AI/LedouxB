import dotenv
from google import genai

def translate(language: str, text: str):
    api_key = dotenv.get_key(dotenv.find_dotenv(), "GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    prompt = f"Translate the following text to {language}: "

    input_prompt = f"{prompt} {text}"

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=input_prompt
    )

    output = response.text.strip()
    print(output)


if __name__ == "__main__":
    translate("Spanish", "Buy me a coffee.")