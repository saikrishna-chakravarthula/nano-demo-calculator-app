from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data=request.json
    num1=data['first']
    num2=data['second']
    rsum=num1+num2
    return jsonify({"result": rsum})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data=request.json
    num1=data['first']
    num2=data['second']
    rs=num1-num2
    return jsonify({"result": rs})

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
