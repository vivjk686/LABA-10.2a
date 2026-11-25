#include "pch.h"
#include "CppUnitTest.h"
#define UNIT_TEST
#include "../LABA-10.2a/LABA-10.2a.cpp"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest102a
{
    TEST_CLASS(UnitTest102a)
    {
    public:
        TEST_METHOD(TestPhysicalSort)
        {
            const int N = 4;
            Student p[N] = {
                { "Andriyenko", 2, KN,  5, 4, 5 },
                { "Zaharchenko",2, INF, 5, 5, 4 },
                { "Boyko",      1, ME,  5, 3, 4 },
                { "Koval",      3, FI,  3, 5, 5 }
            };
            Sort(p, N);
            Assert::AreEqual(string("Koval"), p[0].prizv);       // fiz=3
            Assert::AreEqual(string("Boyko"), p[1].prizv);       // fiz=5, kurs=1
            Assert::AreEqual(string("Zaharchenko"), p[2].prizv); // fiz=5, kurs=2, Z > A
            Assert::AreEqual(string("Andriyenko"), p[3].prizv);  // fiz=5, kurs=2
        }

        TEST_METHOD(TestIndexSort)
        {
            const int N = 4;
            Student p[N] = {
                { "Andriyenko", 2, KN,  5, 4, 5 },
                { "Zaharchenko",2, INF, 5, 5, 4 },
                { "Boyko",      1, ME,  5, 3, 4 },
                { "Koval",      3, FI,  3, 5, 5 }
            };
            int* I = IndexSort(p, N);
            Assert::AreEqual(3, I[0]);
            Assert::AreEqual(2, I[1]);
            Assert::AreEqual(1, I[2]);
            Assert::AreEqual(0, I[3]);
            delete[] I;
        }

        TEST_METHOD(TestBinarySearch)
        {
            const int N = 4;
            Student p[N] = {
                { "Andriyenko", 2, KN,  5, 4, 5 },
                { "Zaharchenko",2, INF, 5, 5, 4 },
                { "Boyko",      1, ME,  5, 3, 4 },
                { "Koval",      3, FI,  3, 5, 5 }
            };
            Sort(p, N);
            Assert::AreEqual(2, BinSearch(p, N, "Zaharchenko", 2, 5));
            Assert::AreEqual(-1, BinSearch(p, N, "NonExistent", 1, 4));
        }
    };
}
