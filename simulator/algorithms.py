from simulator.objects import Process
import copy

class Algorith:

	_processes = []
	_quantum = None

	def __init__(self, processes, **kwargs):
		sorted_by_arrival = sorted(processes, key=lambda x: x.arrival_time)
		self._processes = sorted_by_arrival
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
		for process in sorted(self._processes, key=lambda x: x.id):
			print process
		print "Avg turnaround time = " + str(self.get_avg_turnaround_time()) + " Avg waiting time = "+str(self.get_avg_waiting_time())


	def get_sched_order(self):
		res = ""
		sorted_by_start = sorted(self._processes, key=lambda x: x.start_time)
		for proc in sorted_by_start:
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

	_prev_job = None
	_proc_timer = 0

	def get_next_unfinished_job(self,pc):
		curr_job = self._prev_job
		if not curr_job:
			curr_job = self.get_earliest_unfinished_job(pc)
			return curr_job
		prev_job_index = self._processes.index(curr_job)
		i = (prev_job_index + 1) % len(self._processes)
		while i != prev_job_index:
			process = self._processes[i]
			i = (i + 1) % len(self._processes)
			if not process.is_finished() and process.arrival_time <= pc:
				return process
		return None
		

	def get_process(self, pc):
		if not (self._proc_timer % self._quantum) or self._prev_job.is_finished():
			next_job = self.get_next_unfinished_job(pc)
			if next_job:
				self._prev_job = next_job
				self._proc_timer = 0
		if self._prev_job:
			self._proc_timer += 1
 		return self._prev_job





