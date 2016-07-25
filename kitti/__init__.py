"""
   kitti
   __init__.py

   @author: jason corso

   Just defines the module index
"""

# to allow from kitti import *
__all__ = ["data","raw","stereo","velodyne"]

# to allow kitti.XXX
import data
import raw
import stereo
import velodyne
