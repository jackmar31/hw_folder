import os

basedir= os.path.abspath(os.path.dirname(__file__))

# Giving acess to thr project in ANY os WE find ourselves in
# Allow outside files/folders to be added to the projects
# base directory

class Config():
    """
        Set Config variables for the flask app.
        Using Envorinment variables where avaible
        create config variables if not done already.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Turn off message for updates in sqlalchemy