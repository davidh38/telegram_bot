# telegram bot
import requests
import json

TOKEN = "1328791617:AAHe8g9dP4POxSP4dB_f5_feocXNxeEAJJc"

# send message
# def sendMessage(token, message):
#     resp = requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id=421367814&text=test message")
#     pass


def exclude_spam(message):
    if "bitcoin" in message or "crypto" in message:
        return True
    else:
        return False


def get_updates(token):
    resp = requests.get(f"https://api.telegram.org/bot{token}/getUpdates")
    if resp.ok is True:
        return resp.text


def analyse_spam(token, updates):
    updates_result_json = json.loads(updates)["result"]
    ids = [(x["message"]["message_id"], x["message"]["chat"]["id"]) for x in updates_result_json
           if x["message"].get("text") and exclude_spam(x["message"]["text"])]
    return ids


def delete_messages(token, messages):
    deleted_messages = []
    for id, chat_id in messages:
        resp = requests.get(f"https://api.telegram.org/bot{token}/deleteMessage?chat_id={chat_id}&message_id={id}")
        deleted_messages.append(resp.ok)
    return deleted_messages


if __name__ == "__main__":
    updates = get_updates(TOKEN)
    messages_to_delete = analyse_spam(TOKEN, updates)
    deleted_messages = delete_messages(TOKEN, messages_to_delete)
    print(deleted_messages)
