#include "../include/coloringProblem.h"

std::pair<int, double> colorizeGraph(std::vector<int> &colors,
                                     std::vector<std::set<int>> &edges,
                                     std::vector<int> &vertices) {
  auto begin = std::chrono::high_resolution_clock::now();
  utils::sortVertices(vertices, edges);
  int maxColor = 0;
  for (auto vertex : vertices) {
    if (colors[vertex]) {
      continue;
    }
    ++maxColor;
    std::set<int> banned(edges[vertex]);
    colors[vertex] = maxColor;
    for (int node = 0; node < edges.size(); ++node) {
      if (colors[node] || banned.count(node))
        continue;
      colors[node] = maxColor;
      banned.insert(edges[node].begin(), edges[node].end());
    }
  }
  auto end = std::chrono::high_resolution_clock::now();
  double elapledTime = (std::chrono::duration<double, std::milli>(end - begin).count()) * 10e-3;
  return std::pair<int, double>(maxColor, elapledTime);
}