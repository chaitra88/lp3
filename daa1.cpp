#include <iostream>
using namespace std;

void fib_recursive(int n)
{
    if (n <= 1)
        return n;
    else
        return fib_recursive(n - 1) + fib_recursive(n - 2);
}

void fib_iterative(int n)
{
    if (n <= 1)
        return n;

    int a = 0;
    int b = 1;

    for (int i = 2; i <= n; i++)
    {

        int c = a + b;
        a = b;
        b = c;
    }
    return b;
}

void toh(int n, char src, char aux, char dest)
{
    if (n == 1)
        cout << "Move disk from " << src << " to " << dest << endl;
    else
    {
        toh(n - 1, src, dest, aux);
        cout << "move disk " << n << " from " << src << " to " << dest << endl;
        toh(n - 1, aux, src, dest);
    }
}

int main()
{
    int n;
    cout << "enter num ";
    cin >> n;

    if (n < 0)
        cout << "num must be greater than 0 ";

    // recursive .......

    int result = fib_recursive(n);
    cout << "fib of n is " << result << endl;

    // to print series......

    for (int i = 0; i <= n; i++)
    {
        cout << fib_recursive(i);
        if (i < n)
            cout << " , ";
    }

    // iterative.........

    int result = fib_iterative(n);
    cout << "fib of n is " << result << endl;

    // toh

    if (n < 1)
        cout << "There must be atleast one disk ";
    else
    {
        toh(n, 'A', 'B', 'C');
    }
}
