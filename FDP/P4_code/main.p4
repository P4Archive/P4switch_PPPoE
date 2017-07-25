/*definition of main program */



#include "headers.p4"

control egress {

}


control ingress {
if(eth.etherType==0x8863)
{
	apply(traffic_distribute_discover);
}

else{
	if(eth.etherType==0x8864) 
		{
			apply(traffic_distribute_session);
		}

}
   

}





table traffic_distribute_discover  //Active discovery stage match
	{
	reads { eth.dstAddr : exact;
		standard_metadata.ingress_port : exact;		
		PPPoE_D.PPPoE_code: exact;
		
	       }

	actions{
		_drop;
		//PADO;
		route_discovery;
		}
}

table traffic_distribute_session  //Active discovery stage match
	{
	reads { eth.dstAddr : exact;
		standard_metadata.ingress_port : exact;
		PPPoE_protocol.PPP_protocol: exact;	
	       }

	actions{
		_drop;
		route_session;
		}
}

counter traffic_distribute_discover_p {
    type: packets;
    static: traffic_distribute_discover;
    instance_count: 8;
}
counter traffic_distribute_session_p {
    type: packets;
    static: traffic_distribute_session;
    instance_count: 8;
}

action route_discovery(in bit<16> port, in bit<3> count_id) {
    modify_field(standard_metadata.egress_spec, port );
    count(traffic_distribute_discover_p, count_id);
    //count(traffic_distribute_discover_b, count_id);
}

action route_session(in bit<16> port, in bit<3> count_id) {
    modify_field(standard_metadata.egress_spec, port );
    count(traffic_distribute_session_p, count_id);
    //count(traffic_distribute_session_b, count_id);
}

/*
action PADO (in bit<3> count_id) {


    add_header(PPPoE_tags_ac_name);    

    modify_field(PPPoE_tags_ac_name.tag_type, 0x0102);
    modify_field(PPPoE_tags_ac_name.tag_length, 0x000c);
    modify_field(PPPoE_tags_ac_name.tag_content_1, AC_Name_1);
    modify_field(PPPoE_tags_ac_name.tag_content_2, AC_Name_2);

    modify_field(PPPoE_D.PPPoE_code, 0x07);
    modify_field(PPPoE_D.load_length, 48);
    modify_field(eth.srcAddr, FDP_MAC_address);
    modify_field(eth.dstAddr, meta_data.mac_src);

    modify_field(standard_metadata.egress_spec, standard_metadata.ingress_port);
    count(traffic_distribute_discover_p, count_id);
  //  count(traffic_distribute_discover_b, count_id);


	    
}
*/

action _drop() {
drop();
}


/*
control ingress {


	apply(traffic_distribute);
   
}
*/
/*


table traffic_distribute  //Active discovery stage match
	{
	reads {
		eth.etherType: exact;
		standard_metadata.ingress_port : exact;
		PPPoE_D.PPPoE_code: exact;
		PPPoE_protocol.PPP_protocol: exact;
		
	       }

	actions{
		_drop;
		PADO;
		route;
		}

}


counter traffic_distribute_p {
    type: packets;
    static: traffic_distribute;
    instance_count: 8;
}


action _drop() {
drop();
}

action route(in bit<16> port, in bit<3> count_id) {
    modify_field(standard_metadata.egress_spec, port );
    count(traffic_distribute_p, count_id);
   
}

action PADO (in bit<3> count_id) {


    add_header(PPPoE_tags_ac_name);    
    modify_field(PPPoE_tags_ac_name.tag_type, 0x0102);
    modify_field(PPPoE_tags_ac_name.tag_length, 0x000c);
    modify_field(PPPoE_tags_ac_name.tag_content_1, AC_Name_1);
    modify_field(PPPoE_tags_ac_name.tag_content_2, AC_Name_2);
    modify_field(PPPoE_D.PPPoE_code, 0x07);
    modify_field(PPPoE_D.load_length, 48);
    modify_field(eth.srcAddr, FDP_MAC_address);
    modify_field(eth.dstAddr, meta_data.mac_src);
    modify_field(standard_metadata.egress_spec, standard_metadata.ingress_port);
    count(traffic_distribute_p, count_id);
  //  count(traffic_distribute_discover_b, count_id);

	    
}
/*
action route_discovery(in bit<16> port, in bit<5> count_id) {
    modify_field(standard_metadata.egress_spec, port );
    count(traffic_distribute_discover_p, count_id);
    //count(traffic_distribute_discover_b, count_id);
}

action route_session(in bit<16> port, in bit<5> count_id) {
    modify_field(standard_metadata.egress_spec, port );
    count(traffic_distribute_session_p, count_id);
    //count(traffic_distribute_session_b, count_id);
}
*/












/*
counter traffic_distribute_session_b {
    type: bytes;
    static: traffic_distribute_session;
    instance_count: 8;
}

counter traffic_distribute_discover_b {
    type: bytes;
    static: traffic_distribute_discover;
    instance_count: 8;
}

*/



