# Fleury-s_Algorithm
A partir de um vertice inicial:
1. Verifica quantos caminhos partem deste vertice;
2. * Se houver apenas um caminho: Passa por ele;
   * Se houver multiplos caminhos: Passa pelo primeiro que não é uma ponte;
   * Se não houver caminhos: Vai para saida;
3. Apagar a aresta utilizada;
4. Volta para 1.

Saida. Imprime o caminho Euleriano

---

From an initial vertex:
1. Check how many paths start from this vertex;
2. * If there is only one path: Go through it;
   * If there are multiple paths: Go through the first one that is not a bridge;
   * If there are no paths: Go to exit;
3. Delete the used edge;
4. Returns to 1.

Exit. Print the Eulerian path
