import pandas as pd  # Import pandas for data manipulation and analysis
import spacy  # Import spaCy for natural language processing
from spacytextblob.spacytextblob import SpacyTextBlob  # Import SpacyTextBlob for sentiment analysis

# Load the spaCy model and add the TextBlob component for sentiment analysis
nlp = spacy.load("en_core_web_md")
nlp.add_pipe('spacytextblob')

# Load the dataset containing Amazon product reviews
dataframe = pd.read_csv('amazon_product_reviews.csv')

# Select the 'reviews.text' column and remove missing values
reviews_data = dataframe['reviews.text']
clean_data = reviews_data.dropna().reset_index(drop=True)

# Function to preprocess the text data
def clean_text(text):
    # Convert text to lowercase and strip leading/trailing whitespace
    text = str(text).lower().strip()
    
    # Process the text with spaCy to perform tokenisation, lemmatisation, etc.
    doc = nlp(text)
    
    # Remove stopwords and non-alphabetic tokens
    cleaned_tokens = [token.text for token in doc if not token.is_stop and token.is_alpha]
    
    # Join the cleaned tokens back into a single string
    cleaned_text = ' '.join(cleaned_tokens)
    
    return cleaned_text

# Create a new column with preprocessed reviews
dataframe['cleaned.reviews'] = dataframe['reviews.text'].apply(clean_text)

# Function for sentiment analysis
def analyse_sentiment(text):
    # Process the text with spaCy
    doc = nlp(text)
    
    # Get the polarity score from SpacyTextBlob
    polarity = doc._.blob.polarity
    
    # Determine the sentiment based on the polarity score
    if polarity > 0:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment

# Select 5 specific reviews for sentiment analysis
review1 = dataframe['cleaned.reviews'][17]
review2 = dataframe['cleaned.reviews'][31]
review3 = dataframe['cleaned.reviews'][47]
review4 = dataframe['cleaned.reviews'][154]
review5 = dataframe['cleaned.reviews'][98]

# Print the selected reviews
print(f'Review1: {review1}\nReview2: {review2}\nReview3: {review3}\nReview4: {review4}\nReview5: {review5}')

# Perform sentiment analysis on the selected reviews and print the results
print(f'The first review is {analyse_sentiment(review1).lower()}.')
print(f'The second review is {analyse_sentiment(review2).lower()}.')
print(f'The third review is {analyse_sentiment(review3).lower()}.')
print(f'The fourth review is {analyse_sentiment(review4).lower()}.')
print(f'The fifth review is {analyse_sentiment(review5).lower()}.')

# Function to compare similarity between two reviews
def compare_similarity(review1, review2):
    # Process the reviews with spaCy
    doc1 = nlp(review1)
    doc2 = nlp(review2)
    
    # Compute the similarity between the two processed reviews
    similarity = doc1.similarity(doc2)
    
    return similarity

# Compare the similarity of the first and second reviews and print the result
print(f'The similarity of reviews 1 and 2 is {compare_similarity(review1, review2):.2%}')