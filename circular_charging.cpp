#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cctype>

using namespace std;

// O(N) Greedy logic
int get_start_station(const vector<int>& charge, const vector<int>& cost) {
    int total_diff = 0;
    int curr_diff = 0;
    int start_idx = 0;
    int n = charge.size();
    
    if (n == 0) return -1;
    
    for (int i = 0; i < n; ++i) {
        int diff = charge[i] - cost[i];
        total_diff += diff;
        curr_diff += diff;
        
        if (curr_diff < 0) {
            start_idx = i + 1;
            curr_diff = 0; 
        }
    }
    
    return (total_diff >= 0) ? start_idx : -1;
}
vector<int> parse_line(string line) {
    vector<int> result;
    for (char &c : line) {
        if (!isdigit(c)) {
            c = ' ';
        }
    }
    
    stringstream ss(line);
    int num;
    while (ss >> num) {
        result.push_back(num);
    }
    return result;
}

int main() {
    string line1, line2;
    
    if (getline(cin, line1) && getline(cin, line2)) {
        vector<int> charge = parse_line(line1);
        vector<int> cost = parse_line(line2);
        
        cout << get_start_station(charge, cost) << "\n";
    }
    
    return 0;
}