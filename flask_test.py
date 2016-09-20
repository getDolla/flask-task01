#Yikai Wang
#Period 6 SoftDev

from flask import Flask

app = Flask(__name__)

@app.route("/")
def sup():
    return "Wassup homie?"

@app.route( "/name" )
def myName():
    return "Hello, " +  __name__ + "!"

@app.route( "/404" )
def notFound():
    return "Page not found. (Which is ironic.)"

if __name__ == "__main__":
    app.run()
