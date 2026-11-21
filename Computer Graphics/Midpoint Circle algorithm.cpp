
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int r;
    cout << "Enter radius: ";
    cin >> r;

    if (r <= 0) {
        cout << "Radius must be positive.";
        return 0;
    }

    int size = 2 * r + 1;
    vector<vector<char>> grid(size, vector<char>(size, ' '));

    int xc = r, yc = r;
    int x = 0, y = r;
    int p = 1 - r;

    while (x <= y)
    {
        grid[yc + y][xc + x] = '*';
        grid[yc + y][xc - x] = '*';
        grid[yc - y][xc + x] = '*';
        grid[yc - y][xc - x] = '*';

        grid[yc + x][xc + y] = '*';
        grid[yc + x][xc - y] = '*';
        grid[yc - x][xc + y] = '*';
        grid[yc - x][xc - y] = '*';

        x++;

        if (p < 0)
        {
            p += 2 * x + 1;
        }
        else
        {
            y--;
            p += 2 * (x - y) + 1;
        }
    }

    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
            cout << grid[i][j] << ' ';
        cout << endl;
    }

    return 0;
}
