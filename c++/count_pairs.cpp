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

int where_in_A(const int * arr1, const int l1, const int num){ // can be done in log(n) time with binary search
    for(int i=0; i<l1; i++) {
        long p1 = pow(arr1[i], num);
        long p2 = pow(num, arr1[i]);
        if (p1 >= p2) {
            return i+1;
        }
    }
}

int pairs(const int * arr1, const int * arr2, const int l1, const int l2){
    int result = 0;
    for (int i=0; i<l2; i++){
        result += l1 - where_in_A(arr1, l1, arr2[i]);
    }
    return result;
}

void test(){
    int array1[] = {2, 1, 6}; 
    int array2[] = {1, 5};  
    int len1 = *(&array1 + 1) - array1;
    int len2 = *(&array2 + 1) - array2;

    sort(array1, array1+len1);
    
    print_array(array1, len1, "array1");
    print_array(array2, len2, "array2");


    int pairs1 = pairs(array1, array2, len1, len2);
    cout << "Pairs: "<<pairs1 << endl;
}

int main(){
    test();
    // int array1[] = {1, 3, 5, 89, 6, 4, 9, 2};
}