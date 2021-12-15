from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    message = 'Hello Flask!'

    output = {
        'data': message
    }

    return output


@app.route('/current_datetime')
def date_time():
    message = ''
    hour_int = int(datetime.now().strftime("%H"))

    if hour_int <= 24:
        message = 'Boa noite!'
    if hour_int < 18:
        message = 'Boa tarde!'
    if hour_int < 12:
        message = 'Bom dia!'


    output = {
        'current_datetime': datetime.now().strftime("%d/%m/%Y %H:%M:%S %p"),
        'message': message
    }

    return output