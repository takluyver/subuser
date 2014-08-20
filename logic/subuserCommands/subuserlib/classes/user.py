#!/usr/bin/env python
# This file should be compatible with both Python 2 and 3.
# If it is not, please file a bug report.

#external imports
import getpass, os
#internal imports
import subuserlib.classes.registry, subuserlib.classes.repositories, subuserlib.classes.config, subuserlib.classes.installedImages, subuserlib.classes.dockerDaemon, subuserlib.test

class User(object):
  """
  This class provides a "base" User object used by subuser.  This is the stem of a tree like data structure which holds all of the various objects owned by a given user:

   - settings
   - subusers
   - repository lists
  ect.

  You create a new User object by passing the home dir of the user.

  >>> import subuserlib.classes.user
  >>> u = subuserlib.classes.user.User("root","/root/")
  >>> u.homeDir
  '/root/'

  """
  name = None
  homeDir = None
  __config = None
  __registry = None
  __installedImages = None
  __dockerDaemon = None
  
  def __init__(self,name=None,homeDir=None):
    if name:
      self.name = name
    else:
      self.name = getpass.getuser()

    if homeDir:
      self.homeDir = homeDir
    else:
      if subuserlib.test.testing:
        self.homeDir = "/home/test/"
      else:
        self.homeDir = os.path.expanduser("~") 

  def getConfig(self):
    if self.__config == None:
      self.__config = subuserlib.classes.config.Config(self)
    return self.__config

  def getRegistry(self):
    if self.__registry == None:
      self.__registry = subuserlib.classes.registry.Registry(self)
    return self.__registry

  def getInstalledImages(self):
    if self.__installedImages == None:
      self.__installedImages = subuserlib.classes.installedImages.InstalledImages(self)
    return self.__installedImages

  def getDockerDaemon(self):
    if self.__dockerDaemon == None:
      self.__dockerDaemon = subuserlib.classes.dockerDaemon.DockerDaemon(self)
    return self.__dockerDaemon
