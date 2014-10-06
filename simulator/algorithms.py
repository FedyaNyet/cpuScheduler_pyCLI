from simulator.objects import Process
import copy

class Algorith:

	_processes = []
	_quantum = None

	def __init__(self, processes, **kwargs):
		self._processes = processes
		if 'quantum' in kwargs:
			self._quantum = kwargs['quantum']

	def is_finished(self):
		for process in self._processes:
			if not process.is_finished():
				return False
		return True

	def print_results(self):
		print "The schedule order using "+self.name+" is:"
		print self.get_sched_order()
		for process in self._processes:
			print process
		print "Avg turnaround time = " + str(self.get_avg_turnaround_time()) + " Avg waiting time = "+str(self.get_avg_waiting_time())


	def get_sched_order(self):
		res = ""
		sorted_proc = sorted(self._processes, key=lambda x: x.start_time)
		for proc in sorted_proc:
			res +="P"+str(proc.id)+"("+str(proc.start_time)+"-"+str(proc.end_time)+"), "
		return res

	def get_avg_turnaround_time(self):
		total = 0.0
		for proc in self._processes:
			total += (proc.end_time -  proc.arrival_time)
		return total / len(self._processes)

	def get_avg_waiting_time(self):
		total = 0.0
		for proc in self._processes:
			total += (proc.start_time - proc.arrival_time)
		return total / len(self._processes)


class FIFO(Algorith):
	name = "FIFO"

	def get_earliest_unfinished_job(self, pc):
		earliest_unfinished_proc = None
		for process in self._processes:
			if process.arrival_time > pc: continue
			if process.is_finished(): continue
			if not earliest_unfinished_proc or earliest_unfinished_proc.arrival_time > process.arrival_time:
				earliest_unfinished_proc = process
 		return earliest_unfinished_proc

	def get_process(self, pc, **kwargs):
		return self.get_earliest_unfinished_job(pc)


class SJF(FIFO):
	name = "SJF"

	prev_job = None

 	def get_shortest_unifished_job(self,pc):
		shortest_unfinished_proc = None
		for process in self._processes:
			if process.arrival_time > pc: continue
			if process.is_finished(): continue
			if not shortest_unfinished_proc or shortest_unfinished_proc.length_time > process.length_time:
				shortest_unfinished_proc = process
 		return shortest_unfinished_proc

	def get_process(self, pc, **kwargs):
		earliest_unfinished_job = self.get_earliest_unfinished_job(pc)
		if not self.prev_job or self.prev_job is earliest_unfinished_job:
			self.prev_job = earliest_unfinished_job
		else:
			self.prev_job = self.get_shortest_unifished_job(pc)
 		return self.prev_job



class RoundRobin(FIFO):
	name = "RoundRobin"

	prev_job = None
	proc_timer = 0

	def get_next_job(self,pc):
		earliest_unfinished_proc = None
		for process in self._processes:
			if process.arrival_time > pc: continue
			if process.is_finished(): continue
			if (not earliest_unfinished_proc or earliest_unfinished_proc.arrival_time > process.arrival_time) and process is not self.prev_job:
				earliest_unfinished_proc = process
 		return earliest_unfinished_proc

	def get_process(self, pc):
		if not self.prev_job:
			self.prev_job = self.get_earliest_unfinished_job(pc)
			self.proc_timer += 1
		elif self.proc_timer % self._quantum:
			next_job = self.get_next_job(pc)
			if next_job:
				self.prev_job = next_job
				self.proc_timer = 0
				return next_job
		self.proc_timer += 1
 		return self.prev_job





