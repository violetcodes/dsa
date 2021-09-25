#include <iostream> 
#include <string>
#include <cmath>
using namespace std; 



template <typename T>
T sum(const T a, const T b) {
    return a+b;
}


template <typename T>
class Point {
    private:
        T x, y;
    
    public:
        Point(const T u, const T v): x(u), y(v) {};
        T get_x() {return x;}
        T get_y() {return y;}
        void get_xandy();
};

template <typename T>
void Point<T>::get_xandy() {
    cout << "(" << x << ", " << y << ")" << endl;
}

template <typename T>
class Container {
    private:
        T element; 
    
    public:
        Container(T elem): element(elem) {};
        void print_it() {
            cout << element << endl;
        }
};

template <>
class Container<string> {
    private:
        string elem;
    
    public:
        Container(string e): elem(e) {};
        void print_it() {
            cout << elem << endl;
        }

};

int main() {

    Container<string> c1 = Container<string>("hello, Vishal");
    c1.print_it();

    Container<int> c2 = Container<int>(32);
    c2.print_it();
    
    // Point<int> p1 = Point<int>(3, 2);
    // cout << "X:" << p1.get_x() << " " << "Y:" << p1.get_y() << endl;
    // p1.get_xandy();


    // Point<int> p2 = Point<int>(1, 1);
    // cout << "Distance from p2(1,1):" << p1.distance(p2) << endl;
    
    // cout<<sum(3.1, 5.9)<<endl;
    // return 0;
}