from flask import Flask, render_template_string # type: ignore

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <title>Геолокация с Flask и Leaflet</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css"/>
  <style>#map { height: 400px; width: 100%; }</style>
</head>
<body>
  <h2>Моё местоположение</h2>
  <div id="map"></div>

  <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js"></script>
  <script>
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;

        const map = L.map('map').setView([lat, lon], 13);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 19,
        }).addTo(map);

        L.marker([lat, lon]).addTo(map)
          .bindPopup('Вы здесь')
          .openPopup();
      }, function(error) {
        alert('Ошибка получения геолокации: ' + error.message);
      });
    } else {
      alert('Геолокация не поддерживается вашим браузером');
    }
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
