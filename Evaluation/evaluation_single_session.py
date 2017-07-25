from pexpect import pxssh
import getpass, os, json, time, datetime, subprocess
from multiprocessing import Process
from scapy.all import *


VNF_hostname= 'user@192.168.122.158'
HWA_hostname='user@192.168.122.66'
CLIENT_hostname='zhiqiang.qian@192.168.122.1'
VNF_username='user'
CLIENT_username='zhiqiang.qian'
PSW='222222'
PSW_host='123456'
PSW_CLIENT='qzqjsqzq'
tx_pcap_VNF2Host='scp /home/user/*.pcap root@192.168.122.1:/home/zhiqiang.qian/evaluation'
tx_pcap_HWA2Host='scp /home/user/*.pcap root@192.168.122.1:/home/zhiqiang.qian/evaluation'
tx_pcap_VM2Host='scp *.pcap root@192.168.122.1:/home/zhiqiang.qian/evaluation'
pppoe_start ='pppoe-start'       
pppoe_stop ='pppoe-stop'
VM_8='vm8@192.168.122.67'
VM_9='vm9@192.168.122.214'
VM_10='vm10@192.168.122.143'
VM_11='vm11@192.168.122.12'

def vnf_process():
   vnf = pxssh.pxssh()
   hostname = VNF_hostname
   username = VNF_username
   password = PSW
   vnf.login(hostname, username, password)
   vnf.sendline('sudo -s')
   vnf.prompt()          
   vnf.sendline(PSW)
   vnf.prompt()
   print('VNF Time: {0}\n'.format(datetime.datetime.time(datetime.datetime.now())))
   vnf.sendline('tcpdump -w vnf_data_9.pcap -i ens5 ')
   print('VNF Time: {0}\n'.format(datetime.datetime.time(datetime.datetime.now())))
   time.sleep(60)
   vnf.prompt()        
   vnf.sendcontrol('c')
   vnf.prompt()        
   vnf.sendline(tx_pcap_VNF2Host)
   vnf.prompt()
   vnf.sendline('yes')
   vnf.prompt()
   vnf.sendline(PSW_host)
   vnf.prompt()
   print vnf.before

def vnf_sync_process():
   vnf = pxssh.pxssh()
   hostname = VNF_hostname
   username = VNF_username
   password = PSW
   vnf.login(hostname, username, password)
   vnf.sendline('sudo -s')
   vnf.prompt()          
   vnf.sendline(PSW)
   vnf.prompt()
   vnf.sendline('tcpdump -w sync_data_9.pcap -i ens3 port 5000 ')
   time.sleep(60)
   vnf.prompt()        
   vnf.sendcontrol('c')
   print vnf.before
   vnf.prompt()        
   vnf.sendline(tx_pcap_VNF2Host)
   vnf.prompt()
   vnf.sendline('yes')
   vnf.prompt()
   vnf.sendline(PSW_host)
   vnf.prompt()
   print vnf.before

def hwa_process():
    hwa = pxssh.pxssh()
    hostname=HWA_hostname
    username = VNF_username
    password = PSW
    hwa.login(hostname, username, password)
    hwa.sendline('sudo -s')
    hwa.prompt()          
    hwa.sendline(PSW)
    hwa.prompt()
    print('HWA Time: {0}\n'.format(datetime.datetime.time(datetime.datetime.now())))   
    hwa.sendline('tcpdump -w hwa_data_9.pcap -i ens5 ')
    print('HWA Time: {0}\n'.format(datetime.datetime.time(datetime.datetime.now())))
    time.sleep(60)
    hwa.prompt()        
    hwa.sendcontrol('c')
    hwa.prompt()        
    hwa.sendline(tx_pcap_VNF2Host)
    hwa.prompt()
    print hwa.before
    hwa.sendline('yes')
    hwa.prompt()
    print hwa.before
    hwa.sendline(PSW_host)
    hwa.prompt()
    print hwa.before

def hwa_sync_process():
    hwa = pxssh.pxssh()
    hostname=HWA_hostname
    username = VNF_username
    password = PSW
    hwa.login(hostname, username, password)
    hwa.sendline('sudo -s')
    hwa.prompt()          
    hwa.sendline(PSW)
    hwa.prompt()
    print('HWA Time: {0}\n'.format(datetime.datetime.time(datetime.datetime.now())))   
    hwa.sendline('tcpdump -w hwa_sync_data_9.pcap -i ens3 port 5000 ')
    print('HWA Time: {0}\n'.format(datetime.datetime.time(datetime.datetime.now())))
    time.sleep(60)
    hwa.prompt()        
    hwa.sendcontrol('c')
    hwa.prompt()        
    hwa.sendline(tx_pcap_VNF2Host)
    hwa.prompt()
    print hwa.before
    hwa.sendline('yes')
    hwa.prompt()
    print hwa.before
    hwa.sendline(PSW_host)
    hwa.prompt()
    print hwa.before


def client_tcpdump_process():
    client = pxssh.pxssh()
    hostname=CLIENT_hostname
    username = CLIENT_username
    password = PSW_CLIENT
    client.login(hostname, username, password)
    client.sendline('sudo -s')
    client.prompt()          
    client.sendline(PSW_CLIENT)
    client.prompt()
    print('client Time: {0}\n'.format(datetime.datetime.time(datetime.datetime.now())))   
    client.sendline('tcpdump -w client_data_9.pcap -i vf0_4 ')
    print('client Time: {0}\n'.format(datetime.datetime.time(datetime.datetime.now())))
    time.sleep(60)
    client.prompt()        
    client.sendcontrol('c')
    client.prompt()        
    client.sendline('mv client_data_9.pcap evaluation/ ')
    client.prompt()
    print client.before

def fdp_process():
    client = pxssh.pxssh()
    hostname=CLIENT_hostname
    username = CLIENT_username
    password = PSW_CLIENT
    client.login(hostname, username, password)
    client.sendline('sudo -s')
    client.prompt()          
    client.sendline(PSW_CLIENT)
    client.prompt()
    print('client Time: {0}\n'.format(datetime.datetime.time(datetime.datetime.now())))   
    client.sendline('tcpdump -w fdp_data_9.pcap -i virbr0 host 192.168.122.1 and port 5000 ')
    print('client Time: {0}\n'.format(datetime.datetime.time(datetime.datetime.now())))
    time.sleep(60)
    client.prompt()        
    client.sendcontrol('c')
    client.prompt()        
    client.sendline('mv fdp_data_9.pcap evaluation/ ')
    client.prompt()
    print client.before

def vm8_process():
    vm8 = pxssh.pxssh()
    hostname=VM_8
    username = 'vm8'
    password = PSW
    vm8.login(hostname, username, password)
    vm8.sendline('sudo -s')
    vm8.prompt()          
    vm8.sendline(PSW)
    vm8.prompt()
    print('VM8 Time: {0}\n'.format(datetime.datetime.time(datetime.datetime.now())))   
    vm8.sendline('tcpdump -w vm8_data_9.pcap -i ens5 ')
    print('VM8 Time: {0}\n'.format(datetime.datetime.time(datetime.datetime.now())))
    time.sleep(60)
    vm8.prompt()        
    vm8.sendcontrol('c')
    vm8.prompt()        
    vm8.sendline(tx_pcap_VM2Host)
    vm8.prompt()
    print vm8.before
    vm8.sendline('yes')
    vm8.prompt()
    print vm8.before
    vm8.sendline(PSW_host)
    vm8.prompt()
    print vm8.before

def vm8_process_1():
    vm8 = pxssh.pxssh()
    hostname=VM_8
    username = 'vm8'
    password = PSW
    vm8.login(hostname, username, password)
    vm8.sendline('sudo -s')
    vm8.prompt()          
    vm8.sendline(PSW)
    vm8.prompt()
    time.sleep(35)
    vm8.sendline(pppoe_start)
    print('VM8 start pppoe client: {0}\n'.format(datetime.datetime.time(datetime.datetime.now()))) 
    vm8.prompt()
    print vm8.before 

def vm8_process_2():
    vm8 = pxssh.pxssh()
    hostname=VM_8
    username = 'vm8'
    password = PSW
    vm8.login(hostname, username, password)
    vm8.sendline('sudo -s')
    vm8.prompt()          
    vm8.sendline(PSW)
    vm8.prompt()
    vm8.sendline(pppoe_stop)
    vm8.prompt()
    vm8.sendline('ping 172.32.50.1 -i 0.01')
    print('VM8 start ping : {0}\n'.format(datetime.datetime.time(datetime.datetime.now())))
    vm8.prompt() 
    vm8.sendcontrol('c')  

def vm9_process():
    vm9 = pxssh.pxssh()
    hostname=VM_9
    username = 'vm9'
    password = PSW
    vm8.login(hostname, username, password)
    vm8.sendline('sudo -s')
    vm8.prompt()          
    vm8.sendline(PSW)
    vm8.prompt()
    print('VM8 Time: {0}\n'.format(datetime.datetime.time(datetime.datetime.now())))   
    vm8.sendline('tcpdump -G 60 -W 1 -w vm8_data_9.pcap -i ens5 ')
    print('VM8 Time: {0}\n'.format(datetime.datetime.time(datetime.datetime.now())))
    time.sleep(60)
    vm8.prompt()        
    vm8.sendline(tx_pcap_VM2Host)
    vm8.prompt()
    print hwa.before
    vm8.sendline('yes')
    vm8.prompt()
    print vm8.before
    vm8.sendline(PSW_host)
    vm8.prompt()
    print vm8.before

 


def client_process():
    time.sleep(70)
    os.system(pppoe_stop)
    os.system(pppoe_start)
    print('PPPoE client started: {0}\n'.format(datetime.datetime.time(datetime.datetime.now())))


if __name__ == '__main__':
   p1 = Process(target=vnf_process)
   p1.start()
   p2 = Process(target=hwa_process)
   p2.start()
   p5 = Process(target=vnf_sync_process)
   p5.start()
   p6 = Process(target=hwa_sync_process)
   p6.start()
   p7 = Process(target=fdp_process)
   p7.start()
   p8 = Process(target=vm8_process)
   p8.start()
   p9 = Process(target=vm8_process_1)
   p9.start()
   p10 = Process(target=vm8_process_2)
   p10.start()
   p1.join()
   p2.join()
   p5.join()
   p6.join()
   p7.join()
   p8.join()
   p9.join()
   p10.join()

#   calculate packet rate at the time scale of 0.01m
   pkts_vnf=rdpcap('evaluation/vnf_data_9.pcap')
   pkts_hwa=rdpcap('evaluation/hwa_data_9.pcap')
   pkts_sync=rdpcap('evaluation/sync_data_9.pcap')
   pkts_hwa_sync=rdpcap('evaluation/hwa_sync_data_9.pcap')
   pkts_fdp=rdpcap('evaluation/fdp_data_9.pcap')
   pkts_vm8=rdpcap('evaluation/vm8_data_9.pcap')
   zero_point=0
   packet_rates_vm8=[]
   zero_point=0
   packet_rates_vnf=[]
   packet_rates_hwa=[]
   packet_rates_client=[]
   packet_rates_sync=[]
   packet_rates_hwa_sync=[]
   packet_rates_fdp=[]
   
   for pkt in pkts_vm8:
          if PPPoED in pkt and pkt[PPPoED].code==0x09:
             zero_point=pkt.time
             break
   print '%(time).6f s' % {'time': zero_point,}
   print(
     datetime.datetime.fromtimestamp(zero_point).strftime('%Y-%m-%d %H:%M:%S')
   )

   for x in xrange(0, 130):
       count=0
       for pkt in pkts_vm8:
           if pkt.time >=(zero_point + 0.01 * x) and pkt.time < (zero_point + 0.01 * x+ 0.01) :
              count = count + 1
       packet_rate= count / 0.01
       packet_rates_vm8.append(packet_rate)
   print('VM8(ckient 1) packet rate: {0}\n'.format(packet_rates_vm8))

   for x in xrange(0, 130):
       count=0
       for pkt in pkts_vnf:
           if pkt.time >=(zero_point + 0.01 * x) and pkt.time < (zero_point + 0.01 * x+ 0.01) :
              count = count + 1
       packet_rate= count / 0.01
       packet_rates_vnf.append(packet_rate)
   print('VNF packet rate: {0}\n'.format(packet_rates_vnf))

   for x in xrange(0, 130):
       count=0
       for pkt in pkts_hwa:
           if pkt.time >=(zero_point + 0.01 * x) and pkt.time < (zero_point + 0.01 * x+ 0.01) :
              count = count + 1
       packet_rate= count / 0.01
       packet_rates_hwa.append(packet_rate)
   print('HWA packet rate: {0}\n'.format(packet_rates_hwa) ) 

   for x in xrange(0, 130):
       count=0
       for pkt in pkts_sync:
           if pkt.time >=(zero_point + 0.01 * x) and pkt.time < (zero_point + 0.01 * x+ 0.01) :
              count = count + 1
       packet_rate= count / 0.01
       packet_rates_sync.append(packet_rate)
   print('Synchronization packet rate: {0}\n'.format(packet_rates_sync))

   for x in xrange(0, 130):
       count=0
       for pkt in pkts_hwa_sync:
           if pkt.time >=(zero_point + 0.01 * x) and pkt.time < (zero_point + 0.01 * x+ 0.01) :
              count = count + 1
       packet_rate= count / 0.01
       packet_rates_hwa_sync.append(packet_rate)
   print('Synchronization in HWA packet rate: {0}\n'.format(packet_rates_hwa_sync))

   with open(r'/home/zhiqiang.qian/evaluation/evaluation_single_session_log.txt', 'w') as f:
        f.write("VM8(ckient 1) packet rate: \n {0}\n\n VNF packet rate: \n {1}\n\n HWA packet rate: \n {2}\n\n Synchronization packet rate: \n {3}\n\n Synchronization in HWA packet rate: \n {4}\n\n".format(packet_rates_vm8,packet_rates_vnf,packet_rates_hwa,packet_rates_sync,packet_rates_hwa_sync))


   



