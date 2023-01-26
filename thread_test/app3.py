from flask import Flask , jsonify,render_template,request
import requests
import threading
import concurrent.futures

app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def api_test():
    if request.method == 'POST':
        res = ''
        keyword = request.form.get('keyword')
        t = threading.Thread(target=send_req,args=[keyword])
        t.start()
       
        # with concurrent.futures.ThreadPoolExecutor() as executor:
        #     future = executor.submit(send_req, keyword)
        #     res = future.result()
        # return render_template('testapipost.html',res=res)
        return render_template('testapipost.html')
    return render_template('thread_api.html')

def send_req(keyword):
    link = f'https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={keyword}'            
    response = requests.get(link)
        
    res = response.text
    print(res)
    return res
 
@app.route('/test')
def test_page():
    return 'new test page'

if __name__ == '__main__':
    app.run(debug=True)   


# import concurrent.futures``
# 
# def foo(bar):
    # print('hello {}'.format(bar))
    # return 'foo'
# 
# with concurrent.futures.ThreadPoolExecutor() as executor:
    # future = executor.submit(foo, 'world!')
    # return_value = future.result()
    # print(return_value)