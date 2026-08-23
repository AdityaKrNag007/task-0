import os
import pandas as pd


def main():
    csv_path = os.path.join("data", "student_performance.csv")
    df = pd.read_csv(csv_path)

    print("--- First 5 Rows ---")
    print(df.head(), "\n")

    print("--- Dataset Shape ---")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")

    print("--- Column Names ---")
    print(list(df.columns), "\n")

    print("--- Missing Values Count ---")
    print(df.isnull().sum(), "\n")

    avg_final = df["Final_Score"].mean()
    print("--- Average Final Score ---")
    print(f"Average Final Score: {avg_final:.2f}\n")

    top_student_row = df.loc[df["Final_Score"].idxmax()]
    print("--- Student with Highest Final Score ---")
    print(f"Student: {top_student_row['Student']} (Score: {top_student_row['Final_Score']})\n")

    df["Improvement"] = df["Final_Score"] - df["Previous_Score"]

    high_attendance_df = df[df["Attendance"] >= 80]
    print(f"--- Students with Attendance >= 80 (Count: {len(high_attendance_df)}) ---")
    print(high_attendance_df.head(), "\n")

    df_sorted = df.sort_values(by="Final_Score", ascending=False)

    output_path = os.path.join("data", "processed_student_performance.csv")
    df_sorted.to_csv(output_path, index=False)
    print(f"Processed dataset successfully saved to: {output_path}")


if __name__ == "__main__":
    main()