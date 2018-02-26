from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():
    name = "Jon Snow"
    return "Hello world! My name is " + name


if __name__ == '__main__':
    application.run()
