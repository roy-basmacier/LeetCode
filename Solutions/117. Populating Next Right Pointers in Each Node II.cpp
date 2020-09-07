/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() {}

    Node(int _val, Node* _left, Node* _right, Node* _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/
class Solution {
public:
    Node* connect(Node* root) 
    {
        helper(root, nullptr);
        return root;
    }
    
    void helper(Node* root, Node* parent)
    {
        if(!root)
            return;
            
        if(parent)
        {
            
        
            //checking if parent has a a right child that isnt the current node
            if (parent->right != nullptr && parent->right != root)
            {
                root->next = parent->right;
            }

            //if the parent has nor right but has a next
            else if ((parent->right == nullptr || parent->right == root) && parent->next != nullptr)
            {
                // traverse all next pointers to find left, right then next
                Node* ptr = parent->next;

                while(ptr)
                {
                    if(ptr->left != nullptr)
                    {
                        root->next = ptr->left;
                        break;
                    }
                    if(ptr->right != nullptr)
                    {
                        root->next = ptr->right;
                        break;
                    }
                    ptr = ptr->next;

                }

            }
        }
        helper(root->right, root);
        helper(root->left, root);

    }
};