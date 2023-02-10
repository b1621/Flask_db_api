import requests
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

data = {
    "part":"o",
    "vendor":"microsoft",
    "product":"windows_11",
    "version": "15.0.22"
}
    
# with open("data.json") as json_file:
#     data = json.load(json_file)


@app.route('/check_json')
def check_json():
    return jsonify(data)

@app.route('/check_cve', methods=['GET'])
def check_cve():
    # cve_id = request.args.get('cve_id')
    # cve_id = 'CVE-2023-22884'
    # cve_id = 'CVE-2021-41823'
    cve_id = 'CVE-2019-8278'
    product = data["product"]
    if not cve_id:
        return jsonify({"error": "Missing 'cve_id' parameter in the query string."}), 400

    # Retrieve the CVE data from the NVD database
    # response = requests.get(f'https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2019-8278')
    response = requests.get(f'https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:{data["part"]}:{data["vendor"]}:{data["product"]}:{data["version"]}')
    if response.status_code != 200:
        return jsonify({"error": f"Failed to retrieve CVE data for {cve_id}"}), 500

    cve_data = response.json()

    # Check the severity of the CVE
    # cve_severity = cve_data.get('impact', {}).get('baseMetricV2', {}).get('severity')

    # check the vulnerabilities of the cve
    cve_vuln = cve_data.get('vulnerabilities',[])
    

    # return jsonify({"cve_id": cve_id, "severity": cve_severity})
    # return jsonify({"cve_id":cve_id, "vuln": cve_vuln})
    return jsonify(cve_data)
    # return data

if __name__ == '__main__':
    app.run(debug=True)

