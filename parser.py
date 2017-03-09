from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, edges, transform, screen, color ):
    f = open (fname, "r")
    script = f.read()
    tmatrix = transform
    print script
    print "__________________"
    scr = script.split("\n")
    str = ""
    for i in range(len(scr)):
    	str += "["
    	str += scr[i]
    	str += "],"
    print str
    for i in range(len(scr)):
    	if scr[i] == "line":
    		n = scr[i+1].split(" ")
    		add_edge(edges,int(n[0]),int(n[1]),int(n[2]),int(n[3]),int(n[4]),int(n[5]))
		if scr[i] == "ident":
			ident(tmatrix)
		elif scr[i] == "scale":
			n = scr[i+1].split(" ")
			smatrix = make_scale(int(n[0]),int(n[1]),int(n[2]))
			matrix_mult(smatrix,tmatrix)
		elif scr[i] == "translate":
			n = scr[i+1].split(" ")
			tmat = make_translate(int(n[0]),int(n([1])),int(n[2]))
			matrix_mult(tmat,tmatrix)
        elif scr[i] == "rotate":
        	n = scr[i+1].split(" ")
        	if n[0] == "x":
        	    rx = make_rotX(int(n[1]))
        	    matrix_mult(rx, tmatrix)
        	elif n[0] == "y":
        	    ry = make_rotY(int(n[1]))
        	    matrix_mult(ry, tmatrix)
        	else:
        	    rz = make_rotZ(int(n[1]))
                matrix_mult(rz, tmatrix)
        elif scr[i] == "apply":
        	matrix_mult(tmatrix,edges)
        elif scr[i] == "display":
            draw_lines( edges, screen, color )
            display(screen)
        elif scr[i] == "save":
        	fname = scr[i+1]
        	draw_lines(edges, screen, color)
        	save_extension(screen, fname)
        elif scr[i] == "quit":
        	f.close()
        	exit
