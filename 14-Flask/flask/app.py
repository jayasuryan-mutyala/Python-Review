from flask import Flask 

app = Flask(__name__) # __name__ is the entry point

# creating a basic route, ex /home
# / indicates home page
@app.route(rule='/')
def welcome():
    return "Welcome to this page. This is the best website"

@app.route('/index')
def index():
    return "Welcome to the index page"
# entry point of py file 
# checks for this and execution will start
if __name__ == '__main__':
    app.run(debug=True) # the entire flask app runs
    # always put debug=True saves a lot of time 
