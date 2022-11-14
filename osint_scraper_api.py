import requests
import re
import sys

def get_osint_scrap(word):
    url = "https://tubesel.p.rapidapi.com/search/" + word

    querystring_google = {"google": word}
    querystring_yahoo = {"yahoo": word}
    querystring_bing = {"bing": word}
    querystring_youtube = {"youtube": word}

    headers = {
        "X-RapidAPI-Key": "U5v6Olvwez5h82gnIStMIkknRYJkLeXf",
        "X-RapidAPI-Host": "tubesel.p.rapidapi.com"
    }

    response_google = requests.request("GET", url, headers=headers, params=querystring_google)
    # response_yahoo = requests.request("GET", url, headers=headers, params=querystring_yahoo)
    # response_bing = requests.request("GET", url, headers=headers, params=querystring_bing)
    # response_youtube = requests.request("GET", url, headers=headers, params=querystring_youtube)

    keywords = set()

    try:
        response_google = response_google.json()[0]
        for res in response_google:
            title = str(res["title"])
            title = title[:title.find('http')]
            title = re.sub(r"[^A-Za-z\s]", "", title.strip())
            words = title.split()
            for w in words:
                keywords.add(w)
    except:
        pass

    try:
        response_yahoo = response_yahoo.json()[0]
        for res in response_yahoo:
            title = str(res["title"])
            title = title[:title.find('http')]
            title = re.sub(r"[^A-Za-z\s]", "", title.strip())
            words = title.split()
            for w in words:
                keywords.add(w)
    except:
        pass

    try:
        response_bing = response_bing.json()[0]
        for res in response_bing:
            title = str(res["title"])
            title = title[:title.find('http')]
            title = re.sub(r"[^A-Za-z\s]", "", title.strip())
            words = title.split()
            for w in words:
                keywords.add(w)
    except:
        pass

    try:
        response_youtube = response_youtube.json()[0]
        for res in response_youtube:
            title = str(res["title"])
            title = title[:title.find('http')]
            title = re.sub(r"[^A-Za-z\s]", "", title.strip())
            words = title.split()
            for w in words:
                keywords.add(w)
    except:
        pass
    
    return keywords


if (len(sys.argv) < 2):
    print ("Error: Provide file name as argument")
else:
    filename = sys.argv[1]
    newFile = open('target_info_with_osint.txt', 'w')
    
    try:
        with open(filename, 'r') as file:   
            for line in file:    
                for word in line.split():
                    keywords = list(get_osint_scrap(word))
        
                    newFile.write(word)
                    newFile.write("\n")  
                    for i in range(len(keywords)):                    
                        newFile.write(keywords[i])
                        newFile.write("\n")             
    except:
        print("Error: File " + filename + ". Not found!")
    
    newFile.close
               
    print("DONE! saved as: target_info_with_osint.txt")