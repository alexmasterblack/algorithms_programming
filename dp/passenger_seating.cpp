#include <vector>
#include <fstream>
#include <iostream>

#define modul 1000000007

using namespace std;

int main() {
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int n, k;
    fin >> n >> k;

    int *pattern = new int[n + 1]();

    int place;
    for (int i = 0; i < k; i++) {
        fin >> place;
        pattern[place] = 1;
    }

    int support[n + 1][3];
    for (int i = 0; i < n + 1; i++) {
        for (int j = 0; j < 3; j++) {
            support[i][j] = 0;
        }
    }
    support[0][1] = 1;

    for (int i = 1; i < n + 1; i++) {
        support[i][0] = (support[i - 1][1] + support[i - 1][2]) % modul;
        if (pattern[i] != 1) {
            support[i][1] = support[i - 1][0] % modul;
            support[i][2] = support[i - 1][1] % modul;
        }
    }

    fout << (support[n][0] + support[n][1]) % modul;
}
