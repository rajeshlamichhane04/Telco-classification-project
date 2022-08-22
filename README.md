# Telco-classification-project



initial hypotheses and/or questions you have of the data, ideas

data dictionary

project planning (lay out your process through the data science pipeline)

instructions or an explanation of how someone else can reproduce your project and findings (What would someone need to be able to recreate your project on their own?)

key findings, recommendations, and takeaways from your project.

Overview

This repository houses a complete files for this project. These files are

1. README.md: It contains the outline of this project
2. Final_report_Telco.ipynb: This jupyter notebook consists of data science pipeline used to study the churn at Telco
3. predictions.csv: It consists of customers prediction of churn modeled by our prediction model.
4.acquire.py: It consists of codes for data acquition process
5.prepare.py: It consists of codes for data cleaning and data split
6. .igitignore file: It consists of file names that I do not want to be push to git

Project Goals

The goals of this project are to identify the drivers of customer churn at Telco, produce a prediction model to identify the customers who are at a greater risk of churn, and offer recommendations for reducing such churns.

Project Description

Telco is a telecommunication company that is seeing 27% churn and hurting its revenue. This project attempts to study this phenomenon. We will compare the customers that have churned with those who have not. We will analyze the attributes that are driving the churn and then build a prediction model. This model will provide a list of customers who are more likely to churn in form of predictions.csv. Finally, we will recommend courses of action to help promote customer retention.

Initial Questions

1. What portion of customers are churning?
2. What is the timeline of the most churn?
3. Do the customers who churner pay higher monthly charges?
4. Does contract type determine those customers who like churn?
5. Do customers who churn oftem have more or less have services?

Data Dictionary

Variable	Meaning
customer_id	alphas numeric identifer for each customer
gender	if customer is male or female
senior_citizen	if customer is a senior citizen or not
partner	if customer has a partner or not
dependents	if customer has dependents or not
tenure	number of months the customer has been with telco
phone_service	if customer has phone service or not
multiple_lines	if customer has phone multiple phone lines or not, or no phone service
online_security	if customer has online security or not, or no internet service
online_backup	if customer has online backup or not, or no internet service
device_protection	if customer has device protection or not, or no internet service
tech_support	if customer has tech support or not, or no internet service
streaming_tv	if customer has streaming tv or not, or no internet service
streaming_movies	if customer has streaming movies or not, or no internet service
paperless_billing	if custome has paperless billing or not
monthly_charges	amount paid by custome per month
total_charges	total amount paid by customer over tenure
churn	if customer has left telco or not
contract_type	if customer has a month-to-month, 1 year, or 2 year contract
internet_service_type	if customer's internet service is fiber optic, DSL, or no internet service
payment_type	payment is mailed check, electronic check, auto credit card, or auto bank account








