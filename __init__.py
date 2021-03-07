from mycroft import MycroftSkill, intent_file_handler


class Skyneela(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skyneela.intent')
    def handle_skyneela(self, message):
        self.speak_dialog('skyneela')


def create_skill():
    return Skyneela()

