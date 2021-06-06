from project import app
from flask import render_template, session, redirect, request, url_for
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO


@app.route('/')
def loadLogin():
    return render_template('admin/login.html')


@app.route("/checkLogin",methods=["POST"])
def checkLogin():
    loginDao = LoginDAO()
    loginVo = LoginVO()
    loginEmail = request.form['loginEmail']
    loginPassword = request.form['loginPassword']
    LoginVO.loginEmail = loginEmail
    LoginVO.loginPassword = loginPassword
    checkdata = loginDao.checkLogin(loginVo)
    if len(checkdata) == 0:
        return render_template("admin/login.html",msg = "Invalid email")
    elif checkdata[0]['loginPassword'] != loginVo.loginPassword:
        return render_template("admin/login.html",msg = "Invalid Password")
    elif len(checkdata[0]['loginRole']) != 0:
        session['loginId'] = checkdata[0]['loginId']
        session['loginRole'] = checkdata[0]['loginRole']
        return redirect(url_for('checkindex'))


@app.route("/index")
def checkindex():
    try:
        if session['loginRole'] == "admin":
            return render_template("admin/index.html")
        else:
            return render_template("user/index.html")
    except:
        return render_template('admin/login.html',msg="Please Login First")


@app.route("/logout")
def logOut():
    session.clear()
    return loadLogin()



