#include "../include/utils.h"

namespace utils {
void readDIMACSFile(std::string filename,
                    std::map<int, std::vector<int>> &edges) {
  std::ifstream DIMACSFile(filename);
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
  for (int lineCounter = 0; lineCounter < edgesNum; ++lineCounter) {
    std::getline(DIMACSFile, line);
    std::stringstream lineRepresentation(line);
    lineRepresentation >> line >> line;
    int firstVertex = std::stoi(line);
    lineRepresentation >> line;
    int secondVertex = std::stoi(line);
    if (!edges.count(firstVertex)) {
      edges.insert(
          std::pair<int, std::vector<int>>(firstVertex, std::vector<int>()));
    }
    edges[firstVertex].push_back(secondVertex);
  }
}

void printAdjustList(std::map<int, std::vector<int>> &adjList) {
  for (auto adjListEl = adjList.begin(); adjListEl != adjList.end();
       ++adjListEl) {
    std::cout << "[" << adjListEl->first << "] = {";
    for (auto connectedVertex = adjListEl->second.begin();
         connectedVertex != adjListEl->second.end(); ++connectedVertex) {
      std::cout << *connectedVertex << " ";
    }
    std::cout << "}\n";
  }
}
} // namespace utils