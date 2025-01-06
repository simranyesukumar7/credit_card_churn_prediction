# 💳 Credit Card Churn Prediction

Customer churn refers to the percentage of customers who terminate or discontinue their relationship with a company. In the banking industry, customers often switch credit card companies based on offers or services, leading to a churn rate of 13%. Predicting customer churn allows companies to focus retention efforts on high-risk clients and reduce overall churn.

This project involves building a predictive model that can identify which customers are likely to churn based on their behaviors and interactions with the company. By using machine learning techniques, we aim to predict churn probability and assist banks in retaining their most valuable customers.

## 📂 Dataset

The dataset used for this project is the **Churn_Modelling.csv**, available on Kaggle. It contains data about bank customers, including their personal details, account status, and behaviors.

- **Dataset Link**: [Churn_Modelling.csv](https://www.kaggle.com/code/kmalit/bank-customer-churn-prediction/data?select=Churn_Modelling.csv)

### Metadata:

- **Row Number**: A unique identifier for each row.
- **Customer ID**: A unique identifier for each client.
- **Surname**: The client's last name.
- **CreditScore**: The client's credit card score (numeric).
- **Geography**: The location of the customer (categorical).
- **Gender**: The gender of the customer (categorical: Male/Female).
- **Age**: The age of the customer (numeric).
- **Tenure**: The number of months the client has been with the company (numeric).
- **Balance**: The account balance of the customer (numeric).
- **NumOfProducts**: The number of products or services the client is using (numeric).

---

## 💡 Objective

The main objectives of this project are:

1. **Analyze and visualize** the factors contributing to customer churn in the banking industry.
2. **Build a predictive model** that determines the likelihood of a client churning, helping banks take preventive actions.
3. Use the model to **assign probabilities** of churn, allowing customer service teams to focus on high-risk clients.

---

## 🚀 Workflow

### 1. **Data Preprocessing:**
- Handle missing values, encode categorical variables, and scale numerical features.
- Analyze the data to identify correlations and important features.

### 2. **Model Building:**
- Train various machine learning models (e.g., Logistic Regression, Random Forest, XGBoost).
- Use cross-validation to evaluate model performance and avoid overfitting.

### 3. **Model Evaluation:**
- Evaluate the model using metrics like **accuracy**, **precision**, **recall**, **F1-score**, and **ROC-AUC**.
- Select the best-performing model and fine-tune hyperparameters.

---

## 🛠️ Requirements

To run this project, make sure you have the following dependencies installed:

- **Python 3.7+**
- **Pandas**: For data manipulation.
- **Scikit-learn**: For building and evaluating machine learning models.
- **Matplotlib**: For visualizations.
- **Seaborn**: For statistical plots.
- **XGBoost**: For building gradient boosting models.

---

## 📝 How to Use

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/credit-card-churn-prediction.git
