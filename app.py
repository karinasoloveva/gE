from flask import Flask, request, jsonify, render_template # type: ignore

app = Flask(__name__)

users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def location():
    data = request.get_json()
    name = data.get('name')
    lat = data.get('lat')
    lon = data.get('lon')
    if not name or lat is None or lon is None:
        return jsonify({'error': 'Invalid data'}), 400
    users[name] = {'lat': lat, 'lon': lon}
    return jsonify({'status': 'ok'})

@app.route('/users')
def get_users():
    # Возвращаем список всех пользователей и их координат
    return jsonify([
        {'name': name, 'lat': info['lat'], 'lon': info['lon']}
        for name, info in users.items()
    ])

if __name__ == '__main__':
    app.run(debug=True)
