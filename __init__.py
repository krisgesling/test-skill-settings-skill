from mycroft import MycroftSkill, intent_handler


class TestSkillSettings(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.gui.register_settings()

    @intent_handler('display.settings.intent')
    def handle_display_settings(self, message):
        self.speak_dialog('on.screen')
        self.gui.show_settings()


def create_skill():
    return TestSkillSettings()

