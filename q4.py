import numpy as np


def main():

    hours_studied = np.array([6.9, 3.8, 6.8, 5.4, 1.2, 7.3, 5.8, 7.8, 5.9, 2.0])
    attendance = np.array([100, 85, 73, 73, 78, 96, 69, 87, 81, 76])
    previous_scores = np.array([52, 74, 49, 78, 77, 49, 83, 92, 95, 78])
    final_scores = np.array([60, 47, 41, 50, 35, 69, 53, 79, 67, 82])

    print("--- Shapes and Data Types ---")
    print(f"Hours Studied   - Shape: {hours_studied.shape}, Dtype: {hours_studied.dtype}")
    print(f"Attendance      - Shape: {attendance.shape}, Dtype: {attendance.dtype}")
    print(f"Previous Scores - Shape: {previous_scores.shape}, Dtype: {previous_scores.dtype}")
    print(f"Final Scores    - Shape: {final_scores.shape}, Dtype: {final_scores.dtype}\n")

    mean_score = np.mean(final_scores)
    max_score = np.max(final_scores)
    min_score = np.min(final_scores)
    std_score = np.std(final_scores)

    print("--- Final Scores Statistics ---")
    print(f"Mean Final Score: {mean_score:.2f}")
    print(f"Max Final Score:  {max_score}")
    print(f"Min Final Score:  {min_score}")
    print(f"Std Deviation:    {std_score:.2f}\n")

    bonus_scores = final_scores + 5
    print("--- Vectorized Operations ---")
    print("Original Scores:", final_scores)
    print("Scores with +5 Bonus:", bonus_scores, "\n")

    high_scorers_mask = final_scores >= 75
    filtered_scores = final_scores[high_scorers_mask]

    print("--- Boolean Indexing ---")
    print("Scores >= 75 Boolean Array:", high_scorers_mask)
    print("Scores >= 75 Filtered:", filtered_scores)


if __name__ == "__main__":
    main()