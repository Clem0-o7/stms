from flask import Flask, render_template, jsonify
import subprocess
import threading
import os
from model import SimulationModel

app = Flask(__name__)
model = SimulationModel()

def run_simulation(script_name):
    subprocess.run(['python', script_name, '--gui', '-s', '500'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_simulations')
def start_simulations():
    model.load_model()  # Load the model
    
    # Start both simulations in separate threads
    threading.Thread(target=run_simulation, args=('train.py',)).start()
    threading.Thread(target=run_simulation, args=('fixed.py',)).start()
    
    return jsonify({"status": "Simulations started"})

if __name__ == '__main__':
    app.run(debug=True)