#
# PYTHON SCRIPT FOR GENERATION OF A setFieldsDict FOR TWO-PHASE SOLVERS
# WITH HOMOGENEOUS PLACEMENT OF N-SPHERES AND WITH SMALL RANDOM VARIATION 
# OF SPHERE RADIUS AND POSITION
#
# AUTHOR: SEBASTIAN, WEISS, TU BERGAKADEMIE FREIBERG
# VERSION: 0.1
#

import os.path
import random

#
# USER MODIFICATIONS
###########################################################
# COORDINATES OF DOMAIN ORIGIN
xcoord = 0.0
ycoord = 0.0
zcoord = 0.0

# DOMAIN SIZE
xlength = 0.1
ylength = 0.1
zlength = 0.001

# SPHERE RADIUS
R = 0.003

# PERCENT OF RADIUS FOR RANDOM VARIATION
PR = 0.2

# VARIATION IN SPHERE POSITION
PR2 = 0.05

# NUMBER OF SPHERES IN X AND Y
Nx = 5
Ny = 5

# ALPHA VALUE INSIDE AND OUTSIDE OF SPHERE
alphaIN = 0.51
alphaOUT = 0.49
###########################################################


# DISTANCE BETWEEN SPHERES
disx = (xlength)/(Nx)
disy = (ylength)/(Ny)
R2x = PR2 * disx
R2y = PR2 * disy
# RADIUS VARIATION
RR = PR*R

def killF():
    print "ERROR."
    return 1

# HEADER
#--------------------------------------------------------------------------------------------#

h1 = '/*--------------------------------*- C++ -*----------------------------------*\\'
h2 = '| =========                 |                                                 |'
h3 = '| \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |'
h4 = '|  \\\\    /   O peration     | Version:  2.2.0                                 |'
h5 = '|   \\\\  /    A nd           | Web:      www.OpenFOAM.org                      |'
h6 = '|    \\\\/     M anipulation  |                                                 |'
h7 = '\\*---------------------------------------------------------------------------*/'
h8 = 'FoamFile'
h9 = '{'
h10 = '    version     2.0;'
h11 = '    format      ascii;'
h12 = '    class       dictionary;'
h13 = '    location    "system";'
h14 = '    object      setFieldsDict;'
h15 = '}'
h16 = '// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //'
h17 = '// ************************************************************************* //'

#--------------------------------------------------------------------------------------------#

fName = './system/setFieldsDict'

if (os.path.exists(fName)):
    fobj = open(fName, 'w')
else:
    killF()

fobj.write('%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n' % (h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16))


# INITIAL POSITION
if (((xcoord + R) <= xlength) & ((ycoord + R) <= ylength)):
    xPos0 = xcoord + 0.5*disx
    yPos0 = ycoord + 0.5*disy

    # FOR TWO-DIMENSIONAL CASES
    zPos0 = zcoord + 0.5*zlength
else:
    killF()

# WRITE DEFAULT VALUES TO DICT
d1 = 'defaultFieldValues'
d2 = '('
d3 = '    volScalarFieldValue alpha1 ' + str(alphaOUT)
d4 = '    volVectorFieldValue U ( 0 0 0 )'
d5 = ');'


fobj.write('%s\n%s\n%s\n%s\n%s\n\n' % (d1,d2,d3,d4,d5))

c1 = 'regions'
c2 = '('
c3 = ');'

fobj.write('%s\n%s\n' % (c1,c2))

e1 = '    sphereToCell'
e2 = '    {'
e3 = '        fieldValues'
e4 = '        ('
e5 = '            volScalarFieldValue alpha1 ' + str(alphaIN)
e6 = '        );'
e7 = '    }'


#
# GENERATION OF SPHERES
#

xPos = xPos0

for XX in range(1,Nx+1):
    yPos = yPos0
    zPos = zPos0

    for YY in range(1,Ny+1):
        fobj.write('%s\n%s\n' % (e1,e2))
        fobj.write('        centre ( %f %f %f );\n' % (xPos,yPos,zPos))
        fobj.write('        radius %f;\n' % (R + random.uniform(-RR,RR)))
        fobj.write('%s\n%s\n%s\n%s\n%s\n\n' % (e3,e4,e5,e6,e7))

        yPos += disy + random.uniform(-R2y,R2y)
    xPos += disx + random.uniform(-R2x,R2x)


fobj.write('%s\n\n' % c3)
fobj.write('%s\n' % h17)
fobj.close()
