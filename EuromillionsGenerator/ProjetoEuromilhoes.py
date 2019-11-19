
import random;


def GenerateRandomKey (numberOfElements, minValue, maxValue) :
    randomList = [];

    while len(randomList) <= numberOfElements-1 :

        randomElement = random.randint(minValue, maxValue);

        if randomElement in randomList :
            continue;

        randomList.append(randomElement);

    return randomList;



def getGameConfiguration (games, choosedGame) :
    for game in games :
        if game['gameId'] == choosedGame :
            return game;

    return {};


def LoadGameConfiguration () :
    gameConfiguration = [
            {
            'gameId':1,
            'game':'Euromillions',
            'gameNumbers' : 5,
            'gameNumberMinValue' : 1,
            'gameNumberMaxValue' : 50,
            'gameStars' : 2,
            'gameStarsMinValue' : 1,
            'gameStarsMaxValue' : 12        
            },
            {
            'gameId':2,
            'game':'Totoloto',
            'gameNumbers' : 5,
            'gameNumberMinValue' : 1,
            'gameNumberMaxValue' : 49,
            'gameStars' : 0,
            'gameStarsMinValue' : 0,
            'gameStarsMaxValue' : 0        
            }
        ];
    return gameConfiguration;










print('Welcome to Euromillions (and other games) generator.');


while True :

    gameConfiguration = {};
    randomKey = '';
    randomStarts = '';
    choosedGame = -1;

    games = LoadGameConfiguration();    
    
    print('Available Games:');
    for i in games :
        print(str(i['gameId']) + ' - ' + str(i['game']));

    while choosedGame < 0 :
        choosedGame = input("Choose the number of game, or press 0 to exit :");

        try :
            choosedGame = int(choosedGame);
        except :
            choosedGame = -1;
            continue;

        if choosedGame == 0 :
            continue;

        gameConfiguration = getGameConfiguration (games, choosedGame);

        if len(gameConfiguration) == 0 :
            choosedGame = -1;
            continue;
        
        
    if choosedGame == 0 :
        break;

    
    ## special trick :)
    superbPotencial = '';
    dummyNumber = random.randint(1,100);
    if dummyNumber >= 90 :
        superbPotencial = '(this key has great potencial... :) Good Luck!)';
        
    randomKeyList = GenerateRandomKey(gameConfiguration['gameNumbers'], gameConfiguration['gameNumberMinValue'], gameConfiguration['gameNumberMaxValue']);
    randomStartsList = GenerateRandomKey(gameConfiguration['gameStars'], gameConfiguration['gameStarsMinValue'], gameConfiguration['gameStarsMaxValue']);

    for i in randomKeyList :
        randomKey += ' ' + str(i) + ' ';
    for i in randomStartsList :
        randomStarts += ' ' + str(i) + ' ';

    print('*'*10);
    print('Generated key ' + superbPotencial);
    print(randomKey + '*' + randomStarts);
    print('*'*10);
    print('\n');
        
    


