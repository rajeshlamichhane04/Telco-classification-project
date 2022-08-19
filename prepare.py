import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

#define function to 
def clean_telco_data(telco):
    telco.total_charges = telco.total_charges.str.replace(' ', '0')
    telco.total_charges = telco.total_charges.astype(float)
    telco = telco.drop(columns=['internet_service_type_id', 'contract_type_id', 'payment_type_id'])
    telco['gender_encoded'] = telco.gender.map({'Female': 1, 'Male': 0})
    telco['partner_encoded'] = telco.partner.map({'Yes': 1, 'No': 0})
    telco['dependents_encoded'] = telco.dependents.map({'Yes': 1, 'No': 0})
    telco['phone_service_encoded'] = telco.phone_service.map({'Yes': 1, 'No': 0})
    telco['paperless_billing_encoded'] = telco.paperless_billing.map({'Yes': 1, 'No': 0})
    telco['churn_encoded'] = telco.churn.map({'Yes': 1, 'No': 0})
    non_binary = ['multiple_lines','online_security','online_backup','device_protection','tech_support',\
               'streaming_tv','streaming_movies','contract_type', 'internet_service_type', 'payment_type']


    dummy_telco = pd.get_dummies(telco[non_binary],drop_first=True)
    telco= pd.concat([telco,dummy_telco],axis = 1)
    telco = telco.drop(columns = non_binary)
    encoded_col = ["gender","partner","dependents","phone_service","paperless_billing"]
    telco = telco.drop(columns = encoded_col)
    telco.columns = telco.columns.str.lower().str.replace(" ","_").str.replace("[(,)]","",regex =True)

    return telco

def my_train_test_split_telco(telco):

     train, test = train_test_split(telco, test_size=.2, random_state=123, stratify=telco.churn)
     train, validate = train_test_split(train, test_size=.25, random_state=123, stratify=train.churn)

     return train, validate, test 


def prep_telco_data(telco):
    telco = clean_telco_data(telco)
    train, validate, test = my_train_test_split_telco(telco)
    return train,validate,test
