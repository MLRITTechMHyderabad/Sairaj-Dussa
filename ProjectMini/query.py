import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="youtube_2k25"
)
cursor = connection.cursor()

#Total number of videos
query_total_videos = """
SELECT SUM(Total_Video_Count) AS Total_Videos FROM youtube_dataset;
"""
cursor.execute(query_total_videos)
result = cursor.fetchall()
print(f"Total Videos Across All Channels: {result[0][0]}")

#Top performing channels by subscribers
query_top_channels = """
SELECT Channel_Name, Total_Subscribers 
FROM youtube_dataset 
ORDER BY Total_Subscribers DESC 
LIMIT 10;
"""
cursor.execute(query_top_channels)
top_channels = cursor.fetchall()
df_top_channels = pd.DataFrame(top_channels, columns=['Channel Name', 'Total Subscribers'])
print("\nTop Channels by Subscriber Count:")
print(df_top_channels)

#Average video length
query_avg_video_length = """
SELECT AVG(Avg_Video_Length_min) AS Avg_Video_Length 
FROM youtube_dataset;
"""
cursor.execute(query_avg_video_length)
avg_video_length = cursor.fetchall()
print(f"\nAverage Video Length: {avg_video_length[0][0]:.2f} minutes")

#AI Content Percentage Distribution
query_ai_content_distribution = """
SELECT MIN(AI_Content_Percentage) AS Min_Percentage, 
       MAX(AI_Content_Percentage) AS Max_Percentage, 
       AVG(AI_Content_Percentage) AS Avg_Percentage 
FROM youtube_dataset;
"""
cursor.execute(query_ai_content_distribution)
ai_content_distribution = cursor.fetchall()
print("\nAI Content Percentage Distribution:")
print(f"Minimum: {ai_content_distribution[0][0]:.2f}%")
print(f"Maximum: {ai_content_distribution[0][1]:.2f}%")
print(f"Average: {ai_content_distribution[0][2]:.2f}%")

#Impact of Metaverse Level on Engagement Score
query_metaverse_impact = """
SELECT Metaverse_Level, AVG(Engagement_Score) AS Avg_Engagement_Score 
FROM youtube_dataset 
GROUP BY Metaverse_Level;
"""
cursor.execute(query_metaverse_impact)
metaverse_impact = cursor.fetchall()
df_metaverse_impact = pd.DataFrame(metaverse_impact, columns=['Metaverse Level', 'Average Engagement Score'])
print("\nImpact of Metaverse Level on Engagement Scores:")
print(df_metaverse_impact)

#Quantum Computing Topics
query_quantum_topics = """
SELECT Quantum_Computing_Topics, COUNT(*) AS Topic_Count 
FROM youtube_dataset 
GROUP BY Quantum_Computing_Topics 
ORDER BY Topic_Count DESC;
"""
cursor.execute(query_quantum_topics)
quantum_topics = cursor.fetchall()
df_quantum_topics = pd.DataFrame(quantum_topics, columns=['Quantum Computing Topic', 'Topic Count'])
print("\nChannels Discussing Quantum Computing Topics:")
print(df_quantum_topics)

#Holographic Content Rating Distribution
query_holographic_distribution = """
SELECT Holographic_Content_Rating, COUNT(*) AS Rating_Count 
FROM youtube_dataset 
GROUP BY Holographic_Content_Rating 
ORDER BY Rating_Count DESC;
"""
cursor.execute(query_holographic_distribution)
holographic_distribution = cursor.fetchall()
df_holographic_distribution = pd.DataFrame(holographic_distribution, columns=['Holographic Content Rating', 'Rating Count'])
print("\nHolographic Content Rating Distribution:")
print(df_holographic_distribution)

cursor.close()
connection.close()
