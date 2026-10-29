using System;

int[] digits = [9, 9, 9];

bool wszystkie9 = true; // zakladam ze same 9

// od konca bo dodaje od ostatniej cyfry
for (int i = digits.Length - 1; i >= 0; i--)
{
    if (digits[i] == 9)
    {
        digits[i] = 0; // 9 -> 0, przeniesienie dalej
    }
    else
    {
        digits[i]++; // +1 i koniec
        wszystkie9 = false;
        break;
    }
}

// same 9 -> nowa tablica o 1 dluzsza
if (wszystkie9)
{
    digits = new int[digits.Length + 1]; // same zera
    digits[0] = 1;
}

Console.WriteLine(string.Join(", ", digits)); // wypisanie tablicy