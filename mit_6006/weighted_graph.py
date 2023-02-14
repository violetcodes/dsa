from graphs2 import Graph

class WeightedGraph(Graph):
    def add_edge(self, edge):
        u, v, w = edge 
        super().add_edge((u, v))
        self.adj[u][v] = w 
        if not self.is_directed:
            self.adj[v][u] = w 
    
    def _sssp_dist(graph, source):  # only in case of DAGs
        dist = {n: float('inf') for n in graph.nodes()}
        dist[source] = 0 
        topo_sort = graph.topological_sorting()
        for ts_list in topo_sort:
            if source not in ts_list: continue
            for ts in ts_list:
                for ngh in graph.neighbors_of(ts):
                    dist[ngh] = min(dist[ngh], dist[ts] + graph.adj[ts][ngh])
        return dist
    
    def _path(graph, sn, en, dist):
        parents = {n: None for n in dist}
        for u in dist:
            for v in graph.adj[u]:
                if v not in parents: continue
                if (parents[v] is None) and (dist[v] == dist[u] + graph.adj[u][v]):
                    parents[v] = u

        path = []
        while en != sn:
            if en not in parents:
                return []
            path.append(en)
            en = parents[en]
        path.append(sn)
        return path 


def bellman_ford_sssp(graph, source):
    n = len(list(graph.nodes()))
    
    dist = {node: [float('inf') for _ in range(n+1)] for node in graph.nodes()}
    dist[source] = [0] * (n + 1)

    for step in range(1, n+1):
        for u in graph.nodes():
            for v in graph.neighbors_of(u):
                dist[v][step] = min(
                    dist[u][step-1] + graph.adj[u][v], 
                    dist[v][step], dist[v][step-1]
                )
        if step == n: # remove nodes reachable from -ve sum cycle
            for u in graph.nodes():
                if dist[u][step] < dist[u][step-1]:
                    reachable_nodes, _ = [node for node in graph._dfs(u)]
                    # print(reachable_nodes)
                    for r in reachable_nodes:
                        dist[r][-1] = None # -float('inf')
                    break 
                    


    return {node: d[-1] for node, d in dist.items() if d[-1] is not None}




def dijkstra_sssp(graph, source):
    """Idea: at each node while doing bfs do it in nearest to furthest order among their neighbors"""
    """Only good for non negative edges - monotonically increasing distances"""

    dist = {source: 0}
    queue = {source, }
    
    while queue:
        q = min(queue, key=lambda x: dist.get(x, 2**32))
        queue.remove(q)
        for u in graph.neighbors_of(q):
            if u not in dist: queue.add(u)
            dist[u] = min(dist.get(u, 2*32), dist[q] + graph.adj[q][u])
        
    return dist 

def johnson_apsp(graph):
    """For all pair shortest path, just run V times sssp?, johnson makes it little
    faster with use of potential functions to make graph non-negative"""
    pass 



def test():
    # edge_list = [
    #     (1, 2, 3),
    #     (1, 3, 1),
    #     (2, 4, 4),
    #     (3, 5, 1),
    #     (5, 4, 1),
    #     (4, 6, 2),
    #     (4, 7, 3)
    # ]
    # wgraph = WeightedGraph.build(edge_list, is_directed=True)
    # dist = wgraph._sssp_dist(1)
    # print('shortest path', wgraph._path(1, 7, dist))

    # # bellman-ford test
    # edge_list = [
    #     (1, 3, 5),
    #     (1, 2, 3),
    #     (2, 4, 4),
    #     (3, 4, -2),
    #     (4, 6, 1),
    #     (3, 5, -3),
    #     (6, 5, -3)
    # ]
    # wgraph = WeightedGraph.build(edge_list, is_directed=True)
    # dist = bellman_ford_sssp(wgraph, 1)
    # print(dist)
    # path = wgraph._path(1, 5, dist)
    # print(path)

    # # bellman ford with cycle
    # edge_list = [
    #     (1, 3, 5),
    #     (1, 2, 3),
    #     (2, 4, 4),
    #     (3, 4, -2),
    #     (4, 6, 1),
    #     (3, 5, -3),
    #     (5, 6, 6),
    #     (2, 7, 2),
    #     (7, 6, -3),
    #     (6, 3, -1)
    # ]
    # wgraph = WeightedGraph.build(edge_list, is_directed=True)
    # dist = bellman_ford_sssp(wgraph, 1)
    # print(dist)
    # path = wgraph._path(1, 7, dist)
    # print(path)

    # # dijkstra 
    edge_list = [
        (1, 3, 6),
        (1, 2, 2),
        (2, 4, 1),
        (3, 4, 2),
        (4, 6, 1),
        (3, 5, 1),
        (5, 6, 1),
        (6, 3, 1)
    ]
    wgraph = WeightedGraph.build(edge_list, is_directed=True)
    dist = dijkstra_sssp(wgraph, 1)
    print(dist)
    path = wgraph._path(1, 5, dist)
    print(path)

    pass 
    

if __name__ == '__main__':
    test()
