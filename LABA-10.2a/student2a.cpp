#include "student2a.h"
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <string>

using namespace std;

const string specialnistStr[] = {
    "Комп'ютерні науки",
    "Інформатика",
    "Математика та економіка",
    "Фізика та інформатика",
    "Трудове навчання"
};

void Create(Student* p, int N)
{
    int ispec;
    for (int i = 0; i < N; i++)
    {
        cout << "Студент № " << i + 1 << ":" << endl;
        cin.get();
        cin.sync();

        cout << "  прізвище: "; getline(cin, p[i].prizv);
        cout << "  курс: "; cin >> p[i].kurs;
        cout << "  спеціальність (0 - Комп'ютерні науки, 1 - Інформатика, 2 - Математика та економіка, 3 - Фізика та інформатика, 4 - Трудове навчання): ";
        cin >> ispec;
        if (ispec < 0 || ispec > 4) ispec = 0;
        p[i].spec = (Specialnist)ispec;
        cout << "  оцінка з фізики: "; cin >> p[i].physics;
        cout << "  оцінка з математики: "; cin >> p[i].math;
        cout << "  оцінка з інформатики: "; cin >> p[i].it;
        cout << endl;
    }
}

void Print(const Student* p, int N)
{
    cout << "==========================================================================================" << endl;
    cout << "| №   | Прізвище       | Курс | Спеціальність           | Фізика | Математика | Інформатика |" << endl;
    cout << "------------------------------------------------------------------------------------------" << endl;
    for (int i = 0; i < N; i++)
    {
        cout << "| " << setw(3) << right << i + 1 << " ";
        cout << "| " << setw(14) << left << p[i].prizv << " ";
        cout << "| " << setw(4) << right << p[i].kurs << " ";
        cout << "| " << setw(23) << left << specialnistStr[p[i].spec] << " ";
        cout << "| " << setw(6) << right << p[i].physics << " ";
        cout << "| " << setw(10) << right << p[i].math << " ";
        cout << "| " << setw(11) << right << p[i].it << " |" << endl;
    }
    cout << "==========================================================================================" << endl;
    cout << endl;
}

bool compareStudents(const Student& a, const Student& b)
{
    if (a.physics != b.physics) return a.physics < b.physics;
    if (a.kurs != b.kurs) return a.kurs < b.kurs;
    return a.prizv > b.prizv;
}

void PhysicalSort(Student* p, int N)
{
    for (int i = 0; i < N - 1; i++)
    {
        for (int j = 0; j < N - i - 1; j++)
        {
            if (compareStudents(p[j + 1], p[j]))
            {
                swap(p[j], p[j + 1]);
            }
        }
    }
}

void BuildIndexArray(const Student* p, int N, int* idx)
{
    for (int i = 0; i < N; i++)
    {
        idx[i] = i;
    }
    for (int i = 0; i < N - 1; i++)
    {
        for (int j = 0; j < N - i - 1; j++)
        {
            if (compareStudents(p[idx[j + 1]], p[idx[j]]))
            {
                swap(idx[j], idx[j + 1]);
            }
        }
    }
}

void PrintWithIndex(const Student* p, int N, const int* idx)
{
    cout << "==========================================================================================" << endl;
    cout << "| №   | Прізвище       | Курс | Спеціальність           | Фізика | Математика | Інформатика |" << endl;
    cout << "------------------------------------------------------------------------------------------" << endl;
    for (int i = 0; i < N; i++)
    {
        int k = idx[i];
        cout << "| " << setw(3) << right << i + 1 << " ";
        cout << "| " << setw(14) << left << p[k].prizv << " ";
        cout << "| " << setw(4) << right << p[k].kurs << " ";
        cout << "| " << setw(23) << left << specialnistStr[p[k].spec] << " ";
        cout << "| " << setw(6) << right << p[k].physics << " ";
        cout << "| " << setw(10) << right << p[k].math << " ";
        cout << "| " << setw(11) << right << p[k].it << " |" << endl;
    }
    cout << "==========================================================================================" << endl;
    cout << endl;
}

int BinarySearch(const Student* p, int N, const string& prizv, unsigned kurs, int physics)
{
    int left = 0;
    int right = N - 1;
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        if (p[mid].physics == physics && p[mid].kurs == kurs && p[mid].prizv == prizv)
        {
            return mid;
        }

        bool targetBeforeMid = false;
        if (physics != p[mid].physics)
            targetBeforeMid = (physics < p[mid].physics);
        else if (kurs != p[mid].kurs)
            targetBeforeMid = (kurs < p[mid].kurs);
        else
            targetBeforeMid = (prizv > p[mid].prizv);

        if (targetBeforeMid)
            right = mid - 1;
        else
            left = mid + 1;
    }
    return -1;
}
