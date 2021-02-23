import sys

# From https://www.geeksforgeeks.org/convert-string-to-title-case-in-python/ ; all rights to the author
# Edited by Cody Gagnon on 2-23-21
# Function to convert into title case 
def generateTitleCase(input_string): 
    
    # list of articles 
    articles = ["a", "an", "the"] 
    
    # list of coordinating conjunctins 
    conjunctions = ["and", "but", 
                    "for", "nor", 
                    "or", "so", 
                    "yet"] 
    
    # list of some short articles 
    prepositions = ["in", "to", "for", 
                    "with", "on", "at", 
                    "from", "by", "about", 
                    "as", "into", "like", 
                    "through", "after", "over", 
                    "between", "out", "against", 
                    "during", "without", "before", 
                    "under", "around", "among", 
                    "of"] 
    
    # merging the 3 lists 
    lower_case = articles + conjunctions + prepositions 

    output = []
    input_list = input_string.split(" ")
    for word in input_list: 
        if word not in lower_case:
            word = word.title()

        output.append(word)
    return ' '.join(output)

# Driver code 
if __name__=='__main__': 
    original_text = sys.argv[1]
    print(generateTitleCase(original_text))