from pathlib import Path

import bleach
import markdown
from flask import Flask, abort, render_template
#from weasyprint import HTML

app = Flask(__name__)
MARKDOWN_PAGES_DIR = Path(__file__).resolve().parent / "pages"
MARKDOWN_TAGS = bleach.sanitizer.ALLOWED_TAGS.union({
    "blockquote", "br", "code", "del", "dd", "dl", "dt", "h1", "h2", "h3",
    "h4", "h5", "h6", "hr", "img", "li", "ol", "p", "pre", "table",
    "tbody", "td", "th", "thead", "tr", "ul",
})
MARKDOWN_ATTRIBUTES = {
    "a": ["href", "title"],
    "code": ["class"],
    "img": ["alt", "src", "title"],
    "td": ["align"],
    "th": ["align"],
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/my-story')
def my_story():
    return render_template('my-story.html')

@app.route('/blackboard')
def blackboard():
    return render_template('blackboard.html')

@app.route('/<slug>')
def markdown_page(slug):
    markdown_path = MARKDOWN_PAGES_DIR / f"{slug}.md"
    if not markdown_path.is_file():
        abort(404)

    source = markdown_path.read_text(encoding="utf-8")
    rendered = markdown.markdown(source, extensions=["extra"])
    safe_html = bleach.clean(
        rendered,
        tags=MARKDOWN_TAGS,
        attributes=MARKDOWN_ATTRIBUTES,
        strip=True,
    )
    return render_template(
        "markdown_page.html",
        title=slug.replace("-", " ").title(),
        content=safe_html,
    )

'''
@app.route('/download-cv')
def download_cv():
    # Render the CV template
    html = render_template('cv.html')
    
    # Create PDF in memory
    pdf = HTML(string=html).write_pdf()
    
    # Create response
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=CV Pavel Bakunovich.pdf'
    
    return response

'''

if __name__ == '__main__':
    app.run(debug=True)
