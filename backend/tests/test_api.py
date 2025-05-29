import pytest
from httpx import AsyncClient, ASGITransport
from main import app

import api


@pytest.mark.asyncio
async def test_healthcheck():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.get("/")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"


@pytest.mark.asyncio
async def test_ask_endpoint(monkeypatch):
    async def fake_ask_ai(question, context=""):
        return f"Fake answer to: {question}"

    monkeypatch.setattr(api, "ask_ai", fake_ask_ai)

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {"user_id": 123, "message": "Hello, AI"}
        resp = await ac.post("/api/ask", json=payload)
        assert resp.status_code == 200
        assert resp.json()["reply"] == "Fake answer to: Hello, AI"
