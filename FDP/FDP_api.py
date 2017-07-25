import os, json
import time
from flask import Flask, jsonify, request, abort


os.system('python /home/zhiqiang.qian/npu/PPPoE/src/create_dyn_rule.py')
os.system('/opt/sdk/p4/bin/rtecli config-reload -c /home/zhiqiang.qian/npu/PPPoE/src/rule.json')
with open(r'/home/zhiqiang.qian/npu/PPPoE/src/rule.json') as json_file:  
        rule = json.load(json_file)
print 'default rule:'
print rule['tables']['traffic_distribute_session']['default_rule']['action']['data']['port']

app = Flask(__name__)

@app.route('/fdp/change_rule', methods=['GET'])
def change_rule():

#change default rule for PPPoE session as VF of HWA
    global rule
    port = {"value": "v0.3"}
    count_id ={"value": "0"}
    data={"port":port, "count_id":count_id}
    action={"data":data,"type":"route_session"}
    rule['tables']['traffic_distribute_session']['default_rule']={"action":action, "name":"Default"}


    with open(r'/home/zhiqiang.qian/npu/PPPoE/src/rule.json', 'w') as outfile:  
         json.dump(rule,outfile)
    os.system('/opt/sdk/p4/bin/rtecli config-reload -c /home/zhiqiang.qian/npu/PPPoE/src/rule.json')
    print 'updated rule:'
    print rule['tables']['traffic_distribute_session']['default_rule']['action']['data']['port']
    return json.dumps(rule['tables']['traffic_distribute_session']['default_rule']), 201

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000,debug=True)
