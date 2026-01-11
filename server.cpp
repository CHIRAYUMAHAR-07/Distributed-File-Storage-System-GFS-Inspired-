#include "storage_engine.h"
#include <iostream>

int main()
{
    StorageEngine engine;
    engine.write("chunk-0", "hello world");
    std::cout << engine.read("chunk-0") << std::endl;
    return 0;
}