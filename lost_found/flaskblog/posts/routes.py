from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route("/post/lost", methods=['GET', 'POST'])
@login_required
def lost_something():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, description=form.description.data, location=form.location.data,
                    datetime=form.datetime.data, treat=form.treat.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created! Hope you find it soon.', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='Reporting a loss')


@posts.route("/post/found", methods=['GET', 'POST'])
@login_required
def found_something():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, description=form.description.data, location=form.location.data,
                    datetime=form.datetime.data, treat=form.treat.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created! Hope you find the owner soon.', 'success')
        return redirect(url_for('main.home'))
    return render_template('found.html', title='New Post',
                           form=form, legend='Reporting a find')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.description = form.description.data
        post.location = form.location.data
        post.datetime = form.datetime.data
        post.treat = form.treat.data
        db.session.commit()
        flash('Your post has been updated! Hope you find it soon.', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.description = post.description.data
        form.location = post.location.data
        form.datetime = post.datetime.data
        form.treat = post.treat.data
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Are you sure to delete this?", 'success')
    return redirect(url_for('main.home'))