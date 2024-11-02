import pandas as pd

def preprocess():
    # Read the CSV files
    df = pd.read_csv('athlete_events.csv')
    region_df = pd.read_csv('noc_regions.csv')
    
    # Filter for Summer Olympics
    df = df[df['Season'] == 'Summer']
    
    # Merge with region_df
    df = df.merge(region_df, on='NOC', how='left')
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # Create medal columns
    medal_dummies = pd.get_dummies(df['Medal'])
    
    # Rename columns to ensure correct names
    if 'Gold' not in medal_dummies.columns:
        medal_dummies['Gold'] = 0
    if 'Silver' not in medal_dummies.columns:
        medal_dummies['Silver'] = 0
    if 'Bronze' not in medal_dummies.columns:
        medal_dummies['Bronze'] = 0
    
    # Add the medal columns to the main dataframe
    df['Gold'] = medal_dummies['Gold']
    df['Silver'] = medal_dummies['Silver']
    df['Bronze'] = medal_dummies['Bronze']
    
    # Ensure region column exists
    if 'region' not in df.columns and 'Region' in df.columns:
        df['region'] = df['Region']
    
    # Fill NaN values in region with NOC code
    df['region'] = df['region'].fillna(df['NOC'])
    
    return df