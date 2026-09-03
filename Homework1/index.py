#-------------------------------------------------------------------------
# AUTHOR: Sarah Liu
# FILENAME: index.py
# SPECIFICATION: Read the collection.csv file and create an inverted index 
# FOR: CS 4250 - Assignment #1
# TIME SPENT: 45 mins 
#-------------------------------------------------------------------------

# Importing Python libraries
import pandas as pd

# Reading the document collection
data = pd.read_csv("collection.csv")

# Defining the dictionary used for lemmatization
lemmas = {
    "homes" : "home",
    "increases" : "increase",
    "increasing" : "increase",
    "rising" : "rise",
    "sales" : "sale"
}

# Creating the data structure that will store the inverted index
invertedIndex = {}

# Processing each document in the collection
for i, row in data.iterrows():

    docID = row["Document"]
    text = row["Text"]

    # Applying surface-level normalization
    # make lowercase
    text = text.lower()

    # remove punctuation
    text = text.replace(".", "")

    # Tokenizing the document
    tokens = text.split()

    # remove common stop words
    filteredTokens = []
    for token in tokens:
        if token != "in":
            filteredTokens.append(token)
    
    tokens = filteredTokens

    # Applying lemmatization
    normalizedTokens = []
    for token in tokens:
        lemma = lemmas.get(token, token)
        normalizedTokens.append(lemma)

    # Building the inverted index
    for term in normalizedTokens:
        if term not in invertedIndex:
            invertedIndex[term] = set()

        invertedIndex[term].add(docID)


# Printing the inverted index with terms ordered alphabetically
# Expected format:
# term1 : ['Doc1', 'Doc2']
# term2 : ['Doc3']
for term in sorted(invertedIndex):
    documentIDs = sorted(invertedIndex[term])
    print(f"{term} : {documentIDs}")