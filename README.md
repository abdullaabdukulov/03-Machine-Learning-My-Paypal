# 03-Machine-Learning-My-Paypal

<div class="row">
<div class="col tab-content">
<div class="tab-pane active show" id="subject" role="tabpanel">
<div class="row">
<div class="col-md-12 col-xl-12">
<div class="markdown-body">
<p class="text-muted m-b-15">
</p><h2>My Paypal</h2>
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
<p>Credit card companies must recognize fraudulent credit card transactions so that customers are not charged for items that they did not purchase. Credit card fraud is a fascinating subject for data scientists because of the enormous data sets, real and costly business implications, and potential to solve significant business problems that save millions and millions of dollars/pounds/euros/money.</p>
<p>In global efforts to understand and improve machine learning models and data analysis approaches, some datasets have been made open source.</p>
<p>For this project, you will use a somewhat de-identified dataset of credit card transactions in Europe. The dataset contains transactions made by credit cards in September 2013 by European cardholders.
This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced. The positive class (frauds) accounts for 0.172% of all transactions.</p>
<p>It contains only numerical input variables, which are the result of a PCA transformation. Unfortunately, we cannot provide the original features and more background information about the data due to confidentiality issues. Features V1, V2, … V28 are the principal components obtained with PCA. The only features that have not been transformed with PCA are 'Time' and 'Amount.' Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount; for example-dependant cost-sensitive learning. Feature 'Class' is the response variable, and it takes value 1 in case of fraud and 0 otherwise.</p>
<p>Given the class imbalance ratio, we recommend measuring the accuracy using the Area Under the Precision-Recall Curve (AUPRC). Confusion matrix accuracy is not meaningful for unbalanced classification.</p>
<p>You have been hired by FriendPay, a competitor of PayPal, to help them improve their credit card fraud identification system. They are having difficulty identifying which transactions are or are not fraudulent, and this is creating significant business problems that are costing them a lot in missed transaction fees.</p>
<p><em>Your Mission</em>
Your mission is to build a fraud detection model using the dataset that has been provided and in doing so, increase revenue from transaction fees.</p>
<p>What are the success criteria?</p>
<ul>
<li>During our next meeting, you will have to show us some data (plot? report?) of what you've been building.</li>
<li>You will also be evaluated on your model's impact on the business. We need to make our customers happy by denying fraudulent transactions and allowing genuine ones.</li>
</ul>
<p>What to expect?</p>
<ul>
<li>A presentation with slides on how you classified, as well as assumptions, implications, and other important information.</li>
<li>Code that the DevOps team should be able to push to production.</li>
<li><a href="https://fraud-detection-handbook.github.io/fraud-detection-handbook/Chapter_3_GettingStarted/SimulatedDataset.html" target="_blank">Transaction data simulator</a></li>
</ul>
<h2>Technical specification</h2>
<p>Companies that involve a lot of transactions with the use of cards need to find anomalies in the system. Build a fraud detection model on credit cards. Use the transaction and their labels as fraud or non-fraud to detect if new transactions made by the customer are fraud or not.</p>
<p>Learning outcomes: the five stages of your project</p>
<ol>
<li>Data Collecting / Cleaning (see below)</li>
<li>Data Exploration</li>
<li>Data Visualization</li>
<li>Machine Learning</li>
<li>Communication</li>
</ol>
<p>You will have to prove yourself in each of these. We are confident you've already done it! :)</p>
<p>Where to find the data?</p>
<ul>
<li><a href="https://storage.googleapis.com/qwasar-public/track-ds/my_paypal_creditcard.csv" target="_blank">Credit card transaction dataset</a></li>
</ul>
<p>Reminder, it will be one of your portfolio projects. You can find a lot of different ideas. Plagiarism is not tolerated in the company either here. :-)</p>
<p>Acknowledge the data collection of:
Andrea Dal Pozzolo, Olivier Caelen, Reid A. Johnson and Gianluca Bontempi. Calibrating Probability with Undersampling for Unbalanced Classification. In Symposium on Computational Intelligence and Data Mining (CIDM), IEEE, 2015</p>
<p>Dal Pozzolo, Andrea; Caelen, Olivier; Le Borgne, Yann-Ael; Waterschoot, Serge; Bontempi, Gianluca. Learned lessons in credit card fraud detection from a practitioner perspective, Expert systems with applications,41,10,4915-4928,2014, Pergamon</p>
<p>Dal Pozzolo, Andrea; Boracchi, Giacomo; Caelen, Olivier; Alippi, Cesare; Bontempi, Gianluca. Credit card fraud detection: realistic modeling and a novel learning strategy, IEEE transactions on neural networks and learning systems,29,8,3784-3797,2018, IEEE</p>
<p>Dal Pozzolo, Andrea Adaptive Machine learning for credit card fraud detection ULB MLG Ph.D. thesis (supervised by G. Bontempi)</p>
<p>Carcillo, Fabrizio; Dal Pozzolo, Andrea; Le Borgne, Yann-Aël; Caelen, Olivier; Mazzer, Yannis; Bontempi, Gianluca. Scarff: a scalable framework for streaming credit card fraud detection with Spark, Information fusion,41, 182-194,2018,Elsevier</p>
<p>Carcillo, Fabrizio; Le Borgne, Yann-Aël; Caelen, Olivier; Bontempi, Gianluca. Streaming active learning strategies for real-life credit card fraud detection: assessment and visualization, International Journal of Data Science and Analytics, 5,4,285-300,2018, Springer International Publishing</p>
<p>Bertrand Lebichot, Yann-Aël Le Borgne, Liyun He, Frederic Oblé, Gianluca Bontempi Deep-Learning Domain Adaptation Techniques for Credit Cards Fraud Detection, INNSBDDL 2019: Recent Advances in Big Data and Deep Learning, pp 78-88, 2019</p>
<p>Fabrizio Carcillo, Yann-Aël Le Borgne, Olivier Caelen, Frederic Oblé, Gianluca Bontempi Combining Unsupervised and Supervised Learning in Credit Card Fraud Detection Information Sciences, 2019</p>
<p>Yann-Aël Le Borgne, Gianluca Bontempi Machine Learning for Credit Card Fraud Detection - Practical Handbook</p>

<p></p>
</div>

</div>
</div>
</div>
<div class="tab-pane" id="resources" role="tabpanel">
</div>
</div>
</div>
