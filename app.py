from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('user_input', '')
    message = f"You entered: {user_input}"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
