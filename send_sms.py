from twilio.rest import Client
from secret_keys import credentials

ACCT_SID = credentials.get('account_sid')
AUTH_TOKEN = credentials.get('auth_token')
CLIENT = Client(ACCT_SID, AUTH_TOKEN)

TGTS = credentials['targets']
TEXT = ''
SENDER = credentials['twilio_us'][0]
SINGLE_TGT = 0

print(f'sending {TEXT} from {SENDER} to {TGTS[SINGLE_TGT]}')


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


# for _ in range(30):
#     print(send_sms(TGTS[SINGLE_TGT], TEXT, SENDER))