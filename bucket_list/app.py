from flask import Flask, render_template
from controllers.visited_controller import visited_blueprint

app = Flask(__name__)
app.register_blueprint(visited_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)