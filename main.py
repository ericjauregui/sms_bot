from twilio.rest import Client
from secret_keys import credentials
import send_sms

ACCT_SID = credentials.get('account_sid')
AUTH_TOKEN = credentials.get('auth_token')
CLIENT = Client(ACCT_SID, AUTH_TOKEN)

TEXT = ''
SENDER = credentials['twilio_us'][0]

TARGETS = []
print(f'sending {TEXT} from {SENDER} to: {TARGETS}')