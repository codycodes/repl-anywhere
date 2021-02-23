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
    
    # variable declaration for the output text 
    output_string = "" 
    
    # separating each word in the string 
    input_list = input_string.split(" ") 
    
    # checking each word 
    for word in input_list: 
        
        # if the word exists in the list 
        # then no need to capitalize it 
        if word in lower_case: 
            output_string += word + " "
            
        # if the word does not exists in 
        # the list, then capitalize it 
        else: 
            temp = word.title() 
            output_string += temp + " "
            
    
    return output_string 

# Driver code 
if __name__=='__main__': 
    input_text1 = "The quick brown fox jumps over the lazy dog."
    input_text2 = "A tale of two cities"
    
    print(generateTitleCase(input_text1)) 
    print(generateTitleCase(input_text2)) 

