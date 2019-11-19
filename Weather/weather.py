
import requests;
import json;
#import pprint;

accuweatherAPIKey = 'pdH1tnZNWdwFTFdrxCEd6O37UKdH0JvC';


def getCoordinates () :
    r = requests.get('http://www.geoplugin.net/json.gp');

    if (r.status_code != 200) :
        print('Unable to detect localization.');
        
    else :    
        location = json.loads(r.text);
        coordinates = {};
        coordinates['lat'] = location['geoplugin_latitude'];
        coordinates['long'] = location['geoplugin_longitude'];
        return coordinates;



def getLocalCode(latitude, longitude) :
    localizationAPIUrl = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=' + accuweatherAPIKey \
                         + '&q=' + str(latitude) + '%2C' + str(longitude) + '&language=pt-pt';
    r = requests.get(localizationAPIUrl);
    if (r.status_code != 200) :
        print('Unable to detect location code ');
    else :
        accuweatherLocation = json.loads(r.text);
        infoLocal = {};    
        infoLocal['localName'] = accuweatherLocation['LocalizedName'] + ', ' \
                    + accuweatherLocation['AdministrativeArea']['LocalizedName'] + '. ' \
                    + accuweatherLocation['Country']['LocalizedName'] ;

        infoLocal['localCode'] = accuweatherLocation['Key'];

        return infoLocal;



def getCurrentCondition(localCode, localName) :
    currentConditionsAPIUrl = 'http://dataservice.accuweather.com/currentconditions/v1/' + localCode \
                              + '?apikey=' + accuweatherAPIKey + '&language=pt-pt';
    r = requests.get(currentConditionsAPIUrl);
    if (r.status_code != 200) :
        print('Unable to detect current conditions ');
    else :
        accuweatherCurrentConditions = json.loads(r.text);
        infoWeather = {};
        #print(pprint.pprint(accuweatherCurrentConditions));
        infoWeather['temperature'] = accuweatherCurrentConditions[0]['Temperature']['Metric']['Value'];
        infoWeather['conditionsText'] = accuweatherCurrentConditions[0]['WeatherText'];
        infoWeather['localName'] = localName;

        return infoWeather;
        


# Program start

coordinates = getCoordinates();
infoLocal = getLocalCode(coordinates['lat'], coordinates['long']);
infoWeather = getCurrentCondition(infoLocal['localCode'], infoLocal['localName']);


print('Get weather from ' + infoWeather['localName']);
print('Current conditions : ' + infoWeather['conditionsText']);
print('Temperature : ' + str(infoWeather['temperature']) + '\xb0' + 'C');
        
        
    







