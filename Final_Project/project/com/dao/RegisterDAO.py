from project.com.dao import con

class RegisterDAO:

    def insertRegister(self,registerVO):
        connection = con()
        cursur = connection.cursor()
        cursur.execute("INSERT INTO registermaster(registerFirstName,registerLastName,registerMobilenumber,registerBirthDate,registerGender,registerAddress,register_loginId) VALUES ('"+registerVO.registerFname+"','"+registerVO.registerLname+"','"+registerVO.registerMobilenumber+"','"+registerVO.registerBirthdate+"','"+registerVO.registerGender+"','"+registerVO.registerAddress+"','"+str(registerVO.register_loginId)+"') ")
        connection.commit()
        cursur.close()
        connection.close()

    def viewRegister(self):
        connection = con()
        cursur = connection.cursor()

        cursur.execute("SELECT * FROM registermaster JOIN loginmaster ON registermaster.registerId=loginmaster.loginId WHERE registerActiveStatus='active' ")
        data = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()
        return data

    def deleteRegister(self,registerVO):
        connection = con()
        cursur = connection.cursor()
        cursur.execute(
            "UPDATE registermaster SET registerActiveStatus='deactive'  WHERE registerId='" + registerVO.registerId + " '")
        # data = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()