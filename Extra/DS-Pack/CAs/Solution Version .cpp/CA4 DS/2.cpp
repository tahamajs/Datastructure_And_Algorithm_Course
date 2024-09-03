#include <iostream>
#include <queue>

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

constexpr int DIRECTIONS = 8;
const std::pair<int, int> offset[DIRECTIONS] {
    {-1, 0},
    {-1, 1},
    {0, 1},
    {1, 1},
    {1, 0},
    {1, -1},
    {0, -1},
    {-1, -1},
};

enum class Types : char {
    crystal = '$',
    wall = '#',
    empty = '@'
};

template <class T>
bool isValidBoundary(const structure::Array2D<T>& arr, int row, int col) {
    if (col < 0 || row < 0) return false;
    if (col >= arr.cols() || row >= arr.rows()) return false;
    return true;
}

int shortestPathOut_BFS(const structure::Array2D<char>& arr, std::pair<int, int> startPos) {
    structure::Array2D<bool> visited(arr.rows(), arr.cols());
    std::queue<std::pair<int, int>> queue;

    visited[startPos.first][startPos.second] = true;
    queue.push({startPos.first, startPos.second});

    int length = 0;
    int prevLayerElems = 1;
    int currLayerElems = 0;

    while (!queue.empty()) {
        auto curr = queue.front();
        queue.pop();

        for (int i = 0; i < DIRECTIONS; ++i) {
            const auto r = curr.first + offset[i].first;
            const auto c = curr.second + offset[i].second;

            if (!isValidBoundary(arr, r, c)) return length + 1;
            if (arr[r][c] != static_cast<char>(Types::empty)) continue;
            if (visited[r][c]) continue;

            visited[r][c] = true;
            queue.push({r, c});
            ++currLayerElems;
        }

        if (--prevLayerElems == 0) {
            prevLayerElems = currLayerElems;
            currLayerElems = 0;
            ++length;
        }
    }

    return -1;
}

std::pair<int, int> getCrystalLocation(const structure::Array2D<char>& arr) {
    for (int i = 0; i < arr.rows(); ++i) {
        for (int j = 0; j < arr.cols(); ++j) {
            if (arr[i][j] == static_cast<char>(Types::crystal)) return {i, j};
        }
    }
    return {-1, -1};
}

int solve(structure::Array2D<char>& arr) {
    std::pair<int, int> crystalLoc(getCrystalLocation(arr));
    return shortestPathOut_BFS(arr, crystalLoc);
}

int main() {
    int n, m;
    std::cin >> n >> m;
    structure::Array2D<char> arr(n, m);
    for (int i = 0; i < arr.rows(); ++i) {
        std::cin.get();
        for (int j = 0; j < arr.cols(); ++j) {
            arr[i][j] = std::cin.get();
        }
    }

    std::cout << solve(arr);
    return 0;
}