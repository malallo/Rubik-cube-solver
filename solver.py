import rubik
import sys

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    """
    make dictionaries for both the start's history and the end's history
    as well as a queue list that will work on the order of turns
    """
    """
    The solution is represented by a list of moves,
    the histories are represented by dictionaries,
    and the invariance is how there is at most 14 moves needed.
    To go further, for every new frontier that is created in these loops,
    the number of moves needed goes down by one.
    """
    path = []
    StartVisit = {}
    EndVisit = {}
    oldSFron = []
    newSFron = []
    oldEFron = []
    newEFron = []
    StartVisit[start] = "n/a"
    EndVisit[end] = "n/a"
    left = start
    right = end
    newSFron.append(start)
    newEFron.append(end)
    i = 0
    while i<7: #7 for each side should guarantee a match
        if start == end:
            return path
        oldSFron = newSFron
        newSFron = []
        oldEFron = newEFron
        newEFron = []
        for form in oldSFron:#Create the new Start side frontier
            for twist in rubik.quarter_twists:
                temp = rubik.perm_apply(twist, form)
                if temp not in oldEFron:
                    if temp not in StartVisit:
                        StartVisit[temp] = twist
                        newSFron.append(temp)
                else:
                    #Calculate the path and return it
                    chaser = temp
                    StartVisit[temp] = twist
                    while chaser != start: #make the path from the start first
                        move = StartVisit.get(chaser)
                        path.insert(0,move)
                        chaser = rubik.perm_apply(rubik.perm_inverse(move), chaser)
                    chaser = temp
                    while chaser != end:
                        move = rubik.perm_inverse(EndVisit.get(chaser))
                        path.append(move)
                        chaser = rubik.perm_apply(move, chaser)
                    return path
        for form2 in oldEFron:#Create the new End side frontier
            for twist2 in rubik.quarter_twists:
                temp = rubik.perm_apply(twist2, form2)
                if temp not in newSFron:
                    if temp not in EndVisit:
                        EndVisit[temp] = twist2
                        newEFron.append(temp)
                else:
                    #Calculate the path and return it
                    chaser = temp
                    EndVisit[temp] = twist2
                    while chaser != start: #make the path from the start first
                        move = StartVisit.get(chaser)
                        path.insert(0,move)
                        chaser = rubik.perm_apply(rubik.perm_inverse(move), chaser)
                    chaser = temp
                    while chaser != end: #then append the path from the end
                        move = rubik.perm_inverse(EndVisit.get(chaser))
                        path.append(move)
                        chaser = rubik.perm_apply(move, chaser)
                    return path
        i+=1
    return None
