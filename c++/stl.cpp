# include <iostream>
# include <set>
# include <algorithm>

using namespace std;
typedef ostream os;

os& operator<<(os& o1, set<int> st) {
    o1 << "{";
    for (auto x: st) o1 << x << ", ";
    o1 << "}";
    return o1; 
}

int main() {
    
    // using sets
    set<int> iset;
    int arr[] = {5, 6, 3, 12, 1, 1, 3, 4, 3, 5, 9, 10};

    for (auto x: arr) iset.insert(x);

    cout << "Set: "<<iset <<endl;


    int a_num = 10;
    if (binary_search(iset.begin(), iset.end(), a_num))
        cout << "Found " << a_num << endl;
    else cout << "Didn't found" << endl;

    
}

