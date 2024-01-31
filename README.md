# Credit Card Fraud Detection Project

## Task

<div id="user-content-subject" dir="auto">
<div dir="auto">
<div dir="auto">
<div dir="auto">
<p dir="auto">
</p><h2 tabindex="-1" dir="auto"><a id="user-content-my-paypal" class="anchor" aria-hidden="true" tabindex="-1" href="#my-paypal"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a>My Paypal</h2>
<table>
<thead>
<tr>
<th>Technical details</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Submit file</td>
<td>**</td>
</tr>
<tr>
<td>Languages</td>
<td>It needs to be completed in the language you are working on right now. If you are doing Bootcamp Javascript, then javascript (file extension will be .js). If you are doing Bootcamp Ruby, then Ruby (file extension will be .rb). It goes the same for Python, Java, C++, Rust, ...</td>
</tr>
</tbody>
</table>
<hr>
<p dir="auto">Credit card companies must recognize fraudulent credit card transactions so that customers are not charged for items that they did not purchase. Credit card fraud is a fascinating subject for data scientists because of the enormous data sets, real and costly business implications, and potential to solve significant business problems that save millions and millions of dollars/pounds/euros/money.</p>
<p dir="auto">In global efforts to understand and improve machine learning models and data analysis approaches, some datasets have been made open source.</p>
<p dir="auto">For this project, you will use a somewhat de-identified dataset of credit card transactions in Europe. The dataset contains transactions made by credit cards in September 2013 by European cardholders.
This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced. The positive class (frauds) accounts for 0.172% of all transactions.</p>
<p dir="auto">It contains only numerical input variables, which are the result of a PCA transformation. Unfortunately, we cannot provide the original features and more background information about the data due to confidentiality issues. Features V1, V2, … V28 are the principal components obtained with PCA. The only features that have not been transformed with PCA are 'Time' and 'Amount.' Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount; for example-dependant cost-sensitive learning. Feature 'Class' is the response variable, and it takes value 1 in case of fraud and 0 otherwise.</p>
<p dir="auto">Given the class imbalance ratio, we recommend measuring the accuracy using the Area Under the Precision-Recall Curve (AUPRC). Confusion matrix accuracy is not meaningful for unbalanced classification.</p>
<p dir="auto">You have been hired by FriendPay, a competitor of PayPal, to help them improve their credit card fraud identification system. They are having difficulty identifying which transactions are or are not fraudulent, and this is creating significant business problems that are costing them a lot in missed transaction fees.</p>
<p dir="auto"><em>Your Mission</em>
Your mission is to build a fraud detection model using the dataset that has been provided and in doing so, increase revenue from transaction fees.</p>
<p dir="auto">What are the success criteria?</p>
<ul dir="auto">
<li>During our next meeting, you will have to show us some data (plot? report?) of what you've been building.</li>
<li>You will also be evaluated on your model's impact on the business. We need to make our customers happy by denying fraudulent transactions and allowing genuine ones.</li>
</ul>
<p dir="auto">What to expect?</p>
<ul dir="auto">
<li>A presentation with slides on how you classified, as well as assumptions, implications, and other important information.</li>
<li>Code that the DevOps team should be able to push to production.</li>
<li><a href="https://fraud-detection-handbook.github.io/fraud-detection-handbook/Chapter_3_GettingStarted/SimulatedDataset.html" rel="nofollow">Transaction data simulator</a></li>
</ul>
<h2 tabindex="-1" dir="auto"><a id="user-content-technical-specification" class="anchor" aria-hidden="true" tabindex="-1" href="#technical-specification"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a>Technical specification</h2>
<p dir="auto">Companies that involve a lot of transactions with the use of cards need to find anomalies in the system. Build a fraud detection model on credit cards. Use the transaction and their labels as fraud or non-fraud to detect if new transactions made by the customer are fraud or not.</p>
<p dir="auto">Learning outcomes: the five stages of your project</p>
<ol dir="auto">
<li>Data Collecting / Cleaning (see below)</li>
<li>Data Exploration</li>
<li>Data Visualization</li>
<li>Machine Learning</li>
<li>Communication</li>
</ol>
<p dir="auto">You will have to prove yourself in each of these. We are confident you've already done it! :)</p>
<p dir="auto">Where to find the data?</p>
<ul dir="auto">
<li><a href="https://storage.googleapis.com/qwasar-public/track-ds/my_paypal_creditcard.csv" rel="nofollow">Credit card transaction dataset</a></li>
</ul>
<p dir="auto">Reminder, it will be one of your portfolio projects. You can find a lot of different ideas. Plagiarism is not tolerated in the company either here. :-)</p>
<p dir="auto">Acknowledge the data collection of:
Andrea Dal Pozzolo, Olivier Caelen, Reid A. Johnson and Gianluca Bontempi. Calibrating Probability with Undersampling for Unbalanced Classification. In Symposium on Computational Intelligence and Data Mining (CIDM), IEEE, 2015</p>
<p dir="auto">Dal Pozzolo, Andrea; Caelen, Olivier; Le Borgne, Yann-Ael; Waterschoot, Serge; Bontempi, Gianluca. Learned lessons in credit card fraud detection from a practitioner perspective, Expert systems with applications,41,10,4915-4928,2014, Pergamon</p>
<p dir="auto">Dal Pozzolo, Andrea; Boracchi, Giacomo; Caelen, Olivier; Alippi, Cesare; Bontempi, Gianluca. Credit card fraud detection: realistic modeling and a novel learning strategy, IEEE transactions on neural networks and learning systems,29,8,3784-3797,2018, IEEE</p>
<p dir="auto">Dal Pozzolo, Andrea Adaptive Machine learning for credit card fraud detection ULB MLG Ph.D. thesis (supervised by G. Bontempi)</p>
<p dir="auto">Carcillo, Fabrizio; Dal Pozzolo, Andrea; Le Borgne, Yann-Aël; Caelen, Olivier; Mazzer, Yannis; Bontempi, Gianluca. Scarff: a scalable framework for streaming credit card fraud detection with Spark, Information fusion,41, 182-194,2018,Elsevier</p>
<p dir="auto">Carcillo, Fabrizio; Le Borgne, Yann-Aël; Caelen, Olivier; Bontempi, Gianluca. Streaming active learning strategies for real-life credit card fraud detection: assessment and visualization, International Journal of Data Science and Analytics, 5,4,285-300,2018, Springer International Publishing</p>
<p dir="auto">Bertrand Lebichot, Yann-Aël Le Borgne, Liyun He, Frederic Oblé, Gianluca Bontempi Deep-Learning Domain Adaptation Techniques for Credit Cards Fraud Detection, INNSBDDL 2019: Recent Advances in Big Data and Deep Learning, pp 78-88, 2019</p>
<p dir="auto">Fabrizio Carcillo, Yann-Aël Le Borgne, Olivier Caelen, Frederic Oblé, Gianluca Bontempi Combining Unsupervised and Supervised Learning in Credit Card Fraud Detection Information Sciences, 2019</p>
<p dir="auto">Yann-Aël Le Borgne, Gianluca Bontempi Machine Learning for Credit Card Fraud Detection - Practical Handbook</p>
<p dir="auto"></p>
</div>
</div>
</div>
</div>

## Overview

This project aims to develop a robust credit card fraud detection model for FriendPay, a competitor of PayPal. The implementation includes data exploration, insightful visualizations, and the utilization of machine learning techniques. Additionally, a neural network using TensorFlow is integrated into the project.

## Table of Contents

- [Introduction](#introduction)
- [Data Exploration](#data-exploration)
- [Data Preprocessing](#data-preprocessing)
- [Model Development](#model-development)
- [Model Evaluation](#model-evaluation)
- [Neural Network](#neural-network)
- [Conclusion](#conclusion)

## Introduction

The project utilizes a dataset of European credit card transactions, addressing the challenge of class imbalance. The emphasis is on machine learning techniques, particularly the Area Under the Precision-Recall Curve (AUPRC) due to the dataset's nature.

```python
# Sample code for loading the dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

url = "https://storage.googleapis.com/qwasar-public/track-ds/my_paypal_creditcard.csv" if not os.path.exists('my_paypal_creditcard.csv') else 'my_paypal_creditcard.csv'
df = pd.read_csv(url)
```

## Data Exploration

The project includes thorough data exploration and visualization using Python essentials for data analysis (Pandas, NumPy, Matplotlib, Seaborn).

```python
# Sample code for class distribution analysis
def balanc(df):
    # Function to compute class percentages and print a summary
    # ...

def plot_balanc(data=None, column='Class'):
    # Function to plot class distributions
    # ...

balanc(df)
plot_balanc(df)
```

## Model Development

The project addresses class imbalances in credit card fraud detection and employs machine learning models such as Logistic Regression, Decision Tree Classifier, SVC, and K-Neighbors Classifier.

```python
# Sample code for training and evaluating machine learning models
ml_models = [LogisticRegression(), DecisionTreeClassifier(), SVC(), KNeighborsClassifier()]
ml = MachineLearning(models=ml_models, x=X, y=Y)
ml.fit()
ml.predict()
ml.display()
```

## Neural Network

A neural network using TensorFlow and Keras is implemented for multi-class classification.

```python
# Sample code for building and training a neural network
model = Sequential()
# ... (model architecture)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')
model.summary()
```

## Conclusion

In conclusion, the project provides a comprehensive approach to credit card fraud detection, contributing to increased revenue and improved customer satisfaction for FriendPay.
