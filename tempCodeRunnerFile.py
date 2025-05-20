from subprocess import Popen, STDOUT, PIPE
p = Popen(['bc','-q','-i'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
print(p.stdout.readline().rstrip())