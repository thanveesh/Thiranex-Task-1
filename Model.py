import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")
df = pd.read_csv("uncleaned_ipl_matches_2026.csv")
df.drop_duplicates(inplace=True)
def extract_city(row):
    if pd.isnull(row["city"]):
        venue = str(row["venue"]).lower()
        for city_name in [
            "delhi",
            "jaipur",
            "ahmedabad",
            "kolkata",
            "dharamsala",
            "bengaluru",
            "mumbai",
            "lucknow",
            "hyderabad",
            "chennai",
            "guwahati",
            "chandigarh",
            "raipur",
        ]:
            if city_name in venue:
                return (
                    "Chandigarh"
                    if city_name == "chandigarh"
                    else city_name.capitalize()
                )
    return row["city"]

df["city"] = df.apply(extract_city, axis=1)
valid_runs_mask = (df["team1_runs"] >= 0) & (df["team1_runs"] <= 300)
overall_median = df[valid_runs_mask]["team1_runs"].median()
def impute_runs(row):
    runs = row["team1_runs"]
    if pd.isnull(runs) or runs < 0 or runs > 300:
        team_mask = valid_runs_mask & (df["team1"] == row["team1"])
        team_median = df[team_mask]["team1_runs"].median()
        return team_median if not pd.isnull(team_median) else overall_median
    return runs
df["team1_runs"] = df.apply(impute_runs, axis=1)
toss_decision_mode = df["toss_decision"].mode()[0]
df["toss_decision"] = df["toss_decision"].fillna(toss_decision_mode)
toss_winner_mode = df["toss_winner"].mode()[0]
df["toss_winner"] = df["toss_winner"].fillna(toss_winner_mode)
fig, axes = plt.subplots(2, 2, figsize=(18, 14), layout="constrained")
fig.suptitle(
    "IPL 2026 Season - Key Insights Dashboard", fontsize=22, fontweight="bold"
)
sns.histplot(
    data=df, x="team1_runs", bins=15, kde=True, ax=axes[0, 0], color="skyblue"
)
axes[0, 0].set_title(
    "Distribution of Team 1 Scores", fontsize=14, pad=10
)
axes[0, 0].set_xlabel("Runs", fontsize=12)
axes[0, 0].set_ylabel("Count", fontsize=12)
avg_runs = (
    df.groupby("team1")["team1_runs"].mean().sort_values(ascending=False)
)
sns.barplot(
    x=avg_runs.values, y=avg_runs.index, ax=axes[0, 1], palette="viridis"
)
axes[0, 1].set_title("Average Runs Scored by Team 1", fontsize=14, pad=10)
axes[0, 1].set_xlabel("Average Runs", fontsize=12)
axes[0, 1].set_ylabel("", fontsize=12)
toss_counts = df["toss_decision"].value_counts()
axes[1, 0].pie(
    toss_counts,
    labels=toss_counts.index,
    autopct="%1.1f%%",
    pctdistance=0.75,
    startangle=90,
    colors=["#ff9999", "#66b3ff"],
    textprops={"fontsize": 12},
)
axes[1, 0].set_title(
    "Toss Decisions Strategy", fontsize=14, pad=10
)
city_avg_order = (
    df.groupby("city")["team1_runs"].mean().sort_values(ascending=False).index
)
sns.barplot(
    data=df,
    x="team1_runs",
    y="city",
    hue="toss_decision",
    ax=axes[1, 1],
    palette=["#ff9999", "#66b3ff"],  # Using identical match colors to the pie chart
    order=city_avg_order,
    errorbar=None,
    hue_order=["bat", "field"],  # Enforces explicit ordering
)
axes[1, 1].set_title(
    "Average Runs by City & Toss Decision (Sorted)", fontsize=14, pad=10
)
axes[1, 1].set_xlabel("Average Innings Runs", fontsize=12)
axes[1, 1].set_ylabel("", fontsize=12)
axes[1, 1].legend(
    title="Toss Decision", loc="lower right", frameon=True, shadow=True
)
plt.savefig(
    "ipl_2026_dashboard_clean_bars.png", dpi=300, bbox_inches="tight"
)
plt.show()