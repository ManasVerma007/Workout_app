from . import db
from .models import User

from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import current_user, login_required

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',name=current_user.name)

@main.route("/new", methods=['POST'])
@login_required
def new_workout():
    return render_template('main.index')