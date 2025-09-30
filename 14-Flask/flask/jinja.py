# Building the url dynamically 
# variable rule 
# jinja2 template engine 

'''
Jinja template engine has multiple ways to read data source from python in html. We have 3 ways:
{{ }} expressions to print output in html 
{%..%} conditions, for loops 
{#..#} comments

'''

from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html><h1>Welcome to this flask course</h1></html>"

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.csv')

@app.route('/form',methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET',"POST"])
def form():
    if request.method == "POST":
        name = request.form['name']
        return f"Hello {name}"
    return render_template('form.html')

# score is just some value 
# variable rule: we can only pass strings through the success/5000
# typecast to str if its int or float
# if we return html page, pass another called results 
# to take the input value we use jinja template in html page {{}}
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',results=res)


# Variable rule 
@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score >= 50:
        res="PASSED"
    else:
        res="FAILED"

    exp = {'score':score,'res':res}
    return render_template('result1.html',results=exp)

# if condition
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)

# dynamic url 
@app.route('/submit',methods=['GET',"POST"])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))



if __name__ == '__main__':
    app.run(debug=True)