# Predictive Maintenance in Manufacturing

### Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [Data Collection](#data-collection)
4. [Data Exploration](#data-exploration)
5. [Data Preparation](#data-preparation)
6. [Modeling](#modeling)
7. [Model Assessment](#model-assessment)
8. [Model Deployment](#model-deployment)
9. [Contributing](#contributing)
10. [License](#license)

## Introduction

This project focuses on using machine learning algorithms to predict maintenance needs in manufacturing. Predictive maintenance helps industries minimize downtime and increase efficiency by identifying when equipment or machinery is likely to fail so that maintenance can be scheduled proactively.

## Getting Started

### Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Jupyter Notebook
- Required Python packages (NumPy, Pandas, Scikit-Learn, Flask)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/predictive-maintenance.git
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Data Collection

We utilized the AI4I 2020 Predictive Maintenance Dataset, which reflects the functioning of milling machines in the industry. The dataset contains various attributes such as UID, Product ID, Type, Air Temperature [K], Process Temperature [K], Rotational Speed [rpm], Torque [Nm], Tool Wear [min], and Machine Failure Label.

## Data Exploration

In this phase, we conducted exploratory data analysis to gain insights into the dataset's structure, distribution, and relationships. We used various statistical measures and visualizations, including histograms, box plots, and scatter plots.

## Data Preparation

Data preparation is a critical step in building machine learning models. We performed several data preprocessing tasks, including feature engineering, categorical encoding, handling outliers, standardization, feature selection, and addressing imbalances in the dataset.

## Modeling

We approached this problem as a classification task, with the goal of classifying data instances as failures or non-failures. We trained and evaluated multiple machine learning models, including Decision Trees, Random Forest, Logistic Regression, and K-Nearest Neighbor (KNN).

## Model Assessment

To assess the performance of our classification models, we used several evaluation metrics, including accuracy, recall, precision, F1 score, true positive rate, and true negative rate. These metrics provide insights into how well the models perform in identifying failures.

## Model Deployment

We deployed our best-performing model using Flask, creating a web service that allows users to interact with the model. Users can input data, and the model will predict whether a failure is likely to occur.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Test your changes
5. Submit a pull request

