from project import app
from flask import render_template,request,session,redirect,url_for
from project.com.dao.TicketDAO import TicketDAO
from project.com.vo.TicketVO import TicketVO
from project.com.dao.CompanyDAO import CompanyDAO
from project.com.dao.FlightDAO import FlightDAO


@app.route('/loadTicket')
def loadTicket():
    companyDAO = CompanyDAO()
    flightDAO = FlightDAO()
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    companyDict = companyDAO.viewCompany()
    flightDict = flightDAO.viewFlight()
    return render_template('admin/addTicket.html', companyDict=companyDict, flightDict=flightDict)


@app.route('/insertTicket',methods=['POST'])
def insertTicket():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    ticketVO = TicketVO()
    ticketDAO = TicketDAO()

    ticketName = request.form['ticketName']
    #print ticketName
    ticketDescription = request.form['ticketDescription']
    #print ticketDescription
    ticketPrice = request.form['ticketPrice']
    #print ticketPrice
    ticketCompany_CompanyId = request.form['companyId']
    #print ticketCompany_CompanyId
    ticketFlight_FlightId = request.form['flightId']
    #print ticketFlight_FlightId
    ticketVO.ticketName = str(ticketName)
    ticketVO.ticketPrice = str(ticketPrice)
    ticketVO.ticketDescription = str(ticketDescription)
    ticketVO.ticketCompany_CompanyId = str(ticketCompany_CompanyId)
    ticketVO.ticketFlight_FlightId = str(ticketFlight_FlightId)
    ticketVO.ticketActiveStatus = 'active'

    ticketDAO.insertTicket(ticketVO)
    return render_template('admin/addTicket.html')


@app.route('/viewTicket')
def viewTicket():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    ticketVO = TicketVO()
    ticketDAO = TicketDAO()
    companyDAO = CompanyDAO()

    ticketDict = ticketDAO.viewTicket()
    return render_template('admin/viewTicket.html',ticketDict=ticketDict)


@app.route('/editTicket',methods=['GET'])
def editTicket():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    ticketVO = TicketVO()
    ticketDAO = TicketDAO()
    flightDAO = FlightDAO()
    companyDAO = CompanyDAO()

    ticketVO.ticketId = request.args.get('ticketId')
    companyDict = companyDAO.viewCompany()
    flightDict = flightDAO.viewFlight()
    ticketDict = ticketDAO.editTicket(ticketVO)
    return render_template('admin/editTicket.html',companyDict=companyDict, flightDict=flightDict,ticketDict=ticketDict)


@app.route('/updateTicket',methods=['POST'])
def updateTicket():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    ticketVO = TicketVO()
    ticketDAO = TicketDAO()

    ticketName = request.form['ticketName']
    # print ticketName
    ticketDescription = request.form['ticketDescription']
    # print ticketDescription
    ticketPrice = request.form['ticketPrice']
    # print ticketPrice
    ticketCompany_CompanyId = request.form['companyId']
    # print ticketCompany_CompanyId
    ticketFlight_FlightId = request.form['flightId']
    # print ticketFlight_FlightId
    ticketVO.ticketName = str(ticketName)
    ticketVO.ticketPrice = str(ticketPrice)
    ticketVO.ticketDescription = str(ticketDescription)
    ticketVO.ticketCompany_CompanyId = str(ticketCompany_CompanyId)
    ticketVO.ticketFlight_FlightId = str(ticketFlight_FlightId)
    ticketVO.ticketActiveStatus = 'active'

    ticketDAO.updateTicket(ticketVO)
    return redirect(url_for('viewTicket'))

