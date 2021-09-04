class MyLinkedList {

public:
    /** Initialize your data structure here. */
    struct LinkedNode {
        int val;
        LinkedNode* next;
        LinkedNode(int x): val(x), next(nullptr){}
    };
    
    MyLinkedList() {
        _dummyhead = new LinkedNode(0);
        _size = 0;
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if(index > _size-1 || index < 0){
            return -1;
        }
        
        LinkedNode* cur = _dummyhead->next;
        while(index--){
            cur = cur->next;
        }
        
        return cur->val;
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        LinkedNode* node = new LinkedNode(val);
        node->next = _dummyhead->next;
        _dummyhead->next = node;
        _size++;
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        LinkedNode* node = new LinkedNode(val);
        LinkedNode* cur = _dummyhead;
        while(cur->next != nullptr){
            cur = cur->next;
        }
        cur->next = node;
        _size++;
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        LinkedNode* node = new LinkedNode(val);
        LinkedNode* cur = _dummyhead;
        while(index--){
            cur = cur->next;
        }
        node->next = cur->next;
        cur->next = node;
        _size++;
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        //index must be greater or equal to _size because, otherwise, cur will get to nullptr
        if(index>=_size || index<0) return;
        LinkedNode* cur = _dummyhead;
        while(index--){
            cur = cur->next;
        }
        LinkedNode* temp = cur->next;
        cur->next = temp->next;
        _size--;
        delete temp;
    }
private:
    LinkedNode* _dummyhead;
    int _size;
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */