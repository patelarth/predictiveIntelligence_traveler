from project.com.dao import con


class TicketDAO:

    def insertTicket(self,ticketVO):
        connection = con()
        cursur = connection.cursor()

        cursur.execute(
            "INSERT INTO ticketmaster(ticketName,ticketDescription,ticketPrice,ticketFlight_FlightId,ticketCompany_CompanyId,ticketActiveStatus) VALUES ('" + ticketVO.ticketName + "','" + ticketVO.ticketDescription + "','" + ticketVO.ticketPrice + "','"+ticketVO.ticketFlight_FlightId+"','"+ticketVO.ticketCompany_CompanyId+"','" + ticketVO.ticketActiveStatus + "')")

        connection.commit()
        cursur.close()
        connection.close()

    def viewTicket(self):
        connection = con()
        cursur = connection.cursor()
        cursur.execute("SELECT * FROM ticketmaster t INNER JOIN flightmaster f ON t.ticketFlight_FlightId=f.flightId INNER JOIN companymaster c ON t.ticketCompany_CompanyId=c.companyId WHERE ticketActiveStatus='active'")
        ticketDict = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()
        return ticketDict

    def deleteTicket(self,ticketVO):
        connection = con()
        cursur = connection.cursor()
        cursur.execute(
            "UPDATE ticketmaster SET ticketActiveStatus='deactive'  WHERE ticketId='" + ticketVO.ticketId + " '")
        # data = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()

    def editTicket(self,ticketVO):
        connection = con()
        cursur = connection.cursor()
        cursur.execute("SELECT * FROM ticketmaster t INNER JOIN flightmaster f ON t.ticketFlight_FlightId=f.flightId INNER JOIN companymaster c ON t.ticketCompany_CompanyId=c.companyId WHERE ticketId='" + ticketVO.ticketId + " '")
        flightDict = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()
        return flightDict

    def updateTicket(self,ticketVO):
        connection = con()
        cursur = connection.cursor()
        # print(companyVO.companyContactNo,companyVO.companyEmail,companyVO.companyName)
        cursur.execute(
            "UPDATE ticketmaster SET ticketName='" + ticketVO.ticketName + "', ticketDescription='" + ticketVO.ticketDescription + "',ticketPrice='" + ticketVO.ticketPrice + "',ticketFlight_FlightId='"+str(ticketVO.ticketFlight_FlightId)+"',ticketCompany_CompanyId='"+str(ticketVO.ticketCompany_CompanyId)+"',ticketActiveStatus='" + ticketVO.ticketActiveStatus + "'  WHERE ticketId='" + ticketVO.ticketId + "'")
        # data = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()
