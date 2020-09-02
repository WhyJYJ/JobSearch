from flask import Flask

app = Flask("SuperScrapper")

@app.route("/")
def home():
  return "Hello Welcome"

app.run(host = "0.0.0.0")