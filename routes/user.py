from routes import *

main = Blueprint('user', __name__)


def current_user():
    uid = session.get('user_id')
    if uid is not None:
        user_id = ObjectId(uid)
        u = User.objects.get(id=user_id)
        return u


@main.route("/")
def login_view():
    us = User.objects.all()
    u = current_user()
    if u is not None:
        username = u.username
        created_time = u.created_time
        log('user_id', u.username)
    else:
        username = '游客'
        created_time = None
    return render_template('hello.html', users=us, username=username, time=created_time)


@main.route("/register", methods=['POST'])
def register():
    form = request.form
    u = User()
    u.write(form)
    if u.valid()[0]:
        u.save()
        log(u.valid())
    else:
        log('注册失败')
        abort(410)
    return redirect(url_for('.login_view'))


@main.route("/login", methods=['POST'])
def login():
    form = request.form
    u = User()
    u.write(form)
    user = User.objects(username=u.username).first()
    log(user)
    if user is not None and user.valid_login(u):
        log('登录成功')
        # user_id = json.dumps(str(user.id))
        log(type(user.id))
        session['user_id'] = str(user.id)
    else:
        log('登录失败')
    return redirect(url_for('.login_view'))


@main.route('/logout')
def logout():
    session.pop('user_id', None)
    print("注销", session)
    return redirect(url_for('.login_view'))