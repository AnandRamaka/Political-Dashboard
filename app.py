from flask import Flask, request, render_template
from flask.templating import render_template_string
from tweepy import debug 
from tweet_nlp import get_tweets, tweet_list
from flask_bootstrap import Bootstrap
import random

# Flask constructor
app = Flask(__name__)   
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
      names = ["Bernie Sanders", "AOC", "Joe Biden", "Mitch McConnell", "Ted Cruz", "Donald Trump"]
      tweets = tweet_list(names)
      to_display = []
      for data in tweets:
         to_display.append( random.sample(data[0], 8) )
      
      pics = ["bernie.jpg", "AOC.jpg", "joebiden.jpg", "mitch.jpg", "Cruz.jpg", "trump.jpg"]
      return render_template("dashboard.html", tweets=tweets, pics=pics, names=names, display=to_display)
  
if __name__=='__main__':
   app.run(debug=True)
