#include <iostream>
#include <queue>
#include <vector>

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

    explicit Array2D(size_type row, size_type col)
        : arr_(new value_type[row * col]()),
          row_(row),
          col_(col) {};
    ~Array2D() {
        delete[] arr_;
    }

    Array2D(const Array2D& other)
        : Array2D(other.row_, other.col_) {
        std::copy(other.arr_, other.arr_ + other.size(), arr_);
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

    size_type rows() const noexcept { return row_; }
    size_type cols() const noexcept { return col_; }
    size_type size() const noexcept { return row_ * col_; }

    // clang-format off
    pointer         operator[](size_type i)       noexcept { return arr_ + i * col_; }
    const_pointer   operator[](size_type i) const noexcept { return arr_ + i * col_; }
    // clang-format on

private:
    pointer arr_ = nullptr;
    size_type row_;
    size_type col_;
};

} // namespace structure

template <class BiIter, class Pred>
void insertionSort(BiIter first, BiIter last, Pred compare) {
    if (first == last) return;
    BiIter i = first;
    for (++i; i != last; ++i) {
        auto key(std::move(*i));
        BiIter insertPos = i;

        for (BiIter movePos = i;
             movePos != first && compare(key, *(--movePos));
             --insertPos) {
            *insertPos = std::move(*movePos);
        }

        *insertPos = std::move(key);
    }
}

constexpr int DIRECTIONS = 4;
const std::pair<int, int> offset[DIRECTIONS] {
    {-1, 0},
    {0, +1},
    {+1, 0},
    {0, -1},
};

bool isValidSpot(const structure::Array2D<bool>& arr, int row, int col) {
    if (col < 0 || row < 0) return false;
    if (col >= arr.cols() || row >= arr.rows()) return false;
    return true;
}

int bfs(const structure::Array2D<bool>& arr, structure::Array2D<bool>& visited, int row, int col) {
    if (!arr[row][col]) return 0;
    if (visited[row][col]) return 0;

    std::queue<std::pair<int, int>> queue;
    visited[row][col] = true;
    queue.push({row, col});

    int spots = 1;
    while (!queue.empty()) {
        auto curr = queue.front();
        queue.pop();

        for (int i = 0; i < DIRECTIONS; ++i) {
            const auto r = curr.first + offset[i].first;
            const auto c = curr.second + offset[i].second;

            if (!isValidSpot(arr, r, c)) continue;
            if (!arr[r][c]) continue;
            if (visited[r][c]) continue;

            visited[r][c] = true;
            queue.push({r, c});
            ++spots;
        }
    }

    return spots;
}

int solve(const structure::Array2D<bool>& arr, int k) {
    std::vector<int> lengths;
    lengths.reserve(arr.size());

    structure::Array2D<bool> visited(arr.rows(), arr.cols());
    for (int row = 0; row < arr.rows(); ++row) {
        for (int col = 0; col < arr.cols(); ++col) {
            lengths.emplace_back(bfs(arr, visited, row, col));
        }
    }

    insertionSort(lengths.begin(), lengths.end(), std::greater{});
    int ans = 0;
    for (int i = 0; i < lengths.size() && k > 0; ++i) {
        ans += lengths[i];
        --k;
    }
    return ans;
}

int main() {
    int n, m, k;
    std::cin >> n >> m >> k;
    structure::Array2D<bool> arr(n, m);
    for (int i = 0; i < arr.rows(); ++i) {
        std::cin.get();
        for (int j = 0; j < arr.cols(); ++j) {
            arr[i][j] = std::cin.get() - '0';
        }
    }

    std::cout << solve(arr, k);
    return 0;
}