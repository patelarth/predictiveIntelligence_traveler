from wtforms import *


class TicketVO:
    ticketId = IntegerField
    ticketName = StringField
    ticketDescription = StringField
    ticketPrice = StringField
    ticketActiveStatus = StringField
    ticketFlight_FlightId = IntegerField
    ticketCompany_CompanyId = IntegerField