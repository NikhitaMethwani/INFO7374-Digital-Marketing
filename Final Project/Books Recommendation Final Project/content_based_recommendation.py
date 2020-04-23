import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def content(title):
    books = pd.read_csv('s3://admfinalproject0801/unique_books.csv')
    books.head()

    """# Combining Authors, Genres and language for better results"""

    books['corpus'] = (
        pd.Series(books[['book_authors', 'genres', 'language_code']].fillna('').values.tolist()).str.join(' '))

    tf_corpus = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')
    tfidf_matrix_corpus = tf_corpus.fit_transform(books['corpus'])
    cosine_sim_corpus = linear_kernel(tfidf_matrix_corpus, tfidf_matrix_corpus)

    # Build a 1-dimensional array with book titles
    titles = books['book_title']
    indices1 = pd.Series(books.index, index=books['book_title'])

    # Function that get book recommendations based on the cosine similarity score of books tags

    idx = indices1[title]
    sim_scores = list(enumerate(cosine_sim_corpus[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    book_indices = [i[0] for i in sim_scores]
    c = titles.iloc[book_indices]

    return books[books['book_title'].isin(c)].head()
