from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email, "created_at": self.created_at.isoformat()}

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/students", methods=["GET"])
def list_students():
    students = Student.query.all()
    return jsonify([s.to_dict() for s in students]), 200

@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    s = Student.query.get_or_404(id)
    return jsonify(s.to_dict()), 200

@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json() or {}
    name = data.get("name")
    email = data.get("email")
    if not name or not email:
        return jsonify({"error":"name and email required"}), 400
    if Student.query.filter_by(email=email).first():
        return jsonify({"error":"email exists"}), 400
    s = Student(name=name, email=email)
    db.session.add(s)
    db.session.commit()
    return jsonify(s.to_dict()), 201

@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    s = Student.query.get_or_404(id)
    data = request.get_json() or {}
    s.name = data.get("name", s.name)
    s.email = data.get("email", s.email)
    db.session.commit()
    return jsonify(s.to_dict()), 200

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    s = Student.query.get_or_404(id)
    db.session.delete(s)
    db.session.commit()
    return jsonify({"result":"deleted"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)