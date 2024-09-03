#include <cstddef>

namespace structure {

template <class T>
struct Node {
    Node() = default;
    Node(void*) : left(nullptr),
                  right(nullptr),
                  parent(nullptr) {}
    Node(const T& v, Node* l, Node* r, Node* p)
        : val(v),
          left(l),
          right(r),
          parent(p) {}

    T val;
    Node* left;
    Node* right;
    Node* parent;
};

template <class T>
class BasicBinaryTree {
public:
    using TNode = Node<T>;

    // clang-format off
    using value_type      = T;
    using reference       = T&;
    using const_reference = const T&;
    using pointer         = T*;
    using const_pointer   = const T*;
    using size_type       = std::size_t;
    using difference_type = std::ptrdiff_t;
    // clang-format on

public:
    BasicBinaryTree() = default;
    virtual ~BasicBinaryTree() {
        if (!empty()) cleanup(begin());
    }

    BasicBinaryTree(const BasicBinaryTree& other) = delete;
    BasicBinaryTree(BasicBinaryTree&& other) noexcept = delete;
    BasicBinaryTree& operator=(const BasicBinaryTree& rhs) = delete;
    BasicBinaryTree& operator=(BasicBinaryTree&& rhs) noexcept = delete;

    reference top() noexcept { return root_->val; }
    const_reference top() const noexcept { return root_->val; }

    TNode* begin() noexcept { return root_; }
    const TNode* begin() const noexcept { return root_; }

    size_type size() const noexcept { return size_; }
    bool empty() const noexcept { return size_ == 0; }

protected:
    TNode* makeNode(const_reference x, TNode* parent) {
        TNode* temp = allocNode(x, nullptr, nullptr, parent);
        ++size_;
        return temp;
    }
    void delNode(TNode* a) noexcept {
        delete a;
        --size_;
    }

    TNode* root_ = nullptr;

private:
    size_type size_ = 0;

    TNode* allocNode(const_reference v, TNode* l, TNode* r, TNode* p) {
        return new TNode(v, l, r, p);
    }

    void cleanup(TNode* a) noexcept {
        if (a->left != nullptr) {
            cleanup(a->left);
        }
        if (a->right != nullptr) {
            cleanup(a->right);
        }
        delete a;
    }
};

template <class T>
class BinarySearchTree : public BasicBinaryTree<T> {
public:
    using typename BasicBinaryTree<T>::value_type;
    using typename BasicBinaryTree<T>::const_reference;
    using typename BasicBinaryTree<T>::size_type;
    using typename BasicBinaryTree<T>::TNode;

public:
    BinarySearchTree() = default;

    void insert(const_reference x) {
        insert_impl(this->begin(), x);
    }

    TNode* find(const_reference x) noexcept {
        return find_impl(this->begin(), x);
    }
    const TNode* find(const_reference x) const noexcept {
        return find_impl(this->begin(), x);
    }

private:
    void insert_impl(TNode* a, const_reference x) {
        TNode* prev = a;
        while (a != nullptr) {
            prev = a;
            if (x < a->val) {
                a = a->left;
            }
            else {
                a = a->right;
            }
        }

        TNode* newNode = this->makeNode(x, prev);
        if (this->root_ == nullptr) {
            this->root_ = newNode;
            return;
        }

        if (x < prev->val) {
            prev->left = newNode;
        }
        else {
            prev->right = newNode;
        }
    }

    TNode* find_impl(TNode* a, const_reference x) {
        while (a != nullptr) {
            if (x == a->val) break;
            else if (x < a->val) {
                a = a->left;
            }
            else {
                a = a->right;
            }
        }
        return a;
    }
};

} // namespace structure

#include <iostream>

template <class T>
T min(const T& a, const T& b) {
    return a < b ? a : b;
}

template <class T>
T abs(const T& a) {
    return a < 0 ? -a : a;
}

template <class T>
T getLeastDiff(const structure::BasicBinaryTree<T>& self, const T& x) noexcept {
    auto a = self.begin();
    auto prev = a;
    while (a != nullptr) {
        prev = a;
        if (x == a->val) return 0;
        else if (x < a->val) {
            a = a->left;
        }
        else {
            a = a->right;
        }
    }
    //if (prev == self.begin()) return ::abs<T>(prev->val - x);

    auto itr = prev;
    if (x < prev->val) {
        auto temp = prev;
        while (itr->parent) {
            itr = itr->parent;
            if (itr->left == temp) {
                temp = itr;
                continue;
            }
            break;
        }
    }
    else {
        auto temp = prev;
        while (itr->parent) {
            itr = itr->parent;
            if (itr->right == temp) {
                temp = itr;
                continue;
            }
            break;
        }
    }
    return ::min<T>(::abs<T>(prev->val - x), ::abs<T>(itr->val - x));
}

enum class Types {
    addX = 1,
    smallestDiff = 2
};

int main() {
    int n;
    std::cin >> n;
    structure::BinarySearchTree<long long> tree;
    for (int i = 0; i < n; ++i) {
        int t;
        std::cin >> t;

        switch (t) {
            long long x;
        case static_cast<int>(Types::addX):
            std::cin >> x;
            tree.insert(x);
            break;
        case static_cast<int>(Types::smallestDiff):
            std::cin >> x;
            std::cout << getLeastDiff(tree, x) << '\n';
            break;
        }
    }
    return 0;
}