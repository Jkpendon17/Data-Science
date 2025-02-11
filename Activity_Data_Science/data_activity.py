import pandas as pd
import matplotlib .pyplot as plt
df = pd.read_csv("students_scores.csv")


# print(df.head())
# print(df.shape)
# print(df.columns)
# print("Average Score: ", df["Score"].mean())
# print("Highest Score: ",df["Score"].max())
# print("Lowest Score: ", df["Score"].min())
plt.bar(df["Name"], df["Score"])
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Stu3.Basic Data Analysis") 


#Display column names
print(df.columns)
#Display Average Score
print("Average Score", df["Score"].mean())
#Display highest and lowest scores
print("Highest Score:", df["Score"].max())
print("Lowest Score", df["Score"].min())
plt.title("Student Scores")
plt.xticks(rotation=45)
plt.show()

