from flask import Flask
from flask import request
from pprint import pprint
import json
import emoji
import requests
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route('/app', methods=['POST']) 

def bot():
  incoming_msg = request.values.get('Body', '').lower()
  resp = MessagingResponse()
  msg = resp.message()
  responded = False
  if ['hey', 'hello', 'sho', 'molo', 'hy'] in incoming_msg:
      # return a quote
      response = emoji.emojize("""
*Hi! I am the Water Bot* :wave:
How can I help :wink:
You can give me the following commands:
:black_small_square: *'water tips'*: Fing out how to be better with water :rocket:
:black_small_square: *'report leakes'*: Help us fix the problem :wrench:
:black_small_square: *'news'*: Latest news in South Africa. :newspaper:
:black_small_square: *'offers'*: Find the best offers :gift_heart:
""", use_aliases=True)

      elif incoming_msg == 'water tips':
          r = requests.get('https://www.fundi.co.za/fundiconnect/10-easy-tips-to-save-water/') # add website link
            
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve water tips at this time, sorry. :cry:'
      msg.body(response)
      responded = True
  if 'cat' in incoming_msg:
      # return a cat pic
      msg.media('https://cataas.com/cat')
      responded = True
  if not responded:
      msg.body('I only know about famous quotes and cats, sorry!')
  return str(resp)



if __name__ == '__main__':
  app.run(debug=False)