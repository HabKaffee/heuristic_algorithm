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
    if (filename.empty()) {
      break;
    }
    std::vector<std::set<int>> edges;
    std::vector<int> vertices;
    utils::readDIMACSFile(filename, edges, vertices);
    std::vector<int> colors(vertices.size(), 0);
    auto colorizationResult = colorizeGraph(colors, edges, vertices);
    std::cout << filename << " <========================================\n";
    std::cout << "========================= Greedy coloring =============================\n";
    std::cout << colorizationResult.first << " " << colorizationResult.second << std::endl;
    // std::cout << "========================================================================\n";
    std::fill(colors.begin(), colors.end(), 0);
    colorizationResult = colorizeGraph(colors, edges, vertices, true);
    // utils::printAdjustList(edges, vertices);
    std::cout << "======================= Randomized coloring ============================\n";
    std::cout << colorizationResult.first << " " << colorizationResult.second << std::endl;
    std::cout << "========================================================================\n";
    
  }

  return 0;
}