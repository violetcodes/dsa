# include <iostream>
using namespace std;

void print_array(const int* arr, const int n, const string desc="array"){
    cout << desc << ": ";
    for (int i=0; i<n; ++i) {
        cout << arr[i] << ' ';
    }
    cout << endl;
}



void merge(int arr[], int p, int q) {
    

    int merged_array[p+q];

    int L[p], R[q];
    for (int i=0; i<p; i++) L[i] = arr[i];
    for (int i=0; i<q; i++) R[i] = arr[p+i];

    int curr_p = 0, curr_q = 0, i=0;
    while (curr_p < p && curr_q < q) {
        if (L[curr_p] < R[curr_q]) merged_array[i++] = L[curr_p++];
        else merged_array[i++] = R[curr_q++];
    }

    while (curr_p < p) merged_array[i++] = L[curr_p++];
    while (curr_q < q) merged_array[i++] = R[curr_q++];

    i = 0;
    while (i < p+q) {
        arr[i] = merged_array[i];
        i++;
    }
}

int MAX_REC = 20;

void merge_sort(int arr[], int start, int end){

    if (MAX_REC>0) MAX_REC--;
    else {
        exception e;
        throw e;
    }

    if (start >= end) return;
    
    // merge sort first half and second half
    int half = (start + end)/2;

    // print_array(arr, end+1, "splitting this array");
    merge_sort(arr, start, half);
    merge_sort(arr, half+1, end);

    // print_array(arr, half, "merging this array and:");
    // print_array(arr+half+1, end, "merging this array:");

    merge(arr, half, start+end+1);

    // print_array(arr, end+1, "\nthis array it the out:");


    // cout<<"\n\n";

    return;

    

    

}

void solve(int arr[], int len) {
    print_array(arr, len, "before mergesort");
    merge_sort(arr, 0, len-1);
    print_array(arr, len, "after mergesort");
}

void test(){
    int array1[] = {2, 1, 2, 3, 5, 9, 4, 3, 5, 6}; 
    int array2[] = {1, 5};  
    int len1 = *(&array1 + 1) - array1;
    int len2 = *(&array2 + 1) - array2;

    solve(array1, len1);
    
    // print_array(array1, len1, "array1");
    // print_array(array2, len2, "array2");


    // int pairs1 = pairs(array1, array2, len1, len2);
    // cout << "Pairs: "<<pairs1 << endl;
}

int main(){
    test();
    // int array1[] = {1, 3, 5, 89, 6, 4, 9, 2};
    // int * as = array1 + 4;

    // cout <<  as[2] << endl;
}

