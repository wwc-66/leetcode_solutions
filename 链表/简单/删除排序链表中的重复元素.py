'''
83. 删除排序链表中的重复元素
给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。



示例 1：


输入：head = [1,1,2]
输出：[1,2]
示例 2：


输入：head = [1,1,2,3,3]
输出：[1,2,3]


提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序 排列
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #如果头节点为空，返回None
        if not head:
            return None
        #当前节点初始化为head头节点
        current = head
        #当前节点的next不为None时
        while current.next:
            #如果有重复值（next），则跳过next，指针指向下下一个节点
            if current.val == current.next.val:
                current.next = current.next.next
            #无重复值，当前节点继续前进
            else:
                current = current.next
        #返回去重后的链表
        return head