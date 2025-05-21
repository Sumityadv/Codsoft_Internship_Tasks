import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer                                     #importing all the required libraries
from sklearn.metrics.pairwise import linear_kernel

data = pd.read_csv('Task_3 - Books-review.csv', encoding='latin-1')
books_df = pd.DataFrame(data)                                                                  # reading the books csv file and coverting into DataFrame

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(books_df['Description'])                                    # we are using tfidf vectorizer to convert the description text data into numerical value form

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)                                         # computing the cosine similarity on tfidf matrix for finding similarity between books based on description

def recommendations(category, top_n=3):
    
    category_books = books_df[books_df['Category'] == category]

    if category_books.empty:
        return []

    category_books = category_books.sort_values(by=['Rating', 'Reviews'], ascending=[False, False])        #here we are sorting the books in the category based on ratings and reviews

    recommended_books = category_books.head(top_n)

    return recommended_books['Title'].tolist()

print(books_df['Category'].unique())                                                              # here we have to take user input of categoary they want to find
category_input = input("Choose a category: ")

recommended_books = recommendations(category_input)

if recommended_books:
    print(f"The Best book in the '{category_input}' category based on ratings and reviews:")
    for book_title in recommended_books:                                                                # here we are printing the top 3 books in the category based on ratings and reviews
        print(book_title)                                                                               # if the category is not listed then it will print the message that the category is not listed
else:
    print(f"The category you have enterd is not listed there '{category_input}'")