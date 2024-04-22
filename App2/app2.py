from flask import Flask 

# Creating flask app
app = Flask(__name__)

# Define route for the root url 
@app.route('/')
def hello_world():
    return 'Hello from Application 2'

# Run the flask app if this file is executed 
if __name__ == '__main__':
    app.run(debug=True, port=8081, host='0.0.0.0')