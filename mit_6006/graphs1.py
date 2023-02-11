
class Graph:
    def __init__(self, ):
        self.adj = {}
    
    def _build(self, nodes, edges, directed=True):
        for i in nodes:
            self.adj[i] = set() 
        
        for u, v in edges:
            self.adj[u].add(v)
            if not directed:
                self.adj[v].add(u)

        return self 
        

    def bfs(self, s):
        queue = [s]
        visited = set()
        parents = {s: s}
        while queue:
            n = queue.pop()
            for v in self.adj[n]:
                if v not in parents: parents[v] = n
                if v not in visited: queue.append(v)
            visited.add(n)
        
        return parents 
    
    def nbr_of(self, s):
        return self.adj[s]

    def dfs(self, s):
        if not self.adj[s]:
            return {}
        return 


    

    def shortest_path(self, u, v, parents=None):
        parents = parents or self._bsf(u)
        if (u not in parents) or (v not in parents):
            return None 
        def flatten(parents, u, v):
            if u == v:
                return (u, )
            return flatten(parents, u, parents[v],) + (v,)
        return flatten(parents, u, v)


    def dfs(graph, s, visited=None, parents=None):
        visited = visited or set()
        parents = parents or {s: s}
        visited.add(s)
        for n in graph.adj[s]:
            if n not in parents: parents[n] = s
        
        for n in graph.adj[s]:
            if n not in visited: dfs(graph, n, visited, parents)
        
        return parents


        



def test_graph():
    import random 
    edge_list = list({(random.randint(0, 6), random.randint(0, 6)) for _ in range(25)})
    edge_list = [(u, v) for u, v in edge_list if u!=v]
    print(sorted(edge_list, key=lambda x: x[0]))
    nodes = list({n for pair in edge_list for n in pair})

    graph = Graph()._build(nodes=nodes, edges=edge_list)
    for i in range(5):
        u, v = random.choices(nodes, k=2)
        if u == v: continue
        parents = graph.bfs(u)
        print('bsf_from', u, parents)
        sp = graph.shortest_path(u, v, parents)
        print('shortest_path:', u, v, sp)
        if sp is not None:
            for u, v in zip(sp[::2], sp[1::2]):
                if (u, v) not in edge_list:
                    print(u, v, 'not in edgelist')

    #TODO: test dfs
    
test_graph()

        

        
            

