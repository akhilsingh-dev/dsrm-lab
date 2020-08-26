inputs = {
    ## Answer = True
    "snapshot1" : [
        [3,1,2],
        [1,3,2],
        [1,2,3]
    ],
    ## Answer = False (Node 1 counter is messed up)
    "snapshot2" : [
        [2,1,2],
        [1,3,2],
        [3,2,3]
    ],
    ## Answer = True
    "snapshot3" : [
        [2,1,2],
        [1,3,2],
        [2,2,3]
    ]
}

def is_consistent(snapshot: list) -> bool:
    # Transpose the snapshot
    snapshot = [list(map(lambda x:x[i],snapshot)) for i in range(len(snapshot))]        
    # Check if max is self
    for i,tmp in enumerate(snapshot):
        if max(tmp) != tmp[i]:
            return False
    return True


for snapshot in inputs.values():
    print(is_consistent(snapshot))