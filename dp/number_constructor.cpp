#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int n;
    string pattern;
    fin >> n >> pattern;

    int support[10][n + 1];

    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < n + 1; j++) {
            support[i][j] = 0;
        }
    }

    for (int i = 0; i < n; i++) {
        if (pattern[i] == '*') {
            for (int j = 0; j < 10; j++) {
                for (int q = 0; q < 10; q++) {
                    if (j != q)
                        support[q][i + 1] = max(support[q][i + 1], support[j][i] + j * q);
                }
            }
        } else {
            int element = pattern[i] - '0', result;
            for (int q = 0; q < 10; q++) {
                if (q == element)
                    result = 0;
                else
                    result = element * q;
                support[q][i + 1] = max(support[q][i + 1], support[element][i] + result);
            }
            for (int q = 0; q < 10; q++){
                if (q != element)
                    support[q][i] = 0;
            }
        }
    }
    fout << 8 * 9 * (n - 1) - support[0][n];
}
