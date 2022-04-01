from flask_app import app
from flask_app.controllers import users
from flask_app.controllers import songs
from flask_app.controllers import composers
from flask_app.controllers import sources
from flask_app.controllers import albums
from flask_app.controllers import keywords
from flask_app.controllers import songs







if __name__ == '__main__':
    app.run(debug=True, port = 5001)