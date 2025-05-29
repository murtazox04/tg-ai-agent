from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ai_agent import ask_ai
from context import get_context, update_context
from logger import log_request

router = APIRouter()


class AIRequest(BaseModel):
    user_id: int
    message: str


class AIResponse(BaseModel):
    reply: str


@router.post("/ask", response_model=AIResponse)
async def ask_endpoint(request: AIRequest):
    # Context management (optional)
    context = get_context(request.user_id)
    try:
        reply = await ask_ai(request.message, context)
        update_context(request.user_id, request.message, reply)
        log_request(request.user_id, request.message, reply)
        return AIResponse(reply=reply)
    except Exception as e:
        # Log error
        log_request(request.user_id, request.message, f"ERROR: {str(e)}")
        raise HTTPException(status_code=500, detail="AI processing failed")
