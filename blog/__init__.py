from flask import Flask

app = Flask(__name__)
app.config['SECRECT KEY'] = '5d6aeb010c199323b32da8894826b8dd958751a886ffdea9'
app.secret_key = "hello"

from blog import routes
