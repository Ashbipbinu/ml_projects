# Heart Disease Prediction using Logistic Regression

##  Overview

This project uses a machine learning model to predict whether a person has heart disease based on various medical parameters. It is built with Python and trained on the Kaggle Heart Disease Dataset using logistic regression.

##  Dataset

- Dataset: Kaggle Heart Disease Dataset
    - link: https://www.kaggle.com/code/desalegngeb/heart-disease-predictions/input
- Contains 303 samples and 14 features including:
  - Age, Sex, Chest Pain Type, Resting Blood Pressure, Cholesterol, etc.

##  Workflow

1. **Data Preprocessing**
   - Checked for missing/null values.
   - Performed exploratory analysis and correlation heatmap.
   
2. **Modeling**
   - Split data into train and test sets (80% train, 20% test).
   - Trained a Logistic Regression model.
   - Achieved **87.7% accuracy** on the test set.
   
3. **Serialization**
   - Trained model saved using `pickle` for deployment.

##  How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/Ashbipbinu/ml_projects.git
cd ml_projects/Heart_Disease_Prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Notebook
Open the notebook in Jupyter or Google Colab and run all cells:

### 4. Run Predictions
After training, you can use the pickled model:

```bash
model = pickle.load(open("model.pkl", "rb"))
model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
```

Note: Replace the input values with actual patient data.

### Model Performance
```
Model Used: Logistic Regression
Accuracy: 87.7% on test data
```

