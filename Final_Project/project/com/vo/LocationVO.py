from wtforms import *


class LocationVO:
    locationId = IntegerField
    locationName = StringField
    locationDescription = StringField
    locationActiveStatus = StringField