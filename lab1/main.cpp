#include "include/utils.h"

int main () {
    std::string filename = "test_data/myciel3.col";
    std::map<int, std::vector<int>> edges;
    utils::readDIMACSFile(filename, edges);
    utils::printAdjustList(edges);
    return 0;
}