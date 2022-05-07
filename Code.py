import pandas as panda
import numpy as num
import random

"Loading The Test CSV And Printing It's Data"
h=panda.read_csv('test.csv')
h.head()

"Generating Random Numbers In Random Numbbers Column For Test CSV And Printing It's Data"
test = panda.read_csv('test.csv')
test['Random Number'] = num.random.uniform(0,1, test.shape[0])
print(test)

"Using For Loop With Condition On Target Column Of Test CSV And Generating 1 or 0 on Condition"

for row in test['Random Number']:
    if row >= 0.5:
      test['target'] = 1
    else :
      test['target'] = 0

print(test)

"Inserting The Two Columns id and Target Into Our sample CSV File From Test CSV File"

sample = test[['id','target']].copy()
print(sample)


"Creating Our Csv File With That Two Exported Columns For Submission On Kaggle"
sample.to_csv('sample.csv',index=False)
