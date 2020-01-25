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
fileInfo = subprocess.check_output("git log " + "info.txt")
#fileInfo = subprocess.check_output("git show \"" + os.getcwd() + "\info.txt\"")
#shell=True
#p = Popen(['grep', pattern, filename], stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=-1)
#fileInfo = subprocess.Popen(["\Cursos", "dir"])
#fileInfo = subprocess.Popen(["ls", "-l", "/dev/null"])
#fileInfo = subprocess.check_output("svn info \"" + os.getcwd() + "\info.txt\"")
#fileInfo = subprocess.check_output("svn info \"" , "\info.txt\"")
#fileInfo = subprocess.check_call(["ls", "-l"])
print ">>>>>>>>> Informacoes do commit realizado no arquivo info.txt <<<<<<<<<< \n" + fileInfo + "\n"

p = open("C:\Program Files (x86)\Jenkins\workspace\check info\password.txt",'r')
password = p.read()
p.close() 

print ">> Log do Git:\n\n"
logGIT = subprocess.check_output("git log " + " --author=joaopgioio@gmail.com ")
print logGIT + "\n\n"