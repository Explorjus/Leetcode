using System;

string s = "Hello world";
int dlugosc = 0;

int i = s.Length - 1;

while (i >= 0 && s[i] == ' ')
{
	i--;
}


while (i >= 0 && s[i] != ' ')
{
	dlugosc++;
	i--;
}

Console.WriteLine(dlugosc);