# 🚀 The Amazing Morphling Agent: Your Question-Driven AI Expert\! 🧠✨

Welcome to the **Morphling Agent** project\! Get ready to witness the magic of a truly dynamic, question-driven AI agent that can become an expert on virtually **ANY** topic you throw at it\!

This project showcases a powerful and flexible AI agent architecture that leverages the latest advancements in Large Language Models (LLMs) and web search to deliver expert-level answers to your questions. Forget static, pre-programmed responses – the Morphling Agent **morphs** into the ideal expert based on the question you ask, dynamically retrieves relevant information from the web, and crafts insightful, knowledgeable answers\!

**🔥 Key Features that Make the Morphling Agent Awesome:**

- **Dynamic Topic Inference:** Ask ANY question\! The agent uses a sophisticated AI-powered **Question Analysis Tool** (powered by `gpt-4o-mini`\!) to intelligently determine the most relevant expert topic or domain of knowledge required to answer your question. No more pre-defined topics - it truly understands your intent\!
- **AI-Powered Instruction Optimization:** For each inferred topic, the agent dynamically generates an **optimized system message** using the **Instruction Optimization Tool** (powered by `gpt-3.5-turbo`). This means the agent truly _becomes_ an expert in that topic, tailoring its persona and response style on the fly\!
- **Real-World Context Building:** The **Context Building Tool** leverages the **DuckDuckGo Search API** to fetch up-to-date and relevant information from the web based on your question and the inferred topic. No more stale, limited datasets – your agent learns in real-time\!
- **Expert-Level Question Answering:** Finally, the agent uses **`gpt-4o-mini`** (or your LLM of choice\!) to generate a comprehensive and expert-sounding answer, drawing upon the dynamically generated system message and the web-retrieved context. Prepare to be impressed\!
- **Modular and Extensible Architecture:** The project is built with a modular design, making it easy to understand, modify, and extend. Want to add more tools? Refine the personas? Integrate different knowledge sources? Go for it\! The Morphling Agent is designed for you to experiment and build upon\!
- **Logging for Deep Insights:** Includes detailed logging throughout the agent's process, allowing you to peek "behind the scenes" and understand exactly how it's thinking, inferring topics, building context, and generating answers. Perfect for debugging, learning, and further development\!

**🛠️ Technologies Used:**

- **Python:** The core programming language.
- **OpenAI API:** Leverages powerful LLMs like `gpt-4o-mini` and `gpt-3.5-turbo` for question analysis, instruction optimization, and question answering.
- **Langchain:** A fantastic framework for building LLM-powered applications.
- **DuckDuckGo Search API (via Langchain):** For real-time web search and context retrieval.
- **dotenv:** For secure API key management.
- **(Optional) uv:** For faster Python package installation (recommended\!).

**🚀 Get Started - Unleash the Morphling Agent in 3 Easy Steps\!**

1.  **Clone the Repository (or just grab `advanced_morphling_agent.py`):**

    If you're viewing this on GitHub, you're already there\! You can clone the repository to your local machine. If you just have the `advanced_morphling_agent.py` file, that's fine too\!

2.  **Set up your Virtual Environment and Install Dependencies:**

    It's highly recommended to use a virtual environment to keep your project dependencies isolated. You can use either `venv` (standard Python) or `uv` (much faster\!).

    **Using `venv` (standard Python):**

    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    source venv/bin/activate # On macOS/Linux
    pip install -r requirements.txt
    ```

    **Using `uv` (faster - recommended\!):**

    First, make sure you have `uv` installed. If not, follow the installation instructions here: [https://astral.sh/uv](https://www.google.com/url?sa=E&source=gmail&q=https://astral.sh/uv)

    Then, create and activate your virtual environment and install dependencies:

    ```bash
    uv venv venv
    .\venv\Scripts\activate  # On Windows
    source venv/bin/activate # On macOS/Linux
    uv pip install -r requirements.txt
    ```

3.  **Configure your OpenAI API Key:**

    - Create a `.env` file in the same directory as `advanced_morphling_agent.py`.

    - Add your OpenAI API key to the `.env` file like this:

      ```
      OPENAI_API_KEY=YOUR_OPENAI_API_KEY_HERE
      ```

    **Replace `YOUR_OPENAI_API_KEY_HERE` with your actual OpenAI API key\!** You can get one from [https://platform.openai.com/account/api-keys](https://www.google.com/url?sa=E&source=gmail&q=https://platform.openai.com/account/api-keys).

**🎉 Run the Morphling Agent and Ask it Anything\!**

That's it for setup\! Now you're ready to unleash the Morphling Agent\!

Run the script from your terminal:

```bash
python advanced_morphling_agent.py
```

The agent will prompt you:

```
Enter your question:
```

**Ask it anything you want\!** Here are some example questions to get you started (try pasting these in\!):

- `What trends are coming back in style?`
- `How did ancient Egypt feel about cats?`
- `What is the meaning of life?`
- `Give me some tips for writing a compelling screenplay`
- `Explain the concept of quantum superposition in simple terms.`

**Example Output (you'll see more detailed logs now too\!):**

```
Enter your question: What trends are coming back in style?

--- Question Analysis Tool ---
User Question: What trends are coming back in style?
Prompt sent to LLM for topic inference:
... (Prompt for topic inference) ...

Inferred Topic (from LLM): fashion trends
Inferred topic from question (using LLM): fashion trends

--- Context Building Tool ---
Topic for Context Building: fashion trends
Search Query sent to DuckDuckGo: What trends are coming back in style? fashion trends
Retrieved Context (first 200 chars):
You May Also Like: How To Get Ideas For Writing - 6 Must-Know Tips. These are all pretty basic ideas for writing a screenplay. While these are undoubtedly important (and we will naturally touch on som ... (truncated)

Context loaded for topic: fashion trends

--- Instruction Optimization Tool ---
Topic for Instruction Optimization: fashion trends
Prompt sent to LLM for system message generation:
... (Prompt for system message generation) ...

Generated System Message Content:
As an AI assistant specializing in fashion trends, I will provide expert answers to your questions ... (truncated system message) ...

--- Main Agent Call ---
System Message:
As an AI assistant specializing in fashion trends, I will provide expert answers to your questions ... (truncated system message) ...
User Message (with Context):
Context: You May Also Like: How To Get Ideas For Writing - 6 Must-Know Tips. ... (truncated context) ... Question: What trends are coming back in style?

Answer (as a fashion trends expert):
... (Detailed fashion trends answer!) ...
```

**🔮 Take it Further - Your Morphling Agent Adventure Continues\!**

This is just the beginning\! Here are some exciting ideas to expand and enhance your Morphling Agent:

- **Persona Perfection:** Dive deeper into prompt engineering to create even more nuanced and engaging expert personas\! Experiment with different tones, styles, and levels of detail in the system messages.
- **Knowledge Expansion:** Integrate more knowledge sources\! Add Wikipedia API, specialized APIs for different domains (movies, recipes, science, etc.), or even your own custom knowledge databases\!
- **Tool Power-Up:** Equip your agent with more tools beyond web search\! Think about tools for calculations, code execution, image search, accessing real-time data, and more\!
- **User Interface Magic:** Deploy your Morphling Agent as a web app or chatbot to share its amazing capabilities with the world\!

**🙌 We can't wait to see what incredible things you build with the Morphling Agent\!** This project is a playground for AI exploration and creativity\! Dive in, experiment, and let your imagination run wild\!

**Contributions Welcome\!** (Optional - If you want to make it open to contribution)

If you'd like to contribute to making the Morphling Agent even more amazing, feel free to submit pull requests with improvements, new features, or bug fixes\!

**License:**

[MIT License](https://www.google.com/url?sa=E&source=gmail&q=LICENSE) (Optional - Add a license file if you want to open source it)

**Happy Morphing!** ✨🚀
