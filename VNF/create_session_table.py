from scapy.all import *
from flask import Flask, jsonify
import json,requests


#clear function
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

#setup table entry
session_table=[]

filt = "pppoes or ether proto 0x8863"
Session_ID=0

def process_pppoe(packet):
    global session_table     
   
    if PPPoE in packet and packet[PPP].proto == 0x8021:
        if packet[PPP_IPCP].code == 2:                                    #if sniffed packet is IPCP ACK                        
            if packet[PPP_IPCP_Option_IPAddress].data != "172.32.50.1":     #add client IP
                new_session={"session_id":packet[PPPoE].sessionid, "peer_ip": packet[PPP_IPCP_Option_IPAddress].data}
# add authenticated session to table
                session_table.append(new_session)
                print "session {} added".format(new_session) 
                jsonFile = open(r'/home/user/vnf/src/session_table.json', 'r+')
                deleteContent(jsonFile)
                jsonFile.write(json.dumps(session_table))
# synchronize with HWA
                session_data= json.dumps(session_table)
                url = 'http://192.168.122.66:5000/hwa/session_table'
                headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
                r = requests.post(url, data=session_data, headers=headers)

#if HWA successfully uptate its session table, issue change_rule command to data plane
                if r.status_code==201:
                   print "session table of HWA updated"                    
                   url = 'http://192.168.122.1:5000/fdp/change_rule'
                   r = requests.get(url)
                   if r.status_code==201:
                        print "rule of data plane changed"

    elif PPPoED in packet and packet[PPPoED].code==0xa7:
                
                for x in session_table:  
                    if x['session_id'] == packet[PPPoED].sessionid:
                       session_table.remove(x)
                       print "session {} deleted".format(x)      
                       jsonFile = open(r'/home/user/vnf/src/session_table.json', 'r+')
                       deleteContent(jsonFile)
                       jsonFile.write(json.dumps(session_table))
                       session_data= json.dumps(session_table)
                       url = 'http://192.168.122.66:5000/hwa/delete_session/%s' % x['session_id']
                       r = requests.get(url)
                       #session table of HWA successfully updated, issue request to change rule in data plane

                   



sniff(iface="ens5",prn=process_pppoe)
