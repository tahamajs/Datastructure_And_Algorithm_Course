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
class LinkedList {
private:
#define HEAD_ADRS std::addressof(head_)
    using Node = detail::Node<LinkedList>;
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

    using iterator = IterBi<pointer, LinkedList>;
    using const_iterator = IterBi<const_pointer, LinkedList>;
    friend iterator;
    friend const_iterator;

    LinkedList() { ctor_impl(); }
    ~LinkedList() { dtor_impl(); }
    LinkedList(const LinkedList& other) = delete;
    LinkedList(LinkedList&& other) noexcept = delete;
    LinkedList& operator=(const LinkedList& rhs) = delete;
    LinkedList& operator=(LinkedList&& rhs) noexcept = delete;

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
        node_ptr newNode = new Node(x, posPtr, posPtr->prev);

        posPtr->prev->next = newNode;
        posPtr->prev = newNode;
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

        delete posPtr;
        --size_;
        return temp;
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

    friend std::ostream& operator<<(std::ostream& os, const LinkedList& list) noexcept {
        os << '[';
        if (!list.empty()) {
            for (const_iterator itr = list.begin();;) {
                os << *itr;
                if (++itr == list.end()) break;
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
        for (node_ptr p = head_.next; p != HEAD_ADRS;) {
            node_ptr const temp(p);
            p = p->next;
            delete temp;
        }
    }
};

} // namespace structure

#include <string>

int main() {
    std::string input;
    std::cin >> input;

    structure::LinkedList<char> stack;
    stack.push_back(input[0]);
    for (int i = 1; i < input.size(); ++i) {
        if (stack.back() == input[i]) {
            stack.pop_back();
        }
        else stack.push_back(input[i]);
    }

    for(const auto& c : stack) {
        std::cout << c;
    }

    return 0;
}