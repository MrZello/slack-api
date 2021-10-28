import requests

def postSlack():
        access_tok = 'xoxp-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        channel_id = 'CU6AY8N3F'
        msg = 'Hello, this message came from a python script!'
        
        send = f'https://api.slack.com/api/chat.postMessage?token={access_tok}&channel={channel_id}&text={msg}'
        requests.get(send)

postSlack()
