#include <iostream>
#include <string>
#include <windows.h>
#include <ctime>
#include <fstream>

using namespace std;
int main() {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    srand(time(NULL));
    int num, size, form, fchoice, n, dimstat;
    n = 1;
    tryAgainNum:
    cout << "Please, choose the size of array: 1-10, 2-100, 3-1000, 4-10000, 5-1000000000.\n";
    cin >> size;
    if (size == 1) num = 10;
    else if (size == 2) num = 100;
    else if (size == 3) num = 1000;
    else if (size == 4) num = 10000;
    else if (size == 5) num = 1000000000;
    else {
        cout << "Wrong choice!";
        goto tryAgainNum;
    }

    tryAgainAvt:
    cout << "Please, choose the type of array: 1 - int, 2 - double, 3 - str.\n";
    cin >> form;
    if (form != 1 && form != 2 && form != 3) {
        cout << "Wrong choice!";
        goto tryAgainAvt;
    }

    unsigned int start_time = clock();
    int *p_darr_int = new int[num];
    if (form != 1) delete[] p_darr_int;

    double *p_darr_double = new double[num];
    if (form != 2) delete[] p_darr_double;

    char *p_darr_char = new char[num];
    if (form != 3) delete[] p_darr_char;
    if (form == 1) {
        if (size == 1) {
            int p_darr_int[10];
        }
        if (size == 2) {
            int p_darr_int[100];
        }
        if (size == 3) {
            int p_darr_int[1000];
        }
        if (size == 4) {
            int p_darr_int[10000];
        }
        //if (size == 5) {
        //int p_darr_int[1000000000];    //too heavy (>0x7fffffff bites)
        //}
        //if (size == 6) {
        //   int p_darr_int[10000000000];   //too heavy (>0x7fffffff bites)
        //}
    }
    if (form == 2) {
        if (size == 1) {
            double p_darr_double[10];
        }
        if (size == 2) {
            double p_darr_double[100];
        }
        if (size == 3) {
            double p_darr_double[1000];
        }
        if (size == 4) {
            double p_darr_double[10000];
        }
        //if (size == 5) {
        //    double p_darr_double[1000000000];   //too heavy (>0x7fffffff bites)
        //}
        //if (size == 6) {
        //    double p_darr_double[10000000000];  //too heavy (>0x7fffffff bites)
        //}
    }
    if (form == 3) {
        if (size == 1) {
            char p_darr_char[10];
        }
        if (size == 2) {
            char p_darr_char[100];
        }
        if (size == 3) {
            char p_darr_char[1000];
        }
        if (size == 4) {
            char p_darr_char[10000];
        }
        //if (size == 5) {
        //    char p_darr_char[1000000000];     //too heavy (>0x7fffffff bites)
        //}
        //if (size == 6) {
        //    char p_darr_char[10000000000];    //too heavy (>0x7fffffff bites)
        //}
    }
    if (form == 1) {
        for (int i = 0; i < num; i++) {
            p_darr_int[i] = rand() % 100;
        }
    } else if (form == 2) {
        for (int i = 0; i < num; i++) {
            double r = static_cast <double> (rand() % 100) / static_cast <double> (5);
            p_darr_double[i] = r;
        }
    } else if (form == 3) {
        for (int i = 0; i < num; i++) {
            p_darr_char[i] = rand() % 255;
            if (i == 10) cout << endl;
        }
    } else {
        cout << "Wrong choice!";
        goto tryAgainAvt;
    }
    unsigned int end_time = clock();
    unsigned int search_time = (end_time - start_time);
    int n_m;
    int size_m;
    string type_m;
    while (true) {
        cout << endl
             << "Please, choose the operation: 1-display the array, 2-show stats, \n3-write down stats to file, 4-display stats-file 9-exit.\n";
        cin >> fchoice;

        if (fchoice == 1 && form == 1)
            for (int i = 0; i < num; i++) {
                cout << " " << p_darr_int[i];
                if (i == 10) cout << endl;
            }
        if (fchoice == 1 && form == 2)
            for (int i = 0; i < num; i++) {
                cout << " " << p_darr_double[i];
                if (i == 10) cout << endl;
            }
        if (fchoice == 1 && form == 3)
            for (int i = 0; i < num; i++) {
                cout << " " << p_darr_char[i];
                if (i == 10) cout << endl;
            }
        if (fchoice == 2 || fchoice == 3) {
            if (form == 1) {
                size_m = sizeof(int) * num;
                type_m = "int";
            }
            if (form == 2) {
                size_m = sizeof(double) * num;
                type_m = "double";
            }
            if (form == 3) {
                size_m = sizeof(char) * num;
                type_m = "str";
            }
            if (fchoice != 3) {
                cout << endl << "Size: " << size_m << " bytes" << "  |Type: " << type_m << "  |Time: " << search_time
                     << " s";
            }
        }
        if (fchoice == 3) {
            n_m = 0;
            ifstream file;
            string str;
            file.open("stats.txt");
            if (file.is_open()) {
                while (!file.eof()) {
                    str = "";
                    getline(file, str);
                    n_m++;
                }
            }
            file.close();
            ofstream stat;
            stat.open("stats.txt", ofstream::app);
            if (!stat.is_open()) {
                cout << "Error!";
            } else {
                if (n_m == 0) n_m = 1;
                stat << "array # " << n_m << " |Size: " << size_m << " bytes" << "  |Type: " << type_m << "  |Time "
                     << search_time << " s" << endl;
            }
            stat.close();
        }
        if (fchoice == 4) {
            system("stats.txt");
        }
        if (fchoice == 9) {
            break;
        }
    }
}