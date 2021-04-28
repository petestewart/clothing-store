from flask import Flask
from flask_restful import Api

from api.routes import create_routes

# initialize Flask app (later this would be modded to include database config)
app = Flask(__name__)

# initialize api and routes
api = Api(app)
create_routes(api=api)

# main entry point
if __name__ == '__main__':
    app.run(debug=True)