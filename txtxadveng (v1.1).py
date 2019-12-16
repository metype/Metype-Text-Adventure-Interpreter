import re
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
ask_name=False
char_wrap=42
debug=False
vars = []
vals = []
code = []
fle = filedialog.askopenfilename()
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def form2(str):
    ret = ''
    colons = find(str,':')
    commas = find(str,',')
    if(len(colons)==0):
        ret=str[1:int(len(str))]
    else:
        for i in range(len(colons)):
         try:
            if(len(ret)>0):
                ret+=':'+(str[colons[i]+1:commas[i]])
            else:
                ret+=(str[colons[i]+1:commas[i]])
         except IndexError:
            if(len(ret)>0):
                ret+=':'+(str[colons[i]+1:len(str)])
            else:
                ret+=(str[colons[i]+1:len(str)])
            
    return ret

def form3(str):
    ret = ''
    colons = find(str,':')
    commas = find(str,',')
    for i in range(len(colons)):
        if(i>0):
            ret+=str[commas[i-1]:colons[i]]
        else:
            ret+=str[1:colons[i]]
            
    return ret

def init(file):
    lines=file.readlines()
    vars=[]
    vals=[]
    for x in lines:
        if(x.startswith('$')):
            vars.append(x.split('>')[1].split('=')[0])
            if(x.split('<')[1].split(">")[0]=='int'):
                try:
                    vals.append(int(x.split('=')[1].split('\n')[0]))
                except ValueError:
                    try:
                        vals.append(int(x.split('= ')[1].split('\n')[0]))
                    except ValueError:
                        print(f"It seems you have made an int variable but do not have an int opposite the equalss sign, line : {lines.index(x)}")
                except:
                    print(f"There was an eror parsing the variable on line : {lines.index(x)}")
            if(x.split('<')[1].split(">")[0]=='str'):
                vals.append(str(x.split('=')[1].split('\n')[0]))
    return [vars,vals]

def validlines(file):
    lines=file.readlines()
    ids=list(range(len(lines)))
    lns=list(range(len(lines)))
    toids=list(range(len(lines)))
    optns=list(range(len(lines)))
    line=list(range(len(lines)))
    ends=list(range(len(lines)))
    j=0
    y=0
    char_wrap=42
    ask_name=False
    debug_name=''
    code=[]
    codelines=[]
    firsttrue='Null'
    for x in lines:
        if(x.startswith('#')):
            if(x.split('=')[0].split('#')[1]=='char_wrap'):
                char_wrap=int(x.split('=')[1].split('\n')[0])
            if(x.split('=')[0].split('#')[1]=='ask_name'):
                ask_name=bool(x.split('=')[1].split('\n')[0])
            if(x.split('=')[0].split('#')[1]=='debug_name'):
                debug_name=str(x.split('=')[1].split('\n')[0])
        y+=1
        if(x.startswith('[')):
            if(firsttrue=='Null'):
                firsttrue=lines.index(x)
            if(x.split(':')[1].startswith('#')):
                i=1
                while(x[i]!=':'):
                    i+=1
                if not(i==0) or not(i==len(x)):
                    j+=1
                    num=''
                    for p in range(1,i):
                        num+=x[p]
                    ids[j-1]=num
                    lns[j-1]=str(y)
                i=1
                while(x[i]!='('):
                    i+=1
                    if(i>len(x)-1):
                        break
                if not(i==0) or not(i==len(x)):
                    num=''
                    for p in range(i,len(x.split(")")[0])):
                        num+=x[p]
                    codelines.append(str(num).split("(")[1])
                code.append(ids[j-1]+':'+x.split('#')[1].split(']')[0])
            else:
             i=1
             while(x[i]!=':'):
                i+=1
             if not(i==0) or not(i==len(x)):
                j+=1
                num=''
                for p in range(1,i):
                    num+=x[p]
                ids[j-1]=num
                lns[j-1]=str(y)
             kl=i
             i=1
             while(x[i]!=']'):
                i+=1
             if not(i==0) or not(i==len(x)):
                num=''
                for p in range(kl+1,i):
                    num+=x[p]
                line[j-1]=num
             i=1
             while(x[i]!='('):
                i+=1
                if(i>len(x)-1):
                    break
             if not(i==0) or not(i==len(x)):
                num=''
                for p in range(i,len(x.split(")")[0])):
                    num+=x[p]
                toids[j-1]=form2(num)
                optns[j-1]=form3(num)
        if(x.startswith('{')):
            i=1
            while(x[i]!=':'):
                i+=1
            if not(i==0) or not(i==len(x)):
                j+=1
                num=''
                for p in range(1,i):
                    num+=x[p]
                ids[j-1]=num
                ends[j-1]=num
                lns[j-1]=str(y)
            kl=i
            i=1
            while(x[i]!='}'):
                i+=1
            if not(i==0) or not(i==len(x)):
                num=''
                for p in range(kl+1,i):
                    num+=x[p]
                line[j-1]=num
    return [ids,lns,toids,optns,line,ends,char_wrap,ask_name,debug_name,code,codelines,lines,firsttrue]
def form(stryline):
    line = stryline.split(':')[1].split(']')[0]
    return line
def prt(string,vars,vals):
    if(ask_name):
        strng=(('\n'.join(fourtyseven.strip() for fourtyseven in re.findall(r'.{1,'+str(char_wrap)+'}(?:\s+|$)',string))).replace("%name%",name))
        for x in vars:
            strng=strng.replace('%'+x+'%',str(vals[vars.index(x)]))
        print(strng)
    else: 
        strng=('\n'.join(fourtyseven.strip() for fourtyseven in re.findall(r'.{1,'+str(char_wrap)+'}(?:\s+|$)',string)))
        for x in vars:
            strng=strng.replace('%'+x+'%',str(vals[vars.index(x)]))
        print(strng)
game=open(fle,'r')
valid = validlines(game)
code       =  valid[9]
codelines  =  valid[10]
char_wrap  =  valid[6]
ask_name   =  valid[7]
debug_name =  valid[8]
stry=0
game=open(fle,'r')
stuff=(init(game))
vars=stuff[0]
vals=stuff[1] 
oldstry=0

def parse(code,vars,vals,stry):
    funcs = ['redir','prt']
    stry=stry
    redir=False
    end=False
    for i in code:
        for m in vars:
            if i.startswith(m):
                if(type(vals[vars.index(m)])==int):
                #  print('int')
                 if(i.endswith('++')):
                    vals[vars.index(m)]+=1
                 elif(i.split(m)[1].startswith('+=')):
                    vals[vars.index(m)]+=int(i.split('+=')[1])
                 elif(i.split(m)[1].startswith('-=')):
                    vals[vars.index(m)]-=int(i.split('-=')[1])
                 elif(i.split(m)[1].startswith('/=')):
                    vals[vars.index(m)]/=int(i.split('/=')[1])
                 elif(i.split(m)[1].startswith('*=')):
                    vals[vars.index(m)]*=int(i.split('*=')[1])
                 elif(i.split(m)[1].startswith('%=')):
                    vals[vars.index(m)]%=int(i.split('%=')[1])
                 elif(i.split(m)[1].startswith('=') and not (i.split(m)[1].startswith('=='))):
                    vals[vars.index(m)]=int(i.split('=')[1])
                 elif(i.split(m)[1].startswith('==')):
                    if (vals[vars.index(m)]==int(i.split('==')[1].split('>')[0])):
                        w = parse(i.split(">")[1].split(';'),vars,vals,stry)
                        vars=w[0]
                        vals=w[1]
                        stry=w[2]
                    else:
                        if(len(i.split('<'))>1):
                            w=parse(i.split("<")[1].split(';'),vars,vals,stry)
                            vars=w[0]
                            vals=w[1]
                            stry=w[2]
                 elif(i.split(m)[1].startswith('>=')):
                    if (vals[vars.index(m)]>=int(i.split('>=')[1].split('>')[0])):
                        w=[0,0,0]
                        if not(i.split(m)[1].startswith('>'+i.split(">")[1])):
                            w = parse(i.split(">=")[1].split(';'),vars,vals,stry)
                        else:
                            w = parse(i.split(">=")[2].split(';'),vars,vals,stry)
                        vars=w[0]
                        vals=w[1]
                        stry=w[2]
                    else:
                        if(len(i.split('<'))>1):
                            w=parse(i.split("<")[1].split(';'),vars,vals,stry)
                            vars=w[0]
                            vals=w[1]
                            stry=w[2]
                 elif(i.split(m)[1].startswith('<=')):
                    if (vals[vars.index(m)]<=int(i.split('<=')[1].split('>')[0])):
                        w = parse(i.split(">")[1].split(';'),vars,vals,stry)
                        vars=w[0]
                        vals=w[1]
                        stry=w[2]
                    else:
                        if(len(i.split('<'))>2):
                            w=parse(i.split("<")[2].split(';'),vars,vals,stry)
                            vars=w[0]
                            vals=w[1]
                            stry=w[2]
                 elif(i.split(m)[1].startswith('<')):
                    if (vals[vars.index(m)]<int(i.split('<')[1].split('>')[0])):
                        w = parse(i.split(">")[1].split(';'),vars,vals,stry)
                        vars=w[0]
                        vals=w[1]
                        stry=w[2]
                    else:
                        if(len(i.split('<'))>2):
                            w=parse(i.split("<")[2].split(';'),vars,vals,stry)
                            vars=w[0]
                            vals=w[1]
                            stry=w[2]
                 elif(i.split(m)[1].startswith('>')):
                    if (vals[vars.index(m)]>int(i.split('>')[1].split('>')[0])):
                        w=[0,0,0]
                        if not(i.split(m)[1].startswith('>'+i.split(">")[1])):
                            w = parse([i.split(">")[1].split('<')[0]],vars,vals,stry)
                        else:
                            w = parse([i.split(">")[2].split('<')[0]],vars,vals,stry)
                        vars=w[0]
                        vals=w[1]
                        stry=w[2]
                    else:
                        if(len(i.split('<'))>1):
                            w=parse(i.split("<")[1].split(';'),vars,vals,stry)
                            vars=w[0]
                            vals=w[1]
                            stry=w[2]
                elif(type(vals[vars.index(m)])==str):
                    if(i.split(m)[1].startswith('+=')):
                        vals[vars.index(m)]=vals[vars.index(m)]+(str(i.split('+=')[1]))
                    elif(i.split(m)[1].startswith('=')):
                        vals[vars.index(m)]=str(i.split('=')[1])
                elif(type(vals[vars.index(m)])==bool):
                    if(i.split(m)[1].startswith('=')):
                        vals[vars.index(m)]=bool(i.split('=')[1])
                    print(vals[vars.index(m)],bool(i.split('==')[1].split('>')[0]))
                    if (vals[vars.index(m)]==bool(i.split('==')[1].split('>')[0])):
                        w = parse(i.split(">")[1].split(';'),vars,vals,stry)
                        vars=w[0]
                        vals=w[1]
                        stry=w[2]
                    else:
                        if(len(i.split('<'))>1):
                            w=parse(i.split("<")[1].split(';'),vars,vals,stry)
                            vars=w[0]
                            vals=w[1]
                            stry=w[2]
        for q in funcs:
            if i.startswith(q):
                if(i.split('{')[0])=='redir':
                    stry=int(i.split('{')[1].split('}')[0])
                    redir=True
                    break
                elif(i.split('{')[0])=='prt':
                    stringh=(i.split('{')[1].split('}')[0]).split('^')
                    for we in stringh:
                        prt(we,vars,vals)
    return [vars,vals,stry,redir]
def ask(stry):
    oldstry=stry
    inp=input("")
    correct = False
    game=open(fle,'r')
    valid = validlines(game)
    if(len(str(valid[3][valid[0].index(str(stry))]).split(','))==1):
        stry=int(valid[2][valid[0].index(str(stry))])
        correct=True
    else:
     for x in valid[3][valid[0].index(str(stry))].split(','):
        if(inp==str(valid[3][valid[0].index(str(stry))].split(",").index(x)+1)):
            correct=True
            stry=valid[2][valid[0].index(str(stry))].split(':')[int(valid[3][valid[0].index(str(stry))].split(",").index(x)+1)-1]
            break
    if not correct:
        print("That was not an option.")
        teb = ask(stry)
        stry=teb[0]
        oldstry=teb[1]
    game=open(fle,'r')
    valid = validlines(game)
    code=valid[9]
    return [stry,oldstry]

while(True):
    if not('0' in valid[0]):
        print("There is no story ID 0, so the program cannot run.")
        input("Press Enter key to exit.")
        exit()
    if not (str(stry) in valid[0]):
        print(f"Invalid story ID for option or redirect on line : {valid[1][valid[0].index(str(oldstry))]} ({valid[11][valid[0].index(str(oldstry))]}), \ntried to redirect to ID : {stry}, which doesn't exist.")
        input("Press Enter key to exit.")
        exit()
    game=open(fle,'r')
    vars=stuff[0]
    vals=stuff[1] 
    cde=False
    mhm=0
    for i in code:
        if(i.startswith(str(stry))):
            cde=True
            mhm=code.index(i)
    if not cde:
     if(ask_name and stry==0):
        name = input("Before we begin, what's your name? ")
        if(name==debug_name):
            debug=True
     game=open(fle,'r')
     valid = validlines(game)
     code=valid[9]
     game=open(fle,'r')
     p=valid[0].index(str(stry))
     hmm = str(valid[4][p]).split(';')
     for x in range(0,char_wrap):
        print('_',end='')
     print('\n')
     for x in hmm:
        prt(x,vars,vals)
     for x in valid[5]:
        if(x==str(stry)):
            input("Press Enter key to exit.")
            exit()
     game=open(fle,'r')
     valid = validlines(game)
     game=open(fle,'r')
     if (stry == 0):
        input('')
        stry=1
     elif not(len(str(valid[2][valid[0].index(str(stry))]).split(':'))==1):
        for x in valid[3][valid[0].index(str(stry))].split(','):#valid[0].index(str(stry))].split(","):
            print(x+f'({int(valid[3][valid[0].index(str(stry))].split(",").index(x))+1})')
        game=open(fle,'r')
        valid = validlines(game)
        game=open(fle,'r')
        teb = ask(stry)
        stry=teb[0]
        oldstry=teb[1]
     else:
        game=open(fle,'r')
        valid = validlines(game)
        game=open(fle,'r')
        teb = ask(stry)
        stry=teb[0]
        oldstry=teb[1]
    else:
        k=stry
        oh = parse(code[mhm].split(":")[1].split(';'),vars,vals,stry)
        if(stry==0):
            input("")
            stry=1
        else:
            if(oh[2]!=k) or oh[3]:
                stry=oh[2]
            else:
                input("")
                stry=int(codelines[mhm])
