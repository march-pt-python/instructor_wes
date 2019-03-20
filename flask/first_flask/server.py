from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    first_names = ["Wes", "Nathan", "Monica", "Preston", "Jay", "Big Ron"]
    return render_template('index.html', users=first_names)

@app.route('/display_color/<color>')
def display_color(color):
    print(color)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)