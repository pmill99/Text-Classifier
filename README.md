# Naive Bayes Text Classifier
This is my first ever attempt at a text classification program that I wrote during my undergraduate using the Naive Bayes classification algorithm.
It consists of a Jupyter notebook outlining a class that implements the algorithm, and 3 folders containing news articles of 3 different categories; sports, business and politics. The articles are organized according to the category they were given by cnn.com. The model is compared to SciKit-Learn's Naive Bayes classification model, and will run regardless of how
many articles are included in the data directories. Currently, the program does not use a large amount of training data, which may produce inconsistent results in both 
Scikit-Learn's model and my custom model.

### The Naive Bayes Classification Formula
![Naive Bayes Algorithm](https://imgs.search.brave.com/Ask4S0ZXbZ9rxVJG568KG1wStpFMB9rDsuTSR-KkxP4/rs:fit:5106:225:1/g:ce/aHR0cHM6Ly90c2Ux/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC53/MWEwbkRjQlJ0eWxw/Zzl2ZXhZRzh3SGFB/cyZwaWQ9QXBp)

The Naive Bayes Formula uses conditional probabilities to predict the most likely category that a variable belongs to. In the case of text classification, the "x" values in the formula are represented by each word in a document, and the "C" value represents the category or genre that word was found in. Therefore, the program predicts a test category (C) given a series of words(x1, x2...xN), by calculating the probability of finding each of those same words in the training set of categorized data. The highest calculated probability is returned as the predicted category.
