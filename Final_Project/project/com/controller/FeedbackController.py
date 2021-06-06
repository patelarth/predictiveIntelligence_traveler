from project import app
from flask import render_template, session, redirect, request, url_for
from project.com.dao.FeedbackDAO import FeedbackDAO
from project.com.vo.FeedbackVO import FeedbackVO
import time


@app.route('/loadUserFeedback')
def loadUserFeedback():
    if session['loginRole'] != "user":
        return render_template('admin/login.html')
    return render_template('user/addFeedback.html')


@app.route('/insertFeedback',methods=['POST'])
def insertFeedback():
    if session['loginRole'] != "user":
        return render_template('admin/login.html')
    feedbackVO = FeedbackVO()
    feedbackDAO = FeedbackDAO()
    feedbackVO.feedbackRating = request.form['feedbackRating']
    feedbackVO.feedbackDescription = request.form['feedbackDescription']
    feedbackVO.feedbackFrom_LoginId = session['loginId']
    feedbackVO.feedbackActivestatus = "active"
    datetime = time.ctime().split(" ")
    feedbackVO.feedbackTime = datetime[-2]
    feedbackVO.feedbackDate = " ".join([datetime[1], datetime[2], datetime[4]])
    feedbackVO.feedback_LoginId = session['loginId']
    print(feedbackVO.feedbackFrom_LoginId, feedbackVO.feedbackRating, feedbackVO.feedbackDescription, feedbackVO.feedbackActivestatus, feedbackVO.feedbackDate,feedbackVO.feedbackTime,feedbackVO.feedback_LoginId)
    feedbackDAO.insertFeedback(feedbackVO)
    return render_template('user/index.html')


@app.route('/viewUserFeedback')
def viewUserFeedback():
    if session['loginRole'] != "user":
        return render_template('admin/login.html')
    feedbackVO = FeedbackVO()
    feedbackDAO = FeedbackDAO()

    feedbackVO.feedbackFrom_LoginId = session['loginId']
    feedbackVO.feedbackActiveStatus = 'active'
    viewFeedback = feedbackDAO.viewUserFeedback(feedbackVO)
    return render_template('user/viewFeedback.html', viewFeedback=viewFeedback)

#admin
@app.route('/viewFeedback')
def viewFeedback():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    feedbackVO = FeedbackVO()
    feedbackDAO = FeedbackDAO()

    feedbackDict = feedbackDAO.viewFeedback()

    return render_template('admin/viewFeedback.html',feedbackDict=feedbackDict)


@app.route('/viewedFeedback',methods=['GET'])
def viewedFeedback():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    feedbackVO = FeedbackVO()
    feedbackDAO = FeedbackDAO()
    feedbackVO.feedbackId = request.args.get('feedbackId')
    feedbackVO.feedbackTo_LoginId = session['loginId']
    feedbackDAO.updateFeedback(feedbackVO)
    return redirect(url_for('viewFeedback'))


