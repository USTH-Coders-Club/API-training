from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/')

def getInfo():
    user_id = request.args.get('id')
    print(user_id)
    result = {}
    if(user_id=="1"):
        result = {
        'id': '1',
        'name': 'Duong Dang Hung',
        'age': '21',
        'career': 'Student'
        }
    elif (user_id=="2"):
        result={
            'id': '2',
            'name': 'Ta Quang Hieu',
            'age': '22',
            'career': 'HR'
        }
    return jsonify(result)

app.run()