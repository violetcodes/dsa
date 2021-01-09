# include <fstream>
# include <iostream>

using namespace std;

enum suit_t {CLUBS, DIAMONDS, HEARTS, SPAFRS};
void print_suit(const suit_t s) {
    const char *names[] = {"Clubs", "Diamonds", "Hearts", "Spades"};
    // return names[s];
    cout<<names[s]<<'\n';
}

const int DIV_BY_0 = 0;
int divide(const int x, const int y) {
    // if (y == 0 ) throw DIV_BY_0;
    if (y==0) throw runtime_error("Divide by zero");
    return x/y;
}


int g=45;
int & getG() {return g;}

class ct {
    private:
        const int s = 30;
        int e = 50;
        int * s1 = & e;
    
    public:
        int* print() const { // const means no modifying member pointers;
            printf("e: %d and s: %d\n", e, s);
            // e++;
            (*s1)++;
            printf("e: %d and *s: %d\n", e, *s1);
            return s1;
        }

        friend ostream& operator<<(ostream& o, const ct c);


};

ostream& operator<<(ostream& o, const ct c) {
    o << "$" << c.e << "," << c.s;
    return o;
}


int main(){
    // ifstream source("hello.txt");
    // ofstream destin("dest.txt");

    // int x;

    // while (source >> x) {
    //     cout << x << " ";
    //     // cout << endl;
    //     destin << x << endl;

    // }
        
    
    // source.close();

    // return 0; 

    
    // print_suit(DIAMONDS);

    // for (int i=3; i<5; i++) print_suit(i);
    // cout << endl;

    // int& s = getG();
    // s = 34;
    // cout << g << endl;

    ct a_class;

    // int* s1 = a_class.print();
    // cout << *s1 << '\n' << g << '\n';

    // int **arrptr;
    // int x;
    // cin >> x;   

    // int x, y;
    // cin>>x>>y;

    
    // try {
    //     cout << "DIVIDING: ";
    //     // *arrptr = new int[divide(5, x)];
    //     cout << divide(x, y) << endl;
    // } catch (runtime_error error) {
    //     cerr << "Caught error " << error.what() << endl;
    // }

    // friend function

    cout << a_class << endl;

    // other ?
    // casting static_cast<int>val, dynamic_cast<int*>val, const_cast<typename> etc




}