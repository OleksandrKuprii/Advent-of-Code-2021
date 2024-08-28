#include <iostream>
#include <fstream>

using namespace std;

void check(int * data[5][5]) {

}

int main() {
    ifstream File("../input.txt");
    streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    cin.rdbuf(File.rdbuf()); //redirect std::cin to in.txt!

    string line;
    cin >> line;

    int data[100][5][5];

    for (auto & table : data) {
        for (auto & row : table) {
            for (auto & cell : row) {
                cin >> cell;
            }
        }
    }

    std::cin.rdbuf(cinbuf);   //reset to standard input again

    cout << line << endl;


    size_t pos = 0;
    string token;
    int number;
    int count = 0;

    while ((pos = line.find(',')) != string::npos) {
        token = line.substr(0, pos);
        line.erase(0, pos + 1);

        number = stoi(token);
        count++;

        for (auto & table : data) {
            for (auto & row : table) {
                for (auto & cell : row) {
                    if (cell == number) {
                        cell = -1;
                    }
                }
            }
        }

        for (auto & table : data) {
            for (auto &row : table) {
                if (row[0] == row[1] == row[2] == row[3] == row[4]) {
                    int sum = 0;
                    for (auto & row1 : table) {
                        for (auto &cell : row1) {
                            sum += cell;
                        }
                    }
                    sum += count;
                    cout << sum * number << 'a';
                    return 0;
                }
            }
            for (int i = 0; i < 5; i++) {
                if (table[0][i] == table[1][i] == table[2][i] == table[3][i] == table[4][i]) {
                    int sum = 0;
                    for (auto & row1 : table) {
                        for (auto &cell : row1) {
                            sum += cell;
                        }
                    }
                    sum += count;
                    cout << sum * number << 'b' << endl;
                    cout << (table[0][i] == table[1][i]) << endl;
                    cout << table[0][i] << table[1][i] << table[2][i] << table[3][i] << table[4][i] << endl;
                    for (auto & row : table) {
                        for (auto & cell : row) {
                            cout << cell << " ";
                        }
                        cout << endl;
                    }
                    cout << endl;
                    return 0;
                }
            }
            if (table[0][0] == table[1][1] == table[2][2] == table[3][3] == table[4][4]) {
                int sum = 0;
                for (auto & row1 : table) {
                    for (auto &cell : row1) {
                        sum += cell;
                    }
                }
                sum += count;
                cout << sum * number << 'c';
                return 0;
            }
            if (table[0][4] == table[1][3] == table[2][2] == table[3][1] == table[4][0]) {
                int sum = 0;
                for (auto & row1 : table) {
                    for (auto &cell : row1) {
                        sum += cell;
                    }
                }
                sum += count;
                cout << sum * number << 'd';
                return 0;
            }
        }
    }





    for (auto & table : data) {
        for (auto & row : table) {
            for (auto & cell : row) {
                cout << cell << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
    return 0;

}
