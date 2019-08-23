#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Sofa
import math


def moveRestPos(rest_pos, dx, dy, dz):
    str_out = ' '
    for i in xrange(0,len(rest_pos)) :
        str_out= str_out + ' ' + str(rest_pos[i][0]+dx)
        str_out= str_out + ' ' + str(rest_pos[i][1]+dy)
        str_out= str_out + ' ' + str(rest_pos[i][2]+dz)
    return str_out

def rotateRestPos(rest_pos,rx,centerPosY,centerPosZ):
    str_out = ' '
    for i in xrange(0,len(rest_pos)) :
        newRestPosY = (rest_pos[i][1] - centerPosY)*math.cos(rx) - (rest_pos[i][2] - centerPosZ)*math.sin(rx) +  centerPosY
        newRestPosZ = (rest_pos[i][1] - centerPosY)*math.sin(rx) + (rest_pos[i][2] - centerPosZ)*math.cos(rx) +  centerPosZ
        str_out= str_out + ' ' + str(rest_pos[i][0])
        str_out= str_out + ' ' + str(newRestPosY)
        str_out= str_out + ' ' + str(newRestPosZ)
    return str_out

class controller(Sofa.PythonScriptController):

    def initGraph(self, node):

            self.node = node
            self.bellowNode=self.node.getChild('Bellow')
            self.pressureConstraintNode = self.bellowNode.ElasticMaterialObject.getChild('cavitypressure')

            self.centerPosY = 70
            self.centerPosZ = 0
            self.rotAngle = 0                       

    def onKeyPressed(self,c):
            self.dt = self.node.findData('dt').value
            incr = self.dt*1000.0;

            self.MecaObject=self.bellowNode.ElasticMaterialObject.Cavity.getObject('tetras');
            self.pressureConstraint = self.pressureConstraintNode.getObject('SurfacePressureConstraint')

            if (c == "+"):
                pressureValue = self.pressureConstraint.findData('value').value[0][0] + 0.01
                if pressureValue > 1.5:
                    pressureValue = 1.5
                self.pressureConstraint.findData('value').value = str(pressureValue)
                print self.pressureConstraint.findData('value').value
            if (c == "-"):
                pressureValue = self.pressureConstraint.findData('value').value[0][0] - 0.01
                self.pressureConstraint.findData('value').value = str(pressureValue)
                print self.pressureConstraint.findData('value').value
            # # UP key :
            # if ord(c)==19:
               
            # # DOWN key : rear
            # if ord(c)==21:
               
            # # LEFT key : left
            # if ord(c)==20:

            # # RIGHT key : right
            # if ord(c)==18:
             
            # # a key : direct rotation
            # if (ord(c) == 65):

            # # q key : indirect rotation
            # if (ord(c) == 81):

