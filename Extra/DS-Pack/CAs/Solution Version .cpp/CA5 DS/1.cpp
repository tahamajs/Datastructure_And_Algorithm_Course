#include <iostream>
#include <string>
#include <string_view>
#include <vector>

void intersection(std::vector<int>& result, const std::vector<int>& a, const std::vector<int>& b) {
    int aItr = 0, bItr = 0;
    while (aItr < a.size() && bItr < b.size()) {
        if (a[aItr] < b[bItr])
            ++aItr;
        else if (b[bItr] < a[aItr])
            ++bItr;
        else {
            result.push_back(b[bItr]);
            ++aItr;
            ++bItr;
        }
    }
}

bool fullyLoops(std::string_view a, const std::string& here) {
    if (here.size() % a.size() != 0) return false;
    for (int i = a.size(); i < here.size(); i += a.size()) {
        if (a != std::string_view(here.c_str() + i, a.size())) return false;
    }
    return true;
}

int main() {
    constexpr int NUM_OF_INPUTS = 2;

    std::string inp[NUM_OF_INPUTS];
    std::cin >> inp[0] >> inp[1];

    std::vector<int> loops[NUM_OF_INPUTS];
    for (int inputNum = 0; inputNum < 2; ++inputNum) {
        for (int i = 1; i <= inp[inputNum].size(); ++i) {
            if (fullyLoops(std::string_view(inp[inputNum].c_str(), i), inp[inputNum])) {
                loops[inputNum].push_back(i);
            }
        }
    }

    int count = 0;

    std::vector<int> intersect;
    intersection(intersect, loops[0], loops[1]);

    for (int i = 0; i < intersect.size(); ++i) {
        const auto a = std::string_view(inp[0].c_str(), intersect[i]);
        const auto b = std::string_view(inp[1].c_str(), intersect[i]);
        if (a == b) ++count;
    }

    std::cout << count;
    return 0;
}