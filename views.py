from flask import *
from config import SECRET_KEY
from database import conn

app = Flask(__name__)

app.secret_key = SECRET_KEY

@app.route("/")
def index():
    user = session.get('user')
    return render_template('index.html', username=user)



@app.route("/connect", methods= ['POST', 'GET'])
def connect():
    if request.method == 'POST':
      email = request.form['loginEmail']  
      password = request.form['loginPassword']
      try:
        cursor = conn.cursor()
        cursor.execute('SELECT login FROM User WHERE email=? AND password=?', (email, password))
        user = cursor.fetchall()
        cursor.close()
        if len(user) == 1:
            session['user'] = user[0][0]
            flash(f"Heureux de vous revoir {session['user']}", "validate")
            return redirect(url_for('index'))
        else:
            flash("Votre utilisateur n'existe pas", "error")
            return redirect(url_for('login'))
      except Exception as error:
          print(error)
          flash("Une erreur est survenue", "error")
          return redirect(url_for('login'))
    else:
        return redirect(url_for('index'))
        



@app.route("/out")
def out():
    session.clear()
    return redirect(url_for('index'))



@app.route("/login")
def login():
    return render_template('login.html')



@app.route("/create_account", methods = ['POST', 'GET'])
def create_account():
    if request.method == 'POST':
        email = request.form['registerEmail']
        login = request.form['registerName']
        password = request.form['registerPassword']
        try:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO User (login, email, password) VALUES (?, ?, ?)', (login, email, password))
            conn.commit()
            cursor.close()
            session['user'] = login
            flash("Votre compte a bien été créé", 'validate')
            return redirect(url_for('index'))
        except Exception as error:
            print(error)
            flash("Une erreur est survenue", 'error')
            return redirect(url_for('login'))
    else:
        return redirect(url_for('index'))