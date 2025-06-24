from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello asha from docker! 🎉'

@app.route('/about')
def about():
    return 'This is a sample Flask app running in Docker.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)