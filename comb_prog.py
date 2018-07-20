from padatious.intent_container import IntentContainer
import pickle

from padatious import IntentContainer

themes = list(['Food', 'Deals_discounts', 'Ambience', 'Value_for_money',
               'Service', 'Hygiene', 'cleanliness&comfort',
               'Recognition','Relationship with Seniors',
               'Job Satisfaction','Communication','Leadership',
               'Training and Process Orientation','Colleague Relations',
               'Personal Growth', 'Vision Alignment', 'Resources and Benefits',
               'Company Feedback', 'Others','plot', 'characters', 'music',
               'acting', 'cinematography', 'location'])

container = IntentContainer('/Users/jessicasethi/Documents/intent_cache')

for item in themes:
    container.load_file(item, "/Users/jessicasethi/Documents/combined_intents/" + str(item) + ".txt")
# train only the first time, then only need to load the files because they're already in cache
#container.train()

'''
data = container.calc_intents("The ambience is really nice")
sor = sorted(data, key = lambda x: x.conf, reverse = True)
for lem in sor:
    if(lem.conf > 0):
        print(lem.conf,"\t", lem.name)
    else:
        break
'''

import pandas as pd
import numpy as np

jiva = pd.read_csv("/Users/jessicasethi/Documents/Jiva_data.csv")
jiva = np.array(jiva)
l1 = jiva[jiva[:,0]=='Career Growth',1]

for item in l1:
    data = container.calc_intent(item)
    print(data.name)
