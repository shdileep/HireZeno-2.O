"""
=========================================================
HireZeno 2.O
Enterprise Salary Prediction Engine
Author : HireZeno 2.O Team
Version : 9.0
=========================================================
"""

import os
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

try:
    from xgboost import XGBRegressor
    XGBOOST_AVAILABLE = True
except Exception:
    XGBOOST_AVAILABLE = False


class SalaryPredictor:

    def __init__(self):

        self.model_folder = "models"
        os.makedirs(self.model_folder, exist_ok=True)

        self.models = {}

    # =====================================================
    # Generate Sample Dataset
    # =====================================================

    def load_dataset(self):

        np.random.seed(42)

        rows = 1000

        df = pd.DataFrame({

            "Experience":
                np.random.randint(0, 16, rows),

            "Skills":
                np.random.randint(5, 35, rows),

            "Projects":
                np.random.randint(0, 20, rows),

            "Certifications":
                np.random.randint(0, 10, rows),

            "Education":
                np.random.randint(1, 5, rows)

        })

        salary = (

            df["Experience"] * 2.4 +

            df["Skills"] * 0.70 +

            df["Projects"] * 0.40 +

            df["Certifications"] * 0.60 +

            df["Education"] * 2 +

            np.random.normal(0, 2, rows)

        )

        df["Salary"] = salary.round(2)

        return df

    # =====================================================
    # Train Models
    # =====================================================

    def train_models(self):

        df = self.load_dataset()

        X = df.drop("Salary", axis=1)

        y = df["Salary"]

        X_train, X_test, y_train, y_test = train_test_split(

            X,

            y,

            test_size=0.20,

            random_state=42

        )

        models = {

            "Linear Regression":
                LinearRegression(),

            "Random Forest":
                RandomForestRegressor(

                    n_estimators=200,

                    random_state=42

                )

        }

        if XGBOOST_AVAILABLE:

            models["XGBoost"] = XGBRegressor(

                n_estimators=200,

                learning_rate=0.05,

                random_state=42

            )

        results = []

        for name, model in models.items():

            model.fit(X_train, y_train)

            pred = model.predict(X_test)

            mae = mean_absolute_error(y_test, pred)

            rmse = np.sqrt(

                mean_squared_error(

                    y_test,

                    pred

                )

            )

            r2 = r2_score(

                y_test,

                pred

            )

            filename = name.lower().replace(

                " ",

                "_"

            ) + ".pkl"

            joblib.dump(

                model,

                os.path.join(

                    self.model_folder,

                    filename

                )

            )

            self.models[name] = model

            results.append({

                "Model": name,

                "MAE": round(mae, 2),

                "RMSE": round(rmse, 2),

                "R²": round(r2, 4)

            })

        return pd.DataFrame(results)

    # =====================================================
    # Load Models
    # =====================================================

    def load_models(self):

        for file in os.listdir(self.model_folder):

            if file.endswith(".pkl"):

                model = joblib.load(

                    os.path.join(

                        self.model_folder,

                        file

                    )

                )

                name = file.replace(

                    ".pkl",

                    ""

                ).replace(

                    "_",

                    " "

                ).title()

                self.models[name] = model

    # =====================================================
    # Predict Salary
    # =====================================================

    def predict(

        self,

        experience,

        skills,

        projects,

        certifications,

        education,

        model_name="Random Forest"

    ):

        if not self.models:

            self.load_models()

        if not self.models:

            self.train_models()

            self.load_models()

        model = self.models.get(

            model_name,

            list(self.models.values())[0]

        )

        sample = pd.DataFrame({

            "Experience": [experience],

            "Skills": [skills],

            "Projects": [projects],

            "Certifications": [certifications],

            "Education": [education]

        })

        salary = float(

            model.predict(sample)[0]

        )

        return round(

            salary,

            2

        )

    # =====================================================
    # Salary Grade
    # =====================================================

    def salary_grade(

        self,

        salary

    ):

        if salary >= 35:

            return "Excellent"

        elif salary >= 25:

            return "High"

        elif salary >= 18:

            return "Average"

        elif salary >= 12:

            return "Entry Level"

        else:

            return "Beginner"

    # =====================================================
    # Recommendation
    # =====================================================

    def recommendation(

        self,

        salary

    ):

        if salary >= 35:

            return (
                "Eligible for senior roles in leading organizations."
            )

        elif salary >= 25:

            return (
                "Competitive profile with good growth opportunities."
            )

        elif salary >= 18:

            return (
                "Improve projects and certifications to increase salary."
            )

        elif salary >= 12:

            return (
                "Gain experience and strengthen technical skills."
            )

        return (
            "Focus on building strong fundamentals and hands-on projects."
        )

    # =====================================================
    # Complete Report
    # =====================================================

    def full_report(

        self,

        experience,

        skills,

        projects,

        certifications,

        education,

        model_name="Random Forest"

    ):

        salary = self.predict(

            experience,

            skills,

            projects,

            certifications,

            education,

            model_name

        )

        return {

            "Predicted Salary (LPA)": salary,

            "Grade": self.salary_grade(

                salary

            ),

            "Recommendation": self.recommendation(

                salary

            )

        }

    # =====================================================
    # Demo
    # =====================================================

    def demo_prediction(self):

        return self.full_report(

            experience=5,

            skills=20,

            projects=8,

            certifications=4,

            education=4

        )
