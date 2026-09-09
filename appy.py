from flask import Flask, request
import requests
import os

app = Flask(__name__)

WHATSAPP_TOKEN = "PASTE_YOUR_WHATSAPP_TOKEN_HERE"
PHONE_NUMBER_ID = "PASTE_YOUR_PHONE_NUMBER_ID_HERE"
VERIFY_TOKEN = "cif_bot_verify"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Verification failed", 403

    if request.method == "POST":
        data = request.get_json()
        print(data)
        return "OK", 200

@app.route("/")
def home():
    return "CIF Bot is Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
