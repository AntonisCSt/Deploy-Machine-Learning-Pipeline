import re
import pandas as pd
import numpy as np





def init_titanic_data(data):
    def get_first_cabin(row):
        try:
            return row.split()[0]
        except:
            return np.nan

    def get_title(passenger):
        line = passenger
        if re.search('Mrs', line):
            return 'Mrs'
        elif re.search('Mr', line):
            return 'Mr'
        elif re.search('Miss', line):
            return 'Miss'
        elif re.search('Master', line):
            return 'Master'
        else:
            return 'Other'
        
    data2 = data.copy()

    data2 = data2.replace('?', np.nan)
    
    #print(data2.columns)
    data2['Cabin'] = data2['Cabin'].apply(get_first_cabin)

    data2['Title'] = data2['Name'].apply(get_title)

    data2['Fare'] = data2['Fare'].astype('float')
    data2['Age'] = data2['Age'].astype('float')

    data2.drop(labels=['Name', 'Ticket'], axis=1, inplace=True)
    return data2
