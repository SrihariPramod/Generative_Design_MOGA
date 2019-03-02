from src import job

jobDescription = {
	"jobName": "park1",
	"inputsDef": [
		{ "name": "r1", "type": "categorical", "num": 600},
		{ "name": "r2", "type": "categorical", "num": 600},
		{ "name": "r3", "type": "categorical", "num": 600},
		{ "name": "r4", "type": "categorical", "num": 600},
		{ "name": "p1", "type": "categorical", "num": 50},
		{ "name": "p2", "type": "categorical", "num": 50},
		{ "name": "p3", "type": "categorical", "num": 50},
		{ "name": "p4", "type": "categorical", "num": 50},
		{ "name": "px1", "type": "categorical", "num": 12},
		{ "name": "py1", "type": "categorical", "num": 12},
		{ "name": "px2", "type": "categorical", "num": 12},
		{ "name": "py2", "type": "categorical", "num": 12},
		{ "name": "px3", "type": "categorical", "num": 12},
		{ "name": "py3", "type": "categorical", "num": 12},
		{ "name": "px4", "type": "categorical", "num": 12},
		{ "name": "py4", "type": "categorical", "num": 12},
		
		],
	"outputsDef": [
		{ "name": "Parkarea", "type": "objective", "goal": "max"},
		{ "name": "Park Center", "type": "objective", "goal": "max"},
		{ "name": "Roadarea", "type": "objective", "goal": "max"},
		{ "name": "Intersection", "type": "objective", "goal": "max"},
		],
	"algo": "GA",
	"algoOptions": {
		"numGenerations": 40,
		"numPopulation": 20,
		"mutationRate": 0.05,
		"saveElites": 2,
		"DOE": "random",
		# "DOE": ["_job name_", -1],
		},
	"jobOptions": {
		"screenshots": True
		}
	}

# job.createInputFile(jobDescription)
job.run(jobDescription)