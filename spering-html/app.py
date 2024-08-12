from flask import Flask, render_template
from flask_cors import cross_origin
import subprocess

app = Flask(__name__)
app.static_folder = 'static'
@app.route("/")
@cross_origin()
def index():
    return render_template("index.html")
@app.route('/favicon.ico')
def favicon():
    return '', 404

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/run_script')
def run_script():
    # Execute the Python script
    subprocess.run(['python', 'C:\\Users\\mfaha\\OneDrive\\Desktop\\Sign-Language-Reconition-System\\test.py'])
    return 'Python script executed'
@app.route('/run_script2')
def run_script2():
    # Execute the Python script
    subprocess.run(['python', 'C:\\Users\\mfaha\\OneDrive\\Desktop\\Sign-Language-Reconition-System\\Live_cam_feed.py'])
    return 'Python script executed'
@app.route('/run_script3')
def run_script3():
    # Execute the Python script
    subprocess.run(['python', 'C:\\Users\\mfaha\\OneDrive\\Desktop\\Sign-Language-Reconition-System\\predict_with_esp32.py'])
    return 'Python script executed'
if __name__ == '__main__':
    app.run(debug=True)
