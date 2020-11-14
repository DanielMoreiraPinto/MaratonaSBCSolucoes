#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, d, l, r, c, i, j, ans=1;
    int m[11][11];

    for(i=0; i < 11; i++) {
        for(j=0; j < 11; j++) {
            m[i][j]=0;
        }
    }

    cin >> n;
    for(i=0; i < n; i++) {
        cin >> d >> l >> r >> c;
        if(ans == 1) {
            if(d == 0) {
                if(c + l - 1 > 10) {
                    ans = 0;
                }
                if(ans == 1) {
                    for(j=c; j <= c+l-1; j++) {
                        if(m[r][j] == 1) {
                            ans = 0;
                        }
                        m[r][j] = 1;
                    }
                }
            } else {
                if(r + l - 1 > 10) {
                    ans = 0;
                }
                if(ans == 1) {
                    for(j=r; j <= r+l-1; j++) {
                        if(m[j][c] == 1) {
                            ans = 0;
                        }
                        m[j][c] = 1;
                    }
                }
            }

        }

    }


    if(ans == 1) {
        cout << "Y\n";
    } else {
        cout << "N\n";
    }

    return 0;
}
