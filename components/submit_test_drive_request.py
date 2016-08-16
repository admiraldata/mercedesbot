# -*- coding: utf-8 -*-
import requests
from meya import Component


class HelloWorld(Component):

    def start(self):
        car_label = str(self.db.flow.get('test_drive_car_name'))
        phone_str = str(self.db.flow.get('test_drive_contact'))
        url = 'http://slz.io/mb-bot/api/testdrives'#'https://requestb.in/xym3x5xy'
        print self.db.flow.get('test_drive_name')
        data = {
            'facebook_msg_id': self.db.user.user_id,
            'first_name': self.db.user.get('first_name'),
            'last_name': self.db.user.get('last_name'),
            'locale': self.db.user.get('locale'),
            'timezone': self.db.user.get('timezone'),
            'gender': self.db.user.get('gender'),
            'test_drive_name': self.db.user.get('test_drive_name'),
            'test_drive_email': self.db.flow.get('test_drive_email'),
            'test_drive_gdid': self.db.flow.get('test_drive_gdid'),
            'test_drive_car_name': self.db.user.get('test_drive_car_name'),
            'test_drive_purchase': self.db.flow.get('test_drive_purchase'),
            'test_drive_datetime': self.db.flow.get('test_drive_datetime'),
            'test_drive_contact': self.db.flow.get('test_drive_contact')
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
        text='Thank you, we have received your booking request and we will contact you shortly.'
        message = self.create_message(text=text)

        return self.respond(message=message, action="next")
