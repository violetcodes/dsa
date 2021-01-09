# include <iostream>
# include <vector>

using namespace std;

void print_array(const int* arr, const int n, const string desc="array"){
    cout << desc << ": ";
    for (int i=0; i<n; ++i) {
        cout << arr[i] << ' ';
    }
    cout << endl;
}


void decode(int joint_array[], int n1, int key){
    int first_array[n1];
    int second_array[n1];

    for (int i=0; i<n1; i++) first_array[i] = joint_array[i] % key;
    print_array(first_array, n1, "First array");
    
    for (int i=0; i<n1; i++) second_array[i] = joint_array[i] / key;
    print_array(second_array, n1, "Second array");   
}


void two_at_one(int array1[], int array2[], int n1){
    int big_int = 10000;

    int i = 0;
    while(i < n1){
        array1[i] = array1[i] + big_int * array2[i];
        i++;       
    }
}

template<typename Type>
class Vector {
    private:
        Type* elem;
        int sz;
    
    public:
        explicit Vector(int s);
        ~Vector() {delete[] elem;}
    
        Type& operator[](int i);
        const Type& operator[](int i) const;
        int size() const { return sz; }
};

template<typename T>
Vector<T>::Vector(int s){
    // if (s<0) {
    //     exception e;
    //     throw e;
    // }
    elem = new T[s];
    sz = s;
}

template<typename T>
const T& Vector<T>::operator[](int i) const {
    if (i<0 || size()<=i) throw out_of_range{"Vecotr::operator[]"};
    return elem[i];
}

void write(const Vector<string>& vs) {
    for (int i=0; i!=vs.size(); ++i) cout << vs[i] <<'\n';
}

void input_values(Vector<string>& vs) {
    for (int i=0; i!=vs.size(); ++i) {
        string s;
        cin >> s;
        vs[i] = s;
    }
}

void templates() {
    Vector<char> vc(200);
    Vector<string> vs(17);
    Vector<vector<int>> vli(45);

    input_values(vs);
    write(vs);







}

void some_vector(){
    vector<int> vc;
    int x;
    while (cin>>x) vc.push_back(x);

    cout<<"SUBMITTED\n";
    
    for(int i=0; i<vc.size(); i++) cout<<vc[i]<<" ";
    cout << endl;
}


void test() {
    int array1[] = {39, 20, 909, 2390};
    int array2[] = {1049, 201, 20, 391};

    int n1 = 4;

    print_array(array1, n1, "array1");
    print_array(array2, n1, "array2");

    two_at_one(array1, array2, n1);
    print_array(array1, n1, "two at one");    

    decode(array1, n1, 10000);

    cout<<"END of the Document"<<endl;
}


int main(){
    // test();
    // some_vector();
    templates();

}
