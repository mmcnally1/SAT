# python3
import copy
import itertools

# Get number of variables, number of edges, edges
def read_input():
    n, m = map(int, input().split())
    edges = [ list(map(int, input().split())) for i in range(m) ]
    return n, m, edges

# Create n^2 variables, 1 for each vertex i in each possible position j
def create_variables(n):
    variables = []
    val = 1
    for i in range(n):
        variables.append([])
        for j in range(n):
            variables[i].append(val)
            val += 1
    return variables

# Add constraints such that each vertex can only be used once
def one_val_per_var(variables):
    negations = copy.deepcopy(variables)
    one_val = []
    for i in range(len(negations)):
        for j in range(len(negations[i])):
            negations[i][j] = 0 - negations[i][j]
    for var in negations:
        comb = itertools.combinations(var, 2)
        for val in comb:
            one_val.append(list(val))
    return one_val

# Add constraints such that each position in the cycle must be used
def one_in_each_spot(variables, n):
    one_in_each_spot = []
    for i in range(n):
        one_in_each_spot.append([])
        for j in range(n):
            one_in_each_spot[i].append(variables[j][i])
    return one_in_each_spot

# Add constraints such that no two vertices can be in the same position in the cycle
def no_two_in_same_spot(one_in_each_spot):
    negations = copy.deepcopy(one_in_each_spot)
    one_val = []
    for i in range(len(negations)):
        for j in range(len(negations[i])):
            negations[i][j] = 0 - negations[i][j]
    for var in negations:
        comb = itertools.combinations(var, 2)
        for val in comb:
            one_val.append(list(val))
    return one_val

# Add constraints such that any pair of vertices without an edge between them
# can't be in consecutive order in the cycle
def edge_constraints(edges, variables, n):
    edge_constraints = []
    no_edge = []
    for i in range(1, len(variables) + 1):
        for j in range(1, len(variables) + 1):
            check = [i,j]
            rev_check = [j,i]
            if check not in edges and rev_check not in edges and i != j:
                no_edge.append(check)
    for i in range(len(no_edge)):
        for j in range(n):
            if j < (n - 1):
                edge_constraints.append([0 - variables[no_edge[i][0] - 1][j],
                                        0 - variables[no_edge[i][1] - 1][j + 1]])

    return edge_constraints

# Print constraints so they can be entered into a SAT solver
def Print_Formula(num_var, num_clauses, variables, one_val, one_in_each_spot,
                    no_two_in_same_spot, edge_constraints):
    print(num_clauses, num_var)
    for clause in variables:
        s = ""
        for i in range(len(clause)):
            s += str(clause[i]) + " "
        s += "0"
        print(s)
    for clause in one_val:
        s = ""
        for i in range(len(clause)):
            s += str(clause[i]) + " "
        s += "0"
        print(s)
    for clause in one_in_each_spot:
        s = ""
        for i in range(len(clause)):
            s += str(clause[i]) + " "
        s += "0"
        print(s)
    for clause in no_two_in_same_spot:
        s = ""
        for i in range(len(clause)):
            s += str(clause[i]) + " "
        s += "0"
        print(s)
    for clause in edge_constraints:
        s = ""
        for i in range(len(clause)):
            s += str(clause[i]) + " "
        s += "0"
        print(s)

if __name__ == "__main__":
    n, m, edges = read_input()
    variables = create_variables(n)
    one_val  = one_val_per_var(variables)
    edge_constraints = edge_constraints(edges, variables, n)
    one_in_each_spot = one_in_each_spot(variables, n)
    no_two_in_same_spot = no_two_in_same_spot(one_in_each_spot)
    num_var = pow(n, 2)
    num_clauses = len(variables) + len(one_val) + len(edge_constraints) + len(one_in_each_spot) + len(no_two_in_same_spot)
    Print_Formula(num_var, num_clauses, variables, one_val, one_in_each_spot,
                     no_two_in_same_spot, edge_constraints)