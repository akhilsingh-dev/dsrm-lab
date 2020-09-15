from __future__ import annotations
from typing import List,Set

inputs = [

    ## Answer = False, no cycle with initiator
    {
        "wfg" : [
            [1, 1, 0, 0],
            [0, 1, 1, 1],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ],
        "initiator" : 0
    },

    ## Answer = False, no cycle with initiator
    {
        "wfg" : [
            [1, 1, 0, 0],
            [0, 1, 1, 1],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ],
        "initiator" : 1
    },

    ## Answer = True, Cycle = (1,2,3,4)
    {
        "wfg" : [
            [1, 1, 0, 0],
            [0, 1, 1, 1],
            [0, 0, 1, 1],
            [1, 0, 0, 1]
        ],

        "initiator" : 0
    },

    ## Answer = True, cycle = (2,3,4)
    {
        "wfg" : [
            [1, 1, 0, 0],
            [0, 1, 1, 1],
            [0, 0, 1, 1],
            [0, 1, 0, 1]
        ],

        "initiator" : 1
    },

    ## Answer = False cycle exists bw 2,3,4 but 1 is not involved
    {
        "wfg" : [
            [1, 1, 0, 0],
            [0, 1, 1, 1],
            [0, 0, 1, 1],
            [0, 1, 0, 1]
        ],

        "initiator" : 0
    }
]


def send_probe(wfg: List[List[int]], visited: Set[int], initiator: int, source: int, destination: int) -> bool:
    """Run through the complete graph to check for cycles

    Args:
        wfg (List[List[int]]): The wait for graph in form of a 2D mtrix of ints
        visited (set): Set to denote which sites have been probed
        initiator (int): The original initiator for the probe 
        source (int): The current probe's source site
        destination (int): The current probe's destination site


    Returns:
        bool: Is there a cycle between initiator and destination
    """

    tmp = False

    print(f"Probe: ({initiator+1}, {source+1}, {destination+1})")
    
    
    ## Check all sites wrt to the dest
    for site, is_wait in enumerate(wfg[destination]):
        ## If the dest is waiting for a site
        if site not in visited and site != destination and is_wait == 1:
            visited.add(site)        
            ## If we find a probe with initiator same as destination,
            ## Return True
            if initiator == destination:
                print("Deadlock detected")
                return True
            
            ## Otherwise, send a new probe to the new site
            ## from destination to the site its waiting for

            tmp = send_probe(wfg, visited, initiator, destination, site) 
            if tmp:
                return True

    ## If all sites are exhausted,
    ## Return False
    return tmp


def run_cmh(wfg: List[List[int]], initiator: int) -> bool:

    is_deadlock = False
    visited = set()


    for site,is_wait in enumerate(wfg[initiator]):
        ## If src is waiting for site,
        if is_wait == 1 and initiator != site:
            ## Send a probe to that site
            is_deadlock = is_deadlock or send_probe(wfg,visited,initiator,initiator,site)
        
    return is_deadlock


if __name__ == "__main__":
    
    for input in inputs:
        print(run_cmh(**input))
        print("\n\n")
