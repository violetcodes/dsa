#include <iostream> 
using namespace std; 

int sum(const int x, const int y) {
    return x+y;
}

int main() {
    cout<<sum(3, 5)<<endl;
    return 0;
}