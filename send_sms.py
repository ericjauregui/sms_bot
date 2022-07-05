def send_letters(client, target: str, message: str, sender: str) -> str:
    for i, m in enumerate(message):
        if m == ' ':
            txt = client.messages.create(body=m + message[i + 1:],
                                         from_=sender,
                                         to=target)
            return txt.sid
        else:
            txt = client.messages.create(body=m, from_=sender, to=target)
            return txt.sid


def send_sms(client, target: str, message: str, sender: str) -> str:
    txt = client.messages.create(body=message, from_=sender, to=target)
    return txt.sid