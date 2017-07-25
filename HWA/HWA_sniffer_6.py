from scapy.all import *
import json

filter = "pppoes"
jsonFile = open(r'/home/user/session_table.json', 'r+')
session_table=json.load(jsonFile)
Server_MAC='52:54:00:d5:c0:2d'
MAC_Add='52:54:00:31:17:93' #Local MAC Address of ens3
Exteral_Int_IP_Add='192.168.122.66' #Local IP Address of ens3
Internal_Int_IP_Add='172.32.50.1'
ppp_old=PPP()
pppoe_old=PPPoE()
eth_old=Ether()
ip_old=IP()

def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False

#clear function
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

def process_pppoe(packet):
    global session_table
    global ip_old
    global ppp_old
    global pppoe_old
    global eth_old 



    if PPPoE in packet and contains(session_table, lambda x: x['session_id'] == packet[PPPoE].sessionid):
        
        print "session {} get processed".format(packet[PPPoE].sessionid)
        if TCP in packet: 
          payload_old=packet.copy() 
          payload_old=payload_old[TCP]
          print('TCP header: {0}\n'.format(repr(tcp_old)))
        elif ICMP in packet:
           payload_old= packet[ICMP]
           payload_old.chksum=None
           payload_old.seq=packet[ICMP].seq
           ip_old=packet.copy()
           ip_old[IP].remove_payload()
           ip_old=ip_old[IP]
           ip_old.chksum=None
           ppp_old=packet.copy()
           ppp_old[PPP].remove_payload()
           ppp_old=ppp_old[PPP]
           pppoe_old=packet.copy()
           pppoe_old[PPPoE].remove_payload()
           pppoe_old=pppoe_old[PPPoE]
           eth_old=packet.copy()
           eth_old[Ether].remove_payload()
           eth_old=eth_old[Ether]
#       Build new packet
           if packet[IP].dst== Internal_Int_IP_Add:
              eth_new=Ether() 
              eth_new.type=0x8864
              eth_new.src=packet[Ether].dst
              eth_new.dst=packet[Ether].src
              ip_new=ip_old.copy()
              ip_new.dst=ip_old.src
              ip_new.src=ip_old.dst
              payload_new=payload_old.copy()
              payload_new.type=0
              packet_new=eth_new/pppoe_old/ppp_old/ip_new/payload_new
           #packet_new=IP(dst='192.168.122.42')/payload_old
              print('New packet S: {0}\n'.format(repr(packet_new)))
              sendp(packet_new,iface="ens5") 

           else:
              eth_new=eth_old.copy()
              eth_new.type=0x0800
              eth_new.src=MAC_Add
              eth_new.dst=Server_MAC
              ip_new=ip_old.copy()
              ip_new.src=Exteral_Int_IP_Add
              packet_new=ip_new/payload_old
              packet_rx=sr1(packet_new,iface="ens3")
              print('Receive Packet: {0}\n'.format(repr(packet_rx)))
              if TCP in packet_rx: 
                payload_old_s=packet_rx.copy() 
                payload_old_s=payload_old_s[TCP]
                print('TCP header S: {0}\n'.format(repr(tcp_old_s)))
              elif ICMP in packet:
                payload_old_s= packet_rx[ICMP]
                payload_old_s.chksum=None
                ip_old_s=packet_rx.copy()
                ip_old_s[IP].remove_payload()
                ip_old_s=ip_old_s[IP]
                ip_old_s.chksum=None
                print('IP header S: {0}\n'.format(repr(ip_old_s)))
                eth_old_s=Ether()
                print('Ethernet header S: {0}\n'.format(repr(eth_old_s)))

        #       Build new packet
                eth_new_s=eth_old_s.copy() 
                eth_new_s.type=0x8864
                eth_new_s.src=eth_old.dst
                eth_new_s.dst=eth_old.src
                ip_new_s=ip_old_s.copy()
                ip_new_s.dst=ip_old.src
                packet_new_s=eth_new_s/pppoe_old/ppp_old/ip_new_s/payload_old_s
                #packet_new=IP(dst='192.168.122.42')/payload_old
                print('New packet S: {0}\n'.format(repr(packet_new_s)))
                sendp(packet_new_s,iface="ens5")

        
    else:
         if PPPoE in packet: 
            print "session {} get dropped".format(packet[PPPoE].sessionid)          

while True:
 jsonFile = open(r'/home/user/session_table.json', 'r+')
 session_table=json.load(jsonFile)
 sniff(filter=filter,prn=process_pppoe,count=1)


