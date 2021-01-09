# include <iostream>
# include <string>
# include <bits/stdc++.h>
# include <cmath>

using namespace std;

void print_array(const int* arr, const int n, const string desc="array"){
    cout << desc << ": ";
    for (int i=0; i<n; ++i) {
        cout << arr[i] << ' ';
    }
    cout << endl;
}

int solve(int * array, int len) {
    

}

void test(){
    int array1[] = {2, 4, 1, 3, 5}; 
    int len1 = *(&array1 + 1) - array1;
    sort(array1, array1+len1);    
    print_array(array1, len1, "array1");

    // int array2[] = {1, 5};  
    // int len2 = *(&array2 + 1) - array2;
    // print_array(array2, len2, "array2");    

    int ans = solve(array1, len1);

    cout << "Out: "<< ans << endl;
}

int main(){
    test();
    // int array1[] = {1, 3, 5, 89, 6, 4, 9, 2};
}