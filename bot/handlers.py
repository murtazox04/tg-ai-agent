from aiogram import types, Router, F
from aiogram.filters import Command
import httpx


from utils import is_allowed
from config import ALLOWED_USERS, BACKEND_URL

router = Router()


@router.message(Command("start"))
async def start_cmd(msg: types.Message):
    if not is_allowed(msg.from_user.id, ALLOWED_USERS):
        await msg.reply("Access denied.")
        return
    await msg.reply("Hello! I am your AI assistant. Ask me anything.")


@router.message(F.text)
async def handle_text(msg: types.Message):
    if not is_allowed(msg.from_user.id, ALLOWED_USERS):
        await msg.reply("Access denied.")
        return

    user_id = msg.from_user.id
    text = msg.text

    await msg.chat.do("typing")

    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            resp = await client.post(
                f"{BACKEND_URL}/api/ask", json={"user_id": user_id, "message": text}
            )
        if resp.status_code == 200:
            ai_reply = resp.json().get("reply", "No answer")
            await msg.reply(ai_reply)
        else:
            await msg.reply(f"AI error: {resp.status_code} {resp.text}")
    except Exception as e:
        await msg.reply(f"Internal error: {e}")
