from simulator.objects import Process
import copy

class Algorith:

	_processes = []

	def __init__(self, processes):
		self._processes = processes

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

	def get_process(self, pc):
		earliest_unfinished_proc = None
		for process in self._processes:
			if process.arrival_time > pc: continue
			if process.is_finished(): continue
			if not earliest_unfinished_proc or earliest_unfinished_proc.arrival_time > process.arrival_time:
				earliest_unfinished_proc = process
 		return earliest_unfinished_proc


class SJF(Algorith):
	name = "SJF"

	def get_process(self, pc):
		pass


class RoundRobin(Algorith):
	name = "RoundRobin"


	def get_process(self, pc):
		pass