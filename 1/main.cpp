#include <iostream>
#include <fstream>

using namespace std;

int main() {
    string line;
    ifstream File("../input.txt");

    int counter = 0;

    getline(File, line);
    int previous = stoi(line);

    while (getline (File, line)) {
        if (stoi(line) > previous) {
            counter++;
        }
        previous = stoi(line);
    }

    cout << counter;

    File.close();

    return 0;
}