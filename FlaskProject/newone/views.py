from flask import Blueprint
from newone.RegUser.views import regblue
from newone.calculator.views import calblue
from newone import app


app.register_blueprint(regblue)
app.register_blueprint(calblue)

if __name__ == "__main__":
    app.run(debug = True, port= 5002)


