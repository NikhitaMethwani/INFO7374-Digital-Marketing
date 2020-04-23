import pandas as pd


def read_book_details(title, uid):
    df_custom_book = pd.read_csv("s3://admfinalproject0801/final_book_details.csv")
    df_unique_book = pd.read_csv("s3://admfinalproject0801/unique_books.csv")
    df_unique_user = pd.read_csv("s3://admfinalproject0801/user_details.csv")

    lst_user = df_unique_user[df_unique_user['user_id'] == uid]
    if title != "":
        lst_book = df_unique_book[df_unique_book['book_title'] == title.casefold()]
        lst_book['Price'].astype(int)
    return lst_book, lst_user
