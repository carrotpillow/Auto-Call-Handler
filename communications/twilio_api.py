import os
import twilio
import twilio.rest

class TwilioAPI:
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    
    client = twilio.rest.TwilioRestClient(account_sid, auth_token)