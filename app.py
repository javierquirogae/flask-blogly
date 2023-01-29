from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
print('connect_db')



@app.route('/')
def list_users():
    users = User.query.all()
    return render_template('list.html', users=users)


@app.route("/<int:user_id>")
def show_user(user_id):
    """Show details about a single pet"""
    user = User.query.get_or_404(user_id)
    return render_template("details.html", user=user)


@app.route('/form')
def show_form():
    return render_template('form.html')


@app.route('/form', methods=["POST"])
def create_user():
    first = request.form["first_name"]
    last = request.form["last_name"]
    url = request.form["image_url"]
   
    new_user  = User(first_name=first, last_name=last, image_url=url)
    db.session.add(new_user)
    db.session.commit()

    return redirect(f'/{new_user.id}')