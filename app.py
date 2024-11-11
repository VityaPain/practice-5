from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/counter_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Counter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)
    client_info = db.Column(db.String, nullable=False)

    def as_dict(self):
        return {"id": self.id, "datetime": self.datetime, "client_info": self.client_info}

# Создание таблицы
with app.app_context():
    db.create_all()

@app.route("/")
def hello():
    client_info = request.headers.get('User-Agent')
    entry = Counter(client_info=client_info)
    db.session.add(entry)
    db.session.commit()
    entries = Counter.query.all()
    return jsonify([entry.as_dict() for entry in entries]), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
