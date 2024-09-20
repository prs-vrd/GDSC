from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for the panic disorder system
@app.route('/panic-system')
def panic_system():
    return jsonify({'message': 'Panic Disorder System API coming soon!'})

# Route for the mental health tracker
@app.route('/mental-tracker')
def mental_tracker():
    return jsonify({'message': 'Mental Health Tracker API coming soon!'})

# API endpoint to handle form submission (if required)
@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json  # Assume frontend sends JSON data
    print("Received data:", data)
    return jsonify({'status': 'success', 'data': data})

if __name__ == '__main__':
    app.run(debug=True)
