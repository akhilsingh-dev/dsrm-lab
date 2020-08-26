inputs = [
    ## Answer = True
    {
        "snapshot" : [
            [2,0,0],
            [1,1,2],
            [2,0,3]
        ]
    },
    ## Answer = True
    {
        "snapshot" : [
            [2,0,0],
            [1,1,2],
            [1,0,2]
        ]
    },
    ## Answer = False
    {
        "snapshot" : [
            [1,0,0],
            [1,1,2],
            [2,0,3]
        ]
    }
]

def is_consistent(snapshot: list) -> bool:
    # Transpose the snapshot
    snapshot = [list(map(lambda x:x[i],snapshot)) for i in range(len(snapshot))]        
    # Check if max is self
    for i,tmp in enumerate(snapshot):
        if max(tmp) != tmp[i]:
            return False
    return True


if __name__ == "__main__":
    for inp in inputs:
        print("Consistent" if is_consistent(**inp) else "Inconsistent")