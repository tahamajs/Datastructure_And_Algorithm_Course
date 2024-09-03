#include <iostream>
#include <vector>

template <class T, class Compare>
void merge(std::vector<T>& arr, int first, int mid, int last, Compare compare) {
    std::vector<T> a(arr.begin() + first, arr.begin() + mid + 1);
    std::vector<T> b(arr.begin() + mid + 1, arr.begin() + last + 1);

    int subarrL = 0, subarrR = 0, mergedArr = first;

    while (subarrL < a.size() && subarrR < b.size()) {
        if (compare(a[subarrL], b[subarrR])) {
            arr[mergedArr] = a[subarrL];
            ++subarrL;
        }
        else {
            arr[mergedArr] = b[subarrR];
            ++subarrR;
        }
        ++mergedArr;
    }
    while (subarrL < a.size()) {
        arr[mergedArr] = a[subarrL];
        ++subarrL;
        ++mergedArr;
    }
    while (subarrR < b.size()) {
        arr[mergedArr] = b[subarrR];
        ++subarrR;
        ++mergedArr;
    }
}

template <class T, class Compare>
void mergeSort(std::vector<T>& arr, int first, int last, Compare compare) {
    if (first >= last) return;
    int mid = (first + last) / 2;
    mergeSort(arr, first, mid, compare);
    mergeSort(arr, mid + 1, last, compare);
    merge(arr, first, mid, last, compare);
}

struct Person {
    int id;
    int hardwork;
    int teamwork;
    bool selected = false;
};

struct Solver {
    Solver() = default;
    void select(Person* p) {
        sumHardwork += p->hardwork;
        sumTeamwork += p->teamwork;
        p->selected = true;
    }
    void deselect(Person* p) {
        sumHardwork -= p->hardwork;
        sumTeamwork -= p->teamwork;
        p->selected = false;
    }
    int sumHardwork = 0;
    int sumTeamwork = 0;
};

void solve2(std::vector<Person>& sumSort,
            std::vector<Person*>& hwSort,
            std::vector<Person*>& twSort,
            int maxSel,
            int totalHardwork,
            int totalTeamwork) {
    Solver solver;
    const int n = sumSort.size();
    for (int i = 0; i < maxSel; ++i) {
        solver.select(&sumSort[i]);
    }

    int lowestSelHWi = n - 1, highestNotSelHWi = 0;
    int lowestSelTWi = n - 1, highestNotSelTWi = 0;

    while (true) {
        if (solver.sumHardwork * 2 <= totalHardwork) {
            if (hwSort[highestNotSelHWi]->selected) {
                for (int i = highestNotSelHWi + 1; i <= n; ++i) {
                    if (i == n) i = 0;
                    if (!hwSort[i]->selected) {
                        highestNotSelHWi = i;
                        break;
                    }
                }
            }
            if (!twSort[lowestSelTWi]->selected) {
                for (int i = lowestSelTWi - 1; i >= 0; --i) {
                    if (i == 0) i = n - 1;
                    if (twSort[i]->selected) {
                        lowestSelTWi = i;
                        break;
                    }
                }
            }

            solver.deselect(twSort[lowestSelTWi]);
            solver.select(hwSort[highestNotSelHWi]);
        }
        else if (solver.sumTeamwork * 2 <= totalTeamwork) {
            if (twSort[highestNotSelTWi]->selected) {
                for (int i = highestNotSelTWi + 1; i <= n; ++i) {
                    if (i == n) i = 0;
                    if (!twSort[i]->selected) {
                        highestNotSelTWi = i;
                        break;
                    }
                }
            }
            if (!hwSort[lowestSelHWi]->selected) {
                for (int i = lowestSelHWi - 1; i >= 0; --i) {
                    if (i == 0) i = n - 1;
                    if (hwSort[i]->selected) {
                        lowestSelHWi = i;
                        break;
                    }
                }
            }

            solver.deselect(hwSort[lowestSelHWi]);
            solver.select(twSort[highestNotSelTWi]);
        }
        else break;
    }
}

void solve(std::vector<Person>& inp) {
    std::vector<Person*> hardworkSort(inp.size());
    std::vector<Person*> teamworkSort(inp.size());

    int totalHardwork = 0, totalTeamwork = 0;
    for (int i = 0; i < inp.size(); ++i) {
        hardworkSort[i] = &inp[i];
        teamworkSort[i] = &inp[i];
        totalHardwork += inp[i].hardwork;
        totalTeamwork += inp[i].teamwork;
    }

    mergeSort(hardworkSort, 0, hardworkSort.size() - 1, [](const auto a, const auto b) {
        return a->hardwork > b->hardwork;
    });
    mergeSort(teamworkSort, 0, teamworkSort.size() - 1, [](const auto a, const auto b) {
        return a->teamwork > b->teamwork;
    });
    mergeSort(inp, 0, inp.size() - 1, [](const auto& a, const auto& b) {
        return a.hardwork + a.teamwork > b.hardwork + b.teamwork;
    });

    const int maxSel = (inp.size() / 2) + 1;
    solve2(inp, hardworkSort, teamworkSort, maxSel, totalHardwork, totalTeamwork);

    std::cout << maxSel << '\n';
    for (const auto& x : inp) {
        if (x.selected) std::cout << x.id + 1 << ' ';
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    int n;
    std::cin >> n;
    std::vector<Person> inp(n);
    for (int i = 0; i < n; ++i) {
        int t;
        std::cin >> t;
        inp[i].id = i;
        inp[i].hardwork = t;
    }
    for (int i = 0; i < n; ++i) {
        int t;
        std::cin >> t;
        inp[i].teamwork = t;
    }

    solve(inp);
    return 0;
}
