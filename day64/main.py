from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from os import environ
import requests

TMDB_URL = 'https://api.themoviedb.org/3/'
TMDB_HEADERS = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkY2YwYzI3Y2NmMDFiYzFiOTEyOWM1ZDY5NDUyOTM4YSIsInN1YiI6IjY2M2EzZjJlNWE0NjkwMDEyNTNmNGU0NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9OmTKcWsplTfIDBVntiOowT_pD3kIAG1GhkWYrmteP8"
}
TMDB_IMAGE_URL = 'https://image.tmdb.org/t/p/w500/'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass
db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db.init_app(app)
# CREATE TABLE
class Movie(db.Model):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String, nullable=True)
    img_url: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'

with app.app_context():
    db.create_all()

class EditForm(FlaskForm):
    rating = StringField('Your rating out of 10 i.e. 7.5', validators=[DataRequired()])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddForm(FlaskForm):
    title = StringField('Title of the movie', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = [record for record in result.scalars()]
    for i, movie in enumerate(all_movies):
        movie.ranking = len(all_movies) - i
    db.session.commit()
    return render_template('index.html', all_movies=all_movies)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = EditForm()
    movie_id = request.args.get('id')
    if form.validate_on_submit():
        movie_to_update = db.get_or_404(Movie, movie_id)
        movie_to_update.rating = request.form["rating"]
        movie_to_update.review = request.form["review"]
        db.session.commit()
        return redirect(url_for('home')) 
    movie_selected = db.get_or_404(Movie, movie_id)
    return render_template("edit.html", movie=movie_selected, form=form)

@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        params = {
            'query': form.title.data
        }
        response = requests.get(f"{TMDB_URL}/search/movie", headers=TMDB_HEADERS, params=params).json()['results']
        return render_template('select.html', movies=response)    
    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{TMDB_URL}movie/{movie_api_id}"
        response = requests.get(movie_api_url, params={"language": "en-US"}, headers=TMDB_HEADERS).json()
        new_movie = Movie(
            title=response["title"],
            year=response["release_date"].split("-")[0],
            img_url=f"{TMDB_IMAGE_URL}{response['poster_path']}",
            description=response["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
