import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# load dataset (repalce'movie_rating.csv with your actual file')
df = pd.read_csv('movie_rating.csv')

# display the basic info
print(df.head())
print(df.info())

# Date cleaning
df.dropna(inplace=True)
#
# Calculate averge ratings
averge_ratings = df.groupby('movie')['rating'].mean()


# Find most rated movies
most_rated = df.groupby('movie')['rating'].count().sort_values(ascending=False)

# Find the top user who rated the most movie
top_user = df.groupby('user')['rating'].count().sort_values(ascending=False)

#convert to dataFrames for saving
average_ratings_df = averge_ratings.reset_index()
print("\n🎬 Average Ratings of Movies:")
print(average_ratings_df)
      
most_rated_df = most_rated.reset_index()
print("\n🔥 Most Rated Movies:")
print(most_rated_df)

# Bar Chart - top rating
plt.figure(figsize=(8, 5))
sns.barplot(x=most_rated.index, y=most_rated.values, palette='viridis')
plt.xlabel("Movies")
plt.ylabel("Number of Ratings")
plt.title("🔥 Most Rated Movies")
plt.xticks(rotation=45)
plt.show()


top_user_df = top_user.reset_index()
print("\n👑 Top Users Who Rated Most:")
print(top_user_df)

# Bar Chart - Top users
plt.figure(figsize=(8, 5))
sns.barplot(x=top_user.index, y=top_user.values, palette='coolwarm')
plt.xlabel("Users")
plt.ylabel("Number of Ratings")
plt.title("👑 Users Who Rated the Most") 
plt.xticks(rotation=45)
plt.show()


# save processed data
average_ratings_df.to_csv('averge_ratings.csv',index=False)
print("\n✅ CSV file saved successfully: 'average_ratings.csv'")

most_rated_df.to_csv('most_rating.csv',index=False)
top_user_df.to_csv('top_user.csv',index=False)

print("Analysis Complete. Processed data saved.")

