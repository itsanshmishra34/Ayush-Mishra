
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ayush;
        inorder(root, ayush);
        return ayush;
    }

private:
    void inorder(TreeNode* node, vector<int>& ayush) {
        if (node == nullptr) {
            return;
        }

        inorder(node->left, ayush);
        ayush.push_back(node->val);
        inorder(node->right, ayush);
    }
};