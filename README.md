# Thiranex-Task-1
Data Cleaning &amp; Visualization Project
# IPL 2026 Data Cleaning & Insights Dashboard

## Overview

This project performs data cleaning, preprocessing, and exploratory data analysis (EDA) on an IPL 2026 match dataset. The script handles missing and inconsistent values, removes duplicate records, and generates a visual dashboard containing key insights about team performance, toss strategies, and city-wise scoring trends.

The final output is a high-resolution dashboard image that summarizes important statistics from the cleaned dataset.

---

## Features

### Data Cleaning

* Removes duplicate match records.
* Fills missing city values using venue information.
* Detects and corrects invalid team scores.
* Imputes missing numerical values using median-based strategies.
* Fills missing categorical values using the most frequent category (mode).

### Data Analysis

* Distribution of Team 1 scores.
* Average runs scored by each team.
* Toss decision trends across the season.
* City-wise average runs based on toss decisions.

### Visualization Dashboard

1. **Distribution of Team 1 Scores**

   * Histogram with KDE curve.
   * Displays score frequency and distribution.

2. **Average Runs by Team**

   * Horizontal bar chart.
   * Compares team batting performance.

3. **Toss Decision Strategy**

   * Pie chart showing the proportion of "Bat" vs "Field" decisions.

4. **Average Runs by City and Toss Decision**

   * Grouped bar chart.
   * Compares scoring trends across venues and toss strategies.

---

## Dataset Requirements

The script expects a CSV file named:

```text
uncleaned_ipl_matches_2026.csv
```

### Required Columns

```text
team1
team1_runs
city
venue
toss_decision
toss_winner
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## Project Structure

```text
project/
│
├── uncleaned_ipl_matches_2026.csv
├── ipl_dashboard.py
├── ipl_2026_dashboard_clean_bars.png
└── README.md
```

---

## How to Run

Execute the Python script:

```bash
python ipl_dashboard.py
```

The script will:

1. Load the dataset.
2. Clean and preprocess the data.
3. Generate visualizations.
4. Save the dashboard as:

```text
ipl_2026_dashboard_clean_bars.png
```

5. Display the dashboard on screen.

---

## Data Cleaning Logic

### City Imputation

If the city value is missing, the script searches the venue name for known IPL host cities and automatically assigns the appropriate city.

### Score Validation

Valid Team 1 scores are assumed to be within:

```text
0 – 300 runs
```

Scores outside this range or missing values are replaced using:

1. Team-specific median score.
2. Overall median score if team data is unavailable.

### Toss Information

Missing values in:

* toss_decision
* toss_winner

are filled using the most frequent value found in the dataset.

---

## Output

### Dashboard Image

The generated dashboard includes:

* Team score distribution
* Team-wise average runs
* Toss strategy analysis
* City-wise scoring comparison

Output file:

```text
ipl_2026_dashboard_clean_bars.png
```

---

## Learning Outcomes

This project demonstrates:

* Data cleaning and preprocessing
* Missing value imputation
* Feature extraction from text
* GroupBy aggregations
* Statistical visualization
* Dashboard creation using Matplotlib and Seaborn
* Exploratory Data Analysis (EDA)

---

## Future Enhancements

* Add win probability analysis.
* Analyze toss winner vs match winner correlation.
* Include interactive dashboards using Plotly.
* Add team-wise and player-wise performance metrics.
* Automate report generation.

---
