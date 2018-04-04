import sys
from itertools import combinations

########################################################################
# How to build an eulerian path in a odd-size clique?
#   From the very clever post by Aryabhata that can be found here:
#
#       https://math.stackexchange.com/a/16935/451099
########################################################################
def clique_tour(n):
    if n % 2 == 0:
        raise ValueError("The number of node must be odd, otherwise no euler tour exist.")

    middle = (n-1)//2
    path_shape = [ u for i in range(middle) for u in (i,n-2-i) ]

    hamiltonian_paths = []
    # Increment the path shape to "rotate" the hamiltonian path (see stackexchange post)
    for i in range(middle):
        hamiltonian_paths += [ (path_shape[p]+i)%(n-1) for p in range(len(path_shape)) ]
        hamiltonian_paths += [n-1] # Everything is rotated, this node is here to make a junction from one hamiltonian path to the next

    # Close the tour
    hamiltonian_paths += [hamiltonian_paths[0]]

    return hamiltonian_paths

def almost_clique_tour(n):
    if n % 2 == 1:
        raise ValueError("Number of node is odd, use clique_tour() instead of almost_clique_tour, it will produce better results.")

    path_shape = [ u for i in range(n//2) for u in (i,n-1-i) ]
    hamiltonian_paths = []
    # Increment the path shape to "rotate" the hamiltonian path (see stackexchange post)
    for i in range(n//2):
        path = [ (path_shape[p]+i)%n for p in range(len(path_shape)) ]
        print(path)
        hamiltonian_paths += path

    # Close the tour
    hamiltonian_paths += [hamiltonian_paths[0]]
    return hamiltonian_paths

def best_tour_yet(n):
    if n % 2 == 0:
        return almost_clique_tour(n)
    else:
        return clique_tour(n)

def main(n):
    node_order = best_tour_yet(n)
    print("The tour contains {} edges: ".format(len(node_order)-1))
    print("\t{}".format(node_order))
    nodes = [i for i in range(n)]
    edges = set(combinations(nodes, 2))
    if check_eulerian_tour(edges, node_order):
        print("\tit is Eulerian (optimal).")
    else:
        print("\tit is not Eulerian (not optimal).")


def check_eulerian_tour(edges, node_order):
    is_eulerian = True
    euler_tour = [ (node_order[i], node_order[i+1]) for i in range(len(node_order)-1) ]
    if euler_tour[-1][-1] != euler_tour[0][0]:
        return False
    for (u,v) in euler_tour:
        if not delete_edge(edges, u,v):
            print("\t Edge {} appears more than once".format((u,v)))
            is_eulerian = False
    if len(edges) > 0:
        is_eulerian = False
        print("\t Some edges are missing")
    return is_eulerian


def delete_edge(edges, u,v):
    success_1 = True
    success_2 = True
    try:
        edges.remove((u,v))
    except:
        success_1 = False
    try:
        edges.remove((v,u))
    except:
        success_2 = False
    return (success_1 or success_2)

if __name__ == "__main__":
    n = 7
    if (len(sys.argv) > 1):
        n = int(sys.argv[1])
    main(n)
