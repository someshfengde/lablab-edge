import os
from dotenv import load_dotenv

from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from openai.types.chat import ChatCompletion

load_dotenv()

ARIA_API_KEY = os.getenv('ALLEGRO_API_KEY')
base_url = 'https://api.rhymes.ai/v1'

client: ChatOpenAI = ChatOpenAI(
        model="aria",
        api_key=ARIA_API_KEY,
        base_url=base_url,
        streaming=False,
    )

def emotion_therapy(memory: str) -> str:
    """
    Recieves a memory from user, which is processed by AI and provide emotional therapy to the user
    
    Arguments:
        memory (str): The memory from the user
        
    Return:
        ai_response (str): A emotional therapy response to the user from AI
    
    """

    response = client.invoke([
        SystemMessage(content="""You are an empathetic AI therapist designed to help users process and heal from emotional memories. You will be provide a memory {memory} and your goal is to provide compassionate support, validate the  user's feelings, and offer therapeutic insights based on the emotions conveyed. First, identify the core emotion (e.g., sadness, anger, joy), then reflect back with empathy, validating the user’s experience. Provide tailored therapeutic advice, such as cognitive reframing, mindfulness, self-compassion, or closure techniques, to help the user emotionally heal. Encourage positive actions and self-care, while maintaining a respectful, non-judgmental, and sensitive approach to foster growth and resilience, always ensuring the user feels safe and understood."""),
        HumanMessage(content=memory)
    ])
    
    ai_response: AIMessage = response.content
    return ai_response