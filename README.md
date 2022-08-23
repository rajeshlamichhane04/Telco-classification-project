# Telco-classification-project

<hr style="border-top: 50px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

## Overview

> - This repository houses a complete files for this project. These files are

> -  README.md: It contains the outline of this project
> -  Final_report_Telco.ipynb: This jupyter notebook consists of data science pipeline used to study the churn at Telco
> -  predictions.csv: It consists of customers prediction of churn modeled by our prediction model.
> -  acquire.py: It consists of codes for data acquition process
> -  prepare.py: It consists of codes for data cleaning and data split
> -  .igitignore file: It consists of file names that I do not want to be push to git

## Project Goals

> - The goals of this project are to identify the drivers of customer churn at Telco, produce a prediction model to identify the customers who are at a greater risk of churn, and offer recommendations for reducing such churns.

## Project Description

> - Telco is a telecommunication company that is seeing 27% churn and hurting its revenue. This project attempts to study this phenomenon. We will compare the customers that have churned with those who have not. We will analyze the customer features hat are driving the churn by using various seaborn and matplotlib visualizations and hypothesis testings, and then build a prediction model using modeling algorithm such as Decision Trees and Random Forest. This model will provide a list of customers who are more likely to churn in form of predictions.csv. Finally, we will recommend courses of action to help promote customer retention.

## Initial Questions

> -  What portion of customers are churning?
> -  What is the timeline of the most churn?
> -  Do the customers who churner pay higher monthly charges?
> -  Does contract type determine those customers who like churn?
> -  Do customers who churn oftem have more or less have services?

## Data Dictionary

> - 1. customer_id = alphas numeric identifer for each customer|
> - 2. gender = if customer is male or female|
> - 3. senior_citizen = if customer is a senior citizen or not
> - 4. partner = if customer has a partner or not
> - 5. dependents = if customer has dependents or not
> - 6. tenure= number of months the customer has been with telco
> - 7. phone_service = if customer has phone service or not
> - 8. multiple_lines = if customer has phone multiple phone lines or not, or no phone service
> - 9. online_security = if customer has online security or not, or no internet service
> - 10. online_backup = if customer has online backup or not, or no internet service
> - 11. device_protection = if customer has device protection or not, or no internet service
> - 12. tech_support = if customer has tech support or not, or no internet service
> - 13. streaming_tv = if customer has streaming tv or not, or no internet service
> - 14. streaming_movies = if customer has streaming movies or not, or no internet service
> - 15. paperless_billing = if custome has paperless billing or not
> - 16. monthly_charges = amount paid by custome per month
> - 17. total_charges = total amount paid by customer over tenure
> - 18. churn = if customer has left telco or not
> - 19. contract_type = if customer has a month-to-month, 1 year, or 2 year contract
> - 20. internet_service_type = if customer's internet service is fiber optic, DSL, or no internet service
> - 21. payment_type = payment is mailed check, electronic check, auto credit card, or auto bank account
> - 22. payment_id_type = payment type is as encoded 1,2,3,4
> - 23. internet_service_type_id = internet type is encoded as 1,2,3
> - 24. contract_type_id = contract type is encoded as 1,2,3

## Steps to Reproduce

> -  To clone this repo, use this command in your terminal https://github.com/rajeshlamichhane04/Telco-classification-project
> -  You will need login credentials for MySQL database hosted at data.codeup.com
> -  You will need an env.py file that contains hostname,username and password
> -  The env.py should also contain a function named get_db_url() that establishes the string value of the database url.
> -  Store that env file locally in the repository.

## The plan

> - I set up my initial questions during this phase. I made the outline of possible exploration techniques and hypothesis testing I can use.

##  Acquisition

> - I obtanied Telco customer data by using SQL query via MySQL database. I saved the file locally as a csv. I used the code created at acquire.py.

## Preparation

> - I accomplished this using prepare.py file. I cleaned up the data by adding missing values to column and dropping unnecessary columns. I also hard encoded them to fit in to ML format. Further I split my data into train (60%), validate(20%) and test (20%).

> ##  Exploration

> - I used only my training data for exploration. I answered my initial question using various seaborn and matplotlib visualizations and hypothesis testings. This helped me identify my drivers of churn.

##  Modeling

> - First, I set up my baseline model accuracy and split my dataset into X and y where X is the drivers of churn and y is the target variable chirn. Using various features and hyperparameters, I tested my train data on models such as Decision Tree, Random Forest, K-Nearest Neighbor and Logisitic Regression. I tested the models in my validate data to help me identify my best model and used the best model in my test data to make predictions.

## Prediction delivery

> - I submitted a prediction file in csv named as predictions.csv in this repository as per project specification.

## Key Takeaways and Recommendations
> - New customers churn at higher rates so they should be offered discounts in thier monthly charges.
> - Customers on month to month contract are more vunerable to churn so they needed to be provided with incentives to switch to longer contracts.




