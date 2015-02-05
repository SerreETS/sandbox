// 'Hello World!' program
#include <iostream>

int main()
{
	std::cout << "Hello World!" << std::endl;
#ifdef WINDOWS
	std::cin.get();
#endif

	return 0;
}
