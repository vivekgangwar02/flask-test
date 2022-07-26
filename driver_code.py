import os
from flask import Flask, request, jsonify
app = Flask(__name__)

from flask_cors import CORS
CORS(app)

from dotenv import load_dotenv
load_dotenv()


@app.route('/test', methods=['GET'])
def get_test():
    return "Success....."


@app.route('/volume', methods=['GET'])
def test_volume():
    d = dict()
    try:
        current = os.getcwd()
        d['current'] = current
    except:
        pass
    try:
        list_current = os.listdir()
        d['list_cur'] = list_current
    except:
        pass
    try:
        os.chdir(r'/var/log/saurabh')
        d['changed'] = os.listdir()
    except:
        pass
    return jsonify(d)


if __name__ == '__main__':
    try:
        print('Entered code: __main__')
        app.run(port= os.environ.get('AWS_PORT', 5000) )
    except KeyboardInterrupt:
        print(f'Server closed.')
    except Exception as e:
        print('\nCODE CRASHED once due to: {e}\n')
    

