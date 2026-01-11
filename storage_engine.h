#pragma once
#include <fstream>
#include <string>

class StorageEngine
{
public:
    void write(const std::string &chunk, const std::string &data)
    {
        std::ofstream out(chunk, std::ios::binary);
        out << data;
    }

    std::string read(const std::string &chunk)
    {
        std::ifstream in(chunk, std::ios::binary);
        return std::string((std::istreambuf_iterator<char>(in)), std::istreambuf_iterator<char>());
    }
};