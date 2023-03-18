from flask import Flask

app = Flask(__name__)
app.config['SECRECT KEY'] = <SECRET>
app.secret_key = <SECRET KEY>

from blog import routes
