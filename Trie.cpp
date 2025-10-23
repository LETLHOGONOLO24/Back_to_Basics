/*

PROBLEM


Design and implement a Trie that supports the following operations:
insert(word) — inserts a word into the trie.

search(word) — returns true if the word is in the trie.
startsWith(prefix) — returns true if there is any word that starts
with the given prefix.

EXAMPLE

Input:
insert("apple")
search("apple")   → true

search("app")     → false
startsWith("app") → true

insert("app")
search("app")     → true


STEPS


1 - Each node stores: A hash map children that maps character → next
    node. 
    - A boolean isEndOfWord that marks if a word ends here.

2 - Trie() { root = new TrieNode(); } Initializes the Trie with an
    empty root node.
3 - void insert(string word) { For every character: If it doesn’t
    exist, create a new node. or Move to that node. After the loop,
    mark the end node as the end of a word.

4 - 





*/

#include <iostream>
#include <unordered_map>
using namespace std;

class TrieNode {
    public:
        unordered_map<char, TrieNode*> children;
        bool isEndOfWord;

        TrieNode() {
            isEndOfWord = false;
        }
};

class Trie {
    private:
        TrieNode* root;

    public:
        Trie() {
            root = new TrieNode();
        }

        void insert(string word) {
            TrieNode* node = root;

            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isEndOfWord = true;
        }

        bool search(string word) {
            TrieNode* node = root;

            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    return false;
                }
                node = node->children[c];
            }
            return node->isEndOfWord;
        }

        bool startsWith(string prefix) {
            TrieNode* node = root;

            for (char c : prefix) {
                if (node->children.find(c) == node->children.end()) {
                    return false;
                }
                node = node->children[c];
            }
            return true;
        }
};

int main() {
    Trie trie;
    trie.insert("apple");

    cout << trie.search("apple") << endl;
    cout << trie.search("app") << endl;
    cout << trie.startsWith("app") << endl;
    trie.insert("app");
    cout << trie.search("app") << endl;
}