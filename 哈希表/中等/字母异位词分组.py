'''
49. 字母异位词分组
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。



示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

解释：

在 strs 中没有字符串可以通过重新排列来形成 "bat"。
字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。
示例 2:

输入: strs = [""]

输出: [[""]]

示例 3:

输入: strs = ["a"]

输出: [["a"]]



提示：

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #创建存储字典
        dict = {}
        #遍历每个词
        for word in strs:
            #生成对应键（sorted后的当前词）
            key = ''.join(sorted(word))
            #是新词
            if key not in dict:
                #生成对应的键和值（为新词生成空列表，存储当前词与后续的异位词）
                dict[key] = []
            #分类异位词（添加到对应键的值列表）
            dict[key].append(word)
        #返回转化成列表的字典的分类后的异位词值列表）
        return list(dict.values())