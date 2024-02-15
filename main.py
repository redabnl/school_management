from flask import Flask 
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.run(debug=True)

if __name__ == '__main__':
    app.run()
