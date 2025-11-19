'''
LCR 140. 训练计划 II
给定一个头节点为 head 的链表用于记录一系列核心肌群训练项目编号，请查找并返回倒数第 cnt 个训练项目编号。



示例 1：

输入：head = [2,4,7,8], cnt = 1
输出：8


提示：

1 <= head.length <= 100
0 <= head[i] <= 100
1 <= cnt <= head.length
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        #初始化快慢指针
        fast = head
        slow = head
        #快指针先跑出cnt步
        for i in range(cnt):
            fast = fast.next

        #快慢指针同步前进，当快指针遍历完整条链表，慢指针正处在指定的倒数第cnt个节点
        while fast:
            slow = slow.next
            fast = fast.next

        return slow