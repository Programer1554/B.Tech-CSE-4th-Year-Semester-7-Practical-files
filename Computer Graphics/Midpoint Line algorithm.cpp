#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

int main()
{
    int x1, y1, x2, y2;

    cout << "Enter starting point (x1, y1): ";
    cin >> x1 >> y1;

    cout << "Enter ending point (x2, y2): ";
    cin >> x2 >> y2;

    int originalX1 = x1, originalY1 = y1;
    int originalX2 = x2, originalY2 = y2;

    // Check whether the line is steep
    bool steep = abs(y2 - y1) > abs(x2 - x1);

    if (steep)
    {
        swap(x1, y1);
        swap(x2, y2);
    }

    // Ensure that x1 is the left endpoint
    if (x1 > x2)
    {
        swap(x1, x2);
        swap(y1, y2);
    }

    int dx = x2 - x1;
    int dy = abs(y2 - y1);

    int p = 2 * dy - dx;
    int yStep = (y1 < y2) ? 1 : -1;
    int y = y1;

    // Store generated points
    vector<pair<int, int>> points;

    for (int x = x1; x <= x2; x++)
    {
        if (steep)
            points.push_back({y, x});
        else
            points.push_back({x, y});

        if (p >= 0)
        {
            y += yStep;
            p -= 2 * dx;
        }

        p += 2 * dy;
    }

    // Find display boundaries
    int minX = min(originalX1, originalX2);
    int maxX = max(originalX1, originalX2);
    int minY = min(originalY1, originalY2);
    int maxY = max(originalY1, originalY2);

    vector<vector<char>> screen(
        maxY - minY + 1,
        vector<char>(maxX - minX + 1, ' ')
    );

    for (auto point : points)
    {
        int px = point.first - minX;
        int py = maxY - point.second;
        screen[py][px] = '*';
    }

    cout << "\nLine drawing:\n\n";

    for (int i = 0; i < screen.size(); i++)
    {
        for (int j = 0; j < screen[i].size(); j++)
            cout << screen[i][j] << ' ';
        cout << '\n';
    }

    cout << "\nGenerated points:\n";
    for (auto point : points)
        cout << "(" << point.first << ", "
             << point.second << ") ";

    cout << endl;

    return 0;
}
