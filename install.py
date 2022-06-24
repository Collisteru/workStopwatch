import os
import getpass

USER = getpass.getuser()

DESTINATION = "/home/" + USER + "/.workstopwatch"

mkdir = "mkdir " + DESTINATION

exists = os.path.exists(DESTINATION)

if(not exists):
    os.system(mkdir)


for i in range(0, 8):
    file="frame000{0}.png".format(i)
    cmd = "cp " + file + " " + DESTINATION +"/"
    os.system(cmd)
