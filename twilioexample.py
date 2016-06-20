from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC60769aa2912932cb794865e0f9a9bb04"
auth_token  = "a646f0b94d2afb003424a7b5ef89e89d"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="Hi, Hello, hi hello",
    to="+15628880350",    # Replace with your phone number
    from_="+13234751819") # Replace with your Twilio number
print message.sid
