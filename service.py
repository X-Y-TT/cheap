import cheap,tizi
from  flask import Flask,jsonify,request
app = Flask(__name__)
@app.route("/ssr",methods=["GET"])
def cheap1():
    ssr=cheap.main()
    if ssr:
        return jsonify({'code' :200, 'msg': ssr})
    else:
        return jsonify({'code': 404, 'msg': '错误！'})
@app.route("/newtizi",methods=["GET"])
def tizi1():
    ssr=tizi.main()
    if ssr:
        return jsonify({'code' :200, 'msg': ssr})
    else:
        return jsonify({'code': 404, 'msg': '错误！'})
@app.route("/tizi/<invite>",methods=["GET"])
def tizi2(invite):
    invite = 'https://www.zionladdero.com/register/{}'.format(invite)
    tizi.main2(invite)
    if True:
        return jsonify({'code' :200, 'msg': 'ok'})
    else:
        return jsonify({'code': 404, 'msg': '错误！'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5008, debug=True)
