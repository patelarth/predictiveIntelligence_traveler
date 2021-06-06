from project.com.dao import con


class FeedbackDAO:

    def insertFeedback(self, feedbackVO):
        connection = con()
        cursur = connection.cursor()
        cursur.execute(
            "INSERT INTO feedbackmaster(feedbackFrom_LoginId,feedbackRating,feedbackDescription,feedbackDate,feedbackTime,feedbackActivestatus,feedback_LoginId) VALUES ('" + str(feedbackVO.feedbackFrom_LoginId) + "','" + feedbackVO.feedbackRating + "','" +
                feedbackVO.feedbackDescription + "','" + feedbackVO.feedbackDate + "','" + feedbackVO.feedbackTime + "','" + feedbackVO.feedbackActivestatus + "','"+str(feedbackVO.feedback_LoginId)+"')")
        connection.commit()
        cursur.close()
        connection.close()

    def viewFeedback(self):
        connection = con()
        cursur = connection.cursor()

        cursur.execute("SELECT * FROM feedbackmaster JOIN loginmaster ON feedbackmaster.feedbackFrom_LoginId=loginmaster.loginId WHERE feedbackActiveStatus='active' ")
        data = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()
        return data

    def updateFeedback(self, feedbackVO):

        connection = con()
        cursur = connection.cursor()
        cursur.execute("UPDATE feedbackmaster SET feedbackTo_LoginId='"+str(feedbackVO.feedbackTo_LoginId)+"' WHERE feedbackId='" + feedbackVO.feedbackId + " '")
        #data = cursur.fetchall()
        connection.commit()
        cursur.close()
        connection.close()

    def viewUserFeedback(self,feedbackVO):
        connection = con()
        cursur = connection.cursor()
        cursur.execute("SELECT * From feedbackmaster LEFT JOIN loginmaster ON feedbackmaster.feedbackTo_LoginId=loginmaster.loginId WHERE feedbackFrom_LoginId='" + str(
                feedbackVO.feedbackFrom_LoginId) + "' and feedbackActiveStatus ='" + feedbackVO.feedbackActiveStatus + "'")
        viewFeedback = cursur.fetchall()
        print viewFeedback
        connection.commit()
        cursur.close()
        connection.close()
        return viewFeedback
