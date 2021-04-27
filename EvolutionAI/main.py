import random
from bechtest import BechTest

endpoint_list = list(open('files/clean-scripts.txt', 'r'))
results = open('files/results.csv', 'w')

random.shuffle(endpoint_list) #Randomize the list of movies.

#For the 500 first random results, we will create a new object and perform the isBechdel test, then save the results to
#the results.csv file.
for endpoint in endpoint_list[:500]:
    url = 'https://imsdb.com/scripts/' + endpoint.rstrip() + '.html'
    try:
        bech = BechTest(url)
        results.write(endpoint.rstrip() + ';' + str(bech.isBechdel()) + '\n')
    except:
        print("invalid-url or error-in-script")
    