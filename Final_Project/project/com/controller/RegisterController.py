from project import app
from flask import render_template, session, redirect, request, url_for
from project.com.dao.RegisterDAO import RegisterDAO
from project.com.vo.RegisterVO import RegisterVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO
import random
import string
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import Message


@app.route("/registerLoad")
def registerLoad():
    return render_template("user/register.html")


@app.route("/registerUser", methods=["POST"])
def registerUser():
    registerDAO = RegisterDAO()
    registerVO = RegisterVO()
    loginDAO = LoginDAO()
    loginVO = LoginVO()
    loginVO.loginEmail = request.form['Email']
    loginVO.loginPassword = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))
    fromaddr = "arunproject100@gmail.com"
    toaddr = loginVO.loginEmail
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "PYTHON PASSWORD"
    msg.attach(MIMEText(loginVO.loginPassword, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "arun123admin")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    maxloginid = loginDAO.insertLogin(loginVO)
    registerVO.register_loginId = maxloginid[0]['MAX(loginId)']
    registerVO.registerFname = request.form['Firstname']
    registerVO.registerLname = request.form['Lastname']
    registerVO.registerMobilenumber = request.form['Mobilenumber']
    registerVO.registerGender = request.form['gender']
    registerVO.registerBirthdate = request.form['Birthdate']
    registerVO.registerAddress = request.form['Address']
    registerDAO.insertRegister(registerVO)
    return render_template("admin/login.html")


@app.route('/viewRegister')
def viewRegister():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    registerVO = RegisterVO()
    registerDAO = RegisterDAO()

    registerDict = registerDAO.viewRegister()

    return render_template('admin/viewRegister.html', registerDict=registerDict)


@app.route('/deleteRegister',methods=['GET'])
def deleteRegister():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    registerVO = RegisterVO()
    registerDAO = RegisterDAO()
    registerVO.registerId = request.args.get('registerId')

    registerDAO.deleteRegister(registerVO)

    return redirect(url_for('viewRegister'))




