from flask import Blueprint, render_template

pages = Blueprint('pages', __name__)


@pages.route("/")
def create_member():
    return render_template("home.html")
