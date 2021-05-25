print()
print("--------------------------------------------------------------------------------------------------------------")
import sys
print("Импортируем модуль sys и вызовем у него: \nsys.platform === " + str(sys.platform) + "\n")
print("sys.argv === " + str(sys.argv) + "\n")

print("sys.version === " + str(sys.version) + "\n")
print("sys.path === " + str(sys.path) + "\n")
print("sys.api_version === " + str(sys.api_version)+"\n")
print("--------------------------------------------------------------------------------------------------------------")

import os
print("os.getcwd() === " + os.getcwd() + "\n")
print("os.environ === " + str(os.environ) + "\n")