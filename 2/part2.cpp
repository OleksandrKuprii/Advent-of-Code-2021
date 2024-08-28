#include <iostream>
#include <fstream>

using namespace std;

int main() {
    string line;
    fstream File("../input.txt");

    string dir;
    int val;
    bool flag;

    int hor = 0;
    int depth = 0;
    int aim = 0;

    while(getline(File, line)) {
        dir = "";
        flag = false;

        for (char c : line) {
            if (flag) {
                val = c - '0';
                break;
            }
            if (c == ' ') {
                flag = true;
            } else {
                dir += c;
            }
        }

        if (dir == "down") {
            aim += val;
        }
        else if (dir == "up") {
            aim -= val;
        }
        else {
            hor += val;
            depth += aim * val;
        }
    }

    cout << hor * depth;
    return 0;
}
