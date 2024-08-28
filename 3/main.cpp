#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    string line;
    fstream File("../input.txt");

    vector<int> data = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    while (getline(File, line)) {
        for (int i = 0; i < 12; i++) {
            data[i] += line[i] - '0';
        }
    }

    int gamma   = 0b101110100101;
    int epsilon = 0b010001011010;

    cout << gamma * epsilon;
    return 0;
}
