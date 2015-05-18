from optparse import OptionParser
import ConfigParser
import logging
import time
import os
import re
import sys

#download from http://docs.python-requests.org/en/latest/user/install/#install
import requests
import json

def main():
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")
    parser.add_option("-d", "--directory",
                      action="store",
                      dest="location",
                      default="../",
                      help="data location")
   
    parser.add_option("-f", "--file",
                      action="store",
                      dest="file",
                      default="Sports.txt",
                      help="data location")
 
    parser.add_option("-l", "--logfile",
                      action="store",
                      dest="logfile",
                      default="/tmp/script.log",
                      help="log file location")

    parser.add_option("-H", "--host",
                      action="store",
                      dest="host",
                      default="127.0.0.1",
                      help="targe host ip")

    parser.add_option("-P", "--port",
                      action="store",
                      dest="port",
                      default="9000",
                      help="target port")

    #if len(sys.argv) == 1:
    #     print "Learn some usages: " + sys.argv[0] + " -h"
    #     sys.exit(1)


    (options, args) = parser.parse_args()
    print options

    headers = {'content-type': 'application/json'}
    url = 'http://localhost:9000/v1/quiz/add'

    file = open(options.location + options.file, 'r')
    i = 1
    for line in file:
       line = line.rstrip('\n')
       category, question, correct_ans, ans1, ans2, ans3, df = line.split("|")
       payload = {"qid":i,"category":category,"question":question,"right_answer":correct_ans,"ans1":ans1,"ans2":ans2,"ans3":ans3,"df": int(df)}
       r = requests.post(url, data=json.dumps(payload), headers=headers)
       print r.text     
       i = i + 1
       print i


if __name__ == '__main__':
    main()

