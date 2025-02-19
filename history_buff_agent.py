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
    context = """The Industrial Revolution, sometimes divided into the First Industrial Revolution and Second Industrial Revolution, was a transitional period of the global economy toward more widespread, efficient and stable manufacturing processes, succeeding the Second Agricultural Revolution. Beginning in Great Britain around 1760, the Industrial Revolution had spread to continental Europe and the United States by about 1840.[1] This transition included going from hand production methods to machines; new chemical manufacturing and iron production processes; the increasing use of water power and steam power; the development of machine tools; and the rise of the mechanised factory system. Output greatly increased, and the result was an unprecedented rise in population and the rate of population growth. The textile industry was the first to use modern production methods,[2]: 40  and textiles became the dominant industry in terms of employment, value of output, and capital invested.
Many of the technological and architectural innovations were of British origin.[3][4] By the mid-18th century, Britain was the world's leading commercial nation,[5] controlling a global trading empire with colonies in North America and the Caribbean. Britain had major military and political hegemony on the Indian subcontinent; particularly with the proto-industrialised Mughal Bengal, which underwent the de-industrialisation of India through the activities of the East India Company.[6][7][8][9] The development of trade and the rise of business were among the major causes of the Industrial Revolution.[2]: 15  Developments in law also facilitated the revolution, such as courts ruling in favour of property rights. An entrepreneurial spirit and consumer revolution helped drive industrialisation in Britain, which after 1800, was emulated in Belgium, the United States, and France.[10]
The Industrial Revolution marked a major turning point in history, comparable only to humanity's adoption of agriculture with respect to material advancement.[11] The Industrial Revolution influenced in some way almost every aspect of daily life. In particular, average income and population began to exhibit unprecedented sustained growth. Some economists have said the most important effect of the Industrial Revolution was that the standard of living for the general population in the Western world began to increase consistently for the first time in history, although others have said that it did not begin to improve meaningfully until the late 19th and 20th centuries.[12][13][14] GDP per capita was broadly stable before the Industrial Revolution and the emergence of the modern capitalist economy,[15] while the Industrial Revolution began an era of per-capita economic growth in capitalist economies.[16] Economic historians agree that the onset of the Industrial Revolution is the most important event in human history since the domestication of animals and plants.[17]
The precise start and end of the Industrial Revolution is still debated among historians, as is the pace of economic and social changes.[18][19][20][21] According to Cambridge historian Leigh Shaw-Taylor, Britain was already industrialising in the 17th century, and "Our database shows that a groundswell of enterprise and productivity transformed the economy in the 17th century, laying the foundations for the world's first industrial economy. Britain was already a nation of makers by the year 1700" and "the history of Britain needs to be rewritten".[22][23] Eric Hobsbawm held that the Industrial Revolution began in Britain in the 1780s and was not fully felt until the 1830s or 1840s,[18] while T. S. Ashton held that it occurred roughly between 1760 and 1830.[19] Rapid adoption of mechanized textiles spinning occurred in Britain in the 1780s,[24] and high rates of growth in steam power and iron production occurred after 1800. Mechanised textile production spread from Great Britain to continental Europe and the United States in the early 19th century, with important centres of textiles, iron and coal emerging in Belgium and the United States and later textiles in France.[2]
An economic recession occurred from the late 1830s to the early 1840s when the adoption of the Industrial Revolution's early innovations, such as mechanised spinning and weaving, slowed as their markets matured; and despite the increasing adoption of locomotives, steamboats and steamships, and hot blast iron smelting. New technologies such as the electrical telegraph, widely introduced in the 1840s and 1850s in the United Kingdom and the United States, were not powerful enough to drive high rates of economic growth.
Rapid economic growth began to reoccur after 1870, springing from a new group of innovations in what has been called the Second Industrial Revolution. These included new steel-making processes, mass production, assembly lines, electrical grid systems, the large-scale manufacture of machine tools, and the use of increasingly advanced machinery in steam-powered factories.[2][25][26][27]"""    
    question = input("Enter your question: ")
    answer = ask_question(context, question)

    if answer:
        print("Answer:", answer)