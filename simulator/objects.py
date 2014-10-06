class Process:

	id = None
	arrival_time = None
	length_time = None
	execution_time = None
	start_time = None
	end_time = None

	def __init__(self,id,arrival_time,length_time):
		self.id = id
		self.arrival_time = arrival_time
		self.length_time = length_time
		self.execution_time = 0

	def is_finished(self):
		return self.execution_time >= self.length_time

	def __repr__(self):
		"""
		returns the string representation of the object
		"""
		return "P"+str(self.id)+": turnaround time = "+str(self.end_time -  self.arrival_time) + " waiting time = "+ str(self.start_time - self.arrival_time)