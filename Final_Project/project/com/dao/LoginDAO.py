from project.com.dao import con

class LoginDAO:

    def checkLogin(self,loginVo):
        connection = con()
        cursur = connection.cursor()
        cursur.execute(
            "SELECT * FROM loginmaster WHERE loginEmail ='" + loginVo.loginEmail + "'")
        checklogin = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()
        return checklogin

    def insertLogin(self,LoginVO):
        connection = con()
        cursur = connection.cursor()
        cursur.execute(
            "INSERT INTO loginmaster(loginEmail,loginPassword) VALUES ('"+LoginVO.loginEmail +"','"+LoginVO.loginPassword+"')")
        cursur.execute("SELECT MAX(loginId) FROM loginmaster")
        maxlogindata = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()
        return maxlogindata