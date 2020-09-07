/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) 
    {
        if (!head)
            return true;
        //finding center shifted by one of list 
        ListNode *prv_center = nullptr;
        ListNode *center = head;
        ListNode *ptr = head;
        
        while (ptr)
        {
            prv_center = center;
            center = center->next;
            ptr = ptr->next;
            if (ptr)
                ptr = ptr->next;
        }
        
        //reversing the sublist starting from center to end
        ListNode *prev = nullptr;
        ListNode *next = nullptr;
        ListNode *current = center;
        
        while(current)
        {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;    
        }
        prv_center->next = prev;
        center = prev;
        
        //checking if polindrome
        ptr = head;
        while(center)
        {
            if(center->val != ptr->val)
                return false;
            center = center->next;
            ptr = ptr->next;
        }
        
        
        
        return true;
    }
};
