from wtforms import *


class FlightVO():

    flightId = IntegerField
    flightCompany = StringField
    flightCapacity = StringField
    flightNumber = StringField
    flightDate = StringField
    #flightArrivalDestination = StringField
    #flightDepartureDestination = StringField
    flightArrivalTime = StringField
    flightDepartureTime = StringField
    flightCompany_CompanyId = IntegerField
    flightArrivalLocation_LocationId = IntegerField
    flightDepartureLocation_LocationId = IntegerField