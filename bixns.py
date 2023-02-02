import  requests

def find_bixns(ll, spn, request, local="ru_Ru"):
    s_a_s = "https://search-maps.yandex.ru/v1/"
    api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
    s_prms = {"apikey": api_key,
    "text": request,
    "lang": local,
    "ll": ll,
    "spn": spn,
    "type": "biz"}

    response = requests.get(s_a_s, params=s_prms)
    if not response:
        raise RuntimeError(f"lllllllllll")
    json_response = response.json()
    org = json_response["features"]
    return org

def find_biz(ll, spn, request, local="ru_Ru"):
    org = find_bixns(ll, spn, request, local)
    if len(org):
        return org[0]