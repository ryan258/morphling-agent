import openai
import os
from dotenv import load_dotenv
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize DuckDuckGo Search API Wrapper globally
search = DuckDuckGoSearchAPIWrapper()

# --- Instruction Optimization Tool (AI-Powered) ---
def instruction_optimization_tool(question_topic):
    prompt = f"""You are an AI system message generator. Your task is to create effective system messages for an AI assistant.

    The AI assistant will be acting as an expert on a given topic, and it will answer user questions based on context information that it retrieves from the internet.

    Your goal is to create a system message that clearly defines the AI assistant's role as an expert in the specified topic. The system message should instruct the AI to:

    1. Act as a knowledgeable and authoritative expert on the topic.
    2. Answer questions factually and accurately, based on the context provided to it.
    3. Adopt a helpful, informative, and engaging tone, appropriate for an expert in the field.

    The topic for which you need to generate a system message is: {question_topic}

    Generate a concise and effective system message, ready to be used in the 'system' role of a chat completion API call. Just provide the system message content itself, not any extra preamble or explanation.
    """

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_completion_tokens=150,
    )
    system_message_content = response.choices[0].message.content.strip()
    return system_message_content

# --- Real Context Building Tool using DuckDuckGo Search ---
def context_building_tool(question_topic):
    search_results = search.run(f"information about {question_topic}")
    if search_results:
        context = search_results
        return context
    else:
        return "No relevant information found online for this topic."

# --- Question Analysis Tool (Keyword-Based) ---
topic_keywords = {
    "history": ["history", "when", "era", "century", "revolution", "past", "ancient", "historical"],
    "movies": ["movie", "film", "director", "actor", "plot", "genre", "cinema", "films"],
    "recipes": ["recipe", "cook", "bake", "ingredients", "dish", "food", "eat", "cuisine"],
    "quantum physics": ["quantum", "physics", "entanglement", "particle", "atom", "qubit", "quantum mechanics"]
    # Add more topics and keywords here!
}

def question_analysis_tool(question):
    question_lower = question.lower()
    for topic, keywords in topic_keywords.items():
        for keyword in keywords:
            if keyword in question_lower:
                return topic
    return "general" # Default topic if no keywords are found

def ask_question(topic, context, question):
    system_message_content = instruction_optimization_tool(topic)

    messages = [
        {"role": "system", "content": system_message_content},
        {"role": "user", "content": f"Context: {context}\nQuestion: {question}"}
    ]

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_completion_tokens=150,
    )
    answer = response.choices[0].message.content.strip()
    return answer

if __name__ == "__main__":
    question = input("Enter your question: ") # Just ask for the question now!
    topic = question_analysis_tool(question) # Infer topic from question
    print(f"Inferred topic from question: {topic}") # Inform user about inferred topic
    context = context_building_tool(topic) # Build context based on inferred topic

    print("\nContext loaded for topic:", topic)
    # print("Context:\n", context) # Uncomment to see context

    answer = ask_question(topic, context, question)

    if answer:
        print("\nAnswer (as a", topic, "expert):\n", answer)