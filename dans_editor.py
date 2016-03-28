class Danseditor:
	
	groups_config_file = ''

	def __init__(self, config_file_path):
		self.groups_config_file = config_file_path

	def check_group(self, ip):
		group = '0'
		with open(self.groups_config_file, 'r') as assignments_list:
			intext = assignments_list.readlines()
			for line in intext:
				if line.find(ip) != -1:
					group = line[-2:].replace('\n', '').replace('r', '') #this is a bit lazy and seems intuitively unreliable, but i can't find a case where it doesn't work, so.
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
			intext = assignments_list.readlines()

		for i in range(len(intext)):
			if (intext[i].find('#') == -1 and intext[i][-2:].replace('\n', '').replace('r', '') == group):
				intext.insert(i, ip+'=filter'+group+'\n')
				break

		with open(self.groups_config_file, 'w') as assignments:
			for line in intext:
				assignments.write(line)

		return 0



