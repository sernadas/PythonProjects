
import requests;
import json;
import pprint;

accuweatherAPIKey = 'pdH1tnZNWdwFTFdrxCEd6O37UKdH0JvC';


r = requests.get('http://www.geoplugin.net/json.gp');

if (r.status_code != 200) :
    print('Unable to detect localization.');
else :    
    location = json.loads(r.text);
    lat = location['geoplugin_latitude'];
    long = location['geoplugin_longitude'];
    ##print (pprint.pprint(localizacao));
    ##print ('lat=' + str(lat)+ ' long=' + str(long));

    localizationAPIUrl = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=' + accuweatherAPIKey + '&q=' + str(lat) + '%2C' + str(long) + '&language=pt-pt';
    r2 = requests.get(localizationAPIUrl);
    accuweatherLocation = json.loads(r2.text);

    if (r2.status_code != 200) :
        print('Unable to detect location code ');
    else :
        localName = accuweatherLocation['LocalizedName'] + ', ' \
                    + accuweatherLocation['AdministrativeArea']['LocalizedName'] + '. ' \
                    + accuweatherLocation['Country']['LocalizedName'] ;

        localCode = accuweatherLocation['Key'];
        #print(pprint.pprint(accuweatherLocation));
        #print('localCode: ' + localCode);

        print('Get weather from ' + localName);



        currentConditionsAPIUrl = 'http://dataservice.accuweather.com/currentconditions/v1/' + localCode + '?apikey=' + accuweatherAPIKey + '&language=pt-pt';
        r3 = requests.get(currentConditionsAPIUrl);
        if (r3.status_code != 200) :
            print('Unable to detect current conditions ');
        else :
            accuweatherCurrentConditions = json.loads(r3.text);
            #print(pprint.pprint(accuweatherCurrentConditions));
            conditionsTemperature = accuweatherCurrentConditions[0]['Temperature']['Metric']['Value'];
            conditionsText = accuweatherCurrentConditions[0]['WeatherText'];
            
            print('Current conditions : ' + conditionsText);
            print('Temperature : ' + str(conditionsTemperature) + ' degrees');
        
        
    
