from project import app
from flask import render_template,request,session
from project.com.dao.ComplainDAO import ComplainDAO
from project.com.vo.ComplainVO import ComplainVO
import time


#for admin side
@app.route('/loadComplain')
def loadComplain():
    if session['loginRole']!="admin":
        return render_template('admin/login.html')
    complaindao = ComplainDAO()
    complainvo = ComplainVO()
    complainvo.complainActivestatus = "active"
    complainvo.complainStatus = "pending"
    viewcomplainadmin = complaindao.viewComplainAdmin(complainvo)
    return render_template('admin/viewComplain.html',viewcomplainadmin = viewcomplainadmin)


@app.route('/showComplain' ,methods=['GET'])
def viewComplainAdmin():
    if session['loginRole']!="admin":
        return render_template('admin/login.html')
    complaindao = ComplainDAO()
    complainvo = ComplainVO()
    complainvo.complainID = request.args.get('complainid')
    editcomplain = complaindao.editComplainAdmin(complainvo)
    return render_template('admin/updateComplain.html',editcomplain = editcomplain)


@app.route('/updateComplain',methods=['POST'])
def updateComplainAdmin():
    if session['loginRole']!="admin":
        return render_template('admin/login.html')
    complaindao = ComplainDAO()
    complainvo = ComplainVO()
    complainvo.complainID = request.form['complainId']
    complainvo.complainStatus = "replied"
    complainvo.complainTo_LoginId = session['loginId']
    complainvo.replyDescription = request.form['replycomplain']
    complaindao.updateComplainAdmin(complainvo)
    return loadComplain()


#for user side
@app.route('/loadUserComplain')
def loadUserComplain():
    if session['loginRole'] != "user":
        return render_template('admin/login.html')
    return render_template('user/addComplain.html')


@app.route('/viewUserComplain')
def viewComplain():
    if session['loginRole'] != "user":
        return render_template('admin/login.html')
    complaindao = ComplainDAO()
    complainvo = ComplainVO()
    complainvo.complainFrom_LoginId = session['loginId']
    complainvo.complainActiveStatus = "active"
    viewcomplain = complaindao.viewComplain(complainvo)
    return render_template('user/viewComplain.html',viewcomplain = viewcomplain)


@app.route('/insertComplain',methods=['POST'])
def insertComplain():
    if session['loginRole'] != "user":
        return render_template('admin/login.html')
    complaindao = ComplainDAO()
    complainvo = ComplainVO()
    complainvo.complainSubject = request.form['complainSubject']
    complainvo.complainDescription = request.form['complainDescription']
    complainvo.complainFrom_LoginId = session['loginId']
    complainvo.complainActivestatus = "active"
    complainvo.complainStatus = "pending"
    datetime = time.ctime().split(" ")
    complainvo.complainTime = datetime[-2]
    complainvo.complainDate = " ".join([datetime[1],datetime[2],datetime[4]])
    print(complainvo.complainActivestatus,complainvo.complainStatus,complainvo.complainTime,complainvo.complainDate,complainvo.complainFrom_LoginId,complainvo.complainDescription,complainvo.complainSubject)
    complaindao.insertcomplain(complainvo)
    return render_template("user/addComplain.html")


@app.route('/deleteComplain',methods=['GET'])
def deleteComplain():
    if session['loginRole'] != "user":
        return render_template('admin/login.html')
    complaindao = ComplainDAO()
    complainvo = ComplainVO()
    complainvo.complainID = request.args.get('deletecomplain')
    complainvo.complainActivestatus = "deactive"
    complaindao.deleteComplain(complainvo)
    return viewComplain()





