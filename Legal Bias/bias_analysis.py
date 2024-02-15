import json
import sys
import re
import pandas as pd

modelNames = ['alpha','beta','delta','epsilon','eta','gamma','iota','theta','zeta']

# Load data for all LLMs
llm_data = {}
for model_name in modelNames:
    file_path = f'promptDetails/{model_name}/details.tsv'
    llm_data[model_name] = pd.read_csv(file_path, sep='\t')

# Calculate bias scores for each LLM
bias_scores = {}
for model_name, data in llm_data.items():
    # Group data by identity term and gender, and calculate proportion of "Yes" predictions
    bias_scores[model_name] = data.groupby(['identity term', 'gender'])['pred outputs'].apply(lambda x: (x == 'Yes').mean())

# Normalize bias scores
for model_name, scores in bias_scores.items():
    max_score = scores.max()
    min_score = scores.min()
    bias_scores[model_name] = (scores - min_score) / (max_score - min_score)

# Compare bias scores across LLMs
for model_name, scores in bias_scores.items():
    print(f"Normalized Bias Scores for LLM {model_name}:")
    print(scores)

# Identify most and least biased LLMs
most_biased_llm = max(bias_scores, key=bias_scores.get)
least_biased_llm = min(bias_scores, key=bias_scores.get)
print(f"Most Biased LLM: {most_biased_llm}")
print(f"Least Biased LLM: {least_biased_llm}")
