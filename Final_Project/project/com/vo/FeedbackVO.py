from wtforms import *


class FeedbackVO:

    feedbackId = IntegerField
    feedbackFrom_LoginId = StringField
    feedbackTo_LoginId = StringField
    feedbackRating = StringField
    feedbackDescription = StringField
    feedbackDate = StringField
    feedbackTime = StringField
    feedbackActiveStatus = StringField