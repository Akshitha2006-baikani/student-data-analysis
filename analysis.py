import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data.csv")

print("Dataset:\n", data)

# Calculate average marks
data['Average'] = data[['Maths', 'Science', 'English']].mean(axis=1)

# Find topper
topper = data.loc[data['Average'].idxmax()]
print("\nTopper:\n", topper)

# Find lowest performer
lowest = data.loc[data['Average'].idxmin()]
print("\nLowest Performer:\n", lowest)

# Find subject topper
maths_topper = data.loc[data['Maths'].idxmax()]
print("\nMaths Topper:", maths_topper['Name'])

# Overall average
overall_avg = data['Average'].mean()
print("\nOverall Average:", overall_avg)

# Subject-wise average
subject_avg = data[['Maths', 'Science', 'English']].mean()
print("\nSubject-wise Average:\n", subject_avg)

# Sort students by performance
sorted_data = data.sort_values(by='Average', ascending=False)
print("\nRanked Students:\n", sorted_data[['Name', 'Average']])

# Plot subject averages
subject_avg.plot(kind='bar')
plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Save graph as image
plt.savefig("subject_average.png")
print("Graph saved as subject_average.png")