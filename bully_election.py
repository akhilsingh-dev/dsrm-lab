## Bully election Algorithm Simulation
## Descending order (Higher the number, more the priority)
# from __future__ import annotations
from typing import List


class Node:
    def __init__(self,node_id:int,priority:int) -> None:
        self.node_id = node_id
        self.priority = priority
        self.is_alive = True
        self.coord = -1

    def kill(self) -> bool:
        try:
            self.is_alive = False
            return True
        except:
            return False
    
    def revive(self) -> bool:
        try:
            self.is_alive = True
            return True
        except:
            return False
    
    def __repr__(self) -> str:
        return str({"id":self.node_id, "priority":self.priority, "coord":self.coord, "is_alive":self.is_alive})


## We assume here that every node knows every other node
def contest_election(nodes:List[Node],initiator:Node,msg_ctr:dict) -> None:
    """Contest a round of election in a list of nodes started by the initiator

    Args:
        nodes (List[Node]): The list of nodes
        initiator (Node): The node that is contesting election/wants to become the co-ordinator
        msg_ctr (dict): A Message counter dictionary with keys: "broadcast","election","ok"
    """

    print(f"Node {initiator.node_id} Starts an election!\n")
    
    index = -1
    
    ## Election loop, the initiator asks all higher nodes
    for i,node in enumerate(nodes):
        if node.priority > initiator.priority:
            if index == -1 and node.is_alive:
                index = i
            print(f"Node {initiator.node_id} sends Election msg to Node {node.node_id}")
            msg_ctr["election"] += 1
    print("\n")
    
    ## Reply loop, the initiator gets back replies from higher nodes or not depending on higher node
    for node in nodes:
        if node.priority > initiator.priority and node.is_alive:
            print(f"Node {node.node_id} sends OK msg to Node {initiator.node_id}")
            msg_ctr["ok"] += 1
    print("\n\n")


    alive_nodes = list(filter(lambda x:x.is_alive,nodes))

    ## If the initiator is the highest alive node, broadcast and terminate the function 
    if initiator == alive_nodes[-1]:
        print(f"Highest Node = {initiator.node_id}. Broadcasting...\n")
        for node in nodes:
            if node.is_alive:
                node.coord = initiator.node_id
            msg_ctr["broadcast"] += 1
        ## Self setting doesnt need a broadcast
        msg_ctr["broadcast"] -= 1
        return

    ## Start election on higher node if it is alive
    if nodes[index].is_alive:
        contest_election(nodes,nodes[index],msg_ctr)


def kill_nodes(nodes: List[Node], init_idx: int) -> List[Node]:
    idxs_to_kill = str(input("Enter nodes to kill(space separated integers less than number of nodes): "))
    idxs_to_kill = [int(idx) for idx in idxs_to_kill.split() if int(idx) < num_nodes and int(idx) >= 0 and int(idx) != init_idx]

    for idx in idxs_to_kill:
        nodes[idx].kill()
    print(f"Nodes {idxs_to_kill} were killed!\n")
    return nodes



if __name__ == "__main__":

    from pprint import pprint

    ## Number of nodes
    num_nodes = int(input("Enter the number of nodes: "))

    ## Counter to count messages
    msg_ctr = {
        "election" : 0,
        "ok" : 0,
        "broadcast" : 0
    }

    ## Create those many nodes
    nodes = [Node(x,x) for x in range(num_nodes)]

    init_idx = int(input("Enter the initiator index: "))

    contest_election(nodes,nodes[init_idx],msg_ctr)    
    pprint(nodes)
    pprint(msg_ctr)

    ## Kill a few nodes
    nodes = kill_nodes(nodes,init_idx)

    ## Reset counter
    msg_ctr = {key: 0 for key in msg_ctr.keys()}

    ## Re contest election
    contest_election(nodes,nodes[init_idx],msg_ctr)
    pprint(msg_ctr)
    pprint(nodes)