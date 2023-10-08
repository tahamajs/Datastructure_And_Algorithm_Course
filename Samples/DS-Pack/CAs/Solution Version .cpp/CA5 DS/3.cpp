#include <iostream>
#include <vector>

class Graph {
public:
    Graph() = default;
    Graph(int verticies)
        : adj(std::vector<std::vector<Edge>>(verticies)),
          verticies_(verticies) {
    }

    struct Edge {
        int to;
        int weight;
    };

    void addVertex() {
        adj.push_back({});
        ++verticies_;
    }
    void addEdge(int src, int dst, int weight = 1) {
        adj[src].push_back({dst, weight});
        ++edges_;
    }

    int verticies() const noexcept { return verticies_; }
    int edges() const noexcept { return edges_; }

    std::vector<std::vector<Edge>> adj;

private:
    int verticies_ = 0;
    int edges_ = 0;
};

void energyLogic(Graph& g,
                 const std::vector<int>& scc,
                 const std::vector<bool>& isInScc,
                 std::vector<long long>& maxEnergy) {
    long long sccEnergy = 0;
    long long maxOuterSccEnergy = 0;

    for (int sccNode : scc) {
        for (auto edge : g.adj[sccNode]) {
            if (isInScc[edge.to]) {
                sccEnergy += (static_cast<long long>(edge.weight) * (edge.weight + 1)) / 2; //1 + 2 + ... + edge.weight
            }
            else {
                maxOuterSccEnergy = std::max(maxOuterSccEnergy, maxEnergy[edge.to] + edge.weight);
            }
        }
    }

    for (int sccNode : scc) {
        maxEnergy[sccNode] = sccEnergy + maxOuterSccEnergy;
    }
}

void SCC(Graph& g, int node, int& time,
         std::vector<int>& discTime,
         std::vector<int>& lowTime,
         std::vector<bool>& isOnStack,
         std::vector<int>& stack,
         std::vector<long long>& maxEnergy) {
    discTime[node] = time;
    lowTime[node] = time;
    ++time;
    stack.push_back(node);
    isOnStack[node] = true;

    for (auto edge : g.adj[node]) {
        const auto neighbour = edge.to;

        if (discTime[neighbour] == -1) { //if not visited
            SCC(g, neighbour, time, discTime, lowTime, isOnStack, stack, maxEnergy);
            lowTime[node] = std::min(lowTime[node], lowTime[neighbour]);
        }
        else if (isOnStack[neighbour]) {
            lowTime[node] = std::min(lowTime[node], discTime[neighbour]);
        }
    }

    if (discTime[node] == lowTime[node]) {
        std::vector<int> scc;
        std::vector<bool> isInScc(g.verticies(), false);
        while (true) {
            const int x = stack.back();
            if (node == x) break;
            scc.push_back(x);
            isOnStack[x] = false;
            stack.pop_back();
            isInScc[x] = true;
        }
        scc.push_back(node);
        isOnStack[node] = false;
        stack.pop_back();
        isInScc[node] = true;

        energyLogic(g, scc, isInScc, maxEnergy);
    }
}

long long getMaxEnergy(Graph& g, int startPos) {
    std::vector<int> lowTime(g.verticies());
    std::vector<int> discoveryTime(g.verticies(), -1);
    std::vector<bool> isOnStack(g.verticies(), false);
    std::vector<int> stack;
    int time = 0;
    std::vector<long long> maxEnergy(g.verticies(), 0);

    SCC(g, startPos, time, discoveryTime, lowTime, isOnStack, stack, maxEnergy);

    return maxEnergy[startPos];
}

int main() {
    int verticies, edges;
    std::cin >> verticies >> edges;
    Graph graph(verticies);
    for (int i = 0; i < edges; ++i) {
        int from, to, weight;
        std::cin >> from >> to >> weight;
        graph.addEdge(--from, --to, weight);
    }
    int startPos;
    std::cin >> startPos;

    std::cout << getMaxEnergy(graph, --startPos);
    return 0;
}
