from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from typing import List, Dict
import os

class ChatService:
    def __init__(self):
        self.llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.7,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        self.system_prompt = """
        You are a Vedic astrology expert assistant. Provide insightful interpretations 
        of astrological charts based on the following principles:
        - Analyze planetary positions in Rashis
        - Consider Nakshatra influences
        - Explain Dasha periods
        - Offer remedies when appropriate
        """

    async def get_interpretation(self, chart_data: Dict, question: str) -> str:
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=f"Chart Data: {chart_data}\nQuestion: {question}")
        ]
        response = await self.llm.agenerate([messages])
        return response.generations[0][0].text

    async def get_remedies(self, chart_data: Dict, problem: str) -> str:
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=f"Chart Data: {chart_data}\nProblem: {problem}\nSuggest Vedic remedies:")
        ]
        response = await self.llm.agenerate([messages])
        return response.generations[0][0].text
