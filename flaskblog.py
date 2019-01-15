from flask import Flask, render_template
from forms import RegisterationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c9df772c99a87d2f806ffaf6f4c4ea4a'

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

@app.route('/register')
def register():
    form = RegisterationForm()
    return render_template('register.html',title='Register',form=form)

@app.route('/login')
def register():
    form = LoginForm()
    return render_template('login.html',title='Log In',form=form)

if __name__ == '__main__':
    app.run(debug=True)