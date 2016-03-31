class DHCPeditor:
	
	config_file = ''

	def __init__(self, config_file_path):
		self.config_file = config_file_path
	
	def add_entry(self, hostname, ip, mac):
		with open(self.config_file, 'a') as dhcp_list:
			dhcp_list.write('\n\thost ' + hostname + ' {\n\thardware ethernet '+ mac + ';\n\tfixed-address '+ ip + '; }\n')
	
	def delete_entry(self, entry): #Can delete entries either by ip or by mac. IT CANNOT DELETE ANYTHING BY HOSTNAME.
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
				dhcp_file.write(line)

	 			
	def edit_entry(self, old, new): #This looks for an IP or a mac and replace it with a new one.
	#It doesn't change the hostname, so if you want to change something it's better to remove an entry and add a new one.
		intext=''
		with open(self.config_file, 'r') as dhcp_list:
			intext = dhcp_list.read()

		if intext.find(old) == -1:
			return 1

		intext = intext.replace(old, new, 1) #As seen here, it finds a substring in the file and replaces it, so be careful when using it.
			
		with open(self.config_file, 'w') as dhcp_list:
			dhcp_list.write(intext)

		return 0






