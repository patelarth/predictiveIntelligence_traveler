from wtforms import *


class ComplainVO:

    complainID = IntegerField
    complainSubject = StringField
    complainDescription = StringField
    complainTo_LoginId = IntegerField
    complainFrom_LoginId = IntegerField
    complainDate = StringField
    complainTime = StringField
    complainStatus = StringField
    replyDescription = StringField
    complainActiveStatus = StringField
