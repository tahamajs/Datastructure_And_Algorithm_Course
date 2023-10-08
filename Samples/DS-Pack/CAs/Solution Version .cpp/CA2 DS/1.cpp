#include <cstddef>
#include <iostream>
#include <string>
#include <iterator>
#include <type_traits>

template <class T>
void swap(T& a, T& b) {
    T temp(a);
    a = b;
    b = temp;
}

namespace structure {

template <class T>
class Array2D {
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

    explicit Array2D(size_type n)
        : arr_(new value_type[n * n]()),
          size_(n) {};
    ~Array2D() {
        delete[] arr_;
    }
    Array2D(const Array2D& other)
        : Array2D(other.size_) {
        for (int i = 0; i < size_; ++i) {
            arr_[i] = other.arr_[i];
        }
    }
    Array2D(Array2D&& other) noexcept {
        swap(*this, other);
    }
    Array2D& operator=(const Array2D& rhs) {
        Array2D temp(rhs);
        swap(*this, temp);
        return *this;
    }
    Array2D& operator=(Array2D&& rhs) noexcept {
        swap(*this, rhs);
        return *this;
    }

    friend void swap(Array2D& a, Array2D& b) noexcept {
        swap(a.arr_, b.arr_);
        swap(a.size_, b.size_);
    }

    size_type size() const noexcept { return size_; };

    // clang-format off
    reference       operator()(size_type a, size_type b)       noexcept { return arr_[a * size_ + b]; }
    const_reference operator()(size_type a, size_type b) const noexcept { return arr_[a * size_ + b]; }
    reference       operator[](size_type i)       noexcept { return arr_[i]; }
    const_reference operator[](size_type i) const noexcept { return arr_[i]; }
    // clang-format on

private:
    pointer arr_ = nullptr;
    size_type size_;
};

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
template <class T, class U>
std::ostream& operator<<(std::ostream& os, const Pair<T, U>& p) {
    return os << '(' << p.first << ", " << p.second << ')';
}

}; // namespace structure

using namespace structure;

constexpr int DIRECTIONS = 8;
const Pair<int, int> offset[DIRECTIONS] {
    {0, 1},
    {1, 1},
    {1, 0},
    {1, -1},
    {0, -1},
    {-1, -1},
    {-1, 0},
    {-1, 1},
};

bool isValidSpot(const Array2D<char>& map, char letter, const Array2D<bool>& passed, int row, int col) {
    //bounds check
    if (col >= map.size() ||
        row >= map.size()) return false;

    //letter check
    if (map(row, col) != letter) return false;

    //already passed check
    if (passed(row, col)) return false;
    return true;
}

void solve(const Array2D<char>& map, const std::string& word, Array2D<bool>& passed, Array<Pair<int, int>>& road, int row, int col, int letter = 0) {
    if (!isValidSpot(map, word[letter], passed, row, col)) return;
    if (++letter == word.size()) {
        for (const auto& rc : road) {
            std::cout << rc << ',';
        }
        std::cout << Pair<int, int>{row, col} << '\n';
        return;
    }

    road.push_back({row, col});
    passed(row, col) = true;

    for (int i = 0; i < DIRECTIONS; ++i) {
        solve(map, word, passed, road,
              row + offset[i].first,
              col + offset[i].second,
              letter);
    }

    road.pop_back();
    passed(row, col) = false;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::string word;
    std::cin >> n;
    std::cin.ignore();
    std::cin >> word;

    Array2D<char> map(n);
    for (int i = 0; i < n * n; ++i) {
        char a;
        std::cin >> a;
        std::cin.ignore();
        map[i] = a;
    }

    Array2D<bool> passed(n);
    Array<Pair<int, int>> road(word.size());
    for (int row = 0; row < map.size(); ++row) {
        for (int col = 0; col < map.size(); ++col) {
            if (map(row, col) != word[0]) continue;
            solve(map, word, passed, road, row, col);
        }
    }

    return 0;
}