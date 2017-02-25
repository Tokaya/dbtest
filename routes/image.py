from routes import *

main = Blueprint('image', __name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
image_path = 'images'

@main.route('/solutions')
def index():
    root_dir = image_path
    return render_template('upload.html', root_dir=root_dir)


@main.route("/solutions/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, image_path)
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    for file in request.files.getlist("file"):
        print(file)
        print("{} is the file name".format(file.filename))
        filename = file.filename
        log('文件名', filename)
        i = Image(name=filename, path=image_path)
        log('debug-i', i)
        i.save()
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("save it to:", destination)
        file.save(destination)
    return redirect(url_for('.index'))
