#include <forward_list>
#include <iostream>
#include <queue>
#include <vector>

namespace structure {

template <class T>
class Graph {
public:
    // clang-format off
    using value_type      = T;
    using reference       = T&;
    using const_reference = const T&;
    using pointer         = T*;
    using const_pointer   = const T*;
    using size_type       = std::size_t;
    using difference_type = std::ptrdiff_t;
    // clang-format on

    Graph() = default;
    ~Graph() {
        for (int i = 0; i < elems.size(); ++i) delete elems[i].first;
    }
    Graph(const Graph& other) = delete;
    Graph(Graph&& other) noexcept = delete;
    Graph& operator=(const Graph& rhs) = delete;
    Graph& operator=(Graph&& rhs) noexcept = delete;

    void addVertex(const_reference x) {
        elems.push_back({new T(x), {}});
    }

    void addEdge(size_type src, size_type dst) {
        elems[src].second.push_front(dst);
    }

    size_type size() const noexcept { return elems.size(); }

    std::vector<std::pair<pointer, std::forward_list<size_type>>> elems;
};

} // namespace structure

enum class Team {
    A,
    B,
    None
};

Team operator!(const Team a) {
    if (a == Team::A) return Team::B;
    else if (a == Team::B) return Team::A;
    else return a;
}

struct Person {
    Person(int id_) : id(id_) {}
    int id;
    Team team = Team::None;
};

bool solve_BFS(structure::Graph<Person>& graph, int startLoc) {
    if (graph.elems[startLoc].first->team != Team::None) return true;

    graph.elems[startLoc].first->team = Team::A;
    std::queue<int> queue;
    queue.push(startLoc);

    while (!queue.empty()) {
        auto curr = queue.front();
        queue.pop();

        for (auto adj : graph.elems[curr].second) {
            if (graph.elems[curr].first->team == graph.elems[adj].first->team) return false;
            if (graph.elems[adj].first->team == Team::None) {
                graph.elems[adj].first->team = !graph.elems[curr].first->team;
                queue.push(adj);
            }
        }
    }

    return true;
}

bool solve(structure::Graph<Person>& graph) {
    for (int i = 0; i < graph.size(); ++i) {
        if (!solve_BFS(graph, i)) return false;
    }
    return true;
}

int main() {
    int n, m;
    std::cin >> n >> m;

    structure::Graph<Person> graph;
    for (int i = 0; i < n; ++i) {
        graph.addVertex(Person(i));
    }
    for (int i = 0; i < m; ++i) {
        int a, b;
        std::cin >> a >> b;
        graph.addEdge(a - 1, b - 1);
        graph.addEdge(b - 1, a - 1);
    }

    if (solve(graph)) {
        std::cout << "Yes" << '\n';
        for (auto& x : graph.elems) std::cout << ((x.first->team == Team::A) ? 0 : 1) << ' ';
    }
    else std::cout << "No";

    return 0;
}