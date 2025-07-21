import pandas as pd

df = pd.read_excel('Cleaned_Dataset.xlsx')
user_stats = df[['Username', 'User_Post_Count', 'Average_Likes_Post']].drop_duplicates()
user_stats.to_csv('user_stats.csv', index=False)