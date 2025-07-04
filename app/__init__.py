from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://guapoweb:guapo$2025@192.168.2.34:5440/Sig'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ss3cretgu4pok3y'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)

login_manager = LoginManager(app)
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
