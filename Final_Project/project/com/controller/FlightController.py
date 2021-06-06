from project import app
from flask import render_template, session, redirect, request, url_for
from project.com.dao.FlightDAO import FlightDAO
from project.com.vo.FlightVO import FlightVO
from project.com.dao.CompanyDAO import CompanyDAO
from project.com.dao.LocationDAO import LocationDAO


@app.route('/loadFlights')
def addFlight():
    companyDAO = CompanyDAO()
    locationDAO = LocationDAO()
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    companyDict = companyDAO.viewCompany()
    locationDict = locationDAO.viewLocation()
    return render_template('admin/addFlights.html',companyDict=companyDict, locationDict=locationDict)


@app.route('/insertFlight', methods=['POST'])
def insertFlight():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    flightDAO = FlightDAO()
    flightVO = FlightVO()


    no = request.form['flightNo']
    #company = request.form['flightCompany']
    capacity = request.form['flightCapacity']
    date = request.form['flightDate']
    #arrvialdesti = request.form['flightArrivalDestination']
    #departuredesti = request.form['flightDepartureDestination']
    arrvialtime = request.form['flightArrivalTime']
    departuretime = request.form['flightDepartureTime']
    #print (no, company, date, arrvialdesti)
    flightCompany_CompanyId = request.form['companyId']
    flightArrivalLocation_LocationId = request.form['arrivalLocationId']
    flightDepartureLocation_LocationId = request.form['departureLocationId']

    flightVO.flightNumber = str(no)
    #flightVO.flightCompany = str(company)
    flightVO.flightCapacity = str(capacity)
    flightVO.flightDate = str(date)
    #flightVO.flightArrivalDestination = str(arrvialdesti)
    #flightVO.flightDepartureDestination = str(departuredesti)
    flightVO.flightArrivalTime = str(arrvialtime)
    flightVO.flightDepartureTime = str(departuretime)
    flightVO.flightCompany_CompanyId = str(flightCompany_CompanyId)
    flightVO.flightArrivalLocation_LocationId = str(flightArrivalLocation_LocationId)
    flightVO.flightDepartureLocation_LocationId = str(flightDepartureLocation_LocationId)
    flightDAO.addFlight(flightVO)
    return render_template('admin/addFlights.html')


@app.route('/viewFlights')
def viewFlight():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    flightVO = FlightVO()
    flightDAO = FlightDAO()

    flightDict = flightDAO.viewFlight()
    return render_template('admin/viewFlights.html', flightDict=flightDict)


@app.route('/deleteFlights',methods=['GET'])
def deleteFlight():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    flightVO = FlightVO()
    flightDAO = FlightDAO()

    flightVO.flightId = request.args.get('flightId')

    flightDAO.deleteFlight(flightVO)

    return redirect(url_for('viewFlight'))


@app.route('/editFlights', methods=['GET'])
def editFlight():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    flightVO = FlightVO()
    flightDAO = FlightDAO()
    companyDAO = CompanyDAO()
    locationDAO = LocationDAO()
    flightVO.flightId = request.args.get('flightId')

    flightDict = flightDAO.editFlight(flightVO)
    companyDict = companyDAO.viewCompany()
    locationDict = locationDAO.viewLocation()
    return render_template("admin/editFlights.html", flightDict=flightDict,companyDict=companyDict, locationDict=locationDict)


@app.route('/updateFlights', methods=['POST'])
def updateFlight():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    flightVO = FlightVO()
    flightDAO = FlightDAO()

    no = request.form['flightNo']
    # company = request.form['flightCompany']
    capacity = request.form['flightCapacity']
    date = request.form['flightDate']
    # arrvialdesti = request.form['flightArrivalDestination']
    # departuredesti = request.form['flightDepartureDestination']
    arrvialtime = request.form['flightArrivalTime']
    departuretime = request.form['flightDepartureTime']
    # print (no, company, date, arrvialdesti)
    flightCompany_CompanyId = request.form['companyId']
    flightArrivalLocation_LocationId = request.form['arrivalLocationId']
    flightDepartureLocation_LocationId = request.form['departureLocationId']

    flightVO.flightNumber = str(no)
    # flightVO.flightCompany = str(company)
    flightVO.flightCapacity = str(capacity)
    flightVO.flightDate = str(date)
    # flightVO.flightArrivalDestination = str(arrvialdesti)
    # flightVO.flightDepartureDestination = str(departuredesti)
    flightVO.flightArrivalTime = str(arrvialtime)
    flightVO.flightDepartureTime = str(departuretime)
    flightVO.flightCompany_CompanyId = str(flightCompany_CompanyId)
    flightVO.flightArrivalLocation_LocationId = str(flightArrivalLocation_LocationId)
    flightVO.flightDepartureLocation_LocationId = str(flightDepartureLocation_LocationId)
    flightDAO.updateFlight(flightVO)

    return redirect(url_for('viewFlight'))

