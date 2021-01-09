# include <iostream>
# include <cmath>
# include <cctype>
using namespace std;


// int sum(int a, int b) { return a+b;}

// double sum(double a, double b) { return a+b;}

template <typename T1, typename T2>
T1 sum(T1 a, T2 b) { return a+b;}

template <typename T>
class Point {
    private:
        T x, y;
    
    public:
        Point(const T u, const T v): x(u), y(v) {}
        T getX() { return x; }
        T getY() { return y; }

        T distance_from_origin (int ord=2) {
            T total = (pow(x, ord) + pow(y, ord));
            double inv_ord = 1.0 / ord;
            T result = pow(total, inv_ord);
            return result;
        }

};

template <typename T>
std::ostream& operator<<(std::ostream& os, Point<T> pt) {
    os << "Point(" << pt.getX() << ", " << pt.getY() <<")";
    return os;
}

template <typename T>
class Container {
    private:
        T elem;
    public:
        Container(const T e): elem(e) {}
        T inc() {return elem+1;}
};

template <>
class Container <char> {
    private:
        char elem;
    public:
        Container(const char e): elem(e) {}
        char uppercase() { return std::toupper(elem); } 
};

template <typename T, int N>
class ArrayContainer{
    public:
        void set(const int i, const T val) { elems[i] = val; }
        T get(const int i) { return elems[i]; }
        T& operator[](const int i) { return elems[i]; }
    private:
        T elems[N];
};

template <typename T, int N>
ostream& operator<<(ostream& os, ArrayContainer<T, N> arr_cont) {
    for (int i=0; i<N-1; i++) {
        os << arr_cont[i] << " ";
    }
    os << arr_cont[N-1];
    return os;
}



int main() {
    // int a = 3, b = 8;
    // double a = 3.5, b = 4.3;
    // // int b = 4.3;
    // std::cout << "Sum for " << a << " and " << b << " is: " 
    //         << sum(a, b)
    //         << std::endl;


    // Point<double> fpoint(6, 9);
    // std::cout 
    //         << "Distance from origin: "
    //         << "\n  eular: " << fpoint.distance_from_origin(2)
    //         << "\n  manhattan: " << fpoint.distance_from_origin(1)

    //         << "\n" << fpoint
    //         << std::endl;
    
    // Container<int> icont(5);
    // Container<char> ccont('r');
    // std::cout << icont.inc() << std::endl;
    // std::cout << ccont.uppercase() << std::endl;

    ArrayContainer<int, 5> int_arr;
    ArrayContainer<char, 6> char_arr;

    int_arr.set(2, 5);
    char_arr.set(3, 'y');

    cout << "Int arr: " << int_arr << endl;
    cout << "Char arr: " << char_arr << endl;            

}