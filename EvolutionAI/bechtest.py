import requests
from bs4 import BeautifulSoup

class BechTest():
    
    """
    bech = BechTest(URL)
    
    This class' constructor receives a valid URL from http://imsb.com, gets the html response and saves it in the "script" 
    parameter.
    
    bech.script => returns the script without the thick of the html noise.
    bech.blines => returns the lines that are bold, refering to character names, camera transitions and scene titles.
    
    isBechdel() parses the script to see if if passes the Bechdel test: is there a scene within the script that features 
    two women wich have names and lines. returns True, False or "Error"
    """
    
    def __init__(self, URL):
        self.f_names = []
        for name in open('files/female.txt', 'r'):
            self.f_names.append(name.rstrip())
        
        print(URL)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        results = soup.find('td', class_='scrtext').prettify()
        results = results.replace('</b>', '').replace('<pre>', '').split('\n')[1:] #Delete the noise from the first line.
        self.script = results[:-1] #Delete the noise from the last line.
        
        self.blines = []
        for line in self.script:
            if line.startswith('<b>'):
                self.blines.append(line.replace('<b>', '').lstrip())
        
    def isBechdel(self):
        n_scene = True  #Go to next scene
        parser = iter(self.blines)
        if len(self.blines) < 10:
            raise Exception("Invalid Script")
        curr = next(parser).capitalize().rstrip()
        fs_in_scene = set()
    
        try:
            while True:
                #print("Evaluating: %s, next scene: %s" % (curr, n_scene)) 
                if n_scene:
                    while True:
                        if curr in self.f_names:
                            n_scene = False
                            break
                        #print("Evaluating: %s, next scene: %s" % (curr, n_scene)) 
                        curr = next(parser).capitalize().rstrip()
                    continue
                
                else:
                    if curr in self.f_names:
                        fs_in_scene.add(curr.rstrip())
                        if len(fs_in_scene) > 1:
                            return True         
                    else:
                        n_scene = True
                            
                curr = next(parser).capitalize().rstrip()
                
        except StopIteration:
            return False  
    

if __name__ == '__main__':
    url_list = ['https://imsdb.com/scripts/Independence-Day.html',
            'https://imsdb.com/scripts/Thor-Ragnarok.html',
            'https://imsdb.com/scripts/Megamind.html']


    bech = BechTest(url_list[0])
    print(bech.isBechdel())
    
    """
    results = {}

    bech0 = BechTest(url_list[0])
    results[url_list[0]] = bech0.isBechdel()
    bech1 = BechTest(url_list[1])
    results[url_list[1]] = bech1.isBechdel()
    bech2 = BechTest(url_list[2])
    results[url_list[2]] = bech2.isBechdel()
        
    print(results)
    """