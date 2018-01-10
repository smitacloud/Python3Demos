#send text msg using python external package
#download twilio - Refer : 06examples_text_msg.txt
#check out ---- https://www.twilio.com/docs/libraries/python
#copy the code from - https://www.twilio.com/docs/quickstart/python/sms/sending-via-rest#send-sms-via-library
# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
#from twilio.rest import Client
from twilio import rest

# Find these values at https://twilio.com/user/account
#or create a new account at https://www.twilio.com/try-twilio?g=%2Fconsole&t=9cbd31d04513d0805f0a5ca84a516c9aa6948404067a42c755ccee381f63a89b
account_sid = "AC4369f6db3d54677b898adaeb8aaf360a"
auth_token = "e6a9064b0c23e261b778241ef0c6ce98"

#client = Client(account_sid, auth_token)
client = rest.Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+919821668193",#Replace with your phone number
    from_="+16464900316",#Replace with your Twilio number-get your first phone number
    body="Hello there! My name is SMita B Kumar.")

'''Note: If you run this programm
following error will occur as we need to purchase a Twilio number to send sms

mUnable to create record: The number +919821668193 is unverified. Trial accounts cannot send messages to unverified numbers; verify +919821668193 at twilio.com/user/account/phone-numbers/verified, or purchase a Twilio number to send messages to unverified numbers.[0m

'''
