class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        set<pair<int, int>> set1, set2;
        vector<vector<bool>> visited(m, vector<bool>(n, false));

    for (int i = 0; i < guards.size(); ++i) {
        set1.insert({guards[i][0], guards[i][1]});
    }

    for (int i = 0; i < walls.size(); ++i) {
        set2.insert({walls[i][0], walls[i][1]});
    }

    int guarded = 0;
    for (int i = 0; i < guards.size(); i++) {
        int l = guards[i][1] - 1;
        int r = guards[i][1] + 1;
        int u = guards[i][0] - 1;
        int d = guards[i][0] + 1;

        while (l >= 0) {
            if (set1.count({guards[i][0], l}) == 0 && set2.count({guards[i][0], l}) == 0) {
                if (!visited[guards[i][0]][l]) {
                    guarded++;
                    visited[guards[i][0]][l] = true;
                }
                l--;
            } else {
                break;
            }
        }
        while (r < n) {
            if (set1.count({guards[i][0], r}) == 0 && set2.count({guards[i][0], r}) == 0) {
                if (!visited[guards[i][0]][r]) {
                    guarded++;
                    visited[guards[i][0]][r] = true;
                }
                r++;
            } else {
                break;
            }
        }
        while (u >= 0) {
            if (set1.count({u, guards[i][1]}) == 0 && set2.count({u, guards[i][1]}) == 0) {
                if (!visited[u][guards[i][1]]) {
                    guarded++;
                    visited[u][guards[i][1]] = true;
                }
                u--;
            } else {
                break;
            }
        }
        while (d < m) {
            if (set1.count({d, guards[i][1]}) == 0 && set2.count({d, guards[i][1]}) == 0) {
                if (!visited[d][guards[i][1]]) {
                    guarded++;
                    visited[d][guards[i][1]] = true;
                }
                d++;
            } else {
                break;
            }
        }
    }

    return m * n - (guards.size() + walls.size() + guarded);
    }
};