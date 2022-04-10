import flask

flask_app = flask.Flask(__name__)

@flask_app.route('/')
def hello_world():
    return "Hello World!"

def main():
    flask_app.run(debug=True)

main()