
from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '056f75d4db85f08cba41c16a2aafd820d4c77775'


from flaskoffice import routes