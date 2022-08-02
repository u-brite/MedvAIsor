from flask import Flask, render_template

app = Flask(__name__)

def preproceesing(file=None):
    if file!= None:
        print('we process the file')
        print('we return the processed DF')
    else:
        print('return with an error message')

def predictor(data=None):
    if data!= None:
        print('use the model to predict the result and return the predictions')


@app.route('/')
def index():  # put application's code here

    #"get the data file from the the request variable"
    #initial chen on the file
    #call the preprocessing function()
    #call the predictor function()
    # prepare the result
    html = """<!DOCTYPE html>
            <html>
            <body>

            <h1>My First Heading</h1>

            <p>My first paragraph.</p>

            </body>
            </html>"""
    return render_template('test.html' )


if __name__ == '__main__':
    app.run()
