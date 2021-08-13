from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import tweepy
import json
import vonage
import tweepy
import numpy as np
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

client = vonage.Client(key='00a5bc5e', secret='0lny1LEZdnFLizB6')
sms = vonage.Sms(client)

consumer_key = 'UBZOig3uDrBd6knolYnkwr47W'
consumer_secret = 'vEeILI52bctFerou0kmHH9Aza6GKGB2gf59NqFYtk2fXOHsxZU'
access_token = '1302468297904893954-GuRtnmkSulQCx5R6Y0ObYfxQzKTmXC'
access_token_secret = '4mUHCldDrMLYZUpBBd07j9Ic5xvX7g8o46Q4k5rGCHVGo'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)

from flaskblog import routes