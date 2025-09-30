from flask import Flask,render_template

app = Flask(__name__)

# This isn't a good practice since we need to write a lot of HTML code 
# create a seperate html page and we can redirect it to that page render_template() 
 
@app.route("/")
def welcome():
    return "<html><h1>Welcome to this flask course</h1></html>"

@app.route("/index")
def index():
    return render_template('index.html')
# render_template will use jinja 2 to look for templates folder and run that html file

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)