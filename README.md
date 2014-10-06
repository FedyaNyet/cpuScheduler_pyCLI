cpuScheduler_pyCLI
===============

This is a simple CLI based app that simulates scheduling of CPU processes using different algorithms. 

Most basic installations of python include `pip`, which is to be used for installing this project's dependencies. To install the packages, run `$ pip install -r requirements.txt` from the project's source folder. It is suggested that you also use [virtualenv](http://virtualenv.readthedocs.org/en/latest/) in conjunction with this project so as to not clutter your machine with this project's dependent packages.


HOW TO PLAY
===========

To run get started, change into the folder containing this file and run `$ Python simulate.py --help`. This will explain to you the inputs available to run the simulator. 

The simulator runs by using the `input.txt` file to use as the CPU process schedule blueprint. The first line defines the number of processes, and each following line is the corresponding processes' start time and execution time. the optional `--file` param allows you to provide a new file as an input to the simluator.

AUTHORS
============
Fyodor Wolf