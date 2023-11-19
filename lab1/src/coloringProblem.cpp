#include "../include/coloringProblem.h"

std::pair<int, double> colorizeGraph(std::vector<int> &colors,
                                     std::vector<std::set<int>> &edges,
                                     std::vector<int> &vertices,
                                     bool shuffle) {
  auto begin = std::chrono::high_resolution_clock::now();
  utils::sortVertices(vertices, edges);
  if (shuffle) {
    int maxDegree = edges[0].size();
    std::vector<int> degrees;
    for (auto &edge : edges) {
      degrees.emplace_back(edge.size());
    }
    std::vector<int> indices(degrees.begin(), degrees.end());
    std::iota(indices.begin(), indices.end(), 0);
    std::random_device rd;
    std::mt19937 randGenerator(rd());

    while (maxDegree > 0) {
      auto startShuffle = std::find(degrees.begin(), degrees.end(), maxDegree);
      if (startShuffle == degrees.end()) {
        --maxDegree;
        continue;
      }
      auto endShuffle = std::find(startShuffle, degrees.end(), maxDegree - 1);
      // Shuffle indices
      std::shuffle(indices.begin() + std::distance(degrees.begin(), startShuffle), 
                   indices.begin() + std::distance(degrees.begin(), endShuffle),
                   randGenerator);
      // Apply shuffle
      for (int i = std::distance(degrees.begin(), startShuffle); i < std::distance(degrees.begin(), endShuffle); ++i) {
        std::swap(edges[i], edges[indices[i]]);
        std::swap(vertices[i], vertices[indices[i]]);
      }
      --maxDegree;
    }
  }
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