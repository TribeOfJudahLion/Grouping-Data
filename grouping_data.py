import numpy as np
import pandas as pd
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def load_data(file_path):
    """Load the dataset from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Dataset loaded successfully with shape: {data.shape}")
        return data
    except FileNotFoundError:
        logging.error(f"The file {file_path} was not found.")
        return None
    except Exception as e:
        logging.error(f"An error occurred while loading the dataset: {e}")
        return None


def preprocess_data(data):
    """Preprocess the dataset by selecting relevant columns."""
    columns = [
        'ID', 'Year_Birth', 'Education', 'Marital_Status',
        'Income', 'Kidhome', 'Teenhome', 'Dt_Customer',
        'Recency', 'NumStorePurchases', 'NumWebVisitsMonth'
    ]
    return data[columns]


def analyze_data(data):
    """Perform data analysis."""
    # Inspect first 2 rows and data types of the dataset
    print("\nFirst 2 rows of the dataset:")
    print(data.head(2).T)

    print("\nData types of the dataset:")
    print(data.dtypes)

    # Display the shape of the dataset
    print("\nShape of the dataset:")
    print(data.shape)

    # Check the average number of store purchases of customers based on number of kids in the home
    average_purchases = data.groupby('Kidhome')['NumStorePurchases'].mean()
    print("\nAverage number of store purchases based on number of kids in the home:")
    print(average_purchases)


def main():
    # Define the path to the CSV file
    file_path = 'marketing_campaign.csv'  # Replace with the path to your CSV file

    # Check if the provided path is valid
    if not Path(file_path).is_file():
        logging.error("The provided file path does not exist.")
        return

    data = load_data(file_path)
    if data is not None:
        data = preprocess_data(data)
        analyze_data(data)


if __name__ == "__main__":
    main()
