from collections import defaultdict

# In-memory context, for demo. Replace with Redis/DB in prod.
_user_context = defaultdict(str)


def get_context(user_id: int) -> str:
    return _user_context[user_id]


def update_context(user_id: int, question: str, answer: str):
    # Simple context logic: concatenate previous context (demo only)
    _user_context[user_id] += f"User: {question}\nAI: {answer}\n"
