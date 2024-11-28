import re
import os
import logging
from datasets import load_dataset

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create directories if they don't exist
def create_directories(dirs):
    for directory in dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logging.info(f"Created directory: {directory}")
        else:
            logging.info(f"Directory already exists: {directory}")

# Preprocess text: remove URLs, mentions, special characters, and convert to lowercase
def preprocess_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)     # Remove mentions
    text = re.sub(r'[^\w\s]', '', text) # Remove special characters
    text = text.lower().strip()           # Convert to lowercase and strip whitespace
    return text

# Load Hugging Face dataset
def load_hf_dataset(dataset_name):
    try:
        dataset = load_dataset(dataset_name)
        logging.info(f"Successfully loaded dataset: {dataset_name}")
        return dataset
    except Exception as e:
        logging.error(f"Failed to load dataset {dataset_name}: {e}")
        raise

# Save processed data to a file
def save_processed_data(data, file_path):
    try:
        with open(file_path, 'w') as f:
            for prompt, answer in data:
                f.write(f"PROMPT: {prompt}\nANSWER: {answer}\n\n")
        logging.info(f"Data successfully saved to {file_path}")
    except Exception as e:
        logging.error(f"Failed to save data to {file_path}: {e}")
        raise

# Apply preprocessing to a dataset split
def preprocess_dataset(dataset_split):
    logging.info("Preprocessing dataset split...")
    processed_pairs = [(preprocess_text(example[0]['content']), preprocess_text(example[1]['content'])) for example in dataset_split['messages']]
    logging.info("Preprocessing complete.")
    return processed_pairs

# Define directories
RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"

# Create necessary directories
create_directories([RAW_DATA_DIR, PROCESSED_DATA_DIR])

# Load the dataset
def preprocess_hf_dataset(dataset_name = "MBZUAI-Paris/DarijaBench"):
    dataset = load_hf_dataset(dataset_name)

    # Preprocess train, validation, and test splits
    for split in dataset:
        logging.info(f"Processing {split} split...")
        processed_data = preprocess_dataset(dataset[split])
        output_file = f"{PROCESSED_DATA_DIR}/{split}.txt"
        save_processed_data(processed_data, output_file)

    logging.info("Preprocessing complete. All processed files are saved in data/processed/")
