from flask import Blueprint, jsonify, render_template, request

main = Blueprint("main", __name__)

tasks = [
    {"id": 1, "title": "Learn Python", "completed": False},
    {"id": 2, "title": "Learn GitHub Actions", "completed": False},
]


@main.route("/")
def home():
    return render_template("index.html", tasks=tasks)


@main.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@main.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200


@main.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title", "").strip()

    if not title:
        return jsonify({"error": "Task title is required"}), 400

    task = {
        "id": max((item["id"] for item in tasks), default=0) + 1,
        "title": title,
        "completed": False,
    }

    tasks.append(task)

    return jsonify(task), 201


@main.route("/api/tasks/<int:task_id>", methods=["PATCH"])
def update_task(task_id):
    task = next((item for item in tasks if item["id"] == task_id), None)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json(silent=True) or {}

    if "completed" in data:
        if not isinstance(data["completed"], bool):
            return jsonify({"error": "completed must be true or false"}), 400
        task["completed"] = data["completed"]

    return jsonify(task), 200