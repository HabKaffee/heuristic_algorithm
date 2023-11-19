#include "../include/utils.h"

namespace utils {
void readDIMACSFile(std::string filename, std::vector<std::set<int>> &edges,
                    std::vector<int> &vertices) {
  std::ifstream DIMACSFile(filename);
  if (!DIMACSFile) {
    std::cerr << "Can't open a DIMACS file\n";
    throw std::exception();
  }

  std::string line;
  std::getline(DIMACSFile, line);
  while (line[0] == 'c') {
    std::getline(DIMACSFile, line);
  }
  std::stringstream strStream(line);
  strStream >> line >> line >> line;
  int verticesNum = std::stoi(line);
  strStream >> line;
  int edgesNum = std::stoi(line);
  edges.resize(verticesNum);
  vertices.resize(verticesNum);
  std::iota(vertices.begin(), vertices.end(), 0);

  for (int lineCounter = 0; lineCounter < edgesNum; ++lineCounter) {
    std::getline(DIMACSFile, line);
    std::stringstream lineRepresentation(line);
    lineRepresentation >> line >> line;
    int firstVertex = std::stoi(line) - 1;
    lineRepresentation >> line;
    int secondVertex = std::stoi(line) - 1;
    edges[firstVertex].insert(secondVertex);
    edges[secondVertex].insert(firstVertex);
  }
}

void printAdjustList(std::vector<std::set<int>> &edges,
                     std::vector<int> &vertices) {
  for (int vertex = 0; vertex < edges.size(); ++vertex) {
    std::cout << "[" << vertices[vertex] + 1 << "] = {";
    for (auto connectedVertex = edges[vertices[vertex]].begin();
         connectedVertex != edges[vertices[vertex]].end(); ++connectedVertex) {
      std::cout << (*connectedVertex) + 1 << " ";
    }
    std::cout << "}\n";
  }
}

__attribute__((always_inline)) void
sortVertices(std::vector<int> &vertices, std::vector<std::set<int>> &edges) {
  std::sort(vertices.begin(), vertices.end(), [&](int left, int right) {
    return edges[left].size() > edges[right].size();
  });
}
} // namespace utils