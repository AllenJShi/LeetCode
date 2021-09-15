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
    ListNode* sortList(ListNode* head) {
        if(!head) return head;
        int len = 0;
        ListNode* node = head;
        while(node){
            node = node->next;
            len++;
        }
        
        ListNode* dummyhead = new ListNode(0,head);
        
        for(int sublen=1; sublen < len; sublen<<=1){
            ListNode *pre = dummyhead, *cur = dummyhead->next;
            while(cur){
                ListNode *head1 = cur;
                for(int i=1; i<sublen && cur->next; i++){
                    cur = cur->next;
                }
                ListNode *head2 = cur->next;
                cur->next = nullptr;
                cur = head2;
                for(int i=1; i<sublen && cur && cur->next; i++){
                    cur = cur->next;
                }
                ListNode * next = nullptr;
                if(cur){
                    next = cur->next;
                    cur->next = nullptr;
                }
                ListNode* merged = merge(head1, head2);
                pre->next = merged;
                while(pre->next){
                    pre = pre->next;
                }
                cur = next;
            }
        }        
        return dummyhead->next;
    }
    
    ListNode* merge(ListNode* head1, ListNode* head2){
        ListNode* dummyhead = new ListNode();
        ListNode *tmp=dummyhead, *tmp1=head1, *tmp2=head2;
        while(tmp1 && tmp2){
            if(tmp1->val <= tmp2->val){
                tmp->next = tmp1;
                tmp1 = tmp1->next;
            }else{
                tmp->next = tmp2;
                tmp2 = tmp2->next;
            }
            tmp = tmp->next;
        }
        
        if(tmp1){
            tmp->next = tmp1;
        }else if(tmp2){
            tmp->next = tmp2;
        }
        return dummyhead->next;
    }
};