import openai
import os
from dotenv import load_dotenv
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
import datetime  # Import datetime for timestamping log files

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize DuckDuckGo Search API Wrapper globally
search = DuckDuckGoSearchAPIWrapper()

# --- Setup Logging ---
LOG_DIR = "log"  # Directory to store log files
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def create_log_file():
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    log_filename = os.path.join(LOG_DIR, f"morphling_agent_log_{timestamp}.md")
    return log_filename

current_log_file = create_log_file() # Create log file at script start

def log_markdown(content, level=2): # level for markdown heading level (##, ###, etc.)
    with open(current_log_file, "a", encoding="utf-8") as f: # Append to the log file
        f.write(f"{'#' * level} {content}\n\n")

def log_code_block(code): # For logging code blocks (prompts, context, messages)
    with open(current_log_file, "a", encoding="utf-8") as f:
        f.write("```\n")
        f.write(code)
        f.write("\n```\n\n")


# --- Instruction Optimization Tool (AI-Powered) ---
def instruction_optimization_tool(question_topic):
    prompt = f"""You are an AI system message generator. Your task is to create effective system messages for an AI assistant.

The AI assistant will act as an expert on a given topic and answer user questions based on retrieved context.

Your goal is to create a system message that defines the AI assistant's expert role and instructs it to:

1.  Demonstrate expertise and knowledge in the specified topic.
2.  Answer questions factually and accurately, using retrieved context.
3.  Adopt a tone and style that is *appropriate for an expert in the given topic*, and that is also helpful and engaging for the user.

Consider the topic: {question_topic} and choose an appropriate tone and style for an expert in this field.  For example:

*   For a scientific topic like 'quantum physics', a *formal and precise* tone might be suitable.
*   For a practical topic like 'cake baking', a *friendly and encouraging* tone would be better.
*   For a topic like 'funny riddles', a *lighthearted and playful* tone is ideal.

Generate an effective system message that embodies these qualities.  Provide just the system message content itself, without extra preamble.
    """

    log_markdown("Instruction Optimization Tool", level=2) # Start log section
    log_markdown(f"Topic for Instruction Optimization: {question_topic}", level=3) # Log topic
    log_markdown("Prompt sent to LLM for system message generation:", level=3) # Log prompt
    log_code_block(prompt) # Log prompt as code block

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_completion_tokens=150,
    )
    system_message_content = response.choices[0].message.content.strip()
    log_markdown("Generated System Message Content:", level=3) # Log system message
    log_code_block(system_message_content) # Log system message as code block

    return system_message_content

# --- Real Context Building Tool using DuckDuckGo Search ---
def context_building_tool(question_topic, user_question):
    if question_topic == "general":
        search_query = f"information about {question_topic}"
    else:
        # --- MODIFIED SEARCH QUERY FORMATION (Option 1 - Keywords) ---
        search_query = f"{user_question} {question_topic} explanation guide overview tips"
        # --- END MODIFICATION ---

    log_markdown("Context Building Tool", level=2)
    log_markdown(f"Topic for Context Building: {question_topic}", level=3)
    log_markdown(f"Search Query sent to DuckDuckGo:", level=3)
    log_code_block(search_query)

    search_results = search.run(search_query)
    if search_results:
        context = search_results
        log_markdown("Retrieved Context:", level=3)
        log_code_block(context)
        return context
    else:
        log_markdown("No relevant information found online.", level=3)
        return "No relevant information found online for this topic."

# --- Question Analysis Tool (AI-Powered, using gpt-4o-mini as requested!) ---
def llm_question_analysis_tool(question):
    prompt = f"""Determine the most *specific* relevant expert topic or domain of knowledge that is required to answer the user's question most effectively and with expert depth.

Consider the question carefully and identify the *most narrowly defined area of expertise* that an ideal expert would possess to provide a comprehensive, accurate, and *highly specific* answer.  Think about *subfields* of study, *specialized* professions, or *niche* areas of knowledge.

The question is: "{question}"

Respond with a concise, single-word or short phrase that represents the *most specific* appropriate expert topic.  Ideally, this should be a *sub-domain* of a broader field, if applicable. For example, for 'baking questions,' prefer 'cake baking' over just 'cooking.'

Prefer a specific topic if one is clearly identifiable, unless the question is genuinely very broad or cross-disciplinary. If the question is very general or doesn't fit into a specific expert domain, you can respond with 'general'.
    """

    log_markdown("Question Analysis Tool", level=2) # Start log section
    log_markdown(f"User Question: {question}", level=3) # Log user question
    log_markdown("Prompt sent to LLM for topic inference:", level=3) # Log prompt
    log_code_block(prompt) # Log prompt as code block

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_completion_tokens=30
    )
    inferred_topic = response.choices[0].message.content.strip().lower()
    log_markdown(f"Inferred Topic (from LLM): {inferred_topic}", level=3) # Log inferred topic
    return inferred_topic

def ask_question(topic, context, question):
    system_message_content = instruction_optimization_tool(topic)

    messages = [
        {"role": "system", "content": system_message_content},
        {"role": "user", "content": f"Context: {context}\nQuestion: {question}"}
    ]

    log_markdown("Main Agent Call", level=2) # Start log section
    log_markdown("System Message:", level=3) # Log system message
    log_code_block(messages[0]['content']) # Log system message as code block
    log_markdown("User Message (with Context):", level=3) # Log user message
    log_code_block(messages[1]['content']) # Log user message as code block

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_completion_tokens=150,
    )
    answer = response.choices[0].message.content.strip()

    log_markdown("Generated Answer (from Main Agent):", level=3) # Log answer
    log_code_block(answer) # Log answer as code block
    return answer

if __name__ == "__main__":
    question = input("Enter your question: ") # Just ask for the question

    log_markdown(f"Morphling Agent: {question}", level=1) # Top-level log for each run
    # log_markdown(f"User Question: {question}", level=2) # Log user question at top

    topic = llm_question_analysis_tool(question) # USE THE LLM QUESTION ANALYZER!
    print(f"Inferred topic from question (using LLM): **{topic}**") # Keep minimal console output - topic

    context = context_building_tool(topic, question)
    print("\nContext loaded for topic:", topic) # Keep minimal console output - context loaded

    answer = ask_question(topic, context, question)

    if answer:
        print("\nAnswer (as a", topic, "expert):\n", answer) 
        # print("\nAnswer (as a", topic, "expert): \n[See log file for full answer]") # Minimal console answer message

        log_markdown(f"Final Answer (as a {topic} expert):", level=2) # Log final answer in markdown
        log_code_block(answer) # Log final answer as code block

    print(f"\nDetailed logs saved to: {current_log_file}") # Inform user about log file