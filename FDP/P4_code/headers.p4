/*definitions of headers and parsers */

//#define  AC_Name_Length_half_bit 48
//#define  AC_Cookie_Length_bit 128

header_type meta_data_t {
    fields {
        bit<48> mac_src;
	bit<48> mac_dst;
    }
}

header_type ethernet_t {
    fields {
        bit<48> dstAddr;
        bit<48> srcAddr;
        bit<16> etherType;
    }
}



header_type PPPoE_Discovery_t {
    fields {
        bit<4> PPPoE_version; 			//PPPoE version
	bit<4> PPPoE_type; 				// PPPoE type
	bit<8> PPPoE_code; 				//PPPoE code
	bit<16> PPPoE_sissionID; 			//PPPoE session ID
	bit<16> load_length; 			//PPPoE Length
	bit<32> tag_PPPoE; 			//PPPoE Tag	
    }
}



/*defined customized header for ac name*/



/*define customized header for ac cookie */
/*
header_type PPPoE_tags_ac_cookie_t{
	fields{
	bit<16> tag_type ; // Tag Type
	bit<16> tag_length; //Tag Length
	bit<AC_Cookie_Length_bit> tag_content;//Tag content
		}
 
}
*/

header_type PPPoE_session_t {
    fields {
        bit<4> PPPoE_version; 			//PPPoE version
	bit<4> PPPoE_type;				//PPPoE type        
	bit<8> PPPoE_code;				//PPPoE code indicating current stage e.g. PADI	
	bit<16> PPPoE_sessionID; 			//PPPoE session ID
	bit<16> load_length; 			//PPPoE load length	
    }
}

header_type PPPoE_protocol_t {			//PPPoE protocol
    fields {
        bit<16> PPP_protocol ; 		        //PPPoE protocol
    }
}

header ethernet_t eth;
header PPPoE_Discovery_t PPPoE_D;
header PPPoE_protocol_t PPPoE_protocol;
header PPPoE_session_t PPPoE_session;
//header PPPoE_tags_t PPPoE_tags;
//header PPPoE_tags_ac_name_t PPPoE_tags_ac_name;
//header PPPoE_tags_ac_cookie_t PPPoE_tags_ac_cookie;
//metadata meta_data_t meta_data; 




parser start {
	
    extract(eth);	     
    return select ( latest.etherType ) 		//steer traffics to different parser based on eth.type 
	{
	0x8863: parse_PPPoE_Discovery ;         //if 0x8863 to PPPoE discovery parser
	0x8864: parse_PPPoE_Session;		//if 0x8864 to PPPoE session parser
	default: ingress;
	}
}

parser parse_PPPoE_Discovery {
	extract(PPPoE_D);	
	return ingress; 
}





parser parse_PPPoE_Session {

	extract(PPPoE_session);
	return parse_PPPoE_protocol;
        
}

parser parse_PPPoE_protocol {
	extract(PPPoE_protocol);
	return ingress;
        
}

/*
parser parse_PPPoE_tags_ac_name{
	extract(PPPoE_tags_ac_name);
	return select(current(0,4))
		{
		0x0104: parse_PPPoE_tags_ac_cookie;
		default:ingress;
		}

}


parser parse_PPPoE_tags_ac_cookie{
	extract(PPPoE_tags_ac_cookie);
	return ingress;

}

parser parse_PPPoE_tags_ac_name{
	extract(PPPoE_tags_ac_name);
	return ingress;


}

header_type PPPoE_tags_t{
	fields
	{
	bit<16> tag_type ; // Tag Type
	bit<16> tag_length; //Tag Length
	varbit<320> tag_content;//Tag content
		}

	length: (tag_length+4) ; 
}

header_type PPPoE_tags_ac_name_t{
	fields{
	bit<16> tag_type ;//Tag Type
	bit<16> tag_length; //Tag Length
	bit<48> tag_content_1;//Tag content
	bit<48> tag_content_2;//Tag content
	
	}
}

parser parse_PPPoE_tags {
	extract(PPPoE_tags);
	return select(current(0,4))
	{
		0x0102: parse_PPPoE_tags_ac_name;
		default:ingress;

		}
        
}
*/
