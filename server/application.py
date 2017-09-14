from flask import Flask, render_template, request, jsonify # ,redirect, url_for ,jsonify ,flash, session


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    response = jsonify({'status': 'ok', 'message': 'Hello, world!'})
    response.status_code = 503
    return response

@app.route('/api/v1/<resource>', strict_slashes=False)
def api(resource):
    params = request.json
    try:
        return render_template('api/{}/response.json'.format(resource))
    except Exception as e:
        response = jsonify({'status': 'error', 'message': "'%s' not found in this server" % resource})
        response.status_code = 404
        return response

if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=80)
