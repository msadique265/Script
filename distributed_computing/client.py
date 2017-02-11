from distributor.tasks import add
import time

task_ids = []
for i in range(20):
	print('Running : %d'%i)
	id = add.delay(5, i)
	task_ids.append(id)

for i in range(len(task_ids)):
	while not (task_ids[i].state == 'SUCCESS'):
		continue
	print(str(i) + ' : ' + str(task_ids[i].get()))