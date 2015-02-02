"""
Run Flask's bundled web server

"""
from donorchoose import app

if __name__ == '__main__':
    app.run(debug=True)
