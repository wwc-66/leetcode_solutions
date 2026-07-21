'''
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。



示例 1：


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]


提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
'''

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #设置哑节点
        dummy = ListNode(0)
        #当前节点初始化为哑节点
        current = dummy
        #当两个链表都还有元素时
        while list1 and list2:
            #当前节点按照大小顺序前进，连接两个链表
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        #如果其中较短链表已经全部连接好，则把另一链表加到连接链表尾部
        current.next = list1 if list1 else list2
        #返回哑节点的next节点，即需要的结果链表
        return dummy.next