'''
61. 旋转链表
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。



示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
示例 2：


输入：head = [0,1,2], k = 4
输出：[2,0,1]


提示：

链表中节点的数目在范围 [0, 500] 内
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #如果链表为空或仅含一个节点
        if not head or not head.next:
            return head

        #初始化变量：快慢指针，当前节点，链表长度
        slow = head
        fast = head
        cur = head
        leng = 0

        #计算链表长度
        while cur:
            leng += 1
            cur = cur.next

        #对长度取模
        k %= leng
        #如果取模后为0，则说明恰好为完整循环，直接返回原链表
        if k == 0:
            return head

        for i in range(k):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        newHead = slow.next
        fast.next = head
        slow.next = None
        return newHead