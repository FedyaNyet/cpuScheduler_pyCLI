from simulator.algorithms import *
from simulator.objects import Process

ALGORITHMS = {"FIFO":FIFO, "RR":RoundRobin, "SJF":SJF}

class Engine:

	_scheduler = None
	_process_count = 0
	_program_counter = 0

	def __init__(self, filename, algorithm):
		alg_key = str(algorithm).upper()
		if alg_key not in ALGORITHMS:
			print "Please provide a valid algorithm"
			return

		processes = self.parse_processes(filename)
		alg = ALGORITHMS[alg_key]
		self._scheduler = alg(processes)

	def parse_processes(self, filename):
		processes = []
		f = open(filename, 'r')
		for line_num, line in enumerate(f):
			if not self._process_count:
				self._process_count = int(line.strip())
				continue
			process_desc = line.strip().replace('\t',' ').split(' ')
			
			processes.append(Process(id=line_num,arrival_time=int(process_desc[0]),length_time=int(process_desc[1])))
		return processes

	def run(self):
		if not self._scheduler: return
		while not self._scheduler.is_finished():
			#get the process for the current PC
			next_proc = self._scheduler.get_process(self._program_counter)
			if not next_proc:
				#no processes yet
				self._program_counter += 1
				continue
			if not next_proc.start_time:
				next_proc.start_time = self._program_counter
			#increment PC
			next_proc.execution_time+=1
			self._program_counter += 1
			#update process if it finishes...
			if next_proc.is_finished():
				next_proc.end_time = self._program_counter

			
		self._scheduler.print_results()
