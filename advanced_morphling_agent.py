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

    print("\n--- Instruction Optimization Tool ---") # Log: Start of Instruction Optimization
    print(f"Topic for Instruction Optimization: {question_topic}") # Log: Topic for which instructions are being optimized
    print(f"Prompt sent to LLM for system message generation:\n{prompt}") # Log: Prompt for system message generation

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_completion_tokens=150,
    )
    system_message_content = response.choices[0].message.content.strip()
    print(f"Generated System Message Content:\n{system_message_content}") # Log: Generated System Message

    return system_message_content


# --- Real Context Building Tool using DuckDuckGo Search ---
def context_building_tool(question_topic, user_question):
    if question_topic == "general":
        search_query = f"information about {question_topic}"
    else:
        search_query = f"{user_question} {question_topic}"

    print("\n--- Context Building Tool ---") # Log: Start of Context Building
    print(f"Topic for Context Building: {question_topic}") # Log: Topic for context building
    print(f"Search Query sent to DuckDuckGo: {search_query}") # Log: Search Query

    search_results = search.run(search_query)
    if search_results:
        context = search_results
        # Log: Beginning of retrieved context (first 200 characters, for example)
        print(f"Retrieved Context (first 200 chars):\n{context[:200]} ... (truncated)")
        return context
    else:
        print("No relevant information found online.") # Log: No context found
        return "No relevant information found online for this topic."

# --- Question Analysis Tool (AI-Powered, using gpt-4o-mini as requested!) ---
def llm_question_analysis_tool(question):
    prompt = f"""Determine the most relevant expert topic or domain of knowledge required to answer the user's question effectively.

    Consider the question and identify the area of expertise that an ideal expert would possess to provide a comprehensive and accurate answer.  Think about fields of study, professions, or general areas of knowledge.

    The question is: "{question}"

    Respond with a concise, single-word or short phrase that represents the most appropriate expert topic. If the question is very general or doesn't fit into a specific expert domain, you can respond with 'general'."
    """

    print("\n--- Question Analysis Tool ---") # Log: Start of Question Analysis
    print(f"User Question: {question}") # Log: User Question being analyzed
    print(f"Prompt sent to LLM for topic inference:\n{prompt}") # Log: Prompt for topic inference

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        # max_completion_tokens=30
    )
    inferred_topic = response.choices[0].message.content.strip().lower()
    print(f"Inferred Topic (from LLM): {inferred_topic}") # Log: Inferred Topic

    return inferred_topic

def ask_question(topic, context, question):
    system_message_content = instruction_optimization_tool(topic)

    messages = [
        {"role": "system", "content": system_message_content},
        {"role": "user", "content": f"Context: {context}\nQuestion: {question}"}
    ]

    print("\n--- Main Agent Call ---") # Log: Start of Main Agent Call
    print(f"System Message:\n{messages[0]['content']}") # Log: System Message being used
    print(f"User Message (with Context):\n{messages[1]['content']}") # Log: User Message with Context

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        # max_completion_tokens=150,
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