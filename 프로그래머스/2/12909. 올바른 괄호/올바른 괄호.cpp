#include <string>
#include <iostream>

using namespace std;

bool solution(string s)
{
    int bracket_count = 0;
    
    for (char c : s) {
        if (c == '(') {
            bracket_count++;
        } else {
            bracket_count--;
            if (bracket_count < 0) {
                return false;
            }
        }
    }

    return bracket_count == 0;
}