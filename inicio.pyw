import subprocess
from Janela import Janela
process = subprocess.Popen(["apt", "search", 'nvidia'], stdout=subprocess.PIPE)
output = ""
line = "****************"
while line != '':
    line = process.stdout.readline()
    line = str(line)
    line = line.replace("b'", '')
    line = line.replace("\\n'", '')
    line = line.replace('b"', '')
    line = line.replace('\\n"', '')
    line.strip()
    print(line)
    print(line == "'")
    if line != "'":
        output = output + "{}\n".format(line)
    else:
        line = ""
Janela.create('Janela de testes')
Janela.addLabel(output)
Janela.draw()
# print("echo {}".format(output))