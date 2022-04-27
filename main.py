from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# main


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'wyd' in incoming_msg:
        # return a quote
        msg.body("Heyy not much wbu stranger")
        responded = True
    if 'hang' in incoming_msg:
        msg.body("Your place? my roomies have ppl over")
        responded = True
    if 'come' in incoming_msg:
        msg.body("Philly square right??")
        responded = True
    if '4307':
        msg.body("that's right, see you soon ;)")
        responded = True
    if not responded:
        msg.body(
            'Why dont I just come over we both know thats what this is... Im omw')
    return str(resp)


if __name__ == '__main__':
    app.run()
