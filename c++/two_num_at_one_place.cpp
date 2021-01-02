# include <iostream>
using namespace std;

void decode(int joint_array[], int n1, int key){
    for (int i=0;i<n1;i++){
        int num_ = joint_array[i];
        cout<<i<<". "<<(num_%key)<<"  "<<(num_/key)<<endl;
    }
}


void two_at_one(int array1[], int array2[], int n1){
    int big_int = 10000;


    int i = 0;

    while(i< n1){

        array1[i] = array1[i] + big_int * array2[i];
        i++;
        
    }
}


int main(){
    int array1[] = {39, 20, 909, 2390};
    int array2[] = {1049, 201, 20, 391};

    int n1 = 4;
    two_at_one(array1, array2, n1);

    for(int i=0;i<n1;i++){
        cout<<array1[i]<<" ";
    }
    cout<<endl;

    decode(array1, n1, 10000);

    cout<<"END of the Document"<<endl;
}
