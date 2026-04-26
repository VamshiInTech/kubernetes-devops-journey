from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

FILE = os.getenv("FILE_PATH", "/data/notes.txt")
PASSWORD = os.getenv("APP_PASSWORD")

HTML = """
<h2>📝 Vamshi Notes App - CD  v1</h2>

<form method="POST">
    <textarea name="note" rows="10" cols="50">{{ note }}</textarea><br><br>
    
    Password: <input type="password" name="password"><br><br>
    
    <button type="submit">Save</button>
</form>

<p style="color:red;">{{ message }}</p>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        # 🔥 simulate CPU load ONLY on POST (for HPA testing)
        for _ in range(30000000):
            pass

        note = request.form["note"]
        user_pass = request.form["password"]

        if user_pass.strip() == PASSWORD.strip():
            with open(FILE, "w") as f:
                f.write(note)
            message = "Saved successfully ✅"
        else:
            message = "Wrong password ❌"

    try:
        with open(FILE, "r") as f:
            note = f.read()
    except:
        note = ""

    return render_template_string(HTML, note=note, message=message)


# ✅ IMPORTANT: This keeps the Flask app running
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# ❌ OLD TEST CODE (kept for reference — DO NOT USE)
# This caused CrashLoopBackOff / Completed state earlier

# import time
#
# @app.route("/", methods=["GET", "POST"])
# def home():
#     # simulate CPU work
#     for _ in range(10000000):
#         pass
