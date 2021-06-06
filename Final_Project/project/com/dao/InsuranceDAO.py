from project.com.dao import con


class InsuranceDAO():

    def addInsurance(self,insuranceVO):
        try:
            connection = con()
            cursur = connection.cursor()

            cursur.execute(
                "INSERT INTO insurancemaster(insuranceName,insuranceDescription,price,ageLimit,startDate,endDate) VALUES ('" + insuranceVO.insuranceName + "','" + insuranceVO.insuranceDescription + "','" + insuranceVO.price + "','" + insuranceVO.ageLimit + "','" + insuranceVO.startDate + "','" + insuranceVO.endDate + "') ")

            connection.commit()
            cursur.close()
            connection.close()
        except Exception:
            raise Exception

    def viewInsurance(self):
        try:
            connection = con()
            cursur = connection.cursor()

            cursur.execute("SELECT * FROM insurancemaster WHERE insuranceActiveStatus='active' ")
            data = cursur.fetchall()
            connection.commit()
            cursur.close()
            connection.close()
            return data
        except Exception:
            raise Exception

    def deleteFlight(self, insuranceVO):
        try:
            connection = con()
            cursur = connection.cursor()
            cursur.execute("UPDATE insurancemaster SET insuranceActiveStatus='deactive'  WHERE insuranceId='" + insuranceVO.insuranceId + " '")
            #data = cursur.fetchall()
            connection.commit()
            cursur.close()
            connection.close()
        except Exception:
            raise Exception

    def updateInsurance(self, insuranceVO):
        try:
            connection = con()
            cursur = connection.cursor()

            cursur.execute("SELECT * FROM insurancemaster WHERE insuranceId='"+insuranceVO.insuranceId+"' ")
            data = cursur.fetchall()
            connection.commit()
            cursur.close()
            connection.close()
            return data

        except Exception:
            raise Exception

    def editInsurance(self, insuranceVO):

        connection = con()
        cursur = connection.cursor()
        cursur.execute(
            "UPDATE insurancemaster SET insuranceName='" + insuranceVO.insuranceName + "', insuranceDescription='" + insuranceVO.insuranceDescription + "', price='" + insuranceVO.price + "', ageLimit='" + insuranceVO.ageLimit + "', startDate='" + insuranceVO.startDate + "', endDate='" + insuranceVO.endDate + "'  WHERE id='" + insuranceVO.insuranceId + "'")
        # data = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()
