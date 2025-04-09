from fastapi import APIRouter, Depends, HTTPException
from app.services.chat import ChatService
from typing import Dict
import os

router = APIRouter(prefix="/api/chat", tags=["Chat"])

@router.post("/interpret")
async def interpret_chart(
    chart_data: Dict,
    question: str,
    chat_service: ChatService = Depends()
):
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(
            status_code=400,
            detail="OpenAI API key not configured"
        )
    try:
        return await chat_service.get_interpretation(chart_data, question)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Chat interpretation failed: {str(e)}"
        )

@router.post("/remedies")
async def get_remedies(
    chart_data: Dict,
    problem: str,
    chat_service: ChatService = Depends()
):
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(
            status_code=400,
            detail="OpenAI API key not configured"
        )
    try:
        return await chat_service.get_remedies(chart_data, problem)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Remedy suggestion failed: {str(e)}"
        )
