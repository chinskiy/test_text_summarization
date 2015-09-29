import newspaper
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('base.html')


@app.route('/search', methods=['GET'])
def search():
    entered_url = request.args.get('entered_url')
    article = newspaper.Article(entered_url, fetch_images=False)
    article.download()
    article.parse()
    article.nlp()
    return jsonify(result_text=article.text, result_summary=article.summary)


if __name__ == '__main__':
    app.run()
