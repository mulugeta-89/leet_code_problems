/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head){
    if(head == NULL){
        return head;
    }
    struct ListNode*curr = head;
    while(curr->next != NULL){
        if(curr->val == curr->next->val){
            struct ListNode*next_next = curr->next->next;
            struct ListNode *tobe_deleted = curr->next;
            free(tobe_deleted);
            curr->next = next_next;
        }
        else{
            curr = curr->next;
        }
    }
    return head;

}