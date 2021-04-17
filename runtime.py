from datetime import datetime, timedelta
def runtime(filename):
	process ={}
	with open(filename) as file:
		file.readline()
		for line in file:		
			result = []
			time,date, pid, status = line.split()
			process_time = datetime.strptime(time+ ' '+date, '%H:%M:%S %m/%d/%Y')
			print(process_time, pid, status)
			if status == 'start':
				process[pid] =[status, process_time, timedelta(0)]			
			elif status == 'pause' and pid in process.keys():
				print(process)
				process[pid] =[status, process_time, process_time - process[pid][1]]
			elif status == 'resume' and pid in process.keys():
				print(process)
				process[pid][0],process[pid][1] =status,process_time
			elif status == 'exit' and pid in process.keys():
				time = process_time- process[pid][1] 
				process[pid] =[status, process_time,process[pid][2] +time]
				print(pid,str(process[pid][2]))
				#print(pid, datetime.fromtimestamp(process[pid][2]))	
runtime('pid.txt')