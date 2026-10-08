import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)

# Ensure the persistent instance folder exists
os.makedirs(app.instance_path, exist_ok=True)

# Point SQLite directly to the persistent instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    app.instance_path, 'tasks.db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(200), nullable=False)

  def to_dict(self):
    return {'id': self.id, 'title': self.title}


with app.app_context():
  db.create_all()


@app.route('/')
def home():
  return jsonify({
      'message': 'Cloud Task App is live',
      'status': 'online',
      'endpoints': {'GET /tasks': 'View all tasks', 'POST /tasks': 'Create a task'},
  })


@app.route('/tasks', methods=['GET'])
def get_tasks():
  tasks = Task.query.all()
  return jsonify([task.to_dict() for task in tasks])


@app.route('/tasks', methods=['POST'])
def create_task():
  data = request.get_json()
  if not data or 'title' not in data:
    return jsonify({'error': 'Missing title'}), 400
  new_task = Task(title=data['title'])
  db.session.add(new_task)
  db.session.commit()
  return jsonify({'id': new_task.id, 'message': 'Task created'}), 201


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
  
  
  import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
