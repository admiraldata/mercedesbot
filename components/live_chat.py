# -*- coding: utf-8 -*-
import requests
from meya import Component


class HelloWorld(Component):

    def start(self):
        url = 'https://slz.io/mb-bot/api/livechat'
        data = {
            'first_name': self.db.user.get('first_name'),
            'last_name': self.db.user.get('last_name'),
            'user_id': self.db.user.user_id,
            'locale': self.db.user.get('locale'),
            'timezone': self.db.user.get('timezone'),
            'gender': self.db.user.get('gender')
        }
        headers = {
        #'authorization': 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZGVudGl0eV9pZCI6MSwiaWRlbnRpdHlfdHlwZSI6IlVzZXIiLCJkYXRlX2NyZWF0ZWQiOiIyMDE2LTAxLTI1IDExOjQ3OjA1WiJ9.7xvbVBwpvZyVWOHdKZ0LDGG4aRpooT6ZN7m-X4YQLto',
        'cache-control' : 'no-cache',
        'content-type' : 'application/x-www-form-urlencoded',
        }
        response = requests.post(
            url=url,
            headers=headers,
            json=data
        )
        response_json = response.json()
        print response_json
        if response_json.has_key('message'):
            text=response_json['message']
        message = self.create_message(text=text)
        action = "next"
        return self.respond(message=message, action=action)
