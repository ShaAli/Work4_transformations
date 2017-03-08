import math

def make_translate( x, y, z ):
    tmatrix = new_matrix()
    ident(tmatrix)
    tmatrix[3] = [x,y,z,1]
    return tmatrix

def make_scale( x, y, z ):
    smatrix = new_matrix()
    ident(smatrix)
    smatrix[0][0] = x
    smatrix[1][1] = y
    smatrix[2][2] = x

def make_rotX( theta ):    
    rmatrix = new_matrix()
    ident(rmatrix)
    rmatrix[1] = [0,(math.cos(theta)),(math.sin(theta)),0]
    rmatrix[2] = [0,(-math.sin(theta)),(math.cos(theta)),0]

def make_rotY( theta ):
    rmatrix = new_matrix()
    ident(rmatrix)
    rmatrix[0] = [(math.cos(theta)),0,(-math.sin(theta)),0]
    rmatrix[2] = [(math.sin(theta)),0,(math.cos(theta)),0]

def make_rotZ( theta ):
    rmatrix = new_matrix()
    ident(rmatrix)
    rmatrix[0] = [(math.cos(theta)), (math.sin(theta)),0,0]
    rmatrix[1] = [(-math.sin(theta)), (math.cos(theta)),0,0] 

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

def scalar_mult( matrix, s ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r]*= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
