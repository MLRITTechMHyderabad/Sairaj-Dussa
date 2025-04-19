import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:root@localhost/youtube_2k25")
query = "SELECT * FROM youtube_dataset;"
df = pd.read_sql(query, engine)

def visualize_avg_video_length(df):
    if 'Avg_Video_Length_min' in df.columns and 'Total_Video_Count' in df.columns:
        video_length_counts = df.groupby("Avg_Video_Length_min")["Total_Video_Count"].sum()
        top_video_lengths = video_length_counts.nlargest(5)
        plt.figure(figsize=(10, 6))
        bar_positions = np.arange(len(top_video_lengths))
        plt.bar(bar_positions, top_video_lengths.values, color='royalblue', edgecolor='black', width=0.6)
        plt.xticks(bar_positions, top_video_lengths.index, fontsize=12, rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.title("Top 5 Most Common Avg Video Lengths by Video Count", fontsize=14, fontweight='bold')
        plt.xlabel("Avg Video Length (min)", fontsize=12)
        plt.ylabel("Total Number of Videos", fontsize=12)
        plt.tight_layout()
        plt.show()
    else:
        print("Required columns for 'Avg Video Length' visualization are missing.")

def visualize_channel_video_count(df):
    if 'Channel_Name' in df.columns and 'Total_Video_Count' in df.columns:
        top_channels = df.groupby("Channel_Name")["Total_Video_Count"].sum().sort_values(ascending=False).head(5)
        plt.figure(figsize=(10, 6))
        plt.barh(top_channels.index, top_channels.values, color='orange', edgecolor='black')
        plt.title("Top 5 Channels by Total Video Count", fontsize=14, fontweight='bold')
        plt.xlabel("Total Video Count", fontsize=12)
        plt.ylabel("Channel Name", fontsize=12)
        plt.tight_layout()
        plt.show()
    else:
        print("Required columns for 'Channel Video Count' visualization are missing.")


def visualize_total_subscribers(df):
    if 'Channel_Name' in df.columns and 'Total_Subscribers' in df.columns:
        unique_channels = df.groupby("Channel_Name")["Total_Subscribers"].max().reset_index()
        top_subscribers = unique_channels.sort_values("Total_Subscribers", ascending=False).head(10)
        plt.figure(figsize=(10, 6))
        plt.bar(top_subscribers["Channel_Name"], top_subscribers["Total_Subscribers"], 
                color='#6A0DAD', edgecolor='black', width=0.6)
        plt.title("Top 5 Channels by Subscriber Count", fontsize=14, fontweight='bold')
        plt.xlabel("Channel Name", fontsize=12)
        plt.ylabel("Total Subscribers", fontsize=12)
        plt.xticks(rotation=25, ha="right", fontsize=10)
        plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
        plt.grid(axis="y", linestyle="--", alpha=0.6)
        plt.tight_layout()
        plt.show()
    else:
        print("Required columns for 'Total Subscribers' visualization are missing.")


def visualize_holographic_content_rating(df):
    if 'Holographic_Content_Rating' in df.columns:
        holographic_counts = df['Holographic_Content_Rating'].value_counts()
        plt.figure(figsize=(10, 6))
        plt.bar(holographic_counts.index, holographic_counts.values, color='blue', edgecolor='black', width=0.6)
        plt.title("Holographic Content Rating Distribution")
        plt.xlabel("Content Rating")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()
    else:
        print("Column 'Holographic_Content_Rating' does not exist in the dataset.")

def visualize_neural_interface_compatibility(df):
    if 'Neural_Interface_Compatible' in df.columns:
        compatibility_counts = df['Neural_Interface_Compatible'].value_counts()
        colors = ['Blue', 'red'] 
        plt.figure(figsize=(8, 8))
        plt.pie(compatibility_counts, labels=compatibility_counts.index, autopct='%1.1f%%', colors=colors, startangle=90)
        plt.title("Neural Interface Compatibility Distribution")
        plt.tight_layout()
        plt.show()
    else:
        print("Column 'Neural_Interface_Compatible' does not exist in the dataset.")

def main():
    print("Starting Visualization Analysis...")

    visualize_avg_video_length(df)
    visualize_channel_video_count(df)
    visualize_total_subscribers(df)
    visualize_holographic_content_rating(df)
    visualize_neural_interface_compatibility(df)

if __name__ == "__main__":
    main()