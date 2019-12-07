from flask import Flask, render_template, jsonify, abort, send_from_directory
from flask_cors import CORS
from scrape_bbc_news import scrape_bbc_news
from scrape_guardian_news import scrape_guardian_news

app = Flask(__name__)
CORS(app)

# cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

urls_list = []
# urls_list = scrape_bbc_news(summaries_per_section=2,
# summarize_to_lines=2, save=False)

# print(urls_list)

loading = False

@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
  return send_from_directory('./dist/', path)

@app.route("/")
def client():
    return render_template('index.html')
    # return send_from_directory('./dist/', 'index.html')


@app.route("/bbc-news")
def bbc_news():
    global urls_list
    global loading
    return render_template('bbc_news.html', urls_list=urls_list, loading=loading)

@app.route("/api/<site>")
def api_news(site):
    if(site == 'bbc'):
        return api_bbc_news()
    else:
        abort(404)

# @app.route("/api/bbc-news")
def api_bbc_news():
    global urls_list
    if (len(urls_list) == 0):
        urls_list = scrape_bbc_news(summaries_per_section=2, summarize_to_lines=2, save=False)
    return jsonify(urls_list)


@app.route("/fetch-bbc-news", methods=["POST"])
def fetch_bbc_news():
    global loading
    global urls_list
    loading = True
    urls_list = []
    render_template('bbc_news.html', urls_list=[], loading=True)

    urls_list = scrape_bbc_news(summaries_per_section=5,
                                summarize_to_lines=5, save=False)
    loading = False
    print(f"Rendering {len(urls_list)} urls")
    return render_template('bbc_news.html', urls_list=urls_list, loading=False)


@app.route("/the-guardian")
def fetch_guardian_news():
    global loading
    global urls_list
    loading = True
    urls_list = []
    render_template('guardian.html', urls_list=[], loading=True)

    urls_list = scrape_guardian_news(summaries_per_section=5,
                                summarize_to_lines=5, save=False)
    loading = False
    print(f"Rendering {len(urls_list)} urls")
    return render_template('guardian.html', urls_list=urls_list, loading=False)


@app.route("/washington-post")
def fetch_washington_post():
    global loading
    global urls_list
    loading = True
    urls_list = []
    render_template('washington-post.html', urls_list=[], loading=True)

    urls_list = scrape_bbc_news(summaries_per_section=5,
                                summarize_to_lines=5, save=False)
    loading = False
    print(f"Rendering {len(urls_list)} urls")
    return render_template('washington-post.html', urls_list=urls_list, loading=False)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
