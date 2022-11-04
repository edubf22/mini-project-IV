# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
In this project, the aim is to automate a process that predicts if a person will have a loan request approved or not. To do that, we employed a supervised machine learning method and deployed our model in the cloud. 

## Hypothesis
Prior to analyzing the data and building the model, it is important to develop hypotheses of which candidates are likely to get a loan approved. Below are some of these hypotheses: 

* **Candidates who possess a high credit score**. This would mean that the candidate has a good control of their finances and is dependable to pay back the loan. 
* **Candidates in a household with a high total income**. Having a higher income could mean the candidate is more likely to pay back the loan.
* **Candidates with a history of delayed payments**. Banks make money on interest, so it may be interesting to them to approve loans to customers who may have some difficulty in paying back a loan. 
* **Candidates who have been working with the financial institution for a long time**. For example, a bank could be more likely to approve a loan if they new the banking history of a client. A client could also have higher chances of having the loan approved thanks to their loyalty to a bank. 
* **Candidates who have had successful loans with this or other institutions**. An institution could look at this as an indication that the candidate is willing to pay back a loan. 
* **Candidates who are employed**. This related to the second hypothesis - someone with some sort of income is more likely to pay back the loan. 

## EDA 
Different insights could be obtained by performing EDA. Some of these insights are presented below:
- The property area does not seem to play a significant role. Average income, loan amount and term all seemed to be relatively close regardless of the property location
- There is significant disparity in the income of male and female applicants, but it does not seem to be the same for 


## Process
(fill in what you did during EDA, cleaning, feature engineering, modeling, deployment, testing)
### (your step 1)
### (your step 2)

## Results/Demo
(fill in your model's performance, details about the API you created, and (optional) a link to an live demo)

## Challanges 
- Giving priority to the right parts of the project. I spent a lot of time imputing missing values with fancier groups, only to realize later that I would not be able to incorporate that in the pipeline.
- Saving the model using pipeline. Before, I had saved the model using processed data. Figuring out how to include the feature engineering steps in the pipeline was a big challenge.
- Understanding how to build an API using Flask. 

## Future Goals
- Come up with more meaningful ways of treating the data and incorporating that in the pipeline using `FunctionTransformer()`.
- Develop a nicer API using HTML code - maybe the user could input values on the browser.