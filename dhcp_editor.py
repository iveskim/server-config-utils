class DHCPeditor:
	
	config_file = ''

	def __init__(self, config_file_path):
		self.config_file = config_file_path
	
	def add_entry(self, hostname, ip, mac): #this works for sure
		with open(self.config_file, 'a') as dhcp_list:
			dhcp_list.write('\n\thost ' + hostname + ' {\n\thardware ethernet '+ mac + ';\n\tfixed-address '+ ip + '; }\n')
	
	def delete_entry(self, entry): #this works as far as I could test. it can delete entries either by ip or by mac. IT CANNOT DELETE ANYTHING BY HOSTNAME.
		intext = []
		with open(self.config_file, 'r') as dhcp_list:
			intext = dhcp_list.readlines()
			for i in range(len(intext)):
				if intext[i].find(entry) != -1:
					for j in range (i,len(intext)):
						if intext[j].find('}') != -1:
							intext[j] = ''
							break

						intext[j] = ''

					for k in range (i, -1, -1):
						if intext[k].find('{') != -1:
							intext[k] = ''
							break

						intext[k] = ''

		with open(self.config_file, 'w') as dhcp_file:
			for line in intext:
				dhcp_file.write(line) #this works


	def edit_entry(self, old, new): #okay so to keep it simple: all this does is look for an IP or a mac and replace it with a new one. it doesnt even change the hostname, i'll add that soon (never).
		intext=''
		with open(self.config_file, 'r') as dhcp_list:
			intext = dhcp_list.read()

		if intext.find(old) == -1:
			return 1

		intext = intext.replace(old, new, 1) #this might go very wrong. only if the user fucks up tho, afaik.
			
		with open(self.config_file, 'w') as dhcp_list:
			dhcp_list.write(intext)

		return 0






