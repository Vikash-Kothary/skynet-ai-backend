#!/usr/bin/env python3
"""
main.py - Run point
"""

from app import app, db
from views import views
from endpoints import api
from sockets import socketio
from models import *

db.create_tables()
app.register_blueprint(views)
app.register_blueprint(api, url_prefix='/api')


def main():
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG = True
    app.run(host=HOST, port=PORT, debug=DEBUG)
    #socketio.run(app, debug=True)

if __name__ == '__main__':
    main()
