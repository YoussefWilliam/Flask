from flask import Flask, render_template
app = Flask(__name__)

students= [
    {
        'name':'Youssef maged william',
        'age':'21 years old',
        'major':'Engineering'
    },
    {
        'name':'Mariam maged william',
        'age':'19 years old',
        'major':'Dentistry'
    },
    {
        'name':'Nardeen Ashraf',
        'age':'23 years old',
        'major':'Pharmacist'
    }

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',students=students)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

if __name__ == '__main__':
    app.run(debug=True)