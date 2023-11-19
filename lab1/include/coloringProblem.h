#ifndef COLORING_PROBLEM_H
#define COLORING_PROBLEM_H

#include <random>

#include "utils.h"

std::pair<int, double> colorizeGraph(std::vector<int> &colors,
                                     std::vector<std::set<int>> &edges,
                                     std::vector<int> &vertices,
                                     bool shuffle = false);
#endif // COLORING_PROBLEM_H