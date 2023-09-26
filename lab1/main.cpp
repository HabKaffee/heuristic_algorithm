#include "include/coloringProblem.h"
#include "include/utils.h"

int main() {
  std::array<std::string, 10> filenames = {
    "test_data/myciel3.col",
    "test_data/myciel7.col",
    "test_data/school1.col",
    "test_data/school1_nsh.col",
    "test_data/anna.col",
    "test_data/miles1000.col",
    "test_data/miles1500.col",
    "test_data/le450_5a.col",
    "test_data/le450_15b.col",
    "test_data/queen11_11.col"
  };
  for (auto filename : filenames) {
    std::vector<std::set<int>> edges;
    std::vector<int> vertices;
    utils::readDIMACSFile(filename, edges, vertices);
    std::vector<int> colors(vertices.size(), 0);
    auto pr = colorizeGraph(colors, edges, vertices);
    std::cout << filename << " " << pr.first << " " << pr.second << std::endl;
  }

  return 0;
}