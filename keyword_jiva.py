import pandas as pd
import numpy as np
import RAKE
rake_object = RAKE.Rake("/Users/jessicasethi/Desktop/training_phrases.txt")

jiva = pd.read_csv("/Users/jessicasethi/Documents/Jiva_data.csv")
jiv = np.array(jiva)

themes = np.unique(jiv[:,0])
#themes  = np.array(['Belongingness & Support', 'Career Growth', 'Company Vision',
#       'Culture', 'HR & Policies', 'Infrastructure', 'Manager', 'Others',
#       'Settling In', 'Support from Seniors', 'Work Clarity'])
big_list = []

for item in themes:
        l1 = jiv[jiv[:,0]==item,1]
        l1 = np.delete(l1, np.where(l1!=l1))
        text = " ".join(l1)

        phrases = rake_object.run(text, minCharacters = 1, maxWords = 2, minFrequency = 5)

        if(len(phrases)==0):
                phrases = rake_object.run(text, minCharacters = 1, maxWords = 2, minFrequency = 2)


        if(len(phrases)==0):
                phrases = rake_object.run(text, minCharacters = 1, maxWords = 2, minFrequency = 1)
                keys = np.array(phrases)[0:2,0]
        else:
                keys = np.array(phrases)[:,0]

        belong = []
        freq = []

        for item in keys:
                lis = []
                for i in range(len(l1)):
                        if(item in l1[i]):
                                lis.append(l1[i])
                belong.append(lis)
                freq.append(len(lis))

        ar1 = np.array(keys).reshape(len(keys),1)
        ar2 = np.array(belong).reshape(len(keys),1)
        ar3 = np.array(freq).reshape(len(keys),1)
        array = np.concatenate((ar1, ar2, ar3), axis = 1)
        array = array.tolist()

        big_list.append(array)
'''
with open("/Users/jessicasethi/Documents/Carre_Growth.csv", "w") as f:
		writer = csv.writer(f)
		for item in array:
			writer.writerow(item)
'''

ar1 = themes.reshape(len(themes),1)
ar2 = np.array(big_list).reshape(len(themes),1)
array = np.concatenate((ar1, ar2), axis = 1)
array = array.tolist()

dict1 = [{'theme': elem[0], 'keywords' : [{'word' : item[0], 'frequency' : item[2],
                            'responses' : item[1]} for item in elem[1]]} for elem in array]
import json
with open("/Users/jessicasethi/Documents/jiva.json", "w") as f:
		f.write(json.dumps(dict1))


