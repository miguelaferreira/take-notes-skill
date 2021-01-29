from mycroft import MycroftSkill, intent_file_handler


class TakeNotes(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('notes.take.intent')
    def handle_notes_take(self, message):
        self.speak_dialog('notes.take')


def create_skill():
    return TakeNotes()

