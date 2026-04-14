# Handwriting Recognition & Person Identification — ML Mentoring Course

## Course Overview

**Duration:** 9 classes × 1h30min each\
**Framework:** scikit-learn focused\
**Target Audience:** Students with Python knowledge and basic ML mathematics\
**Approach:** Hands-on, practical — every class produces a working ML model applied to handwriting analysis

______________________________________________________________________

## Learning Objectives

By the end of this course, students will be able to:

- Apply fundamental ML algorithms to handwriting and image data
- Use scikit-learn for classification, regression, clustering, and dimensionality reduction
- Choose the right algorithm for a given problem
- Evaluate model performance rigorously and avoid common pitfalls
- Build systems capable of identifying individuals from their handwriting patterns

______________________________________________________________________

## Class Structure

Every class follows the same 90-minute template:

| Block | Duration | Content | |---|---|---| | Setup & Motivation | 15 min | Review, dataset intro, learning objectives
| | Hands-On Implementation | 55 min | Step-by-step coding and exploration | | Interpretation & Discussion | 15 min |
Results analysis, real-world connections | | Wrap-up & Preview | 5 min | Key concepts, assignment, next class |

______________________________________________________________________

## Curriculum

| # | Topic | Algorithm | Application | |---|---|---|---| | 01 | Introduction to ML & Digit Recognition | k-Nearest
Neighbors | Handwritten digit classification | | 02 | Decision Trees & Character Features | Decision Tree | Letter
recognition (A–Z) | | 03 | Linear Regression & Handwriting Metrics | Linear Regression | Predicting writing speed from
pen features | | 04 | Logistic Regression & Writer Classification | Logistic Regression | Binary writer classification |
| 05 | Ensemble Methods | Random Forest | Multi-person handwriting identification | | 06 | Support Vector Machines | SVM
(kernels) | Advanced person identification | | 07 | Clustering & Writing Style Discovery | K-Means, Hierarchical |
Unsupervised writing style grouping | | 08 | Dimensionality Reduction & Visualization | PCA, t-SNE | Visualizing
handwriting feature space | | 09 | Model Evaluation & Validation | Cross-validation, statistical testing | Comprehensive
evaluation strategies |

______________________________________________________________________

## Agents

| Agent | Purpose | Call when | |---|---|---| | **magus** | Q&A — answers questions about the course content and ML
concepts | You have a question about an algorithm, concept, or result | | **lucca** | Content creation — generates
notebooks, code, teacher notes | You need to create or update class materials |

______________________________________________________________________

## Technical Setup

```bash
# Install dependencies
poetry install

# Launch Jupyter
jupyter lab
```

All dependencies are declared in `pyproject.toml`. Python 3.13 or higher required.

______________________________________________________________________

## Repository Structure

```
clean/
├── .github/extensions/   # Agent definitions (magus, lucca)
├── instructions/         # Content creation guidelines for Lucca
├── class-01/             # Already taught — complete materials
├── class-02/ to 09/      # Scaffolded — Lucca generates notebooks
├── pyproject.toml        # Dependencies and tooling config
└── .pre-commit-config.yaml
```
