from mycroft import MycroftSkill, intent_file_handler


class ComplimentMe(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('me.compliment.intent')
    def handle_me_compliment(self, message):
        self.speak_dialog('me.compliment')


def create_skill():
    return ComplimentMe()

