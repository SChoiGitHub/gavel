from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return "THIS IS NOT THE GAVEL YOU WANT TO GO TO."

app.run(
        host='0.0.0.0',
        port=8080
    )