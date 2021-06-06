from project.com.dao import con


class CompanyDAO:

    def insertCompany(self,companyVO):
        connection = con()
        cursur = connection.cursor()

        cursur.execute(
            "INSERT INTO companymaster(companyName,companyEmail,companyContactNo,companyActiveStatus) VALUES ('"+companyVO.companyName+"','"+companyVO.companyEmail+"','"+companyVO.companyContactNo+"','"+companyVO.companyActiveStatus+"')")

        connection.commit()
        cursur.close()
        connection.close()

    def viewCompany(self):
        connection = con()
        cursur = connection.cursor()
        cursur.execute("SELECT * FROM companymaster WHERE companyActiveStatus='active'")
        companyDict = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()
        return companyDict

    def editCompany(self,companyVO):
        connection = con()
        cursur = connection.cursor()
        cursur.execute("SELECT * FROM companymaster WHERE companyId=' " + companyVO.companyId + "' ")
        flightDict = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()
        return flightDict

    def updateCompany(self,companyVO):
        connection = con()
        cursur = connection.cursor()
        #print(companyVO.companyContactNo,companyVO.companyEmail,companyVO.companyName)
        cursur.execute(
            "UPDATE companymaster SET companyName='" + companyVO.companyName + "', companyEmail='" + companyVO.companyEmail + "',companyContactNo='" + str(companyVO.companyContactNo) + "',companyActiveStatus='"+companyVO.companyActiveStatus+"'  WHERE companyId='" + companyVO.companyId + "'")
        # data = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()

    def deleteCompany(self,companyVO):
        connection = con()
        cursur = connection.cursor()
        cursur.execute(
            "UPDATE companymaster SET companyActiveStatus='deactive'  WHERE companyId='" + companyVO.companyId + " '")
        # data = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()