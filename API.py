# import main Flask class and request object
from flask import Flask, request
import requests
# create the Flask app
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/PredictProduct',methods=["Get"])
def query_example():
    image=request.args.get("image")
    resp=requests.post(f'https://detect.roboflow.com/final-k6z7a/1?api_key=wOakuvyV6yJhqFM3gXDs&image={image}')
    return resp.json()


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=False,port=5000, host='0.0.0.0')