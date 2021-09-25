# include <iostream>
# include <algorithm>
# include <vector> 
# include <numeric>
using namespace std;

template <typename T>
void print_arr(vector<T> v, const int len){
    for (int i=0; i<len; i++){
        cout << v[i] << " ";
    }
    cout << endl;

}

int main() {
    int arr[] = {1, 3, 5, 9, 3, 3, 2, 5, 1};
    int n = sizeof(arr)/sizeof(arr[0]);
    
    vector<int> vect(arr, arr+n);
    sort(vect.begin(), vect.end());

    print_arr(vect, n);

    // reverse(vect.begin(), vect.end());
    // print_arr(vect, n);

    cout << accumulate(vect.begin()+3, vect.end(), 0) << endl;

    string s = binary_search(vect.begin(), vect.end(), 9) ? "found" : "not found";
    cout << s << endl;

    vect.erase(unique(vect.begin(), vect.end()), vect.end());
    print_arr(vect, vect.end() - vect.begin());





    

}