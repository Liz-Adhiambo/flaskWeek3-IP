from flask import Flask, render_template, url_for
from config import SECRET_KEY
from forms import RegistrationForm,LoginForm
app = Flask(__name__)


app.config['SECRET_KEY']='SECRET_KEY'

posts = [
    {
        'author': 'Liz lizzy',
        'title': ' Post 1',
        'content': 'First post content',
        'date_posted': 'May 20, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': ' Post 2',
        'content': 'Second post content',
        'date_posted': 'May 21, 2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
  
    return render_template('login.html', title='Login', form=form)





if __name__ == '__main__':
    app.run(debug=True)