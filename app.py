from flask import Flask, request, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["image"]
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

    images = os.listdir(UPLOAD_FOLDER)
    return render_template("index.html", images=images)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)