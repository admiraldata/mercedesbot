# -*- coding: utf-8 -*-
from meya import Component


class UserProfileInformation(Component):

    def start(self):
        first_name = self.db.user.get('first_name')
        if first_name is None:
            text = "Hi! You’re through to Mercedes-Benz Middle East."
        else:
            text = "Hello {} you’re through to Mercedes-Benz Middle East. Ready to start?".format(
                first_name
            )
        message = self.create_message(text=text)
        return self.respond(message=message, action="next")
        
# Need to add alternative generic message if firstname is null
        