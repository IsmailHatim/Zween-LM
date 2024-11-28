# Zween-LM

**Fine-Tuning LLaMa for Darija (Moroccan Arabic)**

Zween-LM is an open-source project that aims to adapt the LLaMa language model to the darija dialect (Moroccan Arabic), making large language models more accessible to low-resource linguistic communities. By fine-tuning LLaMa on darija, this project enhances language understanding and generation capabilities in a dialect that is often overlooked by mainstream NLP models.

## Project Overview

The repository contains all necessary resources to fine-tune, evaluate, and utilize a LLaMa model on darija data. This includes data collection and preprocessing scripts, model training configurations, and evaluation metrics to ensure high-quality results.

### Key Features
- **Fine-Tuning on Darija**: Utilize HuggingFace's Transformers and LLaMa to adapt the model for dialectal Arabic.
- **Data Preprocessing**: Scripts for collecting and preparing datasets specific to darija.
- **Evaluation Metrics**: Analyze the performance using perplexity, BLEU scores, and other NLP metrics.
- **Linguistic Inclusivity**: Addressing the need for better support for low-resource languages.

## Repository Structure
- **`data/`**: Contains raw and processed datasets in darija.
- **`src/`**: Python scripts for data preprocessing, model training, and evaluation.
- **`notebooks/`**: Jupyter notebooks for exploring and experimenting with data and models.
- **`models/`**: Fine-tuned LLaMa model and tokenizer.
- **`results/`**: Evaluation metrics, graphs, and analysis results.
- **`scripts/`**: Shell scripts for automating data processing, training, and evaluation.

## Getting Started

### Prerequisites
- Python 3.8+
- GPU with CUDA support (recommended for training)
- Packages in `requirements.txt` (use `pip install -r requirements.txt`)

### Fine-Tuning the Model
1. **Prepare the Data**: Use `src/data_preprocessing.py` to clean and prepare raw data.
2. **Train the Model**: Run `src/model_training.py` to start the fine-tuning process. You can adjust training parameters as needed.
3. **Evaluate Performance**: Use `src/evaluation.py` to evaluate the model on test data and view performance metrics.

## Usage
After fine-tuning, you can use the model to generate text in darija or perform other NLP tasks. Examples of usage can be found in the `notebooks/` directory.

## Contributing
Contributions are welcome! Please see `CONTRIBUTING.md` for guidelines on how to contribute to this project.

## Acknowledgements
- Thanks to the HuggingFace team for providing the Transformers library.
- Inspired by the LLaMa model by Meta AI.
- Special thanks to bdr-darija community supporting linguistic inclusivity in NLP.

---

Feel free to explore, use, and contribute to Zween-LM.
