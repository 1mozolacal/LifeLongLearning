# Runtime: 881 ms, faster than 6.97% of Python3 online submissions for Merge In Between Linked Lists.
# Memory Usage: 20.3 MB, less than 52.54% of Python3 online submissions for Merge In Between Linked Lists.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # ret_list_head = new ListNode(list1.)

        counter = 0
        counter_node = list1
        while counter < a-1:
            counter_node = counter_node.next
            counter += 1 
        continue_node = counter_node.next
        counter_node.next = list2

        for x in range(b-a+1):
            continue_node = continue_node.next

        list2_head = list2
        while list2_head.next:
            list2_head = list2_head.next
        
        list2_head.next = continue_node

        return list1




    def get_node(self,node,index):
        if index <= 0:
            return node
        if node.next == None:
            return None
        return self.get_node(node.next,index-1)



# Memory limit exceeded


# class Solution:
#     def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
#         # ret_list_head = new ListNode(list1.)

#         l1 = self.node_to_list(list1)
#         l2 = self.node_to_list(list2)

#         combine = l1[:a]
#         combine.extend(l2)
#         combine.extend(l1[b+1:])

#         node_list = self.list_to_node(combine)
#         return node_list
        

#     def list_to_node(self,list):
#         if list == []:
#             return None
#         next_node = self.list_to_node(list[1:])
#         return ListNode(list[0],next_node)

#     def node_to_list(self,node,builder=None):
#         if builder == None:
#             builder = []
#         if node == None:
#             return builder
#         builder.append(node.val)
#         return self.node_to_list(node.next,builder=builder)


#     def get_node(self,node,index):
#         if index <= 0:
#             return node
#         if node.next == None:
#             return None
#         return self.get_node(node.next,index-1)
        