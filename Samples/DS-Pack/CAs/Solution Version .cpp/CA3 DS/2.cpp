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
        setMinMax();
    }

    TNode* find(const_reference x) noexcept {
        return find_impl(this->begin(), x);
    }
    const TNode* find(const_reference x) const noexcept {
        return find_impl(this->begin(), x);
    }

    TNode* getMin() noexcept { return min_; }
    const TNode* getMin() const noexcept { return min_; }
    TNode* getMax() noexcept { return max_; }
    const TNode* getMax() const noexcept { return max_; }

    void delMin() noexcept {
        TNode* temp(min_);
        if (min_->right != nullptr) {
            min_ = min_->right;
            while (min_->left) {
                min_ = min_->left;
            }
        }
        else {
            min_ = min_->parent;
        }
        if (temp == this->root_) {
            this->root_ = temp->right;
            if (temp->right != nullptr) {
                this->root_->parent = nullptr;
            }
            else {
                max_ = nullptr;
            }
        }
        else {
            temp->parent->left = temp->right;
            if (temp->right != nullptr) {
                temp->right->parent = temp->parent;
            }
        }
        this->delNode(temp);
    }
    void delMax() noexcept {
        TNode* temp(max_);
        if (max_->left != nullptr) {
            max_ = max_->left;
            while (max_->right) {
                max_ = max_->right;
            }
        }
        else {
            max_ = max_->parent;
        }
        if (temp == this->root_) {
            this->root_ = temp->left;
            if (temp->left != nullptr) {
                this->root_->parent = nullptr;
            }
            else {
                min_ = nullptr;
            }
        }
        else {
            temp->parent->right = temp->left;
            if (temp->left != nullptr) {
                temp->left->parent = temp->parent;
            }
        }
        this->delNode(temp);
    }

private:
    TNode* min_ = nullptr;
    TNode* max_ = nullptr;

    void insert_impl(TNode* a, const_reference x) {
        TNode* prev = a;
        while (a != nullptr) {
            prev = a;
            if (x <= a->val) {
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

    void setMinMax() {
        if (min_ == nullptr || max_ == nullptr) {
            min_ = this->root_;
            max_ = min_;
        }
        else if (min_->left != nullptr) {
            min_ = min_->left;
        }
        else if (max_->right != nullptr) {
            max_ = max_->right;
        }
    }
};

} // namespace structure

#include <iostream>

enum class Types {
    getPaper = 1,
    printSmallest = 2,
    printBiggest = 3
};

int main() {
    int n;
    std::cin >> n;
    structure::BinarySearchTree<int> tree;
    for (int i = 0; i < n; ++i) {
        int t;
        std::cin >> t;

        switch (t) {
        case static_cast<int>(Types::getPaper):
            int x;
            std::cin >> x;
            tree.insert(x);
            break;
        case static_cast<int>(Types::printSmallest):
            std::cout << tree.getMin()->val << '\n';
            tree.delMin();
            break;
        case static_cast<int>(Types::printBiggest):
            std::cout << tree.getMax()->val << '\n';
            tree.delMax();
            break;
        }
    }
    return 0;
}