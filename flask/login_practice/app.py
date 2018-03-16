#1. Import Flask
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#Create app variable
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kyra:ladies1271@localhost:5433/login_practice'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

#Index route
@app.route('/')
def index():
    users_list = User.query.all()
    return render_template('index.html', users=users_list)

@app.route('/profile/<email>')#displays certain stuff depending on email entered in
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
