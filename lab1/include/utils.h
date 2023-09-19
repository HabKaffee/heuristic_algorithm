#ifndef UTILS_H
#define UTILS_H

#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

namespace utils {

void readDIMACSFile(std::string filename,
                    std::map<int, std::vector<int>> &edges);
void printAdjustList(std::map<int, std::vector<int>> &edges);
} // namespace utils
#endif // UTILS_H