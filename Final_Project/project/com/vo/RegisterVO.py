from wtforms import *

class RegisterVO:

    register_loginId = IntegerField
    registerId = IntegerField
    registerFname = StringField
    registerLname = StringField
    registerMobilenumber = StringField
    registerBirthdate = StringField
    registerAddress = StringField
    registerGender = StringField
    registerActivestatus = StringField