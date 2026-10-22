/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans(0);

        function<void(TreeNode*)> print = [&](TreeNode* node) {
            if (node == nullptr) {
                return;
            }

            print(node->left);
            ans.push_back(node->val); 
            print(node->right);      
        };

        print(root);
        return ans;
    }
};