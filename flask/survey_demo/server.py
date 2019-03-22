from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "asdlf;kjasd;lkjfadas;lhs"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)