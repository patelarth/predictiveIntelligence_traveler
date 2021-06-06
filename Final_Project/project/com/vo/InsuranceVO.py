from wtforms import *


class InsuranceVO():
    insuranceId = IntegerField
    insuranceName = StringField
    insuranceDescription = StringField
    price = StringField
    ageLimit = StringField
    startDate = StringField
    endDate = StringField