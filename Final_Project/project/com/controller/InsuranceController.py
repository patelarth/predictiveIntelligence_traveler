from project import app
from flask import render_template, session, redirect, request, url_for
from project.com.vo.InsuranceVO import InsuranceVO
from project.com.dao.InsuranceDAO import InsuranceDAO


@app.route('/loadInsurance')
def addInsurance():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    return render_template("admin/addInsurance.html")


@app.route('/insertInsurance', methods=['POST'])
def insuranceData():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    insuranceVO = InsuranceVO()
    insuranceDAO = InsuranceDAO()

    insuranceName = request.form['insuranceName']
    insuranceDescription = request.form['insuranceDescription']
    price = request.form['insurancePrice']
    ageLimit = request.form['insuranceAgeLimit']
    startDate = request.form['insuranceStartDate']
    endDate = request.form['insuranceEndDate']

    insuranceVO.insuranceName = str(insuranceName)
    insuranceVO.insuranceDescription = str(insuranceDescription)
    insuranceVO.price = str(price)
    insuranceVO.ageLimit = str(ageLimit)
    insuranceVO.startDate = str(startDate)
    insuranceVO.endDate = str(endDate)

    insuranceDAO.addInsurance(insuranceVO)

    return render_template("admin/addInsurance.html")


@app.route('/viewInsurance')
def viewInsurance():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    insuranceVO = InsuranceVO()
    insuranceDAO = InsuranceDAO()

    insuranceDict = insuranceDAO.viewInsurance()

    return render_template("admin/viewInsurance.html", insuranceDict=insuranceDict)


@app.route('/deleteInsurance',methods=['GET'])
def deleteInsurance():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    insuranceVO = InsuranceVO()
    insuranceDAO = InsuranceDAO()

    insuranceVO.insuranceId = request.args.get('insuranceId')

    insuranceDAO.deleteFlight(insuranceVO)
    return redirect(url_for('viewInsurance'))


@app.route('/updateInsurance', methods=['GET'])
def updateInsurance():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    insuranceVO = InsuranceVO()
    insuranceDAO = InsuranceDAO()

    insuranceVO.insuranceId = request.args.get('insuranceId')

    insuranceDict = insuranceDAO.updateInsurance(insuranceVO)

    return render_template("admin/editInsurance.html", insuranceDict=insuranceDict)


@app.route('/editInsurance', methods=['POST'])
def editInsurance():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    insuranceVO = InsuranceVO()
    insuranceDAO = InsuranceDAO()

    insuranceName = request.form['insuranceName']
    insuranceDescription = request.form['insuranceDescription']
    price = request.form['insurancePrice']
    ageLimit = request.form['insuranceAgeLimit']
    startDate = request.form['insuranceStartDate']
    endDate = request.form['insuranceEndDate']

    insuranceVO.insuranceName = str(insuranceName)
    insuranceVO.insuranceDescription = str(insuranceDescription)
    insuranceVO.price = str(price)
    insuranceVO.ageLimit = str(ageLimit)
    insuranceVO.startDate = str(startDate)
    insuranceVO.endDate = str(endDate)

    insuranceDAO.editInsurance(insuranceVO)

    return redirect(url_for('viewInsurance'))

