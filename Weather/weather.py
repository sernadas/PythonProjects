
import requests;
import json;
import pprint;

r = requests.get('http://www.geoplugin.net/json.gp');

if (r.status_code != 200) :
    print('Unable to detect localization.');
else :    
    localization = json.loads(r.text);
    lat = localization['geoplugin_latitude'];
    long = localization['geoplugin_longitude'];
    ##print (pprint.pprint(localizacao));
    print ('lat=' + str(lat)+ ' long=' + str(long));
