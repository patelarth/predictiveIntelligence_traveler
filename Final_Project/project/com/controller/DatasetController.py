from project import app
from flask import render_template, session, redirect, request, url_for
from project.com.dao.DatasetDAO import DatasetDAO
from project.com.vo.DatasetVO import DatasetVO
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'C:/Users/HP/PycharmProjects/Final_Project/project/static/adminResorces/dataset/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/loadDatasets')
def addDataset():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    return render_template('admin/addDataset.html')


@app.route('/insertDataset', methods=['POST'])
def insertDataset():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    datasetVO = DatasetVO()
    datasetDAO = DatasetDAO()

    file = request.files['file']
    print(file)
    fileDescription = request.form['fileDescription']
    filename = secure_filename(file.filename)
    print(filename)
    filepath = os.path.join("C:/Users/HP/PycharmProjects/Final_Project/project/static/adminResorces/dataset/", filename)
    file.save(filepath)
    datasetVO.datasetName = filename
    datasetVO.datasetDescription = fileDescription
    datasetVO.datasetPath = str(app.config['UPLOAD_FOLDER']+filename)
    datasetDAO.insertDataset(datasetVO)

    return render_template('admin/addDataset.html')


@app.route('/viewDatasets')
def viewDataset():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    datasetVO = DatasetVO()
    datasetDAO = DatasetDAO()

    datasetDict = datasetDAO.viewDataset()
    return render_template('admin/viewDataset.html', datasetDict=datasetDict)


@app.route('/deleteDatasets')
def deleteDataset():
    if session['loginRole'] != 'admin':
        return render_template('admin/login.html')
    datasetVO = DatasetVO()
    datasetDAO = DatasetDAO()

    datasetVO.datasetId = request.args.get('datasetId')
    datasetDAO.deleteDataset(datasetVO)

    return redirect(url_for('viewDataset'))