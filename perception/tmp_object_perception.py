import rospy
import numpy
import tf

import json_prolog



def pose_to_mat(pose):
    quat = [pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w]
    pos = numpy.matrix([pose.position.x,pose.position.y,pose.position.z]).T
    mat = numpy.matrix(tf.transformations.quaternion_matrix(quat))
    mat[0:3, 3] = pos
    return mat


def handle_msg():
    p = pose_to_mat(obj.pose).tolist()
    type = obj.type
    q = "create_object_perception('http://knowrob.org/kb/knowrob.owl#"+type+"', [" + p[0][0] + ","+ p[0][1] + ","+ p[0][2] + ","+ p[0][3] + "," + p[1][0] + ","+ p[1][1] + ","+ p[1][2] + ","+ p[1][3] + "," + p[2][0] + ","+ p[2][1] + ","+ p[2][2] + ","+ p[2][3] + ", + p[3][0] + ","+ p[3][1] + ","+ p[3][2] + ","+ p[3][3] + ", "], ['DummyObjectDetection'], ObjInst)"

 
if __name__ == '__main__':
    rospy.init_node('perception_handler')
    prolog = json_prolog.Prolog()
    query = prolog.query("member(A, [1, 2, 3, 4]), B = ['x', A]")
    for solution in query.solutions():
        print 'Found solution. A = %s, B = %s' % (solution['A'], solution['B'])
    query.finish()
