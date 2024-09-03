#include <iostream>
#include <cmath>

long long h, n;

void solve(long long start, long long end, long long& ans, long long level, bool turnRight = false) {
    if (start >= end) return;
    ++ans;
    long long mid = (start + end - 1) / 2;
    if (n <= mid) {
        if (turnRight) {
            ans += (1LL << level) - 1;
            solve(start, mid, ans, level - 1, turnRight);
        }
        else {
            solve(start, mid, ans, level - 1, !turnRight);
        }
    }
    else {
        if (turnRight) {
            solve(mid + 1, end, ans, level - 1, !turnRight);
        }
        else {
            ans += (1LL << level) - 1;
            solve(mid + 1, end, ans, level - 1, turnRight);
        }
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::cin >> h >> n;

    long long ans = 0;
    solve(1, 1LL << h, ans, h);
    std::cout << ans;

    return 0;
}