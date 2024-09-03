#include <iostream>
#include <vector>

using namespace std;

struct graphNode {
    vector <int> next;
    vector <int> weight;

    bool inline empty() const {
        return next.empty();
    }
    void inline new_edge( int& nodeIndex, int& _weight) {
        next.push_back(nodeIndex);
        weight.push_back(_weight);
    }
};


int energy_helper(vector <graphNode> & graph, int& index,int weight = 0) {
    int maximum = 0,t_m;

    if(graph[index].empty())
        return weight;

    for(int i = 0; i<graph[index].next.size();i++){
        if(graph[index].weight[i] == 0)
            if(graph[index].next.size() > 1)
                continue;
            else
                maximum = energy_helper(graph, graph[index].next[i], 0);
        else {
            t_m = energy_helper(graph, graph[index].next[i], graph[index].weight[i]--);
            if (t_m > maximum)
                maximum = t_m;
        }
    }

    return maximum + weight;
}

inline int maximum_energy(vector <graphNode> & graph, int& N, int& papaya){

    return energy_helper(graph,papaya);
}


int main(){
    int N,M,str,dst,wgt;
    cin >> N >> M;
    vector <graphNode> graph(N);
    for (int i = 0; i < M; i++) {
        cin >> str >> dst >> wgt;
        graph[--str].new_edge(--dst,wgt);
    }
    cin >> str;

    cout << maximum_energy(graph,N,--str);

    return 0;
}