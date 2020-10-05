from flask import Flask, request, render_template
import time
app = Flask(__name__)

@app.route('/left.txt')
def left():
        return render_template('left.txt')

@app.route('/right.txt')
def right():
        return render_template('right.txt')
    
@app.route('/motiondetection.txt')
def motion():
        return render_template('motiondetection.txt')

@app.route('/', methods=['GET'])
def index():
    return render_template('park.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')