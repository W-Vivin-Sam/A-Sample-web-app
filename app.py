from flask import Flask, render_template,jsonify
app = Flask(__name__)
JOBS = [
    {   'id': 1, 
        'title': 'Data Analyst',
        'location': 'Bengaluru, India'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India'
    },
    {
        'id': 3,
        'title': 'Frontend Developer',
        'location': 'Washington, USA' 
}]

@app.route('/')
def hello_world():
    return render_template('home.html',jobs = JOBS)
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
if __name__ == "__main__":
    app.run(host = "0.0.0.0" , debug=True)

