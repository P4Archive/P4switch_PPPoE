import json

#clear function
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

#setup table entry
rule={}
rule['meters']={"configs": []}
rule['multicast']={}
rule['parser_value_sets']={"configs": []}
rule['registers']={"configs": []}
rule['tables']={}

#By default all PPPOED packets to VNF
port = {"value": "v0.2"}
count_id ={"value": "0"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_discovery"}
rule['tables']['traffic_distribute_discover']={}
rule['tables']['traffic_distribute_discover']['default_rule']={"action":action, "name":"Default"}
rule['tables']['traffic_distribute_discover']['rules']=[]

#To Client PADO
port = {"value": "v0.4"}
count_id ={"value": "1"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_discovery"}
standard_metadata_ingress_port = {"value": "v0.2"}
PPPoE_D_PPPoE_code={"value": "0x07"}
eth_dstAddr={"value": "0x00154d000004"}
match={"eth.dstAddr": eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_D.PPPoE_code": PPPoE_D_PPPoE_code}
new_rule={"action": action,"match": match, "name": "0"}
rule['tables']['traffic_distribute_discover']['rules'].insert(0, new_rule)



#To Client PADS
port = {"value": "v0.4"}
count_id ={"value": "2"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_discovery"}
standard_metadata_ingress_port = {"value": "v0.2"}
PPPoE_D_PPPoE_code={"value": "0x65"}
eth_dstAddr={"value": "0x00154d000004"}
match={"eth.dstAddr": eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_D.PPPoE_code": PPPoE_D_PPPoE_code}
new_rule={"action": action,"match": match, "name": "1"}
rule['tables']['traffic_distribute_discover']['rules'].insert(1, new_rule)

#To Client PADO
port = {"value": "v0.5"}
count_id ={"value": "1"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_discovery"}
standard_metadata_ingress_port = {"value": "v0.2"}
PPPoE_D_PPPoE_code={"value": "0x07"}
eth_dstAddr={"value": "0x3a87d73a00ac"}
match={"eth.dstAddr": eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_D.PPPoE_code": PPPoE_D_PPPoE_code}
new_rule={"action": action,"match": match, "name": "0"}
rule['tables']['traffic_distribute_discover']['rules'].insert(2, new_rule)

#VM8
port = {"value": "v0.6"}
count_id ={"value": "1"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_discovery"}
standard_metadata_ingress_port = {"value": "v0.2"}
PPPoE_D_PPPoE_code={"value": "0x07"}
eth_dstAddr={"value": "0xe60ab599c0f5"}
match={"eth.dstAddr": eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_D.PPPoE_code": PPPoE_D_PPPoE_code}
new_rule={"action": action,"match": match, "name": "0"}
rule['tables']['traffic_distribute_discover']['rules'].insert(2, new_rule)

#VM9
port = {"value": "v0.7"}
count_id ={"value": "1"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_discovery"}
standard_metadata_ingress_port = {"value": "v0.2"}
PPPoE_D_PPPoE_code={"value": "0x07"}
eth_dstAddr={"value": "0x2a57c2de0ba9"}
match={"eth.dstAddr": eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_D.PPPoE_code": PPPoE_D_PPPoE_code}
new_rule={"action": action,"match": match, "name": "0"}
rule['tables']['traffic_distribute_discover']['rules'].insert(2, new_rule)

#VM10
port = {"value": "v0.8"}
count_id ={"value": "1"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_discovery"}
standard_metadata_ingress_port = {"value": "v0.2"}
PPPoE_D_PPPoE_code={"value": "0x07"}
eth_dstAddr={"value": "0x96d93a95c745"}
match={"eth.dstAddr": eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_D.PPPoE_code": PPPoE_D_PPPoE_code}
new_rule={"action": action,"match": match, "name": "0"}
rule['tables']['traffic_distribute_discover']['rules'].insert(2, new_rule)

#VM11
port = {"value": "v0.9"}
count_id ={"value": "1"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_discovery"}
standard_metadata_ingress_port = {"value": "v0.2"}
PPPoE_D_PPPoE_code={"value": "0x07"}
eth_dstAddr={"value": "0x3a7138b4a490"}
match={"eth.dstAddr": eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_D.PPPoE_code": PPPoE_D_PPPoE_code}
new_rule={"action": action,"match": match, "name": "0"}
rule['tables']['traffic_distribute_discover']['rules'].insert(2, new_rule)


#To Client PADS
port = {"value": "v0.5"}
count_id ={"value": "2"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_discovery"}
standard_metadata_ingress_port = {"value": "v0.2"}
PPPoE_D_PPPoE_code={"value": "0x65"}
eth_dstAddr={"value": "0x3a87d73a00ac"}
match={"eth.dstAddr": eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_D.PPPoE_code": PPPoE_D_PPPoE_code}
new_rule={"action": action,"match": match, "name": "1"}
rule['tables']['traffic_distribute_discover']['rules'].insert(3, new_rule)

#VM8
port = {"value": "v0.6"}
count_id ={"value": "2"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_discovery"}
standard_metadata_ingress_port = {"value": "v0.2"}
PPPoE_D_PPPoE_code={"value": "0x65"}
eth_dstAddr={"value": "0xe60ab599c0f5"}
match={"eth.dstAddr": eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_D.PPPoE_code": PPPoE_D_PPPoE_code}
new_rule={"action": action,"match": match, "name": "1"}
rule['tables']['traffic_distribute_discover']['rules'].insert(3, new_rule)

#VM9
port = {"value": "v0.7"}
count_id ={"value": "2"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_discovery"}
standard_metadata_ingress_port = {"value": "v0.2"}
PPPoE_D_PPPoE_code={"value": "0x65"}
eth_dstAddr={"value": "0x2a57c2de0ba9"}
match={"eth.dstAddr": eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_D.PPPoE_code": PPPoE_D_PPPoE_code}
new_rule={"action": action,"match": match, "name": "1"}
rule['tables']['traffic_distribute_discover']['rules'].insert(3, new_rule)

#VM10
port = {"value": "v0.8"}
count_id ={"value": "2"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_discovery"}
standard_metadata_ingress_port = {"value": "v0.2"}
PPPoE_D_PPPoE_code={"value": "0x65"}
eth_dstAddr={"value": "0x96d93a95c745"}
match={"eth.dstAddr": eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_D.PPPoE_code": PPPoE_D_PPPoE_code}
new_rule={"action": action,"match": match, "name": "1"}
rule['tables']['traffic_distribute_discover']['rules'].insert(3, new_rule)

#VM11
port = {"value": "v0.9"}
count_id ={"value": "2"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_discovery"}
standard_metadata_ingress_port = {"value": "v0.2"}
PPPoE_D_PPPoE_code={"value": "0x65"}
eth_dstAddr={"value": "0x3a7138b4a490"}
match={"eth.dstAddr": eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_D.PPPoE_code": PPPoE_D_PPPoE_code}
new_rule={"action": action,"match": match, "name": "1"}
rule['tables']['traffic_distribute_discover']['rules'].insert(3, new_rule)



#By default all PPPOES packets to VNF 
rule['tables']['traffic_distribute_session']={}
port = {"value": "v0.2"}
count_id ={"value": "0"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
rule['tables']['traffic_distribute_session']['default_rule']={"action":action, "name":"Default"}
rule['tables']['traffic_distribute_session']['rules']=[]

#LCP packets to VNF
port = {"value": "v0.2"}
count_id ={"value": "1"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.4"}
PPPoE_protocol_PPP_protocol={"value": "0xc021"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "0"}
rule['tables']['traffic_distribute_session']['rules'].insert(0, new_rule)

port = {"value": "v0.2"}
count_id ={"value": "1"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.5"}
PPPoE_protocol_PPP_protocol={"value": "0xc021"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "0"}
rule['tables']['traffic_distribute_session']['rules'].insert(0, new_rule)


port = {"value": "v0.2"}
count_id ={"value": "1"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.6"}
PPPoE_protocol_PPP_protocol={"value": "0xc021"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "0"}
rule['tables']['traffic_distribute_session']['rules'].insert(0, new_rule)

port = {"value": "v0.2"}
count_id ={"value": "1"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.7"}
PPPoE_protocol_PPP_protocol={"value": "0xc021"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "0"}
rule['tables']['traffic_distribute_session']['rules'].insert(0, new_rule)

port = {"value": "v0.2"}
count_id ={"value": "1"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.8"}
PPPoE_protocol_PPP_protocol={"value": "0xc021"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "0"}
rule['tables']['traffic_distribute_session']['rules'].insert(0, new_rule)

port = {"value": "v0.2"}
count_id ={"value": "1"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.9"}
PPPoE_protocol_PPP_protocol={"value": "0xc021"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "0"}
rule['tables']['traffic_distribute_session']['rules'].insert(0, new_rule)

#Encapsulated packets to Client
#Host
port = {"value": "v0.4"}
count_id ={"value": "2"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.3"}
eth_dstAddr={"value": "0x00154d000004"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port}
new_rule={"action": action,"match": match, "name": "1"}
rule['tables']['traffic_distribute_session']['rules'].insert(1, new_rule)
#VM7
port = {"value": "v0.5"}
count_id ={"value": "2"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.3"}
eth_dstAddr={"value": "0x3a87d73a00ac"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port}
new_rule={"action": action,"match": match, "name": "1"}
rule['tables']['traffic_distribute_session']['rules'].insert(1, new_rule)

#VM8
port = {"value": "v0.6"}
count_id ={"value": "2"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.3"}
eth_dstAddr={"value": "0xe60ab599c0f5"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port}
new_rule={"action": action,"match": match, "name": "1"}
rule['tables']['traffic_distribute_session']['rules'].insert(1, new_rule)

#VM9
port = {"value": "v0.7"}
count_id ={"value": "2"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.3"}
eth_dstAddr={"value": "0x2a57c2de0ba9"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port}
new_rule={"action": action,"match": match, "name": "1"}
rule['tables']['traffic_distribute_session']['rules'].insert(1, new_rule)

#VM10
port = {"value": "v0.8"}
count_id ={"value": "2"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.3"}
eth_dstAddr={"value": "0x96d93a95c745"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port}
new_rule={"action": action,"match": match, "name": "1"}
rule['tables']['traffic_distribute_session']['rules'].insert(1, new_rule)

#VM11
port = {"value": "v0.9"}
count_id ={"value": "2"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.3"}
eth_dstAddr={"value": "0x3a7138b4a490"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port}
new_rule={"action": action,"match": match, "name": "1"}
rule['tables']['traffic_distribute_session']['rules'].insert(1, new_rule)

#Session config. packets from VNF to Client
port = {"value": "v0.4"}
count_id ={"value": "3"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.2"}
eth_dstAddr={"value": "0x00154d000004"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port}
new_rule={"action": action,"match": match, "name": "2"}
rule['tables']['traffic_distribute_session']['rules'].insert(2, new_rule)

port = {"value": "v0.5"}
count_id ={"value": "3"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.2"}
eth_dstAddr={"value": "0x3a87d73a00ac"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port}
new_rule={"action": action,"match": match, "name": "2"}
rule['tables']['traffic_distribute_session']['rules'].insert(2, new_rule)

port = {"value": "v0.6"}
count_id ={"value": "3"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.2"}
eth_dstAddr={"value": "0xe60ab599c0f5"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port}
new_rule={"action": action,"match": match, "name": "2"}
rule['tables']['traffic_distribute_session']['rules'].insert(2, new_rule)

port = {"value": "v0.7"}
count_id ={"value": "3"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.2"}
eth_dstAddr={"value": "0x2a57c2de0ba9"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port}
new_rule={"action": action,"match": match, "name": "2"}
rule['tables']['traffic_distribute_session']['rules'].insert(2, new_rule)

port = {"value": "v0.8"}
count_id ={"value": "3"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.2"}
eth_dstAddr={"value": "0x96d93a95c745"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port}
new_rule={"action": action,"match": match, "name": "2"}
rule['tables']['traffic_distribute_session']['rules'].insert(2, new_rule)

port = {"value": "v0.9"}
count_id ={"value": "3"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.2"}
eth_dstAddr={"value": "0x3a7138b4a490"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port}
new_rule={"action": action,"match": match, "name": "2"}
rule['tables']['traffic_distribute_session']['rules'].insert(2, new_rule)

#CHAP packets to VNF
port = {"value": "v0.2"}
count_id ={"value": "4"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.4"}
PPPoE_protocol_PPP_protocol={"value": "0xc223"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "3"}
rule['tables']['traffic_distribute_session']['rules'].insert(3, new_rule)

port = {"value": "v0.2"}
count_id ={"value": "4"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.5"}
PPPoE_protocol_PPP_protocol={"value": "0xc223"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "3"}
rule['tables']['traffic_distribute_session']['rules'].insert(3, new_rule)

port = {"value": "v0.2"}
count_id ={"value": "4"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.6"}
PPPoE_protocol_PPP_protocol={"value": "0xc223"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "3"}
rule['tables']['traffic_distribute_session']['rules'].insert(3, new_rule)

port = {"value": "v0.2"}
count_id ={"value": "4"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.7"}
PPPoE_protocol_PPP_protocol={"value": "0xc223"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "3"}
rule['tables']['traffic_distribute_session']['rules'].insert(3, new_rule)

port = {"value": "v0.2"}
count_id ={"value": "4"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.8"}
PPPoE_protocol_PPP_protocol={"value": "0xc223"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "3"}
rule['tables']['traffic_distribute_session']['rules'].insert(3, new_rule)

port = {"value": "v0.2"}
count_id ={"value": "4"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.9"}
PPPoE_protocol_PPP_protocol={"value": "0xc223"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr, "standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "3"}
rule['tables']['traffic_distribute_session']['rules'].insert(3, new_rule)

#IPCP packets to VNF
port = {"value": "v0.2"}
count_id ={"value": "5"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.4"}
PPPoE_protocol_PPP_protocol={"value": "0x8021"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "4"}
rule['tables']['traffic_distribute_session']['rules'].insert(4, new_rule)

port = {"value": "v0.2"}
count_id ={"value": "5"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.5"}
PPPoE_protocol_PPP_protocol={"value": "0x8021"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "4"}
rule['tables']['traffic_distribute_session']['rules'].insert(4, new_rule)

port = {"value": "v0.2"}
count_id ={"value": "5"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.6"}
PPPoE_protocol_PPP_protocol={"value": "0x8021"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "4"}
rule['tables']['traffic_distribute_session']['rules'].insert(4, new_rule)

port = {"value": "v0.2"}
count_id ={"value": "5"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.7"}
PPPoE_protocol_PPP_protocol={"value": "0x8021"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "4"}
rule['tables']['traffic_distribute_session']['rules'].insert(4, new_rule)

port = {"value": "v0.2"}
count_id ={"value": "5"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.8"}
PPPoE_protocol_PPP_protocol={"value": "0x8021"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "4"}
rule['tables']['traffic_distribute_session']['rules'].insert(4, new_rule)

port = {"value": "v0.2"}
count_id ={"value": "5"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.9"}
PPPoE_protocol_PPP_protocol={"value": "0x8021"}
eth_dstAddr={"value": "0x9aeed716c34a"}
match={"eth.dstAddr":eth_dstAddr,"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "4"}
rule['tables']['traffic_distribute_session']['rules'].insert(4, new_rule)

#CCP packets to VNF
port = {"value": "v0.2"}
count_id ={"value": "6"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.4"}
PPPoE_protocol_PPP_protocol={"value": "0x00FB"}
match={"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "5"}
rule['tables']['traffic_distribute_session']['rules'].insert(5, new_rule)

#CCP packets to VNF
port = {"value": "v0.2"}
count_id ={"value": "7"}
data={"port":port, "count_id":count_id}
action={"data":data,"type":"route_session"}
standard_metadata_ingress_port = {"value": "v0.4"}
PPPoE_protocol_PPP_protocol={"value": "0x00FD"}
match={"standard_metadata.ingress_port": standard_metadata_ingress_port, "PPPoE_protocol.PPP_protocol": PPPoE_protocol_PPP_protocol}
new_rule={"action": action,"match": match, "name": "6"}
rule['tables']['traffic_distribute_session']['rules'].insert(6, new_rule)

jsonFile = open(r'/home/zhiqiang.qian/npu/PPPoE/src/rule.json', 'r+')
deleteContent(jsonFile)
json.dump(rule,jsonFile)

