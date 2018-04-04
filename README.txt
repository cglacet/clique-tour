
Build a clique tour for a given number of node n, if n is odd then the tour is eulerian otherwise the tour contains n/2 duplicate edges.

The algorithm is presented in a post from Aryabhata that can be found on stackexchange (https://math.stackexchange.com/questions/16933/generating-a-eulerian-circuit-of-a-complete-graph-with-constant-memory)

Installation:

pip install clique_tour
Usage:

import clique_tour

odd_n = 7
even_n = odd_n-1
# When n is odd: 
eulerian_tour = clique_tour.eulerian(odd_n)
# When it's even: 
not_eulerian_tour = clique_tour.almost_eulerian(even_n) 
# This function is a shortcut that test the parity of n and returns the correct tour:
odd_tour = clique_tour.build(odd_n)
even_tour = clique_tour.build(even_n)
Results:

print(eulerian_tour)
print(odd_tour)
print(not_eulerian_tour)
print(even_tour)
[0, 5, 1, 4, 2, 3, 6, 1, 0, 2, 5, 3, 4, 6, 2, 1, 3, 0, 4, 5, 6, 0]
[0, 5, 1, 4, 2, 3, 6, 1, 0, 2, 5, 3, 4, 6, 2, 1, 3, 0, 4, 5, 6, 0]
[0, 5, 1, 4, 2, 3, 1, 0, 2, 5, 3, 4, 2, 1, 3, 0, 4, 5, 0]
[0, 5, 1, 4, 2, 3, 1, 0, 2, 5, 3, 4, 2, 1, 3, 0, 4, 5, 0]
