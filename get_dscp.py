import numpy as np
import pandas as pd


def read_CDFT(path):
    with open(path + '\\CDFT.txt') as f:
        mesg = []
        labelPost = []
        dscpPost = []
        dscp = []
        content = f.readlines()
        for line in content:
            idx = content.index(line)
            line = line.strip('\n')
            ls = [x for x in line.split(' ') if (x != '' and x != ')')]
            # print(ls)
            if len(ls) != 0 and ls[0] == 'Atom':
                labelPost.append(idx)
            if len(ls) != 0 and ls[0][0].isdigit():
                dscpPost.append(idx)
            mesg.append(ls)
    labels = mesg[labelPost[0]] + mesg[labelPost[1]][1:] + mesg[labelPost[2]][1:]
    num_atoms = len(dscpPost) // 3
    if len(dscpPost) / 3 != num_atoms:
        raise SystemError
    for i in range(num_atoms):
        dscp.append(mesg[dscpPost[i]] + mesg[dscpPost[i + num_atoms]][1:] + mesg[dscpPost[i + 2 * num_atoms]][1:])
    #print(len(dscp[0]), len(labels))
    df = pd.DataFrame(dscp, columns=labels)
    #print(df)
    df.to_csv(path + '\\dscp.csv', index=False)
    return labels


def merge_table():
    mergeTable = pd.DataFrame()
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
        try:
            df = pd.read_csv(d + 'dscp.csv',index_col=False)
            loc = []
            for i in range(len(locs)):
                if i % 2 == 0:
                    loc.append(locs[i])
                else:
                    yld.append(locs[i])
            for l in loc:
                #print(df.loc[int(l) - 1])
                mergeTable = mergeTable.append(df.loc[int(l) - 1])
        except FileNotFoundError:
            print(d)
    print(mergeTable)
    print(len(yld))
    mergeTable['yield']=yld
    #print(mergeTable)
    mergeTable.to_csv('merge_table.csv',index=False)
    #print(d, loc, yld)
    #print(smls, names, ylds)


for l in ['A','C','E','G']:
    for i in range(1, 30):
        try:
            read_CDFT(l+'\\' + str(i))
        except FileNotFoundError:
            pass

merge_table()
