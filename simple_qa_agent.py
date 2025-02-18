import openai
import os
from dotenv import load_dotenv

# Load API key from.env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_question(context, question):
    # Use the new chat completion API (for openai >= 1.0.0)
    response = openai.chat.completions.create(
        model="gpt-4o-mini",  # Or another suitable model like gpt-4 if you have access, 'o3-mini' might not be a valid OpenAI model
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."}, # Optional system message to set context for the AI
            {"role": "user", "content": f"Context: {context}\nQuestion: {question}"} # User message with context and question
        ],
        temperature=0.7,   # Adjust for creativity
        max_completion_tokens=150,    # Adjust as needed
    )
    # Extract the answer from the response (new way for chat completions)
    answer = response.choices[0].message.content.strip() # Accessing the content from the first choice and message
    return answer

if __name__ == "__main__":
    context = input("Enter the context: ")
    question = input("Enter your question: ")
    answer = ask_question(context, question)

    if answer:
        print("Answer:", answer)