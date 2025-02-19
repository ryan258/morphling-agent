import openai
import os
from dotenv import load_dotenv
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper


# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize DuckDuckGo Search API Wrapper globally
search = DuckDuckGoSearchAPIWrapper()

# --- Simulated Instruction Optimization Tool (for now) ---
system_instruction_templates = {
    "history": "You are a knowledgeable and enthusiastic historian specializing in the Industrial Revolutions. You answer questions factually based on online information, and you speak with the confident and engaging tone of a history expert.",
    "movies":  "You are a seasoned movie critic, providing insightful reviews and recommendations based on online movie information.",
    "recipes": "You are a master chef, expert in culinary arts and recipe creation. You provide helpful and detailed cooking advice based on online recipes and culinary knowledge.",
    # Add more topics and system messages here!
}

def instruction_optimization_tool(question_topic):
    topic_keyword = question_topic.lower()
    system_instruction = system_instruction_templates.get(topic_keyword, "You are a helpful assistant that answers questions based on online information.")
    return system_instruction

# --- Real Context Building Tool using DuckDuckGo Search ---
def context_building_tool(question_topic):
    search_results = search.run(f"information about {question_topic}") # Perform DuckDuckGo search
    if search_results:
        context = search_results # Use search results as context
        return context
    else:
        return "No relevant information found online for this topic." # Handle no results

def ask_question(topic, context, question):
    system_message_content = instruction_optimization_tool(topic) # Get dynamic system message

    messages = [
        {"role": "system", "content": system_message_content},
        {"role": "user", "content": f"Context: {context}\nQuestion: {question}"}
    ]

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        # max_completion_tokens=150,
    )
    answer = response.choices[0].message.content.strip()
    return answer

if __name__ == "__main__":
    topic = input("Enter the topic you want the agent to become an expert in: ") # Get topic input
    context = context_building_tool(topic) # Build context using real search tool

    print("\nContext loaded for topic:", topic) # Inform user context is loaded (from web!)
    # print("Context:\n", context) # Uncomment to see the full context (can be long!)

    question = input(f"Enter your {topic} question: ") # More topic-specific question prompt

    answer = ask_question(topic, context, question) # Pass topic, context, question to ask_question

    if answer:
        print("\nAnswer (as a", topic, "expert):\n", answer)