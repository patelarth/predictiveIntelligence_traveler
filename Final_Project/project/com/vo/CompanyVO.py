from wtforms import *


class CompanyVO:

    companyId = IntegerField
    companyName = StringField
    companyEmail = StringField
    companyContactNo = StringField
    companyActiveStatus = StringField