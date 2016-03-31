class Danseditor:
	
	groups_config_file = ''

	def __init__(self, config_file_path):
		self.groups_config_file = config_file_path

	def check_group(self, ip):
		group = '0'
		with open(self.groups_config_file, 'r') as assignments_list:
			intext = assignments_list.read().splitlines()
			for line in intext:
				if line.find(ip) != -1:
					group = line[-1:]
					break

		return group

	def delete_assignment(self, ip):
		intext = []
		with open(self.groups_config_file, 'r') as assignments_list:
			intext = assignments_list.readlines()

		for line in intext:
			if line.find(ip) != -1:
				intext.remove(line)
				break

		with open(self.groups_config_file, 'w') as assignments:
			for line in intext:
				assignments.write(line)


	def assign_group(self, ip, group):
		if (self.check_group(ip) != '0' and self.check_group(ip) != group):
			self.delete_assignment(ip)
		elif (self.check_group(ip) == group):
			return 1

		intext = []
		with open(self.groups_config_file, 'r') as assignments_list:
			intext = assignments_list.read().splitlines()

		for i in range(len(intext)): #Tries to organize new entry insertion according to comments or existing entries, adds the new entry at end of file on failure.
			if (intext[i].find('# F'+group) != -1):
				intext.insert(i+1, ip+'=filter'+group)
				break
			elif (intext[i].find('#') == -1 and intext[i][-1:] == group):
				intext.insert(i, ip+'=filter'+group)
				break
			elif(i == len(intext)-1):
				intext.append(ip+'=filter'+group)

		with open(self.groups_config_file, 'w') as assignments:
			for line in intext:
				assignments.write(line+'\n')

		return 0



