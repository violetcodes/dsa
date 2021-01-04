# include <iostream>
# include <string>
# include <bits/stdc++.h>
using namespace std;

void print_array(const int* arr, const int n, const string desc="array"){
    cout << desc << ": ";
    for (int i=0; i<n; ++i) {
        cout << arr[i] << ' ';
    }
    cout << endl;
}

void rearrange(int arr1[], const int n1){
    int max_index = n1 - 1;
    int min_index = 0;
    int max_elem = arr1[max_index] + 1;

    for (int i=0; i<n1; i++){
        if (i%2 == 0){
            arr1[i] += (arr1[max_index] % max_elem) * max_elem;
            max_index--;
        }
        else {
            arr1[i] += (arr1[min_index] % max_elem) * max_elem;
            min_index++;
        }
    }

    for (int i=0; i<n1; i++) arr1[i] = arr1[i] / max_elem;

}

void test(){
    int array1[] = {1, 3, 5, 6, 4, 9, 2};    
    int len = *(&array1 + 1) - array1;
    sort(array1, array1+len);
    print_array(array1, len);
    rearrange(array1, len);
    print_array(array1, len, "after rearranging");


}

int main(){
    test();
    // int array1[] = {1, 3, 5, 89, 6, 4, 9, 2};



}