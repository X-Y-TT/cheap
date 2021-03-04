import cheap
from  flask import Flask,jsonify,request
app = Flask(__name__)
@app.route("/ssr",methods=["GET"])
def cheap1():
    ssr=cheap.main()
    if ssr:
        return jsonify({'code' :200, 'msg': ssr})
    else:
        return jsonify({'code': 404, 'msg': '错误！'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
