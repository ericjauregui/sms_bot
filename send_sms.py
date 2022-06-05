from twilio.rest import Client
from secret_keys import credentials

ACCT_SID = credentials.get('account_sid')
AUTH_TOKEN = credentials.get('auth_token')
CLIENT = Client(ACCT_SID, AUTH_TOKEN)

TGTS = credentials['targets']
TEXT = 'MESSAGE'
SENDER = credentials.get('twilio_us')
SINGLE_TGT = -1


def send_letters(target, message, sender):
    for i, m in enumerate(message):
        if m == ' ':
            txt = CLIENT.messages.create(body=m + message[i + 1:],
                                         from_=sender,
                                         to=target)
            print(txt.sid)
        else:
            txt = CLIENT.messages.create(body=m, from_=sender, to=target)
            print(txt.sid)


def send_sms(target, message, sender):
    txt = CLIENT.messages.create(body=message, from_=sender, to=target)
    return txt.sid


for i in range(2):
    print(send_sms(TGTS[SINGLE_TGT], TEXT, SENDER))