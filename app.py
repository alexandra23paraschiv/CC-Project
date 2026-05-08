import os
from flask import Flask, render_template, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests

app = Flask(__name__)

FACT_API = "https://catfact.ninja/fact"
TRANSLATE_API = "https://api.mymemory.translated.net/get"

uri = "mongodb+srv://alexandra23paraschiv_db_user:DuHnQoT1lQ0ouJFh@cluster0.3vjoril.mongodb.net/"
client = MongoClient(uri, server_api=ServerApi("1"))
db = client.catfacts_db
facts_collection = db.facts

@app.route("/", methods=["GET", "POST"])
def index():
    cat_fact_en = None
    cat_fact_ro = None

    if request.method == "POST":
        fact_response = requests.get(FACT_API, timeout=5).json()
        cat_fact_en = fact_response.get("fact")

        try:
            params = {
                "q": cat_fact_en,
                "langpair": "en|ro"
            }
            translate_response = requests.get(
                TRANSLATE_API,
                params=params,
                timeout=10
            )
            translate_response.raise_for_status()

            translate_json = translate_response.json()
            cat_fact_ro = translate_json.get("responseData", {}).get("translatedText")

            if not cat_fact_ro:
                raise ValueError(f"Invalid translation response: {translate_json}")

            facts_collection.insert_one({
                "english": cat_fact_en,
                "romanian": cat_fact_ro
            })
        except Exception as e:
            print("Translation error:", type(e).__name__, e)
            if "translate_response" in locals():
                print("Translate status:", translate_response.status_code)
                print("Translate body:", translate_response.text)
            cat_fact_ro = "(Translation failed)"

    return render_template("index.html", cat_fact_en=cat_fact_en, cat_fact_ro=cat_fact_ro)

if __name__ == "__main__":
    app.run(debug=True)