import os
import matplotlib.pyplot as plt
import pandas as pd


def main():
    os.makedirs("plots", exist_ok=True)

    data_path = os.path.join("data", "processed_student_performance.csv")
    if not os.path.exists(data_path):
        data_path = os.path.join("data", "student_performance.csv")
    
    df = pd.read_csv(data_path)

    plt.figure(figsize=(14, 6))
    sample_df = df.iloc[:25]
    plt.bar(sample_df["Student"], sample_df["Final_Score"], color="royalblue", edgecolor="black")
    plt.title("Student Names vs Final Scores (Sample)", fontsize=14)
    plt.xlabel("Student Name", fontsize=12)
    plt.ylabel("Final Score", fontsize=12)
    plt.xticks(rotation=45, ha="right", fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join("plots", "final_scores.png"), dpi=300)
    plt.close()
    print("Saved plots/final_scores.png")

    plt.figure(figsize=(8, 5))
    plt.scatter(df["Hours_Studied"], df["Final_Score"], color="crimson", edgecolors="black", alpha=0.8)
    plt.title("Hours Studied vs Final Score", fontsize=14)
    plt.xlabel("Hours Studied", fontsize=12)
    plt.ylabel("Final Score", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join("plots", "study_vs_score.png"), dpi=300)
    plt.close()
    print("Saved plots/study_vs_score.png")

    plt.figure(figsize=(8, 5))
    plt.hist(df["Final_Score"], bins=10, color="mediumseagreen", edgecolor="black")
    plt.title("Distribution of Final Scores", fontsize=14)
    plt.xlabel("Final Score", fontsize=12)
    plt.ylabel("Frequency (Number of Students)", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join("plots", "score_distribution.png"), dpi=300)
    plt.close()
    print("Saved plots/score_distribution.png")

    plt.figure(figsize=(8, 5))
    plt.scatter(df["Attendance"], df["Final_Score"], color="purple", edgecolors="black", alpha=0.8)
    plt.title("Attendance vs Final Score", fontsize=14)
    plt.xlabel("Attendance (%)", fontsize=12)
    plt.ylabel("Final Score", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join("plots", "custom_plot.png"), dpi=300)
    plt.close()
    print("Saved plots/custom_plot.png")


if __name__ == "__main__":
    main()