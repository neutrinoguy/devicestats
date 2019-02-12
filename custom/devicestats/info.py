from drozer.modules import common, Module

class Stats(Module, common.Shell):

	name = "Device Stats"
	description = "Gets Various stats from device."
	examples = "run custom.stats"
	author = "Aagam Shah (@neutrinoguy)"
	date = "2019-02-13"
	license = "BSD (3 clause)"
	path = ["custom"]

	def execute(self, arguments):
		self.stdout.write("[+]----Default Properties----[+]\n")
		self.stdout.write(self.readFile("/default.prop") + "\n")
		self.stdout.write("[+]----Disk Stats----[+]\n")
		self.stdout.write(self.readFile("/proc/diskstats") + "\n")
		self.stdout.write("[+]----Memory Info----[+]\n")
		self.stdout.write(self.readFile("/proc/meminfo") + "\n")
		self.stdout.write("[+]----Process Stats----[+]\n")
		self.stdout.write(self.readFile("/proc/stat") + "\n")
		self.stdout.write("[+]----CPU info----[+]\n")
		self.stdout.write(self.readFile("/proc/cpuinfo") + "\n")
		self.stdout.write("[+]----Device Uptime----[+]\n")
		self.stdout.write(self.readFile("/proc/uptime") + "\n")







