from flask import Flask, render_template
from flask_pymongo import PyMongo
import Challenge

app = Flask(__name__)
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
#Set Up App Routes
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("challenge.html", mars=mars)

#route for scraper:
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = Challenge.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return "Scraping Successful!"

if __name__ == "__main__":
   app.run()



