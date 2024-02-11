# This code is for collecting all the stereotypical tuples from the datasets used in nlp-fairness-for-india
import pandas as pd

filePaths = ['nlp-fairness-for-india-main/region_individual_annotation.tsv','nlp-fairness-for-india-main/religion_individual_annotation.tsv']

for filePath in filePaths:
    df = pd.read_csv(filePath, sep="\t")
    
    filePath = filePath.removeprefix('nlp-fairness-for-india-main/')
    filePath = filePath.removesuffix('_individual_annotation.tsv')
    
    stereotypical_df = df[df["annotation"] == "Stereotypical"]
    stereotypical_tuples = stereotypical_df[["identity term", "attribute token"]]
    stereotypical_tuples.drop_duplicates(inplace=True)
    
    finalPath = filePath + "_stereotypes.tsv"
    stereotypical_tuples.to_csv(finalPath, sep="\t", index=False)
