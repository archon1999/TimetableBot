from backend.models import Template


class Messages():
    TIMETABLE = Template.messages.get(id=1).gettext()
    LESSON_INFO = Template.messages.get(id=2).gettext()
    WEEK_PARITY_EVEN = Template.messages.get(id=3).gettext()
    WEEK_PARITY_ODD = Template.messages.get(id=4).gettext()
    REMOTELY = Template.messages.get(id=7).gettext()


class Keys():
    KEY = Template.keys.get(id=5).gettext()


class Smiles():
    SMILE = Template.smiles.get(id=6).gettext()
