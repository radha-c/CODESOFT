from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

contacts = []  # Storing contacts in a list instead of a database

@app.route('/')
def index():
    return render_template('contact.html')

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    data = request.json
    contacts.append(data)
    return jsonify({"message": "Contact added!"})

@app.route('/delete/<int:index>', methods=['DELETE'])
def delete_contact(index):
    if 0 <= index < len(contacts):
        contacts.pop(index)
        return jsonify({"message": "Contact deleted!"})
    return jsonify({"error": "Invalid index"}), 400

@app.route('/update/<int:index>', methods=['PUT'])
def update_contact(index):
    if 0 <= index < len(contacts):
        contacts[index] = request.json
        return jsonify({"message": "Contact updated!"})
    return jsonify({"error": "Invalid index"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)