#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    string line;
    int val;

    ifstream File("../input.txt");

    int i = 1;
    int counter = 0;
    vector<int> data = {};

    getline(File, line);
    val = stoi(line);
    data.push_back(val);

    getline(File, line);
    val = stoi(line);
    data.push_back(val);
    data[i - 1] += val;

    while (getline (File, line)) {
        val = stoi(line);
        i++;

        data.push_back(val);
        data[i-1] += val;
        data[i-2] += val;
    }

    for (int j = 1; j < data.size(); j++) {
        if (data[j] > data[j-1]) counter++;
    }

    cout << counter;

    File.close();

    return 0;
}