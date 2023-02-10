import requests
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check-cve', methods=['GET'])
def check_cve():
    cve_id = request.args.get('cve_id')
    if not cve_id:
        return jsonify({"error": "Missing 'cve_id' parameter in the query string."}), 400

    while True:
        # Retrieve the CVE data from the NVD database
        response = requests.get(f'https://services.nvd.nist.gov/rest/json/cve/1.0/CVE-{cve_id}')
        if response.status_code == 200:
            cve_data = response.json()
            cve_severity = cve_data.get('impact', {}).get('baseMetricV2', {}).get('severity')
            # cve_vuln = cve_data.get('vulnerabilities',[])
            return jsonify({"cve_id": cve_id, "severity": cve_severity})
            

        # Wait for 5 seconds before trying again
        time.sleep(5)

if __name__ == '__main__':
    app.run()
