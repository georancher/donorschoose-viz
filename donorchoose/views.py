"""
Flask web application views

"""
# ============================================================================
# necessary imports
# ============================================================================
import json

from flask import render_template
from bson import json_util

from donorchoose import app, mongo

# ============================================================================
# required database fields constant
# ============================================================================
FIELDS = {'school_state': True, 'resource_type': True, 'poverty_level': True,
          'date_posted': True, 'total_donations': True, '_id': False}


# ============================================================================
# Flask web application views
# ============================================================================
@app.route("/")
def index():
    """Index page """
    return render_template("index.html")


@app.route("/donorschoose/projects")
def donorschoose_projects():
    """Projects data endpoint """
    projects = [proj for proj in mongo.db.projects.find(fields=FIELDS)]

    projects_json = json.dumps(projects, default=json_util.default)

    return projects_json
# ============================================================================
# EOF
# ============================================================================
