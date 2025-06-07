import heapq
import time
class BSTNode:
    def __init__(self, key, urls=None, in_memory=True):
        self.key =key
        self.urls= urls
        self.in_memory= in_memory
        self.left =None
        self.right=None
class BST:
    def __init__(self):
        self.root = None
    def insert(self,key,urls=None,in_memory=True):
        if not self.root:
            self.root =BSTNode(key,urls,in_memory)
        else:
            self._insert(self.root, key, urls, in_memory)
    def _insert(self,node,key,urls=None,in_memory=True):
        if key<node.key:
            if node.left:
                self._insert(node.left, key, urls, in_memory)
            else:
                node.left=BSTNode(key, urls, in_memory)
        else:
            if node.right:
                self._insert(node.right, key, urls, in_memory)
            else:
                node.right=BSTNode(key, urls, in_memory)
    def search(self, key):
        return self._search(self.root, key)
    def _search(self, node, key):
        if node is None:
            return None, None
        if key == node.key:
            return node.urls, node.in_memory
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
def parse_search_history(file_path):
    query_counter = {}
    with open(file_path, 'r') as file:
        for line in file:
            query = line.strip()
            if query in query_counter:
                query_counter[query] += 1
            else:
                query_counter[query] = 1
    heap =[]
    for query, count in query_counter.items():
        if len(heap)<10000:
            heapq.heappush(heap, (count,query))
        else:
            heapq.heappushpop(heap, (count, query))
    top_queries = [(query, count) for count, query in heap]
    return top_queries
def parse_search_results(file_path):
    search_results = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(':', 1)
            if len(parts)==2:
                query = parts[0].strip()
                urls = parts[1].strip().split(',')
                search_results[query] = urls
    return search_results
def build_search_engine(history_path, results_path):
    top_queries = parse_search_history(history_path)
    search_results = parse_search_results(results_path)
    bst = BST()
    def balanced_insert(queries, bst, start, end, search_results):
        if start > end:
            return
        mid = (start + end)//2
        query = queries[mid]
        urls = search_results.get(query, [])
        bst.insert(query, urls,in_memory=True)
        balanced_insert(queries, bst, start, mid - 1, search_results)
        balanced_insert(queries, bst, mid + 1, end, search_results)
    query_keys = [q for q, _ in top_queries]
    balanced_insert(query_keys, bst, 0, len(query_keys) - 1, search_results)
    for query in search_results:
        if query not in query_keys:
            with open(f'{query}.txt','w') as f:
                f.write(','.join(search_results[query]))
            bst.insert(query, [],in_memory=False)
    return bst
def handle_query(bst):
    query = input("Please enter the search query: ").strip()
    urls, in_memory = bst.search(query)
    if urls:
        print(f"Output: {', '.join(urls)}")
        source = 'memory' if in_memory else 'file'
        print(f"URLs Read From: {source}")
    elif in_memory is False: 
        try:
            with open(f'{query}.txt', 'r') as file:
                urls = file.read().strip().split(',')
                print(f"Output: {', '.join(urls)}")
                print("URLs Read From: file")
        except FileNotFoundError:
            print("No results found.")
    else:
        print("No results found.")
def profile_queries(bst, queries):
    memory_times = []
    for query in queries:
        start_time = time.time()
        m, in_memory =bst.search(query.strip())
        end_time = time.time()
        if in_memory:
            memory_times.append(end_time - start_time)
    return memory_times
def report_top_queries(top_queries):
    print("Top 50 Search Queries with Probabilities:")
    for query, count in top_queries[:50]:
        print(f"{query.strip()}: {count}")
def main_menu():
    bst = build_search_engine('search-history.txt', 'search-results.txt')
    top_queries = parse_search_history('search-history.txt')
    while True:
        print("Menu:")
        print("1. Search Query")
        print("2. Time Top Queries")
        print("3. Report Top 50 Queries")
        print("4. Exit")
        choice =input("Enter your choice: ")
        if choice =='1':
            handle_query(bst)
        elif choice =='2':
            queries=[]
            for q ,e in top_queries[:20]:
                queries.append(q.strip())
            memory_times= profile_queries(bst, queries)
            print(f"Memory times: {memory_times}")
        elif choice == '3':
            report_top_queries(top_queries)
        elif choice=='4':
            break
        else:
            print("Invalid choice")
main_menu()