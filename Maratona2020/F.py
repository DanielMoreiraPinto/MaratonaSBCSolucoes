s=input()

gl=0
pl=0
gr=0
pr=0
sacou='l'

for x in s:
    if pl>=5 and (pl-pr)>=2 or pl==10:
        sacou='l'
        gl=gl+1
        pl=0
        pr=0
    elif pr>=5 and (pr-pl)>=2 or pr==10:
        sacou='r'
        gr=gr+1
        pr=0
        pl=0
        
    if x=='S':
        if sacou=='l':
            pl=pl+1
        else:
            pr=pr+1
    elif x=='R':
        if sacou=='r':
            sacou='l'
        elif sacou=='l':
            sacou='r'

        if sacou=='r':
            pr=pr+1
        else:
            pl=pl+1
    elif x=='Q':
        if gl==2:
            print(str(gl)+' (winner)'+' - '+str(gr))
        elif gr==2:
            print(str(gl)+' - '+str(gr)+' (winner)')
        elif sacou=='l':
            print(str(gl)+' ('+str(pl)+'*)'+' - '+str(gr)+' ('+str(pr)+')')
        elif sacou=='r':
            print(str(gl)+' ('+str(pl)+')'+' - '+str(gr)+' ('+str(pr)+'*)')
    
