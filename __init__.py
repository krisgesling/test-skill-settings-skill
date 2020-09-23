from mycroft import MycroftSkill, intent_file_handler


class TestSkillSettings(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('settings.skill.test.intent')
    def handle_settings_skill_test(self, message):
        self.speak_dialog('settings.skill.test')


def create_skill():
    return TestSkillSettings()

