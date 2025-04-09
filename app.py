from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/slack", methods=["POST"])
def slack_command():
    text = request.form.get("text")

    # Handle Slack text
    if "open chrome" in text.lower():
        subprocess.run(["adb", "shell", "am start -a android.intent.action.VIEW -d https://www.google.com"])
        return jsonify({"text": "📱 Chrome opened on Android Emulator!"})

    return jsonify({"text": f"⚠️ Unknown command: {text}"})

import os
port = int(os.environ.get("PORT", 5000))  # Render provides the PORT env variable
app.run(host="0.0.0.0", port=port)

