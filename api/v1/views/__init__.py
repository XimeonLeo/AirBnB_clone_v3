#!/usr/bin/python3
""" Handles all default RESTful API action
"""

<<<<<<< HEAD
from api.v1.views.index import *
=======
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


>>>>>>> 56df7d48c02a66027f70bfbf2f10989956792120
from api.v1.views.amenities import *
from api.v1.views.cities import *
from api.v1.views.states import *
from api.v1.views.amenities import *
from api.v1.views.users import *
<<<<<<< HEAD
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
=======
from api.v1.views.places import *
from api.v1.views.index import *
>>>>>>> 56df7d48c02a66027f70bfbf2f10989956792120
