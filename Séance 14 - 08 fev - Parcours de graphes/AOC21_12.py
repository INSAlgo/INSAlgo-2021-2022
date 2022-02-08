from collections import defaultdict
from typing import List


def read(path: str) -> List[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    print(lines)
    return lines


def DFS(adj, current, visited):
    if current == 'end':
        global numOfPath
        numOfPath += 1
        return
    elif visited[current]:
        return
    else:
        if current == current.lower():
            visited[current] = True
        for adjNode in adj[current]:
            DFS(adj, adjNode, visited)
        visited[current] = False

        pass


def firstProblem(lines: List[str]):
    adj = defaultdict(list)
    visited = defaultdict(bool)
    for line in lines:
        p1, p2 = line.split('-')
        adj[p1].append(p2)
        adj[p2].append(p1)

    global numOfPath
    numOfPath = 0
    DFS(adj, 'start', visited)
    print(numOfPath)
    return


def DFS2(adj, current, visited, doubleVisited):

    if current == 'end':
        global numOfPath
        numOfPath += 1



    elif visited[current] and (doubleVisited or current == 'start' or current == 'end'):
        return
    elif visited[current] and not doubleVisited:

        for adjNode in adj[current]:
            DFS2(adj, adjNode, visited, True)

    else:
        if current == current.lower():
            visited[current] = True

        for adjNode in adj[current]:
            DFS2(adj, adjNode, visited, doubleVisited)
        visited[current] = False


    return


def secondProblem(lines: List[str]):
    adj = defaultdict(list)
    visited = defaultdict(bool)
    for line in lines:
        p1, p2 = line.split('-')
        adj[p1].append(p2)
        adj[p2].append(p1)

    global numOfPath
    numOfPath = 0

    DFS2(adj, 'start', visited, False)
    print(numOfPath)
    return


if __name__ == "__main__":
    lines = read("12input.txt")
    firstProblem(lines)
    secondProblem(lines)
