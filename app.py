from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates')  # Set the templates folder for HTML

def evaluate_password_strength(password):
    """Evaluates the strength of a password."""
    strength = "Weak"
    length_criteria = len(password) >= 8
    digit_criteria = any(char.isdigit() for char in password)
    uppercase_criteria = any(char.isupper() for char in password)
    special_criteria = any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password)

    # Determine password strength
    if length_criteria and digit_criteria and uppercase_criteria and special_criteria:
        strength = "Strong"
    elif length_criteria and (digit_criteria or uppercase_criteria or special_criteria):
        strength = "Moderate"

    return strength

@app.route('/')
def home():
    """Serve the HTML page."""
    return render_template('index.html')  # Renders the frontend file

@app.route('/check_password', methods=['POST'])
def check_password():
    """API endpoint to check password strength."""
    data = request.get_json()
    password = data.get('password', '')

    if not password:
        return jsonify({'error': 'Password cannot be empty'}), 400

    strength = evaluate_password_strength(password)
    return jsonify({'strength': strength})

if __name__ == '__main__':
    app.run(debug=True)
