from ctypes import cdll
import os
lib = cdll.LoadLibrary('./ambha.so')
lib.goTrain()