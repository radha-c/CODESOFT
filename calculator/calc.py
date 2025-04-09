from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calc.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    num1 = data.get("num1")
    num2 = data.get("num2")
    operation = data.get("operation")

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return jsonify({"result": "Error! Division by zero"}), 400
        result = num1 / num2
    else:
        return jsonify({"result": "Invalid operation"}), 400

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)