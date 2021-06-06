from project.com.dao import con


class LocationDAO:

    def insertLocation(self,locationVO):
        connection = con()
        cursur = connection.cursor()

        cursur.execute(
            "INSERT INTO locationmaster(locationName,locationDescription,locationActiveStatus) VALUES ('" + locationVO.locationName + "','" + locationVO.locationDescription + "','" + locationVO.locationActiveStatus + "')")

        connection.commit()
        cursur.close()
        connection.close()

    def viewLocation(self):
        connection = con()
        cursur = connection.cursor()
        cursur.execute("SELECT * FROM locationmaster WHERE locationActiveStatus='active'")
        locationDict = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()
        return locationDict

    def deleteLocation(self,locationVO):
        connection = con()
        cursur = connection.cursor()
        cursur.execute(
            "UPDATE locationmaster SET locationActiveStatus='deactive'  WHERE locationId='" + locationVO.locationId + " '")
        # data = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()