from project.com.dao import con


class ComplainDAO:

    def insertcomplain(self,complainVo):
        connection = con()
        cursur = connection.cursor()
        cursur.execute(
            "INSERT INTO complainmaster(complainSubject,complainDescription,complainFrom_LoginId,complainDate,complainTime,complainStatus,complainActivestatus) VALUES ('"+complainVo.complainSubject+"','"+complainVo.complainDescription+"','"+str(complainVo.complainFrom_LoginId)+"','"+complainVo.complainDate+"','"+complainVo.complainTime+"','"+complainVo.complainStatus+"','"+complainVo.complainActivestatus+"')")
        connection.commit()
        cursur.close()
        connection.close()

    def viewComplain(self,complainVo):
        connection = con()
        cursur = connection.cursor()
        #print(str(complainVo.complainTo_LoginId),complainVo.complainActiveStatus)
        cursur.execute("SELECT * From complainmaster LEFT JOIN loginmaster ON complainmaster.complainTo_LoginId=loginmaster.loginId WHERE complainFrom_LoginId='"+str(complainVo.complainFrom_LoginId)+"' and complainActiveStatus ='"+complainVo.complainActiveStatus+"'")
        viewcomplain = cursur.fetchall()
        #print viewcomplain
        connection.commit()
        cursur.close()
        connection.close()
        return viewcomplain

    def deleteComplain(self,complainVo):
        connection = con()
        cursur = connection.cursor()
        cursur.execute(
            "UPDATE complainmaster SET complainActivestatus='"+complainVo.complainActivestatus+"' WHERE complainId='"+complainVo.complainID+"'")
        connection.commit()
        cursur.close()
        connection.close()


    #for admin side page
    def viewComplainAdmin(self,complainVo):
        connection = con()
        cursur = connection.cursor()
        cursur.execute("SELECT * From complainmaster JOIN loginmaster ON complainmaster.complainFrom_LoginId = loginmaster.loginId WHERE complainActivestatus ='" + complainVo.complainActivestatus + "' and complainStatus='"+complainVo.complainStatus+"'")
        viewcomplain = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()
        return viewcomplain

    def editComplainAdmin(self,complainVo):
        connection = con()
        cursur = connection.cursor()
        cursur.execute(
            "SELECT * From complainmaster JOIN loginmaster ON complainmaster.complainFrom_LoginId = loginmaster.loginId WHERE complainId ='" + complainVo.complainID + "'")
        editcomplain = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()
        return editcomplain

    def updateComplainAdmin(self,complainVo):
        connection = con()
        cursur = connection.cursor()
        cursur.execute(
            "UPDATE complainmaster SET complainTo_LoginId='"+str(complainVo.complainTo_LoginId)+"' ,replyDescription='"+complainVo.replyDescription+"' , complainStatus='"+complainVo.complainStatus+"' WHERE complainId='"+str(complainVo.complainID)+"'")
        connection.commit()
        cursur.close()
        connection.close()
