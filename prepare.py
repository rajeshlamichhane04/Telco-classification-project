#imports
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

#define function to 
#define funtion
def clean_telco_data(telco):
    #replace comma with 0 in values of total charges
    telco.total_charges = telco.total_charges.str.replace(' ', '0')
    #convert total charges to float
    telco.total_charges = telco.total_charges.astype(float)
    #drop unwanted columns
    telco = telco.drop(columns=['internet_service_type_id', 'contract_type_id', 'payment_type_id'])
    #hot encode gender column
    telco['gender_encoded'] = telco.gender.map({'Female': 1, 'Male': 0})
    #hot encode partner column
    telco['partner_encoded'] = telco.partner.map({'Yes': 1, 'No': 0})
    #hot encode dependenst
    telco['dependents_encoded'] = telco.dependents.map({'Yes': 1, 'No': 0})
    #hot encode phone services
    telco['phone_service_encoded'] = telco.phone_service.map({'Yes': 1, 'No': 0})
    #hot encode paperless billing
    telco['paperless_billing_encoded'] = telco.paperless_billing.map({'Yes': 1, 'No': 0})
    #hot encode churn
    telco['churn_encoded'] = telco.churn.map({'Yes': 1, 'No': 0})
    #make list of categorical colmumns
    non_binary = ['multiple_lines','online_security','online_backup','device_protection','tech_support',\
               'streaming_tv','streaming_movies','contract_type', 'internet_service_type', 'payment_type']

    #use dummies to hot encode categorical columns
    dummy_telco = pd.get_dummies(telco[non_binary],drop_first=True)
    #concatenate original dataframe with new one
    telco= pd.concat([telco,dummy_telco],axis = 1)

    #clean up column names
    telco.columns = telco.columns.str.lower().str.replace(" ","_").str.replace("[(,)]","",regex =True)

    #return dataframe back to function
    return telco
    


#define function
def my_train_test_split_telco(telco):

    #split dataframw into 80% train  and 20% test ,target is churn
     train, test = train_test_split(telco, test_size=.2, random_state=123, stratify=telco.churn)
     #split train further into 75% train, 25% validate
     train, validate = train_test_split(train, test_size=.25, random_state=123, stratify=train.churn)
    #return train,validate,test back to function
     return train, validate, test 



#define final function for clean up and split
def prep_telco_data(telco):
    #this funtion returns clean dataframe
    telco = clean_telco_data(telco)
    #this funtion will split cleaned dataframe to train,validate,test
    train, validate, test = my_train_test_split_telco(telco)

    #return values back to function
    return train,validate,test
