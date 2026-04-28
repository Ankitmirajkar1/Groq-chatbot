from groq import Groq

import config

client = Groq(api_key=config.GROQ_API_KEY)

SYSTEM_PROMPT = """ You are a helpful assistant that provides concise and accurate answers to user queries ONLY ON FINANCES. 
    Always respond in a clear and informative manner, and avoid unnecessary details.
    Rules:
    1. Explain the concept with an example
    2. If there are formulaes then mention those as well
    3. If the user asks for advice, provide it based on sound financial principles.
    4. If anything else apart from finances is asked, reply I dont know
    """

def build_messages(user_input, chat_history):

    messsages = []

    ## System role
    messsages.append({"role": "system", "content": SYSTEM_PROMPT})

    ## Previous conversation history
    for msg in chat_history:
        messsages.append(msg)
    
    ## Current user input
    messsages.append({"role": "user", "content": user_input})

    return messsages


def get_chat_response(user_input, chat_history):

    messages = build_messages(user_input, chat_history)

    response = client.chat.completions.create(
        model=config.MODEL,
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content
