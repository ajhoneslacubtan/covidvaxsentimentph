# Philippine COVID-19 Vaccine Sentiment Analysis

## Overview
This repository contains code and data for performing sentiment analysis on Philippine COVID-19 vaccine-related tweets and Reddit posts. The sentiment analysis is performed using four different models: LSTM, Bidirectional LSTM, CNN-LSTM, and CNN. The data were collected by scraping Twitter and Reddit, and then manually labeled using Label Studio. The feature extraction method used in this analysis is Word2Vec, and a pre-trained Word2Vec model from [Filipino Word Embeddings repository](https://github.com/danjohnvelasco/Filipino-Word-Embeddings) is used.

## Models Used
- LSTM
- Bidirectional LSTM
- CNN-LSTM
- CNN

## Data Collection
The data for this sentiment analysis project were scraped from Twitter and Reddit. The data collection process involved fetching tweets and Reddit posts related to COVID-19 vaccines in the Philippines. The data were then manually labeled for sentiment analysis using Label Studio.

## Feature Extraction
Feature extraction is done using Word2Vec, which is a popular technique for word embedding. A pre-trained Word2Vec model from the [Filipino Word Embeddings repository](https://github.com/danjohnvelasco/Filipino-Word-Embeddings) is used to convert the text data into numerical vectors, which are then used as input to the sentiment analysis models.

## Installation
To install the necessary dependencies for this project, you can use the `requirements.txt` file. Follow the instructions below:

1. Clone this repository:
```
git clone https://github.com/ajhoneslacubtan/covidvaxsentimentph/
cd philippine-covid-vaccine-sentiment
```

2. Set up a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```
pip install -r requirements.txt
```


4. Download the pre-trained Word2Vec model:
- Go to the [Filipino Word Embeddings repository](https://github.com/danjohnvelasco/Filipino-Word-Embeddings).
- Download the pre-trained Word2Vec model and place it in a `word2vec` directory of this project.

## Usage
Once you have installed the required dependencies and downloaded the pre-trained Word2Vec model, you can run the sentiment analysis using the provided Jupyter notebooks.

1. Open the Jupyter notebooks or Python scripts for the specific model you want to run.
2. Execute the code cells or run the scripts to perform sentiment analysis on the data.

## Acknowledgments
We would like to thank [Filipino Word Embeddings](https://github.com/danjohnvelasco/Filipino-Word-Embeddings) for providing the pre-trained Word2Vec model, which significantly improved the performance of this sentiment analysis project.
