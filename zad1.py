from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict')
def predict():
    a = request.args.get('a', default=0)
    b = request.args.get('b', default=0)

    try:
        a = float(a)
    except ValueError:
        a = 0

    try:
        b = float(b)
    except ValueError:
        b = 0   

    result = a + b
    prediction = 1 if result > 5.8 else 0

    response = {
        'prediction': prediction,
        'features': {
            'a': a,
            'b': b
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
