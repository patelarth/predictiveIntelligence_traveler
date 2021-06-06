from project.com.dao import con


class FlightDAO:

    def addFlight(self, flightVO):

        connection = con()
        cursur = connection.cursor()

        cursur.execute(
            "INSERT INTO flightmaster(flightNo,flightCapacity,flightDate,flightArrivalLocation_LocationId,flightDepartureLocation_LocationId,flightArrivalTime,flightDepartureTime,flightCompany_CompanyId) VALUES('" + flightVO.flightNumber + "','"+flightVO.flightCapacity+"', '" + flightVO.flightDate + "','" + str(flightVO.flightArrivalLocation_LocationId) + "','" + str(flightVO.flightDepartureLocation_LocationId) + "','" + flightVO.flightArrivalTime + "','" + flightVO.flightDepartureTime + "','"+flightVO.flightCompany_CompanyId +"')")

        connection.commit()
        cursur.close()
        connection.close()


    def viewFlight(self):

        connection = con()
        cursur = connection.cursor()
        cursur.execute(
            "SELECT * FROM flightmaster f INNER JOIN companymaster c ON f.flightCompany_CompanyId=c.companyId LEFT JOIN locationmaster ls1 ON f.flightArrivalLocation_LocationId=ls1.locationId LEFT JOIN locationmaster ls2 ON f.flightDepartureLocation_LocationId=ls2.locationId WHERE flightActiveStatus='active' ")
        data = cursur.fetchall()
        #print data
        connection.commit()
        cursur.close()
        connection.close()
        return data

    def deleteFlight(self,flightVO):
        try:
            connection = con()
            cursur = connection.cursor()
            cursur.execute("UPDATE flightmaster SET flightActiveStatus='deactive'  WHERE flightId='" + flightVO.flightId + " '")
            #data = cursur.fetchall()
            connection.commit()
            cursur.close()
            connection.close()
        except Exception:
            raise Exception

    def editFlight(self, flightVO):
        try:
            connection = con()
            cursur = connection.cursor()
            cursur.execute("SELECT * FROM flightmaster f INNER JOIN companymaster c ON f.flightCompany_CompanyId=c.companyId LEFT JOIN locationmaster ls1 ON f.flightArrivalLocation_LocationId=ls1.locationId LEFT JOIN locationmaster ls2 ON f.flightDepartureLocation_LocationId=ls2.locationId WHERE flightId='" + flightVO.flightId + " ' ")
            flightDict = cursur.fetchall()
            connection.commit()
            cursur.close()
            connection.close()
            return flightDict
        except Exception:
            raise Exception

    def updateFlight(self, flightVO):

        connection = con()
        cursur = connection.cursor()
        cursur.execute(
            "UPDATE flightmaster SET flightNo='" + flightVO.flightNumber + "',flightCapacity='" + flightVO.flightCapacity + "', flightDate='" + flightVO.flightDate + "', flightArrivalLocation_LocationId='" + str(flightVO.flightArrivalLocation_LocationId) + "', flightDepartureLocation_LocationId='" + str(flightVO.flightDepartureLocation_LocationId) + "', flightArrivalTime='" + flightVO.flightArrivalTime + "', flightDepartureTime='" + flightVO.flightDepartureTime + "',flightCompany_CompanyId='"+str(flightVO.flightCompany_CompanyId)+"' WHERE flightId='" + flightVO.flightId + "'")
        #data = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()
