import os
import requests
from dotenv import load_dotenv

load_dotenv()

def generate_x_post(topic: str) -> str:
    prompt = f"""
    You are an expert social media manager, and you excel at crafting viral and highly engaging posts for X (formerly Twitter).
    
    Your task is to generate a post that is concise, engaging, and tailored to the topic provided by the user.
    Avoid using hashtags and lots of emojis. Focus on creating content that encourages interaction and shares valuable insights.

    Keep the post short and focused, structure it in a clean, readable format, and ensure it resonates with a broad audience.

    Here's the topic provided by the user for which you need to generate a post:
    <topic>
    {topic}
    </topic>


    """

    # Placeholder for AI (LLM) integration to generate X post
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }   
    response = requests.post("https://api.openai.com/v1/chat/completions", json=payload,
                             headers={ "Content-Type": "application/json",
                                       "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"})
    
    if response.status_code != 200:
        print(f"Error: API returned status code {response.status_code}")
        print(f"Response: {response.text}")
        return "Failed to generate post."
    
    response_json = response.json()
    response_text = response_json.get("choices", [{}])[0].get("message", {}).get("content", "")

    return response_text.strip()

def main():
    print("Hello from ai-agents-workflows!")
    #user input => AI (LLM) to generate X post => output post
    usr_input = input("What should the post be about? ")
    print("Generating X post...")
    generated_post = generate_x_post(usr_input)
    print(generated_post)

if __name__ == "__main__":
    main()
