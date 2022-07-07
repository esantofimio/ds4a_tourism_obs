from dir import DirOpt
from urllib.request import urlopen
import json

dir_opt = DirOpt()
base_dir = dir_opt.get_base_data()

class HostingGeoData:
    def geo_data(self):
        with urlopen(
                'https://gist.githubusercontent.com/john-guerra/ee93225ca2c671b3550d62614f4978f3/raw/b1d556c39f3d7b6e495bf26b7fda815765ac110a/bogota_cadastral.json') as response:
            bogota = json.load(response)

        bogota_geo = []
        for neighborhood in bogota['features']:
            neigh_name = neighborhood['properties']['scanombre']
            geometry = neighborhood['geometry']
            bogota_geo.append({
                'type': 'Feature',
                'geometry': geometry,
                'id': neigh_name
            })
        bogota_geo_ok = {'type': 'FeatureCollection', 'features': bogota_geo}
        return bogota_geo_ok