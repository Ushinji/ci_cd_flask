from flask import redirect, render_template
from app import application
from app.models import User
from app.forms.user import UserCreateForm


@application.route('/users', methods=['GET'])
def index():
    users = User.query.all()
    return render_template('users/index.html', workspaces=users)


@application.route('/users/new', methods=['GET', 'POST'])
def create():
    form = UserCreateForm()
    if form.validate_on_submit():
        User.create(
            name=form.name.data,
            email=form.email.data,
        )

        return redirect('/users')
    return render_template('users/create.html', form=form)
