#include <cstddef>
#include <iostream>
#include <iterator>
#include <type_traits>

namespace structure {

namespace detail {

    template <class MyList>
    struct Node {
        Node() = default;
        Node(const typename MyList::value_type& v, Node* n, Node* p)
            : val(v),
              next(n),
              prev(p) {}
        typename MyList::value_type val;
        Node* next;
        Node* prev;
    };

} // namespace detail

template <class Pointer, class MyList>
class IterBi {
private:
    using iterTraits = std::iterator_traits<Pointer>;
    using node_ptr = typename MyList::node_ptr;

public:
    // clang-format off
    using iterator_category = std::bidirectional_iterator_tag;
    using value_type        = typename iterTraits::value_type;  //T
    using pointer           = typename iterTraits::pointer;     //(const) T*
    using reference         = typename iterTraits::reference;   //(const) T&
    using difference_type   = typename MyList::difference_type; //std::ptrdiff_t
    // clang-format on

    //make const_iterator a friend of iterator
    friend typename std::conditional<std::is_same<IterBi, typename MyList::iterator>::value,
                                     typename MyList::const_iterator, void>::type;

    friend MyList;

private:
    explicit IterBi(node_ptr ptr) noexcept : ptr_(ptr) {}

    node_ptr unwrap() const noexcept { return ptr_; }

public:
    //enable conversion from iterator to const_iterator
    template <class PTR_,
              class = typename std::enable_if<std::is_same<PTR_, typename MyList::pointer>::value>::type>
    IterBi(const IterBi<PTR_, MyList>& i) noexcept
        : IterBi(static_cast<node_ptr>(i.ptr_)) {}

    //forward_iterator_tag
    friend bool operator==(const IterBi& lhs, const IterBi& rhs) noexcept { return lhs.ptr_ == rhs.ptr_; }
    friend bool operator!=(const IterBi& lhs, const IterBi& rhs) noexcept { return !(lhs == rhs); }

    reference operator*() const noexcept { return ptr_->val; }
    pointer operator->() const noexcept { return std::addressof(ptr_->val); }

    IterBi& operator++() noexcept {
        ptr_ = ptr_->next;
        return *this;
    }
    IterBi operator++(int) noexcept {
        IterBi temp(*this);
        ++(*this);
        return temp;
    }

    //bidirectional_iterator_tag
    IterBi& operator--() noexcept {
        ptr_ = ptr_->prev;
        return *this;
    }
    IterBi operator--(int) noexcept {
        IterBi temp(*this);
        --(*this);
        return temp;
    }

private:
    node_ptr ptr_;
};

template <class T>
class LinkedListCircular {
private:
#define HEAD_ADRS std::addressof(head_)
    using Node = detail::Node<LinkedListCircular>;
    using node_ptr = Node*;

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

    using iterator = IterBi<pointer, LinkedListCircular>;
    using const_iterator = IterBi<const_pointer, LinkedListCircular>;
    friend iterator;
    friend const_iterator;

    LinkedListCircular() { ctor_impl(); }
    ~LinkedListCircular() { dtor_impl(); }
    LinkedListCircular(const LinkedListCircular& other) = delete;
    LinkedListCircular(LinkedListCircular&& other) noexcept = delete;
    LinkedListCircular& operator=(const LinkedListCircular& rhs) = delete;
    LinkedListCircular& operator=(LinkedListCircular&& rhs) noexcept = delete;

    void push_back(const_reference x) {
        insert(end(), x);
    }
    void push_front(const_reference x) {
        insert(begin(), x);
    }
    void pop_back() noexcept {
        erase(--end());
    }
    void pop_front() noexcept {
        erase(begin());
    }

    iterator insert(const_iterator pos, const_reference x) {
        node_ptr posPtr = pos.unwrap();
        node_ptr newNode;

        if (posPtr == HEAD_ADRS) { //pos == end()
            newNode = new Node(x, posPtr->next, posPtr->prev);
            if (empty()) {
                newNode->next = newNode;
                newNode->prev = newNode;
                head_.next = newNode;
            }
            else {
                head_.prev->next = newNode;
                head_.next->prev = newNode;
            }
            head_.prev = newNode;
        }
        else {
            newNode = new Node(x, posPtr, posPtr->prev);
            posPtr->prev->next = newNode;
            posPtr->prev = newNode;
            if (posPtr == head_.next) { //pos == begin()
                head_.next = newNode;
            }
        }

        ++size_;
        return iterator(newNode);
    }
    iterator insert(const_iterator pos, size_type n, const_reference x) {
        iterator prePos(pos.unwrap());
        --prePos;
        for (; n > 0; --n) insert(pos, x);
        return ++prePos;
    }

    iterator erase(const_iterator pos) noexcept {
        node_ptr posPtr = pos.unwrap();
        iterator temp(posPtr->next);

        posPtr->prev->next = posPtr->next;
        posPtr->next->prev = posPtr->prev;

        if (posPtr == head_.next) { //pos == begin()
            if (size_ == 1) {
                ctor_impl();
            }
            else head_.next = posPtr->next;
        }

        delete posPtr;
        --size_;
        return empty() ? end() : temp;
    }
    iterator erase(const_iterator first, const_iterator last) noexcept {
        while (first != last) first = erase(first);
        return iterator(last.unwrap());
    }

    void clear() noexcept {
        dtor_impl();
        ctor_impl();
    }

    size_type size() const noexcept { return size_; }
    size_type empty() const noexcept { return size_ == 0; }

    // clang-format off
    iterator       begin()        noexcept { return iterator(head_.next); }
    iterator       end()          noexcept { return iterator(HEAD_ADRS); }
    const_iterator begin()  const noexcept { return const_iterator(head_.next); }
    const_iterator end()    const noexcept { return const_iterator(const_cast<node_ptr>(HEAD_ADRS)); }
    const_iterator cbegin() const noexcept { return begin(); }
    const_iterator cend()   const noexcept { return end(); }

    reference       front()       noexcept { return *begin(); }
    reference       back()        noexcept { return *(--end()); }
    const_reference front() const noexcept { return *begin(); }
    const_reference back()  const noexcept { return *(--end()); }
    // clang-format on

    void reverse() noexcept {
        node_ptr p = HEAD_ADRS;
        do {
            node_ptr const temp(p->next);
            p->next = p->prev;
            p->prev = temp;
            p = temp;
        } while (p != HEAD_ADRS);
    }

    friend std::ostream& operator<<(std::ostream& os, const LinkedListCircular& list) noexcept {
        os << '[';
        if (!list.empty()) {
            for (const_iterator itr = list.begin();;) {
                os << *itr;
                if (++itr == list.begin()) break;
                os << ", ";
            }
        }
        return os << ']';
    }

private:
    //head_.next/prev is the first/last element
    Node head_;
    size_type size_ = 0;

    void ctor_impl() noexcept {
        head_.next = HEAD_ADRS;
        head_.prev = HEAD_ADRS;
    }
    void dtor_impl() noexcept {
        node_ptr p = head_.next;
        if (p == HEAD_ADRS) return;
        do {
            node_ptr const temp(p);
            p = p->next;
            delete temp;
        } while (p != head_.next);
    }
};

} // namespace structure

#include <string>

const char* NAMES[] = {"Dire", "Radiant"};
enum Teams {
    dire = 0,
    radient,
};

char solve(structure::LinkedListCircular<char>& circle) {
    auto curr = circle.begin();
    while (true) {
        char turn = *curr;
        auto itr = curr;
        do {
            ++itr;
        } while (*itr == turn && itr != curr);
        if (itr == curr) return turn;
        circle.erase(itr);
        ++curr;
    }
    return '\0';
}

int main() {
    std::string input;
    std::cin >> input;

    structure::LinkedListCircular<char> circle;
    for (char c : input) {
        circle.push_back(c);
    }

    char winner = solve(circle);

    switch (winner) {
    case 'D':
        std::cout << NAMES[Teams::dire];
        break;
    case 'R':
        std::cout << NAMES[Teams::radient];
        break;
    }

    return 0;
}