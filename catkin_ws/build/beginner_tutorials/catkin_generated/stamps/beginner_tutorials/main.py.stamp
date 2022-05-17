import rospy
import sensor_msgs.point_cloud2
from sensor_msgs.msg import PointCloud2, PointCloud
import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import time

count = 0


def callback(input_ros_msg):
    start = time.time()
    point_cloud_list = list()
    for point in sensor_msgs.point_cloud2.read_points(input_ros_msg, skip_nans=True):
        point_cloud_list.append([point[0], point[1], point[2]])
    point_cloud = np.array(point_cloud_list)
    num_triangles= int(len(point_cloud[:]) / 3)
    data = np.zeros(num_triangles, dtype=mesh.Mesh.dtype)
    for i in range(num_triangles):
        data["vectors"][i] = np.array([[point_cloud[i*3 + 0][0], point_cloud[i*3 + 0][1], point_cloud[i*3 + 0][2]],
                                    [point_cloud[i*3 + 1][0], point_cloud[i*3 + 1][1], point_cloud[i*3 + 1][2]],
                                    [point_cloud[i*3 + 2][0], point_cloud[i*3 + 2][1], point_cloud[i*3 + 2][2]]])
    m=mesh.Mesh(data)
    global count
    m.save('figure_{}.stl'.format(count))
    count = count+1

    # figure = pyplot.figure()
    # axes = mplot3d.Axes3D(figure)

    # # Load the STL files and add the vectors to the plot
    # your_mesh = mesh.Mesh.from_file('stl_test_cat.stl')
    # axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

    # # Auto scale to the mesh size
    # scale = your_mesh.points.flatten()
    # axes.auto_scale_xyz(scale, scale, scale)

    # # Show the plot to the screen
    # pyplot.show()
    print("Convert Time : ", time.time() - start)

if __name__ == "__main__":
    rospy.init_node("test", anonymous=True)
    rospy.Subscriber('/camera/depth/points', PointCloud2, callback)
    rospy.spin()
