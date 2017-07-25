# P4switch_PPPoE
P4 Switch that can offload PPPoE traffics between x86 based VNF instance and heterogeneous HWA (e.g. FPGA, GPU))
In HWA folder, 
HWA_sniffer_6.py is the HWA emulator that process PPPoE session data, 
HWA_api.py is the Restful prgram that offer a management port for VNF acess.
Both of them should be running during evaluation regardless of fixed or dynamic rule

In VNF folder,
create_session_table_fix.py is the main program running in VNF for state synchronization with HWA in the case of fixed rule
create_session_table_dyn.py is the main program running in VNF in case of dynamic rule

In FDP folder,
In subfolder P4_code is the p4 programm running in switch, headers.p4 contains the header and parser definitions, main.p4 contains table and action definition.
FDP_api.py should be lauched only in the case of dynamic rule, it's a Restful program offerring management port for VNF rule configuration
create_dyn_rule.py is used in case of dynamic rule, to set a default rule of data plane switch
create_fix_rule.py is used in case of fix rule, where rule won't be changed during run-time  

In Evaluation folder
evaluation_single_session.py is evaluation program to evaluate traffic distribution of single session fixed rule 
evaluation_single_session_dyn.py is evaluation program to evaluate traffic distribution of single session dynamic rule
evaluation_multiple_session.py is evaluation program to evaluate traffic distribution of multiple session fixed rule
evaluation_multiple_session_dyn.py is evaluation program to evaluate traffic distribution of multiple session dynamic rule
In subfolder Evaluation_log, evaluation raw data is stored.

Thanks.
