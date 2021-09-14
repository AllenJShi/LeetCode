/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        if(head->next==nullptr) return head;
        
        ListNode* dummyhead = new ListNode();
        dummyhead->next = head;
        ListNode* sorted = head;
        ListNode* cur = head->next;
        while(cur != nullptr){
            if(sorted->val <= cur->val){
                sorted = sorted->next;
            }else{
                ListNode* pre = dummyhead;
                while(pre->next->val <= cur->val){
                    pre = pre->next;
                }
                sorted->next = cur->next;
                cur->next = pre->next;
                pre->next = cur;
            }
            cur = sorted->next;
        }
        return dummyhead->next;
    }
};