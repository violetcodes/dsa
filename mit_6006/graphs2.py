"""Graphs and common problems
- Graph representation (adj)
- BFS and DFS
- Unweighted Graph
- SSSP
- Connected Components
- DAG (cycle presence)
- Topological sorting
"""


class Graph:
    def __init__(self, is_directed=False):
        self.adj = {}
        self.is_directed = is_directed

    def nodes(self, ):
        yield from self.adj 

    def edges(self, ):
        returned = {}
        for u in self.adj:
            for v in self.adj[u]:
                if self.is_directed:
                    if ((u, v) not in returned) and ((v, u) not in returned):
                        returned.add((u, v))
                        yield u, v
                else:
                    yield u, v

    def add_node(self, node):
        if node not in self.adj: self.adj[node] = {}

    def add_edge(self, edge):
        u, v = edge 
        self.add_node(u)
        self.adj[u][v] = 1
        if not self.is_directed:
            self.add_node(v)
            self.adj[v][u] = 1
    
    def neighbors_of(self, node):
        if node in self.adj: 
            yield from self.adj[node]
        return []
    
    @staticmethod
    def build(edge_list, is_directed=False):
        graph = Graph(is_directed=is_directed)
        for u, v in edge_list:
            graph.add_edge((u, v))
        return graph 

    def _bfs(self, source):
        queue = [source, ]
        parent_pointers = {source: None}
        while queue:
            node = queue.pop(0)
            for ngh in self.neighbors_of(node):
                if ngh not in parent_pointers:
                    queue.append(ngh)
                    parent_pointers[ngh] = node 
        return parent_pointers

    def _dfs(self, source, parent_pointers=None, order=None):
        
        parent_pointers = parent_pointers or {source: None}
        order = order or []  # finishing order
        for ngh in self.neighbors_of(source):
            if ngh not in parent_pointers:
                parent_pointers[ngh] = source
                _, order = self._dfs(ngh, parent_pointers=parent_pointers, order=order)
        order.append(source)
        return parent_pointers, order 


    def full_dfs(self, ):
        parent_pointers = {}
        orders = []
        for node in self.nodes():
            if node not in parent_pointers:
                p_pointers, order = self._dfs(node)
                parent_pointers.update(p_pointers)
                orders.append(order)
        
        return parent_pointers, orders 

    def full_bfs(self, ):
        parent_pointers = {}
        
        for node in self.nodes():
            if node not in parent_pointers:
                p_pointers = self._bfs(node)
                parent_pointers.update(p_pointers)
        return parent_pointers

    def connected_components(self, ):
        parent_pointers = {}
        for node in self.nodes():
            if node not in parent_pointers:
                p_pointers = self._dfs(node)
                parent_pointers.update(p_pointers)
                yield [p for p in p_pointers]

    def is_dag(self, ):
        if not self.is_directed:
            return False 
        full_dfs_paths, _ = self.full_dfs()

        def _ancestors(k, full_dfs_paths):
            anc = []
            while k in full_dfs_paths:
                anc.append(full_dfs_paths[k])
                k = full_dfs_paths[k]
            return anc 
        
        for n in self.nodes():
            anc = _ancestors(n, full_dfs_paths)
            for ngh in self.neighbors_of(n):
                if ngh in anc:
                    return False  # can also return ngh
        
        return True


    def topological_sorting(self, ):
        assert self.is_dag(), "not a dag"
        
        _, order = self.full_dfs()
        for i in range(len(order)):
            order[i] = order[i][::-1]

        return order

def test():

    # # general
    # edge_list = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (6, 3), (6, 4), ]
    # graph = Graph.build(edge_list=edge_list, is_directed=False)
    # print('bfs', graph._bfs(1))
    # print('dfs', graph._dfs(1))

    # # connected components
    # edge_list = [
    #     (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), 
    #     (6, 3), (6, 4), (10, 12), (10, 11), (13, 14), (12, 14)]
    # graph = Graph.build(edge_list=edge_list, is_directed=False)
    # for cc in graph.connected_components():
    #     print('cc:', cc)

    # print("full_dfs:", graph.full_dfs())

    # # topological sorting
    # edge_list = [
    #     (1, 2), (2, 3), (3, 4), (4, 5), (5, 7), (3, 6), (6, 8), (7, 8),
    #     (8, 9), (9, 10) 
    #     ]
    # graph = Graph.build(edge_list=edge_list, is_directed=True)
    # print(graph.topological_sorting())


    pass





if __name__ == '__main__':
    test()




