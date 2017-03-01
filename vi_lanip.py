import srp, Ether, ARP, conf



if __name__ == "__main__":
	lan = '10.10.10.0/24'
	  
	ans, unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=lan), timeout=2)
	for snd, rcv in ans:
		cur_mac = rcv.sprintf("%Ether.src%")
		cur_ip  = rcv.sprintf("%ARP.psrc%")
		print (cur_mac + ' - ' +cur_ip)
