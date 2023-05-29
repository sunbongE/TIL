from flask import Flask, g

app = Flask(__name__)
app.debug = True


@app.before_request
def before_request():
    print("before_request!!!")
    g.str = "한글"


@app.route("/gg")
def helloword2():
    return "hello word!" + getattr(g, "str", "111")


@app.route("/")
def helloword():
    return "hello Flask word!!!!!!!!!!!!"
