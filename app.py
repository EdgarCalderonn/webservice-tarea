from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///databases/database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.secret_key = 'mysecretkey'

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/v1/users")
def api_users():
    data = db.engine.execute("SELECT * FROM users")
    return jsonify({ 'usuarios ': [dict(row) for row in data]})

@app.route("/users/list")
def lista_users():
    resultado = db.engine.execute("SELECT * FROM users")
    return render_template('users.html', datos=resultado)



if __name__ == "__main__":
    app.run(debug=True)