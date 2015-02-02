"""
Donorchoose Flask web application

"""
# ============================================================================
# make necessary imports
# ============================================================================
from flask import Flask
from flask.ext.pymongo import PyMongo

from donorchoose.helpers import random_string

# ============================================================================
# initialize flask web app
# ============================================================================
app = Flask(__name__)
app.secret_key = random_string()

# ============================================================================
# load application configs from settings file
# ============================================================================
app.config.from_object('donorchoose.settings')

# ============================================================================
# setup MongoDB for flask web app
# ============================================================================
mongo = PyMongo(app)

# ============================================================================
# import flask web app views
# ============================================================================
import donorchoose.views
