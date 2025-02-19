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
        model="gpt-4o-mini", # Using gpt-3.5-turbo for system message generation - you CAN change to "gpt-4o-mini" here too!
        messages=[{"role": "user", "content": prompt}],
        max_completion_tokens=150,
    )
    system_message_content = response.choices[0].message.content.strip()
    return system_message_content

# --- Real Context Building Tool using DuckDuckGo Search ---
def context_building_tool(question_topic, user_question): # Now takes user_question as input too!
    if question_topic == "general":
        search_query = f"information about {question_topic}" # General search for general topics
    else:
        search_query = f"{user_question} {question_topic}" # More specific search for non-general topics! Combine question and topic!

    search_results = search.run(search_query) # Use the *modified* search query
    if search_results:
        context = search_results
        return context
    else:
        return "No relevant information found online for this topic."

# --- Question Analysis Tool (AI-Powered, using gpt-4o-mini as requested!) ---
def llm_question_analysis_tool(question):
    prompt = f"""Determine the BEST expert topic to answer the following question.  Choose ONE topic from this list: history, movies, recipes, quantum physics, wordplay, OR general.  The question is: "{question}"  Respond with just the SINGLE WORD topic name, nothing else."""

    response = openai.chat.completions.create(
        model="gpt-4o-mini", # Using gpt-4o-mini for topic inference as requested!
        messages=[{"role": "user", "content": prompt}],
        max_completion_tokens=20 #  Short response - just the topic word
    )
    inferred_topic = response.choices[0].message.content.strip().lower() # Extract and clean topic response
    return inferred_topic

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
    question = input("Enter your question: ") # Just ask for the question

    topic = llm_question_analysis_tool(question) # USE THE LLM QUESTION ANALYZER!
    print(f"Inferred topic from question (using LLM): {topic}")

    context = context_building_tool(topic, question) # Pass both topic AND question to context_building_tool!  <--- IMPORTANT CHANGE HERE!
    print("\nContext loaded for topic:", topic)
    # print("Context:\n", context)

    answer = ask_question(topic, context, question)

    if answer:
        print("\nAnswer (as a", topic, "expert):\n", answer)