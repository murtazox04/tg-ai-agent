import datetime


def log_request(user_id, message, reply):
    now = datetime.datetime.now().isoformat()
    print(f"[{now}] user={user_id} | Q: {message} | A: {reply}")
