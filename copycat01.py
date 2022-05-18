#!/usr/bin/env python3
import shutil
import os

#Allow user to run the program from any location on the system
os.chdir("/home/student/mycode/")

#shutil.copy(source, destination) copy fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
#copy the entire directoryA to directoryB
shutil.copytree("5g_research/", "5g_research_backup/")


