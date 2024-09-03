#include <iostream>
#include <string>
#include <string_view>
#include <vector>

class HashSetStr {
public:
    HashSetStr(unsigned bucketSize)
        : bucketSize_(bucketSize),
          table_(new std::vector<std::string>[bucketSize]) {}

    ~HashSetStr() { delete[] table_; }

    void insert(std::string s) {
        const unsigned hash = get_hash(s) % bucketSize_;
        table_[hash].emplace_back(std::move(s));
        ++size_;
    }

    bool find(const std::string& s) {
        const unsigned hash = get_hash(s) % bucketSize_;
        const auto& chain = table_[hash];
        for (auto& a : chain) {
            if (a == s) return true;
        }
        return false;
    }

    static unsigned long long get_hash(const std::string& s) {
        //djb2 hashing alg
        unsigned long long hash = 5381ll;
        for (unsigned c : s) {
            hash = ((hash << 5) + hash) + c; // hash * 33 + c
        }
        return hash;
    }

    unsigned size() const { return size_; }
    unsigned bucket_size() const { return bucketSize_; }

private:
    unsigned size_ = 0;
    unsigned bucketSize_;
    std::vector<std::string>* table_ = nullptr;
};

bool fullyLoops(std::string_view a, const std::string& here) {
    if (here.size() % a.size() != 0) return false;
    for (int i = a.size(); i < here.size(); i += a.size()) {
        const auto slice = std::string_view(here.c_str() + i, a.size());
        if (slice != a) return false;
    }
    return true;
}

int main() {
    constexpr int NUM_OF_INPUTS = 2;

    std::string inp[NUM_OF_INPUTS];
    std::cin >> inp[0] >> inp[1];

    HashSetStr hashTable(inp[0].size());

    for (int i = 1; i <= inp[0].size() / 2; ++i) {
        const auto slice = std::string_view(inp[0].c_str(), i);
        if (fullyLoops(slice, inp[0])) {
            hashTable.insert(std::string(slice));
        }
    }
    hashTable.insert(inp[0]);

    int count = 0;

    for (int i = 1; i <= inp[1].size() / 2; ++i) {
        const auto slice = std::string_view(inp[1].c_str(), i);
        if (fullyLoops(slice, inp[1])) {
            if (hashTable.find(std::string(slice))) ++count;
        }
    }
    if (hashTable.find(inp[1])) ++count;

    std::cout << count;
    return 0;
}