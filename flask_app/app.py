from flask import Flask,request, render_template
import angle_finder
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
   hour = request.form['hour']
   mins = request.form['mins']
   time = f"{hour}:{mins}"
   angle = angle_finder.main(time)
   return render_template('result.html', name = angle)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')