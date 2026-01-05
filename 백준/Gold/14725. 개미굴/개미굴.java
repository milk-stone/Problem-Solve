import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Node trie = new Node();

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int K = Integer.parseInt(st.nextToken());
            List<String> list = new ArrayList<>();
            for (int j = 0; j < K; j++) {
                list.add(st.nextToken());
            }
            insert(trie, list);
        }
        StringBuilder sb = new StringBuilder();
        printResult(sb, trie, 0);
        System.out.println(sb.toString());
    }

    private static void insert(Node trie, List<String> inputList){
        Node node = trie;
        for (String item : inputList){
            if (!node.children.containsKey(item)){
                node.children.put(item, new Node());
            }
            node = node.children.get(item);
        }
    }

    private static void printResult(StringBuilder sb, Node trie, int depth) {
        trie.getChildren().entrySet()
                .stream()
                .sorted(Map.Entry.comparingByKey())
                .forEach(entry -> {
                    String key = entry.getKey();
                    Node node = entry.getValue();

                    sb.append("--".repeat(depth));
                    sb.append(key);
                    sb.append("\n");

                    printResult(sb, node, depth + 1);
                });

    }

    static class Node {
        private Map<String, Node> children;

        public Node(){
            this.children = new HashMap<>();
        }

        public Map<String, Node> getChildren() {
            return children;
        }
    }
}
