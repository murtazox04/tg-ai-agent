import pytest
from ai_agent import ask_ai


@pytest.mark.asyncio
async def test_ask_ai_fake(monkeypatch):
    # Simulate OpenAI error for fallback
    async def fake_openai(*args, **kwargs):
        raise Exception("Simulated error")

    monkeypatch.setattr("ai_agent.client.chat.completions.create", fake_openai)

    result = await ask_ai("Hi?", "Context")
    assert result.startswith("AI error:")
