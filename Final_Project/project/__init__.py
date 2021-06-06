from flask import Flask

app = Flask(__name__)
app.secret_key = '123'

import project.com.controller