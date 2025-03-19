from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/about')
def about():
    return "This is the About Page."

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')  # Get parameter from URL
    return f"Hello, {name}!"

@app.route('/submit', methods=['POST'])
def submit():
    if not request.json:
        return jsonify({"error": "Missing JSON data"}), 400  # Handle missing JSON
    name = request.json.get('name', 'Unknown')
    return jsonify({"message": f"Received data for {name}"}), 201

@app.route('/update', methods=['PUT'])
def update():
    if not request.json:
        return jsonify({"error": "Missing JSON data"}), 400
    name = request.json.get('name', 'Unknown')
    new_data = request.json.get('new_data', 'No new data provided')
    return jsonify({"message": f"Updated {name} with {new_data}"}), 200

@app.route('/delete/<name>', methods=['DELETE'])
def delete(name):
    return jsonify({"message": f"Deleted user {name}"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=8500)
