from flask import Flask, render_template, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests

app = Flask(__name__)

FACT_API = "https://catfact.ninja/fact"
DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"
DEEPL_API_KEY = "00cc8aa6-9e70-4807-8812-3ddf73c95c35:fx"
uri = "mongodb+srv://alexandra23paraschiv_db_user:DuHnQoT1lQ0ouJFh@cluster0.3vjoril.mongodb.net/"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.catfacts_db
facts_collection = db.facts

@app.route("/", methods=["GET", "POST"])
def index():
    cat_fact_en = None
    cat_fact_ro = None

    if request.method == "POST":
        # Get cat fact
        fact_response = requests.get(FACT_API, timeout=5).json()
        cat_fact_en = fact_response.get("fact")

        # Translate the fact to Romanian
        try:
            data = {
                "auth_key": DEEPL_API_KEY,
                "text": cat_fact_en,
                "target_lang": "RO"
            }
            translate_response = requests.post(DEEPL_API_URL, data=data, timeout=10).json()
            cat_fact_ro = translate_response["translations"][0]["text"]
            facts_collection.insert_one({
                "english": cat_fact_en,
                "romanian": cat_fact_ro
            })
        except Exception as e:
            print("Translation error:", e)
            cat_fact_ro = "(Translation failed)"

    return render_template("index.html", cat_fact_en=cat_fact_en, cat_fact_ro=cat_fact_ro)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
