from flask import Flask, render_template, request
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_profile():

    name = request.form.get('name', '').strip()
    bio = request.form.get('bio', '').strip()
    image_url = request.form.get('image_url', '').strip()

    if not name or not bio:
        return render_template(
            'index.html',
            error="Please enter your name and bio."
        )

    if image_url:
        parsed = urlparse(image_url)

        if parsed.scheme not in ('http', 'https') or not parsed.netloc:
            return render_template(
                'index.html',
                error="Please enter a valid image URL."
            )

    return render_template(
        'profile.html',
        name=name,
        bio=bio,
        image_url=image_url
    )


if __name__ == '__main__':
    app.run(debug=True)
