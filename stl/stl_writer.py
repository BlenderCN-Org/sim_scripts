
#!/usr/bin/env python
#coding:utf-8
# Purpose: Export 3D objects, build of faces with 3 or 4 vertices, as ASCII or Binary STL file.
# License: MIT License

import struct

ASCII_FACET = """facet normal 0 0 0
outer loop
vertex {face[0][0]:.4f} {face[0][1]:.4f} {face[0][2]:.4f}
vertex {face[1][0]:.4f} {face[1][1]:.4f} {face[1][2]:.4f}
vertex {face[2][0]:.4f} {face[2][1]:.4f} {face[2][2]:.4f}
endloop
endfacet
"""

BINARY_HEADER ="80sI"
BINARY_FACET = "12fH"

class ASCII_STL_Writer:
    """ Export 3D objects build of 3 or 4 vertices as ASCII STL file.
    """
    def __init__(self, stream):
        self.fp = stream
        self._write_header()

    def _write_header(self):
        self.fp.write("solid python\n")

    def close(self):
        self.fp.write("endsolid python\n")

    def _write(self, face):
        self.fp.write(ASCII_FACET.format(face=face))

    def _split(self, face):
        p1, p2, p3, p4 = face
        return (p1, p2, p3), (p3, p4, p1)

    def add_face(self, face):
        """ Add one face with 3 or 4 vertices. """
        if len(face) == 4:
            face1, face2 = self._split(face)
            self._write(face1)
            self._write(face2)
        elif len(face) == 3:
            self._write(face)
        else:
            raise ValueError('only 3 or 4 vertices for each face')

    def add_faces(self, faces):
        """ Add many faces. """
        for face in faces:
            self.add_face(face)

class Binary_STL_Writer(ASCII_STL_Writer):
    """ Export 3D objects build of 3 or 4 vertices as binary STL file.
    """
    def __init__(self, stream):
        self.counter = 0
        ASCII_STL_Writer.__init__(self,stream)
        #super(Binary_STL_Writer, self).__init__(stream)
	#super(self.__class__, self).__init__(stream)

    def close(self):
        self._write_header()

    def _write_header(self):
        self.fp.seek(0)
        self.fp.write(struct.pack(BINARY_HEADER, b'Python Binary STL Writer', self.counter))

    def _write(self, face):
        self.counter += 1
        data = [
            0., 0., 0.,
            face[0][0], face[0][1], face[0][2],
            face[1][0], face[1][1], face[1][2],
            face[2][0], face[2][1], face[2][2],
            0
        ]
        self.fp.write(struct.pack(BINARY_FACET, *data))


def example():
    
    # cube corner points
    s = 3.
    p1 = (0, 0, 0)
    p2 = (0, 0, s)
    p3 = (0, s, 0)
    p4 = (0, s, s)
    p5 = (s, 0, 0)
    p6 = (s, 0, s)
    p7 = (s, s, 0)
    p8 = (s, s, s)
    
    # define the 6 cube faces
    # faces just lists of 3 or 4 vertices
    return [
        [p1, p5, p7, p3],
        [p1, p5, p6, p2],
        [p5, p7, p8, p6],
        [p7, p8, p4, p3],
        [p1, p3, p4, p2],
        [p2, p6, p8, p4],
    ]

    with open('cube.stl', 'wb') as fp:
        writer = Binary_STL_Writer(fp)
        writer.add_faces(get_cube())
        writer.close()


import Image

def read_image(filename, dimensions ,offset=(0.,0.,0.)):
    im = Image.open(filename)
    sx,sy = im.size
    max = 0
    min = 255
    shift_x = -1 * (dimensions[0] / 2) + offset[0]
    shift_y = -1 * (dimensions[1] / 2) + offset[1]
    shift_z = offset[2]
    height_fac = 1. / 255.
    x_fac = 1. / sx
    y_fac = 1. / sy
    points = list()
    for dx in range(sx):
        c_points = list()
        for dy in range(sy):
            dz  = im.getpixel((dx,dy))
            cx = dx * x_fac * dimensions[0] + shift_y
            cy = dy * y_fac * dimensions[1] + shift_y
            cz = dz * height_fac *dimensions[2] + shift_z
            c_points.append(list((cx,cy,cz)))
            #if size > max:
            #    max = size
            #if size < min:
            #    min = size
        points.append(c_points)
        
    faces = list()
    for dx in range(sx-1):
        for dy in range(sy-1):
            faces.append(list((
                points[dx][dy],
                points[dx][dy+1],
                points[dx+1][dy]
            )))
            faces.append(list((
                points[dx][dy+1],
                points[dx+1][dy+1],
                points[dx+1][dy]
            )))
            
    print(max)
    print(min)
    with open('map.stl', 'wb') as fp:
        writer = Binary_STL_Writer(fp)
        writer.add_faces(faces)
        writer.close()
#    return faces


    
if __name__ == '__main__':
    example()
