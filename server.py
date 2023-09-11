from flask import Flask, jsonify, request
import json
from compute import NumberInput, Calculator
app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greet():
    content = "hello world!"
    return content

@app.post("/calculator/add")
def add():
    if request.is_json:
        numberInput = json.loads(json.dumps(request.get_json()), object_hook=NumberInput.number_decoder)
        calc = Calculator()
        result = calc.add(numberInput.first, numberInput.second)
        return jsonify({"result": result}), 200
    return {"error": "Request must be JSON"}, 415

@app.post("/calculator/subtract")
def sub():
    if request.is_json:
        numberInput = json.loads(json.dumps(request.get_json()), object_hook=NumberInput.number_decoder)
        calc = Calculator()
        result = calc.subtract(numberInput.first, numberInput.second)
        return jsonify({"result": result}), 200
    return {"error": "Request must be JSON"}, 415

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
