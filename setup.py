import os
import json

structure = {
    "Phase1_Python_Pandas": [
        "01_python_basics.ipynb",
        "02_numpy.ipynb",
        "03_pandas_basics.ipynb",
        "04_pandas_cleaning.ipynb",
        "05_pandas_grouping.ipynb",
        "06_data_visualization.ipynb",
    ],
    "Phase2_Statistics": [
        "01_descriptive_stats.ipynb",
        "02_distributions.ipynb",
        "03_probability_basics.ipynb",
        "04_hypothesis_testing.ipynb",
        "05_correlation_vs_causation.ipynb",
        "06_central_limit_theorem.ipynb",
    ],
    "Phase3_SQL": [
        "01_basics.sql",
        "02_aggregations.sql",
        "03_joins.sql",
        "04_subqueries_ctes.sql",
        "05_window_functions.sql",
    ],
    "Phase4_MachineLearning": [
        "01_ml_workflow.ipynb",
        "02_linear_regression.ipynb",
        "03_logistic_regression.ipynb",
        "04_decision_trees_random_forest.ipynb",
        "05_kmeans_clustering.ipynb",
        "06_knn_classifier.ipynb",
        "07_model_evaluation.ipynb",
        "08_overfitting_and_fixes.ipynb",
        "09_feature_engineering.ipynb",
    ],
    "Phase5_Interview_Prep": [
        "sql_interview_practice.sql",
        "python_interview_practice.ipynb",
        "statistics_qa.md",
        "ml_concepts_qa.md",
        "case_studies.md",
    ],
    "Projects": [
        "Project1_EDA/.gitkeep",
        "Project2_ML/.gitkeep",
    ],
    "Checkpoints": [
        "checkpoint1_notes.md",
        "checkpoint2_notes.md",
        "checkpoint3_notes.md",
        "checkpoint4_notes.md",
    ],
}

def make_notebook(title, phase):
    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.10.0"}
        },
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {title}\n\n",
                    f"**Phase:** {phase}  \n",
                    "**Status:** 🔴 Not Started  \n",
                    "**Date Started:**  \n\n",
                    "---\n\n",
                    "## Theory Notes\n\n\n",
                    "## Code Practice\n\n\n",
                    "## Key Takeaways\n"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": ["# Your code here\n"]
            }
        ]
    }

def make_sql(title, phase):
    return f"-- {title}\n-- Phase: {phase}\n-- Status: Not Started\n-- Date Started:\n\n-- Theory Notes:\n\n\n-- Practice Queries:\n\n"

def make_md(title, phase):
    return f"# {title}\n\n**Phase:** {phase}  \n**Status:** Not Started  \n**Date Started:**  \n\n---\n\n## Notes\n\n\n## Interview Q&A\n\n\n## Key Takeaways\n"

created = 0
for folder, files in structure.items():
    for filename in files:
        filepath = os.path.join(folder, filename)
        dirpath = os.path.dirname(filepath)
        os.makedirs(dirpath, exist_ok=True)
        
        if filename.endswith(".gitkeep"):
            open(filepath, "w").close()
        else:
            base = os.path.basename(filename)
            title = base.replace(".ipynb","").replace(".sql","").replace(".md","").replace("_"," ").title()
            if filename.endswith(".ipynb"):
                with open(filepath, "w") as f:
                    json.dump(make_notebook(title, folder), f, indent=1)
            elif filename.endswith(".sql"):
                with open(filepath, "w") as f:
                    f.write(make_sql(title, folder))
            elif filename.endswith(".md"):
                with open(filepath, "w") as f:
                    f.write(make_md(title, folder))
        
        created += 1
        print(f"  ✅ {filepath}")

print(f"\n🎉 Done! {created} files created across {len(structure)} folders.")