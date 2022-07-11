from fastapi import FastAPI
# import uvicorn
from fastapi.responses import HTMLResponse

app = FastAPI()

import save

glat, glon = save.getLat(), save.getLon()

@app.get("/")
def read_root():
    return {
        "lat":glat,
        "lon":glon
    }


def genloc(lat, lon):
    with open('main.html', 'r') as f:
        html_content = f.read()


#     html_content = """
#     <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
#      <link rel="stylesheet" href="https://unpkg.com/leaflet@1.8.0/dist/leaflet.css"
#    integrity="sha512-hoalWLoI8r4UszCkZ5kL8vayOGVae1oxXe/2A4AO6J9+580uKHDO3JdHb7NzwwzK5xr/Fs0W40kiNHxM9vyTtQ=="
#    crossorigin=""/>

#      <!-- Make sure you put this AFTER Leaflet's CSS -->
#  <script src="https://unpkg.com/leaflet@1.8.0/dist/leaflet.js"
#    integrity="sha512-BB3hKbKWOc9Ez/TAwyWxNXeoV9c1v6FIeYiBieIWkpLjauysF18NzgR1MBNBXf8/KABdlkX68nAhlwcDFLGPCQ=="
#    crossorigin=""></script>
# </head>
# <body>

#     <div class="map" id='map'></div>

# </body>

#     <style>
#         #map {
#             height: 100vh;
#         }
#     </style>
#     <script>

#         const lat = %s
#         const lon = %s

#         let map = document.getElementById("map");
#         console.log(map);
#         map = L.map('map').setView([lat, lon], 16);

#         L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
#     maxZoom: 19,
#     attribution: '© OpenStreetMap'
# }).addTo(map);

#         var circle = L.circle([26.032454, 88.469936], {
#     color: 'red',
#     fillColor: '#f03',
#     fillOpacity: 0.5,
#     radius: 30
# }).addTo(map);

#     </script>
# </html>
#     """.format(lat, lon)
    return HTMLResponse(content=html_content, status_code=200)

from pydantic import BaseModel



class Loc(BaseModel):
    lat:str
    lon:str
    



@app.post("/loc")
def read_item(loc:Loc):
    lat, lon = loc.lat, loc.lon
    save.changeLat(lat)
    save.changeLon(lon)
    print(lat)
    print(lon)
    return 200



# uvicorn.run(app, host="0.0.0.0", port="8080")
