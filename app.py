from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import time
import requests
from datetime import datetime
from sklearn.ensemble import IsolationForest
import numpy as np

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["chrome-extension://*"]}})

class AITimeTracker:
    def __init__(self):
        self.history = []
        self.site_profiles = {}  # recognise patterns

    def track_load_time(self, url):
        """Measure load time from server side"""
        start_time = time.time()
        try:
            response = requests.get(url,
                                    headers={'User-Agent': 'Mozilla/5.0'},
                                    timeout=10)
            load_time = (time.time() - start_time) * 1000  # convert to milisecond
            status = 'success'
        except Exception as e:
            load_time = -1
            status = str(e)

        # ai analysis
        analysis = self.analyze_performance(url, load_time)

        entry = {
            'url': url,
            'load_time': load_time,
            'timestamp': datetime.now().isoformat(),
            'status': status,
            'analysis': analysis
        }

        self.history.append(entry)
        return entry

    def analyze_performance(self, url, current_load_time):
        """AI-powered performance analysis"""
        domain = url.split('/')[2] if '//' in url else url.split('/')[0]

        # create profile of performance
        if domain not in self.site_profiles:
            self.site_profiles[domain] = {
                'load_times': [],
                'avg_load_time': None,
                'stability_score': None
            }

        # update statistics
        self.site_profiles[domain]['load_times'].append(current_load_time)
        self.site_profiles[domain]['avg_load_time'] = np.mean(self.site_profiles[domain]['load_times'])

        # anomaly detection
        is_anomaly = False
        if len(self.site_profiles[domain]['load_times']) > 5:
            model = IsolationForest(contamination=0.1)
            data = np.array(self.site_profiles[domain]['load_times']).reshape(-1, 1)
            model.fit(data)
            is_anomaly = model.predict([[current_load_time]])[0] == -1

        # generate insights
        insights = []
        if is_anomaly:
            diff = current_load_time - self.site_profiles[domain]['avg_load_time']
            insights.append(
                f"⚠️ Unusual performance ({(diff / self.site_profiles[domain]['avg_load_time']) * 100:.0f}% {'slower' if diff > 0 else 'faster'} than average)")

        # improved metric case logic
        avg_load_time = self.site_profiles[domain]['avg_load_time']
        if current_load_time < 0:  # Error case
            insights.append("❌ Failed to load website")
        elif current_load_time < 500:
            insights.append("🚀 Very fast load time (<0.5s)")
        elif current_load_time < 1000:
            insights.append("⚡ Fast load time (0.5–1s)")
        elif current_load_time < 2000:
            insights.append("🕒 Moderate load time (1–2s)")
        elif current_load_time < 3000:
            insights.append("🐢 Slow load time (2–3s)")
        else:
            insights.append("🦥 Very slow load time (>3s)")

        # add context if historical data exists
        if avg_load_time and len(self.site_profiles[domain]['load_times']) > 1:
            if current_load_time < avg_load_time * 0.8:
                insights.append("✅ Better than site average")
            elif current_load_time > avg_load_time * 1.2:
                insights.append("⚠️ Worse than site average")

        return {
            'is_anomaly': is_anomaly,
            'insights': insights,
            'comparison': f"Site average: {self.site_profiles[domain]['avg_load_time']:.0f}ms",
            'domain_profile': self.site_profiles[domain]
        }

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []
        self.site_profiles = {}

tracker = AITimeTracker()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/track', methods=['POST'])
def track():
    data = request.get_json()
    url = data['url']

    # validate URL
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    # track from server side
    result = tracker.track_load_time(url)
    return jsonify(result)

@app.route('/history')
def history():
    return jsonify(tracker.get_history())

@app.route('/clear', methods=['POST'])
def clear():
    tracker.clear_history()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
