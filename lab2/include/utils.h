#ifndef UTILS_H
#define UTILS_H

#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <chrono>

namespace utils {

void readDIMACSFile(std::string filename, std::vector<std::set<int>> &edges,
                    std::vector<int> &vertices);
void printAdjustList(std::vector<std::set<int>> &edges,
                     std::vector<int> &vertices);
void sortVertices(std::vector<int> &vertices,
                  std::vector<std::set<int>> &edges);
} // namespace utils
#endif // UTILS_H