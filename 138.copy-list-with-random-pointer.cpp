
class Solution {
public:
    unordered_map<Node*,Node*> cachedNode;
    Node* copyRandomList(Node* head) {
        if (head==nullptr){
            return nullptr;
        }
        if(! cachedNode.count(head)){
            Node* chead = new Node(head->val);
            cachedNode[head] = chead;
            chead->next = copyRandomList(head->next);
            chead->random = copyRandomList(head->random);
        }
        return cachedNode[head];
    }
};
// @lc code=end

