from wtforms import *


class DatasetVO:

    datasetId = IntegerField
    datasetName = StringField
    datasetPath = StringField
    datasetDescription = StringField