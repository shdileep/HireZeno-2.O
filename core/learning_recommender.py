"""
=========================================================
HireZeno 2.O
Enterprise Learning Recommendation Engine
Author : HireZeno 2.O Team
Version : 9.0
=========================================================
"""

import os
import pandas as pd


class LearningRecommender:

    def __init__(self):

        path = "data/learning_paths.csv"

        if os.path.exists(path):

            self.learning = pd.read_csv(path)

        else:

            self.learning = pd.DataFrame(
                columns=[
                    "Skill",
                    "Difficulty",
                    "Duration",
                    "Course",
                    "Project"
                ]
            )

    # --------------------------------------------------
    # Recommend Courses
    # --------------------------------------------------

    def recommend(self, missing_skills):

        if len(missing_skills) == 0:

            return pd.DataFrame()

        recommendations = []

        for skill in sorted(set(missing_skills)):

            row = self.learning[

                self.learning["Skill"]

                .str.lower()

                == skill.lower()

            ]

            if not row.empty:

                item = row.iloc[0]

                recommendations.append({

                    "Skill": item["Skill"],

                    "Difficulty": item["Difficulty"],

                    "Duration": item["Duration"],

                    "Course": item["Course"],

                    "Project": item["Project"],

                    "Priority": "High"

                })

        return pd.DataFrame(recommendations)

    # --------------------------------------------------
    # Learning Roadmap
    # --------------------------------------------------

    def roadmap(

        self,

        recommendations

    ):

        phases = []

        for index, row in recommendations.iterrows():

            phases.append(

                f"Phase {index+1}: "

                f"Learn {row['Skill']} "

                f"({row['Duration']}) "

                f"→ Build {row['Project']}"

            )

        return phases

    # --------------------------------------------------
    # Learning Summary
    # --------------------------------------------------

    def summary(

        self,

        recommendations

    ):

        if recommendations.empty:

            return {

                "Skills": 0,

                "Estimated Duration": "0 Week",

                "Priority": "None"

            }

        return {

            "Skills": len(recommendations),

            "Estimated Duration": recommendations["Duration"].iloc[-1],

            "Priority": "High"

        }

    # --------------------------------------------------
    # Career Impact
    # --------------------------------------------------

    def career_impact(

        self,

        total_missing

    ):

        if total_missing <= 3:

            return "Low Skill Gap"

        elif total_missing <= 7:

            return "Medium Skill Gap"

        else:

            return "High Skill Gap"

    # --------------------------------------------------
    # Learning Score
    # --------------------------------------------------

    def learning_score(

        self,

        total_missing

    ):

        score = max(

            0,

            100 - total_missing * 8

        )

        return score

    # --------------------------------------------------
    # Complete Report
    # --------------------------------------------------

    def full_report(

        self,

        missing_skills

    ):

        recommendations = self.recommend(

            missing_skills

        )

        return {

            "Recommendations": recommendations,

            "Roadmap": self.roadmap(

                recommendations

            ),

            "Summary": self.summary(

                recommendations

            ),

            "Career Impact": self.career_impact(

                len(missing_skills)

            ),

            "Learning Score": self.learning_score(

                len(missing_skills)

            )

        }
