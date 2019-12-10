from flask import Flask, render_template, jsonify, abort, send_from_directory
from flask_cors import CORS
from scrape_bbc import scrape_bbc, scrape_bbc_and_save
from scrape_guardian import scrape_guardian, scrape_guardian_and_save
from scrape_reuters import scrape_reuters, scrape_reuters_and_save
from scrape_washington import scrape_washington, scrape_washington_and_save

app = Flask(__name__)
CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

urls_list_bbc = []
urls_list_guardian = []
urls_list_washington = []
urls_list_reuters = []


loading = False


###############################
##      Web Server Routes    ##
###############################

@app.route('/', methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
def web(path=''):
    print(f"\nPath: /{path}  📰")
    if(path == ''):
        return render_template('index.html')
    elif(path == 'bbc'):
        return render_template('bbc.html', urls_list=urls_list_bbc, loading=loading)
    elif(path == 'guardian'):
        return render_template('guardian.html', urls_list=urls_list_guardian, loading=loading)
    elif(path == 'reuters'):
        return render_template('reuters.html', urls_list=urls_list_reuters, loading=loading)
    elif(path == 'washington'):
        return render_template('washington.html', urls_list=urls_list_washington, loading=loading)
    elif(path == 'about'):
        return render_template('about.html')
    else:
        return render_template('index.html')


###############################
##         API Routes        ##
###############################


@app.route("/api/<site>")
def api(site):
    if(site == 'bbc'):
        return api_bbc()
    elif(site == 'guardian'):
        return api_guardian()
    elif(site == 'reuters'):
        return api_reuters()
    elif(site == 'washington'):
        return api_washington()
    else:
        abort(404)

#################################
##        API Routes DAO       ##
#################################


def api_bbc():
    global urls_list_bbc
    if (len(urls_list_bbc) == 0):
        urls_list_bbc = scrape_bbc()
    return jsonify(urls_list_bbc)


def api_guardian():
    global urls_list_guardian
    if (len(urls_list_guardian) == 0):
        urls_list_guardian = scrape_guardian()
    return jsonify(urls_list_guardian)


def api_washington():
    global urls_list_washington
    if (len(urls_list_washington) == 0):
        urls_list_washington = scrape_washington()
    return jsonify(urls_list_washington)


def api_reuters():
    global urls_list_reuters
    if (len(urls_list_reuters) == 0):
        urls_list_reuters = scrape_reuters()
    return jsonify(urls_list_reuters)


###############################
##       Fetch Routes        ##
###############################

@app.route("/fetch-bbc", methods=["POST"])
def fetch_bbc():
    global loading
    global urls_list_bbc

    return render_template('bbc.html', urls_list=urls_list_bbc, loading=False)


@app.route("/fetch-guardian", methods=["POST"])
def fetch_guardian():
    global loading, urls_list_guardian

    urls_list_guardian = scrape_guardian()
    return render_template('guardian.html', urls_list=urls_list_guardian, loading=False)


@app.route("/fetch-reuters", methods=["POST"])
def fetch_reuters():
    global loading, urls_list_reuters

    urls_list_reuters = scrape_reuters()
    return render_template('reuters.html', urls_list=urls_list_reuters, loading=False)


@app.route("/fetch-washington", methods=["POST"])
def fetch_washington():
    global loading, urls_list_washington

    urls_list_washington = scrape_washington()
    return render_template('washington.html', urls_list=urls_list_washington, loading=False)


###############################
##       Main Program        ##
###############################
if __name__ == '__main__':
    app.run(debug=True)
