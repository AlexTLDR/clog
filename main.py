import os
import sys
from google import genai
from dotenv import load_dotenv


def main():
    # Check if a prompt was provided as a command line argument
    if len(sys.argv) < 2:
        print("Error: No prompt provided.")
        print("Usage: python main.py \"Your prompt here\"")
        sys.exit(1)
    
    # Get the prompt from command line arguments
    prompt = sys.argv[1]
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=prompt,
    )
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
