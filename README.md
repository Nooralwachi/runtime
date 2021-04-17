# runtime
Input: a file with the following content

timestamp	        PID	action

10:00:01 12/23/2020	1234	start

10:00:03 12/23/2020	5678	start

10:00:06 12/23/2020	4321	start

10:00:11 12/23/2020	1234	pause

10:00:21 12/23/2020	2212	start

10:00:25 12/23/2020	1234	resume

10:00:32 12/23/2020	5678	pause

10:00:51 12/23/2020	2212	exit

10:01:01 12/24/2020	1234	exit
 
Output: PIDs and and their run time
Note:
1) start -> exit marks the run time of a process

2) time paused (pause -> resume) is not counted into run time

3) disregard processes that never exit
