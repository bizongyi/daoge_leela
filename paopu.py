# -*- coding: utf-8 -*- 
import sys
import os
import subprocess
import re

def __shell__(cmd):
  os.system(cmd)
  
        

        
__shell__('./autogtp -g 2 -k sgf| grep minute')
