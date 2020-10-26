# python3
import itertools
import copy

# Get number of variables, number of edges, edges
def read_input():
    n, m = map(int, input().split())
    edges = [ list(map(int, input().split())) for i in range(m) ]
    return n, m, edges

# Create 3 variables for each vertex (1 for each possible coloring)
def create_variables(n):
    variables = []
    val = 1
    for i in range(n):
        variables.append([])
        for j in range(3):
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

# Add constraints such that vertices with an edge between them can't be the same color
def if_edge_diff_color(edges, variables):
    edge_constraints = []
    for i in range(len(edges)):
        for j in range(3):
            edge_constraints.append([0 - variables[edges[i][0] - 1][j], 
                                    0 - variables[edges[i][1] - 1][j]])
    return edge_constraints

# Print constraints so they can be entered into SAT solver
def Print_Formula(num_var, num_clauses, variables, one_val, edge_constraints):
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
    for clause in edge_constraints:
        s = ""
        for i in range(len(clause)):
            s += str(clause[i]) + " "
        s += "0"
        print(s)

if __name__ == "__main__":
    n, m, edges = read_input()
    variables = create_variables(n)
    one_val = one_val_per_var(variables)
    edge_constraints = if_edge_diff_color(edges, variables)
    num_var = 0
    for i in range(len(variables)):
        for j in range(len(variables[i])):
            num_var += 1
    num_clauses =  len(variables) + len(one_val) + len(edge_constraints)
    Print_Formula(num_var, num_clauses, variables, one_val, edge_constraints)
