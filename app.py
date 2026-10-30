from flask import Flask, request
from engine import process_task


app = Flask(__name__)

@app.route("/")
def health():
    return {
        "status": "running"
    }

@app.route("/process-task", methods=["POST"])

def process():

    payload = request.get_json()
    print(payload)
    task_id = payload.get("newState", {}).get("ID")

    if not task_id:
        return {
            "success": False,
            "error": "taskID is required"
        }, 400

    try:
        return process_task(task_id)
    except Exception as e:
        return {
            "success" : False,
            "error": str(e)
        }


if __name__ == "__main__":
    app.run()