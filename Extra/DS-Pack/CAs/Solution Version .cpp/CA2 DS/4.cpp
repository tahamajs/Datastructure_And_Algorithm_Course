#include <cstddef>
#include <iostream>
#include <iterator>
#include <type_traits>

namespace structure {

template <class Pointer, class MyArr>
class Iter {
private:
    using iterTraits = std::iterator_traits<Pointer>;

public:
    // clang-format off
    using iterator_category = std::random_access_iterator_tag;
    using value_type        = typename iterTraits::value_type; //T
    using pointer           = typename iterTraits::pointer;    //(const) T*
    using reference         = typename iterTraits::reference;  //(const) T&
    using difference_type   = typename MyArr::difference_type; //std::ptrdiff_t
    // clang-format on

    //make const_iterator a friend of iterator
    friend typename std::conditional<std::is_same<Iter, typename MyArr::iterator>::value,
                                     typename MyArr::const_iterator, void>::type;

    friend MyArr;

private:
    explicit Iter(pointer ptr) noexcept : ptr_(ptr) {}

public:
    //enable conversion from iterator to const_iterator
    template <class PTR_,
              class = typename std::enable_if<std::is_same<PTR_, typename MyArr::pointer>::value>::type>
    Iter(const Iter<PTR_, MyArr>& i) noexcept
        : Iter(static_cast<pointer>(i.ptr_)) {}

    //forward_iterator_tag
    friend bool operator==(const Iter& lhs, const Iter& rhs) noexcept { return lhs.ptr_ == rhs.ptr_; }
    friend bool operator!=(const Iter& lhs, const Iter& rhs) noexcept { return !(lhs == rhs); }

    reference operator*() const noexcept { return *ptr_; }
    pointer operator->() const noexcept { return ptr_; }

    Iter& operator++() noexcept {
        ptr_++;
        return *this;
    }
    Iter operator++(int) noexcept {
        Iter temp(*this);
        ++(*this);
        return temp;
    }

    //bidirectional_iterator_tag
    Iter& operator--() noexcept {
        ptr_--;
        return *this;
    }
    Iter operator--(int) noexcept {
        Iter temp(*this);
        --(*this);
        return temp;
    }

    //random_access_iterator_tag
    reference operator[](difference_type n) const noexcept { return ptr_[n]; }

    Iter& operator+=(difference_type rhs) noexcept {
        ptr_ += rhs;
        return *this;
    }
    friend Iter operator+(Iter lhs, difference_type rhs) noexcept { return lhs += rhs; }
    friend Iter operator+(difference_type lhs, Iter rhs) noexcept { return rhs += lhs; }

    Iter& operator-=(difference_type rhs) noexcept {
        ptr_ -= rhs;
        return *this;
    }
    friend difference_type operator-(Iter lhs, Iter rhs) noexcept { return lhs.ptr_ - rhs.ptr_; }
    friend Iter operator-(Iter lhs, difference_type rhs) noexcept { return lhs -= rhs; }

    friend bool operator<(const Iter& lhs, const Iter& rhs) noexcept { return lhs.ptr_ < rhs.ptr_; }
    friend bool operator>(const Iter& lhs, const Iter& rhs) noexcept { return rhs < lhs; }
    friend bool operator<=(const Iter& lhs, const Iter& rhs) noexcept { return !(rhs < lhs); }
    friend bool operator>=(const Iter& lhs, const Iter& rhs) noexcept { return !(lhs < rhs); }

private:
    pointer ptr_;
};

template <class T>
class Array {
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

    using iterator = Iter<pointer, Array>;
    using const_iterator = Iter<const_pointer, Array>;

    explicit Array(size_type capacity)
        : arr_(new value_type[capacity]()),
          capacity_(capacity) {};
    ~Array() {
        delete[] arr_;
    }
    Array(const Array& other)
        : Array(other.capacity_) {
        for (int i = 0; i < size_; ++i) {
            arr_[i] = other.arr_[i];
        }
    }
    Array(Array&& other) noexcept {
        swap(*this, other);
    }
    Array& operator=(const Array& rhs) {
        Array temp(rhs);
        swap(*this, temp);
        return *this;
    }
    Array& operator=(Array&& rhs) noexcept {
        swap(*this, rhs);
        return *this;
    }

    friend void swap(Array& a, Array& b) noexcept {
        using std::swap;
        swap(a.arr_, b.arr_);
        swap(a.capacity_, b.capacity_);
        swap(a.size_, b.size_);
    }

    void push_back(const_reference x) {
        arr_[size_] = x;
        ++size_;
    }
    void pop_back() {
        --size_;
    }

    size_type size() const noexcept { return size_; };
    size_type capacity() const noexcept { return capacity_; };
    bool empty() const noexcept { return size_ == 0; }

    // clang-format off
    reference       operator[](size_type i)       noexcept { return arr_[i]; }
    const_reference operator[](size_type i) const noexcept { return arr_[i]; }

    iterator       begin()        noexcept { return iterator(&arr_[0]); }
    iterator       end()          noexcept { return iterator(&arr_[size_]); }
    const_iterator begin()  const noexcept { return const_iterator(&arr_[0]); }
    const_iterator end()    const noexcept { return const_iterator(&arr_[size_]); }
    const_iterator cbegin() const noexcept { return begin(); }
    const_iterator cend()   const noexcept { return end(); }
    // clang-format on

private:
    pointer arr_ = nullptr;
    size_type capacity_;
    size_type size_ = 0;
};

template <class T, class U>
struct Pair {
    T first;
    U second;
};

} // namespace structure

using namespace structure;

constexpr std::size_t MAX = 10000;

template <class T, class Iterator>
Iterator find(Iterator first, Iterator last, const T& val) {
    for (; first != last; ++first) {
        if (*first == val) return first;
    }
    return last;
}

template <typename Iterator, class Pred>
void insertionSort(Iterator first, Iterator last, Pred pred) {
    if (first == last) return;

    for (auto i = first + 1; i != last; ++i) {
        auto key = *i;
        auto j = i - 1;
        while (j >= first && pred(key, *j)) {
            *(j + 1) = *j;
            --j;
        }
        *(j + 1) = key;
    }
}

void zip(const Array<int>& arr, const Array<int>& arr2, Array<Pair<int, int>>& dest) {
    for (int i = 0; i < arr2.size(); ++i) {
        dest.push_back({arr[i], arr2[i]});
    }
}

int countGroups(const Array<int>& all, const Array<int>& wanted) {
    int count = 0;
    for (int i = 0, j = 0; i < all.size() && j < wanted.size(); ++i) {
        if (all[i] != wanted[j]) continue;
        do {
            ++i;
            ++j;
        } while (j < wanted.size() && i < all.size() && all[i] == wanted[j]);
        --i;
        ++count;
    }
    return count;
}

void sort(const Array<int>& ref, Array<int>& arr) {
    Array<int> indices(arr.size());
    for (int i = 0; i < arr.size(); ++i) {
        auto x = find(ref.begin(), ref.end(), arr[i]);
        indices[i] = x - ref.begin();
    }

    Array<Pair<int, int>> zipped(arr.size());
    zip(indices, arr, zipped);

    insertionSort(zipped.begin(), zipped.end(), [](const auto& lhs, const auto& rhs) {
        return lhs.first < rhs.first;
    });

    for (int i = 0; i < zipped.size(); ++i) {
        arr[i] = zipped[i].second;
    }
}

void splitLine(std::istream& is, Array<int>& dest, char delim = ',') {
    while (true) {
        int t;
        char c = '\0';
        is >> t >> c;
        dest.push_back(t);
        if (c != delim) break;
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    Array<int> all(MAX);
    Array<int> wanted(MAX);

    std::cin >> std::noskipws;
    splitLine(std::cin, all);
    splitLine(std::cin, wanted);

    sort(all, wanted);

    std::cout << countGroups(all, wanted);

    return 0;
}