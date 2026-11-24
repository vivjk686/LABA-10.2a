#include "pch.h"
#include "CppUnitTest.h"
#include "../LABA-10.2a/student2a.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest102a
{
    TEST_CLASS(UnitTest102a)
    {
    public:
        TEST_METHOD(TestPhysicalSort)
        {
            const int N = 4;
            Student students[N] = {
                { "Коваленко", 1, KOMP_NAUKY,  5, 5, 5 },
                { "Іваненко",  2, INFORMATYKA, 4, 4, 4 },
                { "Петренко",  1, MAT_EKON,    3, 5, 4 },
                { "Сидоренко", 1, FIZ_INF,     5, 3, 5 }
            };

            PhysicalSort(students, N);

            // Expected order (physics asc, kurs asc, prizv desc):
            // 0: Петренко  (phys 3, kurs 1)
            // 1: Іваненко  (phys 4, kurs 2)
            // 2: Сидоренко (phys 5, kurs 1, "Сидоренко" > "Коваленко")
            // 3: Коваленко (phys 5, kurs 1)
            Assert::AreEqual(std::string("Петренко"), students[0].prizv);
            Assert::AreEqual(std::string("Іваненко"), students[1].prizv);
            Assert::AreEqual(std::string("Сидоренко"), students[2].prizv);
            Assert::AreEqual(std::string("Коваленко"), students[3].prizv);
        }

        TEST_METHOD(TestIndexSort)
        {
            const int N = 4;
            Student students[N] = {
                { "Коваленко", 1, KOMP_NAUKY,  5, 5, 5 },
                { "Іваненко",  2, INFORMATYKA, 4, 4, 4 },
                { "Петренко",  1, MAT_EKON,    3, 5, 4 },
                { "Сидоренко", 1, FIZ_INF,     5, 3, 5 }
            };

            int idx[N] = { 0 };
            BuildIndexArray(students, N, idx);

            Assert::AreEqual(2, idx[0]); // Петренко
            Assert::AreEqual(1, idx[1]); // Іваненко
            Assert::AreEqual(3, idx[2]); // Сидоренко
            Assert::AreEqual(0, idx[3]); // Коваленко
        }

        TEST_METHOD(TestBinarySearch)
        {
            const int N = 4;
            Student students[N] = {
                { "Коваленко", 1, KOMP_NAUKY,  5, 5, 5 },
                { "Іваненко",  2, INFORMATYKA, 4, 4, 4 },
                { "Петренко",  1, MAT_EKON,    3, 5, 4 },
                { "Сидоренко", 1, FIZ_INF,     5, 3, 5 }
            };

            PhysicalSort(students, N);

            int pos1 = BinarySearch(students, N, "Сидоренко", 1, 5);
            Assert::AreEqual(2, pos1);

            int pos2 = BinarySearch(students, N, "Петренко", 1, 3);
            Assert::AreEqual(0, pos2);

            int notFound = BinarySearch(students, N, "Мельник", 2, 4);
            Assert::AreEqual(-1, notFound);
        }
    };
}
