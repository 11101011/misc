#
# PYTHON SCRIPT FOR EXTRACTION OF DIAMETER VALUES FROM THE FOLDER "./postProcessing/regionSizeDistribution1"
# WRITING DIAMETER VALUES AND TIME TO OUTPUT FILE
#
# AUTHOR: SEBASTIAN WEISS, TU BERGAKADEMIE FREIBERG
# VERSION: 0.1
#

import os

def killF():
    print "ERROR. PATH DOESN'T EXISTS!"
    return 1

PATH='./postProcessing/regionSizeDistribution1/'
INPUT='diameter_count.csv'
OUTPUT='./diameter_otime.csv'
OUTOPEN=open(OUTPUT,'w')

DELIM=','
LIST=[]
DIAMETER=[]
TIME=[]
COLS=[]
C0=[]
C1=[]


# CHECK IF PATH EXISTS
if (os.path.exists(PATH)):

    for root,dirs,files in os.walk(PATH):

        filename=os.path.join(root,INPUT)
        LIST.append(filename)
        LIST.sort()

    # LOOP THROUGH THE FILES OF EACH FOLDER
    for i in range(len(LIST)-1):

        INOPEN=open(LIST[i], 'r')
        TI = LIST[i].replace(PATH, '')
        TIME.append(float(TI.replace('/' + INPUT, '')))

        COLS=[]
        C0=[]
        C1=[]

        # READ LINES OF EACH FILE
        for LINE in INOPEN.readlines():

            if not LINE.startswith('x', 0, len(LINE)):

                COLS=LINE.split(DELIM)
                C0.append(float(COLS[0]))
                C1.append(int(COLS[1]))

        VALUE=C0[C1.index(1)]
        DIAMETER.append(VALUE)

    # WRITE OUTPUT
    for r in range(len(LIST)-1):
        OUTOPEN.write('%d %f %f\n' % (r, TIME[r], DIAMETER[r]))

    OUTOPEN.close()
    INOPEN.close()

else:
    killF()
