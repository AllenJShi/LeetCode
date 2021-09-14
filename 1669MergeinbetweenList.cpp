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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* dummyhead = new ListNode();
        int start = a;
        dummyhead->next = list1;
        while(a>1){
            list1 = list1->next;
            a--;
        }
        ListNode* right = new ListNode();
        right = list1->next;
        list1->next = list2;
        while(b-start>=0){
            right = right->next;
            b--;
        }
        while(list1->next){
            list1 = list1->next;
        }
        list1->next = right;
        return dummyhead->next;
    }
};