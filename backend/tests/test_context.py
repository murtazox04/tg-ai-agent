from context import get_context, update_context


def test_context_update_and_get():
    user_id = 999
    assert get_context(user_id) == ""
    update_context(user_id, "Hi?", "Hello!")
    ctx = get_context(user_id)
    assert "User: Hi?" in ctx
    assert "AI: Hello!" in ctx
