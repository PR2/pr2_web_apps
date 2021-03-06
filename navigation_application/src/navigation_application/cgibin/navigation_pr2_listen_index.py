#! /usr/bin/env python

"""
usage: %(progname)s [args]
"""

import os, sys, string, time, getopt, re
import neo_cgi, neo_util, neo_cs
from pyclearsilver.log import *
from pyclearsilver import CSPage, odb

from webui import MBPage

class MyPage(MBPage.MBPage):
  def setup(self, hdf):
    pass
    
  def display(self, hdf):
    hdf.setValue('CGI.listen_only', 'true')

def run(context):
  return MyPage(context, pagename="index", nologin=False)

def main():
  context = CSPage.Context()
  run(context).start()

if __name__ == "__main__":
  main()
