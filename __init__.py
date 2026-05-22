import requests

try:
    from .__version__ import *
    from . import __version__ as _vv
except ImportError:
    from __version__ import *
    import __version__ as _vv

history = []
BASE_URL = "https://text.pollinations.ai"


def ask(user_query="hello", model="openai", cache=False, url=BASE_URL):
    """
    sends a query to the pollinations.ai API, stores it in history and returns the reply
    :param user_query:
    :param model:
    :param cache:
    :param url:
    :return:
    """
    global history

    history.append({"role": "user", "content": user_query})

    payload = {
        "messages": history,
        "model": model,
        "cache": cache
    }

    try:
        r = requests.post(url, json=payload, timeout=9999)

        if r.status_code == 200:
            reply = r.text
            history.append({"role": "assistant", "content": reply})
            return reply

        return f"Error {r.status_code}: {r.text}"
    except requests.exceptions.InvalidSchema:
        return f'Message not sent. Try turning off your vpn.'


def reset_history():
    global history
    history.clear()


def get_history():
    """
    Returns history list
    """
    return history


def set_history(new_history: list):
    """
    fully edits the history
    """
    global history
    history = new_history


if __name__ == '__main__':
    for i in _vv.__all__:
        print(i + ':', getattr(_vv, i))