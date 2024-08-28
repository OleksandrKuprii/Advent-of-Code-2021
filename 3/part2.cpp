#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


bool in(int elem, const vector<int>& data) {
    for (int e : data) {
        if (e == elem) return true;
    }
    return false;
}

int main() {
    int a = 0b100000110000;
    int b = 0b001110101101;
    cout << a << " " << b << endl;
    cout << a * b;

    string line;
    fstream File("../input.txt");

    vector<vector<int>> data = {};
    vector<int> ban = {};

    while (getline(File, line)) {
        vector<int> x = {};
        x.reserve(12);
        for (int i = 0; i < 12; i++) {
            x.push_back(line[i] - '0');
        }
        data.push_back(x);
    }

    int position = 0;
    while (data.size() != 1) {
        int common = 0;

        for (const vector<int> &i : data) {
            for (int j : i) {
                if ( !in(j, ban)) {
                    common += j - '0';
                }
            }
        }
        if (common < 500) common = 0;
        else common = 1;

        for (int i = 0; i < data.size(); i++) {
            if (data[i][position] != common) {
                ban.push_back(i);
            }
            cout << endl;
        }
        position++;

        cout << position << endl;
        for (auto & i : data) {
            for (int j : i) {
                cout << j << ' ';
            }
            cout << endl;
        }
        cout << "---------" << endl;
    }

    return 0;
}
