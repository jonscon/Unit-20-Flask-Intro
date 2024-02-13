from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_nums():
    """Add a and b."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a, b)
    return str(result)

@app.route('/sub')
def sub_nums():
    """Subtract a and b."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def mult_nums():
    """Multiply a and b."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a, b)
    return str(result)

@app.route('/div')
def div_nums():
    """Divide a and b."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a, b)
    return str(result)

# Further Study

OPERATIONS = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<operation>')
def do_operation(operation):
    """Depending on the URL parameter, return the result of the operation on a and b."""
    
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = OPERATIONS.get(operation, "No operation found")(a,b)
    return str(result)