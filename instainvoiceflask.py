from flask import Flask, request, redirect
#from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse



app = Flask(__name__)

@app.route("/sms", methods=['POST'])

def sms():
    global number, message_body
    number = request.form['From']
    message_body = request.form['Body']
    #print('%s said %s' % (number,message_body))
    resp = MessagingResponse()
    resp.message('Hello %s, you said: %s' % (number,message_body))
    return str(resp)

"""
def sms_reply():
    #Respond to incoming calls with a simple text message.
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)
"""

if __name__ == "__main__":
    app.run(debug=True)