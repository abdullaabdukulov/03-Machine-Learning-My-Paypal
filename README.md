# 03-Machine-Learning-Visa-For-Lisa
# Task
Data Collecting / Cleaning, Data Exploration, Data Visualization, Machine Learning, Communication

# Description
For this project, you will use a somewhat de-identified dataset of credit card transactions in Europe. The dataset contains transactions made by credit cards in September 2013 by European cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced. The positive class (frauds) accounts for 0.172% of all transactions.

It contains only numerical input variables, which are the result of a PCA transformation. Unfortunately, we cannot provide the original features and more background information about the data due to confidentiality issues. Features V1, V2, … V28 are the principal components obtained with PCA. The only features that have not been transformed with PCA are 'Time' and 'Amount.' Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount; for example-dependant cost-sensitive learning. Feature 'Class' is the response variable, and it takes value 1 in case of fraud and 0 otherwise.

Given the class imbalance ratio, we recommend measuring the accuracy using the Area Under the Precision-Recall Curve (AUPRC). Confusion matrix accuracy is not meaningful for unbalanced classification.

You have been hired by FriendPay, a competitor of PayPal, to help them improve their credit card fraud identification system. They are having difficulty identifying which transactions are or are not fraudulent, and this is creating significant business problems that are costing them a lot in missed transaction fees.

My mission is to build a fraud detection model using the dataset that has been provided and in doing so, increase revenue from transaction fees.

# Installation
If you haven't installed the necessary libraries, run the following command in a code cell to install them:
   ```python
   !pip install pandas numpy scikit-learn plotly seaborn matplotlib xgboost
   ```

# Usage
## Running the Jupyter Notebook

**Open the Notebook:** Start by opening the Jupyter Notebook file (`my_paypal.ipynb`) in Jupyter Notebook or JupyterLab.
**Download the Data:** You can also download the data at this link (https://storage.googleapis.com/qwasar-public/track-ds/my_paypal_creditcard.csv)