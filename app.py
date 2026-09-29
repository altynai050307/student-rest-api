from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "Altynai",
        "group": "IS-701"
    },
    {
        "id": 2,
        "name": "Akbota",
        "group": "IS-702"
    },
    {
        "id": 3,
        "name": "Mariya",
        "group": "IS-701"
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "Student REST API is running"
    })


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = next(
        (student for student in students if student["id"] == student_id),
        None
    )

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student)


@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()

    if not data or "name" not in data or "group" not in data:
        return jsonify({
            "error": "name and group are required"
        }), 400

    new_id = max([student["id"] for student in students], default=0) + 1

    student = {
        "id": new_id,
        "name": data["name"],
        "group": data["group"]
    }

    students.append(student)

    return jsonify(student), 201


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    student = next(
        (student for student in students if student["id"] == student_id),
        None
    )

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    students.remove(student)

    return jsonify({
        "message": "Student deleted successfully"
    })


if __name__ == "__main__":
    app.run(debug=True)