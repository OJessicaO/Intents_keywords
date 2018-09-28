import pandas as pd
import numpy as np
import RAKE

# create rake_object with file containing stop words to be used (optional)
rake_object = RAKE.Rake("/Users/jessicasethi/Desktop/training_phrases.txt")

# read json file
data_as_pandas_df = pd.io.json.read_json("/Users/jessicasethi/Documents/Xane/Jiva_data.json")
data_array = np.array(data_as_pandas_df)

themes = np.unique(data_array[:,1])

# list of lists of keywords for each theme
big_list = []

# traverse through themes
for theme in themes:
        reviews_of_this_theme = data_array[data_array[:,1]==theme, 0]
        reviews_of_this_theme = np.delete(reviews_of_this_theme, np.where(reviews_of_this_theme!=reviews_of_this_theme))
        text = " ".join(reviews_of_this_theme)

        # get key phrases
        phrases = rake_object.run(text, minCharacters = 1, maxWords = 2, minFrequency = 5)

        # handle cases with no keywords above set frequency and pick keys out of the output (containing both keys and frequency in that review)
        if(len(phrases)==0):
                phrases = rake_object.run(text, minCharacters = 1, maxWords = 2, minFrequency = 2)
        if(len(phrases)==0):
                phrases = rake_object.run(text, minCharacters = 1, maxWords = 2, minFrequency = 1)
                keys = np.array(phrases)[0:2,0]
        else:
                keys = np.array(phrases)[:,0]

        # list of lists of reviews with keyword for each keyword
        reviews_with_this_keyword = []
        # list of frequency for each keyword correspondingly
        frequency_of_keyword_in_this_theme = []

        for key in keys:
                reviews_with_key = []
                for i in range(len(reviews_of_this_theme)):
                        if(key in reviews_of_this_theme[i]):
                                reviews_with_key.append(reviews_of_this_theme[i])
                reviews_with_this_keyword.append(reviews_with_key)
                frequency_of_keyword_in_this_theme.append(len(reviews_with_key))

        
        # create table of keywords of the theme, reviews containg each keyword and frequency of each keyword and put in list
        array = list(zip(keys, reviews_with_this_keyword, frequency_of_keyword_in_this_theme))

        # add the list for this theme to the big list
        big_list.append(array)



# create array from big_list with theme names
array = list(zip(themes, big_list))

# create object in json format from array
dict1 = [{'theme': elem[0], 'keywords' : [{'word' : item[0], 'frequency' : item[2],
                            'responses' : item[1]} for item in elem[1]]} for elem in array]

# write output in json file
import json
with open("/Users/jessicasethi/Documents/jiva_da.json", "w") as f:
		f.write(json.dumps(dict1))

