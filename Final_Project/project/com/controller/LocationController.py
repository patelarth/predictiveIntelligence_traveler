from project import app
from flask import render_template, session, redirect, request, url_for
from project.com.dao.LocationDAO import LocationDAO
from project.com.vo.LocationVO import LocationVO


@app.route('/loadLocation')
def loadLocation():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    return render_template('admin/addLocation.html')


@app.route('/insertLocation',methods=['POST'])
def insertLocation():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    locationVO = LocationVO()
    locationDAO = LocationDAO()

    locationName = request.form['locationName']
    locationDescription = request.form['locationDescription']

    locationVO.locationName = locationName
    locationVO.locationDescription = locationDescription
    locationVO.locationActiveStatus = 'active'

    locationDAO.insertLocation(locationVO)

    return render_template('admin/addLocation.html')


@app.route('/viewLocation')
def viewLocation():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    locationVO = LocationVO()
    locationDAO = LocationDAO()

    locationDict = locationDAO.viewLocation()

    return render_template('admin/viewLocation.html',locationDict=locationDict)


@app.route('/deleteCompany',methods=['GET'])
def deleteLocation():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    locationVO = LocationVO()
    locationDAO = LocationDAO()

    locationVO.locationId = request.args.get('locationId')
    locationDAO.deleteLocation(locationVO)
    return redirect(url_for('viewLocation'))

