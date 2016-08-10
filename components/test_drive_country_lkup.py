# -*- coding: utf-8 -*-
import requests
from meya import Component


class HelloWorld(Component):

    def start(self):
        url = 'http://slz.io/mb-bot/api/cntrylookup'
        data = {
            'ctr_name': self.db.flow.get('test_drive_country'),
            'ctr_alias': self.db.flow.get('test_drive_country')
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
        action = "next"
        print response_json
        if response_json.has_key('message'):
            action = "notspecified"
        else:
            self.db.flow.set('test_drive_gdid', response_json['test_drive_gdid'])
            self.db.flow.set('test_drive_country', response_json['test_drive_country'])

        return self.respond(message=None, action=action)
        
        
        