import subprocess
import datetime
import os

print "------------------------------------------------------------------"
print "=================================================================="
print "                       EXEMPLO EM PYTHON                          "
print "=================================================================="
print "------------------------------------------------------------------"

currentDateTime = datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y %H:%M:%S')
print "\nData e hora local: " + currentDateTime + "\n\n"

print ">> Lendo arquivo info.txt ..."
f = open("info.txt",'r')
content = f.read()
print ">> Conteudo lido: \n\n"
print content + "\n\n"
f.close()

print ">> Obtendo informacoes sobre o versionamento do arquivo ...\n\n"
print ">>" os.getcwd()
#fileInfo = subprocess.Popen(["\Cursos", "dir"])
#fileInfo = subprocess.Popen(["ls", "-l", "/dev/null"])
#fileInfo = subprocess.check_output("svn info \"" + os.getcwd() + "\info.txt\"")
#fileInfo = subprocess.check_output("svn info \"" , "\info.txt\"")
#fileInfo = subprocess.check_call(["ls", "-l"])
print fileInfo + "\n"

p = open("C:\checkInfo\password.txt",'r')
password = p.read()
p.close() 

print ">> Log do SVN:\n\n"
logSVN = subprocess.check_output("svn log \"" + os.getcwd() + "\info.txt\" --username brunocaeo --password " + password)
print logSVN + "\n\n"