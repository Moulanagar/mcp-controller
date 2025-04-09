from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Flask server is running on Render!"

@app.route("/slack", methods=["POST"])
def slack_command():
    text = request.form.get("text")

    if "open chrome" in text.lower():
        subprocess.run([
            "adb", "shell", "am", "start", 
            "-a", "android.intent.action.VIEW", 
            "-d", "https://www.google.com"
        ])
        return jsonify({"text": "📱 Chrome opened on Android Emulator!"})

    return jsonify({"text": f"⚠️ Unknown command: {text}"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
