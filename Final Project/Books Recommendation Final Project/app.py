import flask
from flask import Flask
from flask_mail import Mail, Message
import pandas as pd
from promotion import rfm_score
from unique_books import read_book_details
from books_recommendation_for_user import recommend_books_userbased
from content_based_recommendation import content
from flask_s3 import FlaskS3

app = Flask(__name__)
app.config['S3_BUCKET_NAME'] = 'admfinalproject0801'
s3 = FlaskS3(app)

app = flask.Flask(__name__, template_folder='templates')

mail = Mail()

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'vinayrk100@gmail.com'
app.config["MAIL_PASSWORD"] = 'Vinay@1996'

mail.init_app(app)


# # Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return flask.render_template('welcome.html')


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    return flask.render_template('index.html')


@app.route('/books', methods=['GET', 'POST'])
def api_books():
    if flask.request.method == "POST":
        uname = flask.request.form["name"]
        uid = int(flask.request.form["uid"])
        purchased_books, recommendations_genre, recommendations_author, \
        recommendations_bookpages = recommend_books_userbased(uid)
        segment, promo = rfm_score(uid)
    return flask.render_template('booksdetails.html',
                                 uid=uid,
                                 uname=uname,
                                 segment=segment,
                                 promo=promo.values.tolist(),
                                 purchased_books=purchased_books.values.tolist(),
                                 recommendations_genre=recommendations_genre.values.tolist(),
                                 recommendations_author=recommendations_author.values.tolist(),
                                 recommendations_bookpages=recommendations_bookpages.values.tolist())


@app.route('/recommendation', methods=['POST'])
def api_reco():
    # begin 04/20
    button_val = flask.request.form["title"]
    if flask.request.form["uid"] != "":
        uid = int(flask.request.form["uid"])
        uname = flask.request.args.get("uname")

    if button_val == "Submit":
        if flask.request.form["custom_title"] != "":
            title = flask.request.form["custom_title"]
    # end 04/20
    else:
        title = button_val

    first_line = True
    book, user = read_book_details(title, uid)
    return flask.render_template('recommendation.html',
                                 book_details=book.values.tolist(),
                                 user=user.values.tolist(),
                                 uname=uname,
                                 title=title)


@app.route('/purchase', methods=['POST'])
def api_purchase():
    sub = flask.request.form["sub"]
    uname = flask.request.args.get("uname")
    uid = flask.request.form["uid"]
    booktitle = flask.request.args.get("booktitle")
    email = flask.request.form["email"]

    if sub == "Purchase":
        book = content(booktitle)
        df_unique_book = pd.read_csv("s3://admfinalproject08/unique_books.csv")
        book_det = df_unique_book[df_unique_book['book_title'] == booktitle.casefold()]

        for b in book_det.values.tolist():
            title = b[3]
            author = b[2]
            price = b[10]
            rating = b[7]
            img = b[6]

        msg = Message('Greetings from Pick-A-Book', sender='vinayrk100@gmail.com', recipients=[email])
        msg.body = "Hi" + " " + uname + " , " + "title: " + title + "author: " + author + "price: " + str(
            price) + "rating: " + str(rating)

        msg.html = flask.render_template('send_email.html', name=uname, title=title, author=author,
                                         price=price,
                                         rating=rating, img=img)
        mail.send(msg)
        return flask.render_template('purchase.html',
                                     book_details=book.values.tolist(),
                                     user=uid,
                                     uname=uname)


if __name__ == '__main__':
    app.run(debug=True)
