import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import re
import sklearn.metrics.pairwise as pw
from scipy import sparse
from sklearn.metrics.pairwise import pairwise_distances
from scipy.sparse.linalg import svds
import pickle


def train_model():
    books_details_df = pd.read_csv('C:/Users/Nikhita/Desktop/Dataset/Final/final_book_details.csv')
    df_ratings = pd.read_csv('C:/Users/Nikhita/Desktop/Dataset/Final/ratings.csv')
    df_books_ratings = df_ratings.pivot(
        index='user_id',
        columns='book_id',
        values='rating'
    ).fillna(0)

    R = df_books_ratings.values
    user_ratings_mean = np.mean(R, axis=1)
    R_demeaned = R - user_ratings_mean.reshape(-1, 1)

    U, sigma, Vt = svds(R_demeaned, k=50)

    sigma = np.diag(sigma)

    all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)

    preds_df = pd.DataFrame(all_user_predicted_ratings, columns=df_books_ratings.columns)

    with open('C:/Users/Nikhita/Desktop/Dataset/Final/pickle.pkl', 'wb') as file:
        pickle.dump(preds_df, file)


train_model()
