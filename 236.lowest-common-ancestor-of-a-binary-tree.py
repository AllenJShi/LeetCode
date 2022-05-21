#
# @lc app=leetcode id=236 lang=python
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
    
        ################### 我的答案 ############
        ## 通过观察前序和后序遍历的规律，
        # 若p，q在两个遍历中出现的顺序相反，证明他们是在同一棵树的一条branch上
        # 因为对于前序来说，每一个点之前的点都是该点的祖先
        # 对于后序来说，该点之后的点为其祖先
        # 若两点顺序刚好相反，说明一个点一定是另一个点的祖先，两者一定在一棵树上
        # 然后我们只需要对应其在前序或后续中的相对位置，前序中，在前面的是祖先，后续中，相反
        ## 若两点的相对位置相同，那么说明两点在不同的树上
        # 所以我们在前序中取出该点之前的所有的点，后续中则是该点之后的所有点，构成祖先
        # 这两个祖先数列长度必然相同
        # 然后开始同时比较两个数列，找出最接近的祖先
        # 方法：前序祖先数列，从后往前找，因为越往后越靠近pq
        # 后序祖先数列，从前往后找，因为越靠前越接近pq
        
        # pre = []
        # post = []
        # def preorder(node):
        #     if node:
        #         pre.append(node)
        #         preorder(node.left)
        #         preorder(node.right)
        
        # def postorder(node):
        #     if node:
        #         postorder(node.left)
        #         postorder(node.right)
        #         post.append(node)
        
        # preorder(root)
        # postorder(root)
        
        # idx_pre = 0
        # idx_post = len(post) - 1
        # p_idx_pre, p_idx_post, q_idx_pre, q_idx_post = 0,0,0,0
        # while 0 <= idx_pre < len(pre) \
        #     and 0 <= idx_post < len(post):
        #     if pre[idx_pre]==p:
        #         p_idx_pre = idx_pre
        #     if pre[idx_pre]==q:
        #         q_idx_pre = idx_pre
        #     if post[idx_post]==p:
        #         p_idx_post = idx_post
        #     if post[idx_post]==q:
        #         q_idx_post = idx_post
        #     idx_pre += 1
        #     idx_post -= 1
        # if (p_idx_pre < q_idx_pre and p_idx_post > q_idx_post):
        #     return pre[p_idx_pre]
        # if (p_idx_pre > q_idx_pre and p_idx_post < q_idx_post):
        #     return pre[q_idx_pre]
        
        # ancestor_pre = pre[0:min(p_idx_pre,q_idx_pre)]
        # ancestor_post = post[max(p_idx_post,q_idx_post)+1:]
        # # print(len(ancestor_pre))
        # # print(len(ancestor_post))

        # for i in range(len(ancestor_pre)-1,0-1,-1):
        #     for j in range(len(ancestor_post)):
        #         if ancestor_pre[i] == ancestor_post[j]:
        #             return ancestor_pre[i]
        
        
        ############# 参考答案 ##################
        
        if not root or root==p or root==q: return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        # # 1.左右都为空(归并到2，3情况中)
        # if not left and not right: return
        # 2.左子树为空
        if not left: return right
        # 3.右子树为空
        if not right: return left
        # 4.左右都不为空，root即为公共祖先
        return root
    
        # time O(n) | space O(n)
        
# @lc code=end

