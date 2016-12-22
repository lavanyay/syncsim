from cpg import *

from file_parser import *
from frugal1 import * # for default links and flows
import argparse

# use like python frugal1_test.py --cap sam-cap.txt --tm sam-tm.txt

parser = argparse.ArgumentParser()
parser.add_argument("--cap", type = str, default = None)
parser.add_argument("--tm", type = str, default = None)
parser.add_argument("--r", type = int, default = 100)
parser.add_argument("--ev", type = int, default = 2000000)

args = parser.parse_args()




def main():
    links = {1: Link(1, 120), 2: Link(2, 120), 3: Link(3, 120), 4: Link(4, 120)}
    flows = { 1: Msg("1", 1, [1]),\
              2: Msg("2", 2, [1,2]),\
              4: Msg("4", 4, [2,3]),\
              8: Msg("8", 8, [3,4]),\
              32: Msg("32", 32, [4]) }


    if args.cap is not None:
        links = get_cap(args.cap)

    if args.tm is not None:
        flows = get_flows(args.tm)  

    if len(flows) == 0:
        print "No flows."
    else:
        cpg(maxEvents = args.ev, maxRounds = args.r, links = links, flows = flows)

    for linkId in links:
        print "Link %s removed in level %d (sumSat %d, numUnsat %d)"%\
            (linkId, links[linkId].level, links[linkId].sumSat, links[linkId].numUnsat)

    for flowId in flows:
        linkId = flows[flowId].t
        print "Flow %s removed @ %d when link %s removed in level %d (sumSat %d, numUnsat %d)"%\
            (flowId, flows[flowId].AR, linkId, links[linkId].level, links[linkId].sumSat, links[linkId].numUnsat)

main()
