# -*- coding: utf-8 -*-
import requests
from meya import Component


class HelloWorld(Component):

    def start(self):
        url = 'https://slz.io/mb-bot/api/pausebot/' + self.db.user.user_id
        data = {
            'user_id': self.db.user.user_id
        }
        headers = {
        #'authorization': 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZGVudGl0eV9pZCI6MSwiaWRlbnRpdHlfdHlwZSI6IlVzZXIiLCJkYXRlX2NyZWF0ZWQiOiIyMDE2LTAxLTI1IDExOjQ3OjA1WiJ9.7xvbVBwpvZyVWOHdKZ0LDGG4aRpooT6ZN7m-X4YQLto',
        'cache-control' : 'no-cache',
        'content-type' : 'application/x-www-form-urlencoded',
        }
        response = requests.get(
            url=url,
            headers=headers,
            json=data
        )

        return self.respond(message=None, action=None)
