from dnm.models import Member, Reference
from flask import Blueprint, render_template

pages = Blueprint('pages', __name__)


@pages.route("/")
def create_member():
    members = Member.query.all()

    return render_template("home.html", members=members)
