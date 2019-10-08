# http://www.pygame.org/wiki/OBJFileLoader
from OpenGL.GL import *  # @UnusedWildImport
import numpy as np
from OpenGL.GLU import *

OBJ_FOLDER = 'objects/'


def draw_axis():
    THIKNESS = 0.02
    glColor3f(1, 0, 0)
    cyl = gluNewQuadric()
    cy2 = gluNewQuadric()
    gluCylinder(cyl, THIKNESS, THIKNESS, 1, 30, 30)
    glTranslate(0, 0, 1)
    gluCylinder(cy2, THIKNESS, 0, 0.2, 30, 30)
    glTranslate(0, 0, -1)

    glColor3f(0, 0, 1)
    cyl = gluNewQuadric()
    cy2 = gluNewQuadric()
    glRotate(-90, 1, 0, 0)
    gluCylinder(cyl, THIKNESS, THIKNESS, 3, 30, 30)
    glTranslate(0, 0, 3)
    gluCylinder(cy2, THIKNESS, 0, 0.2, 30, 30)
    glTranslate(0, 0, -3)
    glRotate(90, 1, 0, 0)

    glColor3f(0, 1, 0)
    cyl = gluNewQuadric()
    cy2 = gluNewQuadric()
    glRotate(90, 0, 1, 0)
    gluCylinder(cyl, THIKNESS, THIKNESS, 1, 30, 30)
    glTranslate(0, 0, 1)
    gluCylinder(cy2, THIKNESS, 0, 0.2, 30, 30)
    glTranslate(0, 0, -1)
    glRotate(-90, 0, 1, 0)
    glColor(1,1,1)



def MTL(filename):
    contents = {}
    mtl = None
    for line in open(OBJ_FOLDER + filename, "r"):
        if line.startswith('#'): continue
        values = line.split()
        if not values: continue
        if values[0] == 'newmtl':
            mtl = contents[values[1]] = {}
        elif mtl is None:
            raise ValueError("mtl file doesn't start with newmtl stmt")
        elif values[0] == 'map_Kd':
            print("map_kd not implemented")
            '''
            # load the texture referred to by this declaration
            mtl[values[0]] = values[1]
            surf = pygame.image.load(mtl['map_Kd'])
            image = pygame.image.tostring(surf, 'RGBA', 1)
            ix, iy = surf.get_rect().size
            texid = mtl['texture_Kd'] = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, texid)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER,
                GL_LINEAR)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA,
                GL_UNSIGNED_BYTE, image)
            '''
        else:
            mtl[values[0]] = map(float, values[1:])
    return contents


class OBJ:
    def __init__(self, filename, swapyz=False):
        """Loads a Wavefront OBJ file. """
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []

        material = None
        for line in open(OBJ_FOLDER + filename, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'v':
                v = tuple(map(float, values[1:4]))
                if swapyz:
                    v = v[0], v[2], v[1]
                self.vertices.append(v)
            elif values[0] == 'vn':
                v = tuple(map(float, values[1:4]))
                if swapyz:
                    v = v[0], v[2], v[1]
                self.normals.append(v)
            elif values[0] == 'vt':
                self.texcoords.append(map(float, values[1:3]))
            elif values[0] in ('usemtl', 'usemat'):
                material = values[1]
            elif values[0] == 'mtllib':
                self.mtl = MTL(values[1])
            elif values[0] == 'f':
                face = []
                texcoords = []
                norms = []
                for v in values[1:]:
                    w = v.split('/')
                    face.append(int(w[0]))
                    if len(w) >= 2 and len(w[1]) > 0:
                        texcoords.append(int(w[1]))
                    else:
                        texcoords.append(0)
                    if len(w) >= 3 and len(w[2]) > 0:
                        norms.append(int(w[2]))
                    else:
                        norms.append(0)
                self.faces.append((face, norms, texcoords, material))

        self.gl_list = glGenLists(1)
        glNewList(self.gl_list, GL_COMPILE)
        glEnable(GL_TEXTURE_2D)
        glFrontFace(GL_CCW)
        for face in self.faces:
            vertices, normals, texture_coords, material = face

            mtl = self.mtl[material]
            if 'texture_Kd' in mtl:
                # use diffuse texmap
                glBindTexture(GL_TEXTURE_2D, mtl['texture_Kd'])
            else:
                pass
                # just use diffuse colour
                # glColor(*mtl['Kd'])

            glBegin(GL_POLYGON)
            for i in range(len(vertices)):
                if normals[i] > 0:
                    glNormal3fv(self.normals[normals[i] - 1])
                if texture_coords[i] > 0:
                    pass
                    # glTexCoord2fv(self.texcoords[texture_coords[i] - 1]) #TODO: fix textuer reading implementation
                glVertex3fv(self.vertices[vertices[i] - 1])
            glEnd()
        glDisable(GL_TEXTURE_2D)
        glEndList()
