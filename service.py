import cheap,tizi
from  flask import Flask,jsonify,request
app = Flask(__name__)
'''
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
    return ssr
'''
@app.route("/newlog",methods=["GET"])
def tizi1():
    with open('log.log','r')as f:
        f=f.read()
    return f
@app.route("/tizi/<invite>",methods=["GET"])
def tizi2(invite):
    with open("invite.txt", "r") as f:
        s = f.readlines()
        invite = 'https://www.zionladdero.com/register/{}'.format(invite)+'\n'
        if invite in s:
            return jsonify({'code': 404, 'msg': '错误！'})
        else:
            f = open('invite.txt', 'a')
            f.write(invite)
            f.close()
            return jsonify({'code' :200, 'msg': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5008, debug=True)
