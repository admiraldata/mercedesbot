# -*- coding: utf-8 -*-
import requests
from meya import Component


class HelloWorld(Component):

    def start(self):
        car_label = self.db.flow.get('test_drive_car_name')
        phone_str = str(self.db.flow.get('test_drive_contact'))
        url = 'http://slz.io/mb-bot/api/subscriptions'
        data = {
            'facebook_msg_id': self.db.user.user_id,
            'first_name': self.db.user.get('first_name'),
            'last_name': self.db.user.get('last_name'),
            'locale': self.db.user.get('locale'),
            'timezone': self.db.user.get('timezone'),
            'gender': self.db.user.get('gender'),
            'usr_subscription': self.db.flow.get('usr_subscription')
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


        return self.respond(message=None, action="next")
