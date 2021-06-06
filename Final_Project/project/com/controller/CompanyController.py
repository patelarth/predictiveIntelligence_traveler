from project import app
from flask import render_template, session, redirect, request, url_for
from project.com.dao.CompanyDAO import CompanyDAO
from project.com.vo.CompanyVO import CompanyVO

@app.route('/loadCompany')
def loadCompany():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    return render_template('admin/addCompany.html')


@app.route('/insertCompany',methods=['POST'])
def insertCompany():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    companyVO = CompanyVO()
    companyDAO = CompanyDAO()

    companyName = request.form['flightCompany']
    companyEmail = request.form['flightCompanyEmail']
    contactNo = request.form['contactNo']

    companyVO.companyName = str(companyName)
    companyVO.companyEmail = str(companyEmail)
    companyVO.companyContactNo = str(contactNo)
    companyVO.companyActiveStatus = 'active'

    companyDAO.insertCompany(companyVO)
    return render_template('admin/addCompany.html')


@app.route('/viewCompany')
def viewCompany():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    companyVO = CompanyVO()
    companyDAO = CompanyDAO()

    companyDict = companyDAO.viewCompany()
    return render_template('admin/viewCompany.html',companyDict=companyDict)


@app.route('/deleteCompany',methods=['GET'])
def deleteCompany():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    companyVO = CompanyVO()
    companyDAO = CompanyDAO()

    companyVO.companyId = request.args.get('companyId')
    companyDAO.deleteCompany(companyVO)
    return redirect(url_for('viewCompany'))


@app.route('/editCompany',methods=['GET'])
def editCompany():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    companyVO = CompanyVO()
    companyDAO = CompanyDAO()

    companyVO.companyId = request.args.get('companyId')
    companyDict = companyDAO.editCompany(companyVO)
    return render_template('admin/editCompany.html',companyDict=companyDict)


@app.route('/updateCompany',methods=['POST'])
def updateCompany():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    companyVO = CompanyVO()
    companyDAO = CompanyDAO()

    companyName = request.form['flightCompany']
    companyEmail = request.form['flightCompanyEmail']
    contactNo = request.form['contactNo']

    companyVO.companyName = str(companyName)
    companyVO.companyEmail = str(companyEmail)
    companyVO.companyContactNo = str(contactNo)
    companyVO.companyActiveStatus = 'active'

    companyDAO.updateCompany(companyVO)
    return redirect(url_for('viewCompany'))


