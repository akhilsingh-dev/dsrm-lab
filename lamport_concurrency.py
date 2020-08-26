inputs = {
    "pairs" : [
        ([1,8,0],[3,8,0]),
        ([2,0,6],[3,1,9]),
        ([6,8,0],[7,7,0]),
        ([8,0,9],[9,1,8]),
    ]
}


def check_concurrency(m1:list,m2:list) -> None:
    try:
        ## Check for equal length
        assert len(m1) == len(m2)
        n = range(len(m1))

        ## if the one node is older in state1 and another node is younger in state2
        ## the system is concurrent
        if any(m1[i] < m2[i] for i in n) and any(m1[j] > m2[j] for j in n):
            print("Concurrent")
        else:
            if m1 < m2:
                print("m1 is older than m2")
            else:
                print("m1 is younger than m2")

    except AssertionError as ae:
        print("The two vectors are of unequal length")


if __name__ == "__main__":
    for pair in inputs["pairs"]:
        check_concurrency(*pair)
