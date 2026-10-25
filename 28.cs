using System;

string word = "sadbutsad";
string needle = "sad";

if (word.Contains(needle))
{
    Console.WriteLine(word.IndexOf(needle));
}
else
{
    Console.WriteLine(-1);
}


