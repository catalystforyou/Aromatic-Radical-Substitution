from subprocess import call
from subprocess import run
from subprocess import Popen
import subprocess
import os
import pandas as pd

addtext = '%nprocshared=20 \n%mem=5GB \n#p opt b3lyp/6-311+g(2d,p) \n\n'
initialPath = 'D:\OneDrive - pku.edu.cn\Lai Group\Reaction Prediction\ChemSelML\Test\Data\gjf_Ar\\'


def log2gjf(importPath, exportPath):
    p = Popen('D:\chem_software\Multiwfn_3.7_dev_bin_Win64\Multiwfn.exe', stdout=subprocess.PIPE, stdin=subprocess.PIPE,
              shell=True)
    p.stdin.write(bytes(importPath, encoding='gbk'))
    p.stdin.write(b'\n')
    p.stdin.write(b'100\n')
    p.stdin.write(b'2\n')
    p.stdin.write(b'10\n')
    p.stdin.write(bytes(exportPath, encoding='gbk') + b'\n')
    p.stdin.close()
    out = p.stdout.read().decode("gbk")
    p.stdout.close()


def generate_gjf(logpath, gjfpath):
    with open(logpath, 'r') as f:
        content = f.readlines()
        title = content[108] + '\n'
    with open(gjfpath, 'r') as f:
        content = f.read()
        firstpost = content.find('  0  1')
        addUp = addtext + title
        content = addUp + content[firstpost:-2]+'\n'
    with open(gjfpath, 'w') as f:
        f.write(content)

def generate_loc():
    with open('Ar.smi') as f:
        content = f.readlines()
        smls = []
        names = []
        ylds = []
        for line in content:
            line = line.strip('\n')
            ls = [x for x in line.split(' ')]
            smls.append(ls[1])
            names.append(ls[0])
            ylds.append(ls[2:])
    dirs = []
    yld = []
    for name in names:
        dirs.append(name[0] + '\\' + name[1:] + '\\')
    for d in dirs:
        idx = dirs.index(d)
        locs = ylds[idx]
        loc = []
        for i in range(len(locs)):
            if i % 2 == 0:
                loc.append(locs[i])
        editfile=names[idx]+'-1sp.gjf'
        if os.path.exists(editfile):
            print(editfile)
            with open(editfile,'r') as f:
                content=f.readlines()
                print(loc)
                content[4]=content[4].strip('\n').strip(' ')+' '+" ".join(loc)+'\n'
                content[6]='0 1\n'
                for i in range(7,len(content)):
                    content[i]=' '+content[i]
            with open(editfile,'w') as f:
                f.write("".join(content))

'''
for l in ['A','C','E','G']:
    for i in range(1, 30):
        try:
            log2gjf(l + str(i) + '.log', l + str(i) + '-1sp.gjf')
            generate_gjf(l+str(i)+'.log',l+str(i)+'-1sp.gjf')
        except FileNotFoundError:
            pass'''

generate_loc()
