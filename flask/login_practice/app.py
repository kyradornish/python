#1. Import Flask
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required

#Create app variable
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kyra:ladies1271@localhost:5433/login_practice'
app.config['SECRET_KEY'] = 'super-secret' #want to move this somewhere else corss-sit forgery
app.config['SECURITY_REGISTERABLE'] = True #use default forms with flask-security
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_PASSWORD_SALT'] = b"xxx" #randomizes hash
db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

# Define models
roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(),db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create a user to test with
# RUN ONCE AND ONLY ONCE - AFTEWARD COMMENT OUT
# @app.before_first_request
# def create_user():
#     db.create_all()
#     user_datastore.create_user(email='derek@codingtemple.com', password='test')
#     db.session.commit()

#Index route
@app.route('/')
def index():
    users_list = User.query.all()
    return render_template('index.html', users=users_list)

@app.route('/profile/<email>')#displays certain stuff depending on email entered in
@login_required #route to profile after login
def profile(email):#need to pass email to route
    user = User.query.filter_by(email=email).first()
    return render_template('profile.html', user=user)

#User POST route
@app.route('/user', methods=['POST'])
def user():
    user = User(username=request.form['username'], email=request.form['email']) #Get name from form name in HTML
    db.session.add(user) #addig to db
    db.session.commit() #saving to db
    return redirect(url_for('index'))

#Start local hosting port
#If app.py is run from terminal, will start the server. If ran from import, it won't run
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8989, debug=True)
