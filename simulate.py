	#!/usr/bin/env python
from cli.app import CommandLineApp
from simulator.engine import Engine, ALGORITHMS

class CPUScheduleSimluatorApp(CommandLineApp):

	name = "simulator"

	def setup(self):
		super(CPUScheduleSimluatorApp,self).setup()
		self.add_param("-f", "--file", help="Define the input file to run the simulator against. Default is `input.txt`.", 
			default="input.txt", action="store_true")
		self.add_param("-q", "--quantum", help="Round Robin allows for an optional quantum parameter. Default is "+str(Engine._time_quantum)+" cycles.", 
			default=str(Engine._time_quantum), action="store_true")
		self.add_param("algorithm", help="The algorithm to use when running the simulated CPU scheduler. Choices are: "+str(ALGORITHMS.keys()), 
			default=False)
		
	# This is called after run() completes setup()
	def main(self):
		Engine(filename=self.params.file, algorithm=self.params.algorithm, quantum=self.params.quantum).run()


if __name__ == "__main__":
	CPUScheduleSimluatorApp().run()

