from flask import Flask, render_template, url_for, make_response
import io
#from weasyprint import HTML

app = Flask(__name__)

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
