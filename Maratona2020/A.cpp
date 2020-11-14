#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, a, b, i=0, sum=0, num, c, it=1000000;
    long double med=0;

    cin >> n >> a >> b;

    it /= (n/(b-a+1));

    random_device rd;
    mt19937 mt(rd());
    uniform_int_distribution<> dist(a, b);


    for(c=0; c<it; c++) {
        i = 0;
        sum = 0;
        while(sum < n)
        {
            num = dist(mt);
            sum += num;
            i++;
        }
        med += i;
    }

    med /= it;
    cout << med << "\n";

    return 0;
}
