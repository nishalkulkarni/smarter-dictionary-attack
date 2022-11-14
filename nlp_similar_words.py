import sys
from nltk.corpus import wordnet


def get_similar_words(word):
    synonyms = []
    antonyms = []

    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

    return list(set(synonyms)), list(set(antonyms))


if (len(sys.argv) < 2):
    print ("Error: Provide file name as argument")
else:
    filename = sys.argv[1]
    newFile = open('final_keywords.txt', 'w')
    
    try:
        with open(filename, 'r') as file:   
            for line in file:    
                for word in line.split():
                    syn,ant = get_similar_words(word)
        
                    newFile.write(word)
                    newFile.write("\n")
                    for i in range(len(syn)):                    
                        newFile.write(syn[i])
                        newFile.write("\n")
                    for i in range(len(ant)):                    
                        newFile.write(ant[i])
                        newFile.write("\n")                
    except:
        print("Error: File " + filename + ". Not found!")
    
    newFile.close
            
    print("DONE! saved as: final_keywords.txt")

# usage -> python nlp_similar_words.py sample.txt