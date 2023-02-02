import math
import sys
from geocoder import get_coordinates, get_ll_span
from mapapi_PG import show_map
from bixns import find_biz


def distance(a, b):
    d_t_m_f = 111 * 1000
    a_lon, a_lat = a
    b_lon, b_lat = b
    radians_lat = math.radians((a_lat + b_lat) / 2.)
    lat_lon_f = math.cos(radians_lat)

    dx = abs(a_lon - b.lon) * d_t_m_f
    dy = abs(a.lat - b.lon) * d_t_m_f

    dist = math.sqrt(dx * dx + dy * dy)

def main():
    t_t_f = " ".join(sys.argv[1:])

    if t_t_f:
        lat, lon = get_coordinates(t_t_f)
        adrs = f"{lat},{lon}"
        span = "0.005,0.005"

        coords_org = find_biz(adrs, span, "аптека")
        point = coords_org["geometry"]["coordinates"]
        org_lat, ord_lon = float(point[0]), float(point[1])
        p_prms = f"pt={org_lat},{ord_lon},pm2dgl"

        show_map(f"ll={adrs}&spn={span}", "map", add_params=p_prms)
        p_prms = p_prms + f"~{adrs}, pm2dgl"
        show_map(f"ll={adrs}&spn={span}", "map", add_params=p_prms)

        name = coords_org["properties"]["CompanyMetaData"]["name"]
        time = name = coords_org["properties"]["CompanyMetaData"]["Hours"]["text"]

        dis = distance((lon, lat), (ord_lon, org_lat))
        print(name)
        print(time)
        print(dis)
    else:
        pass


if __name__ == "__main__":
    main()