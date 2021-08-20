        bfs 
        O(n)
        O(n) + O(n/2) --> O(n)
        if root is None:
            return 0
        
        min_depth = 0
        q = [root]
                 
        while q:
            lvl_size = len(q)
            min_depth += 1
            for _ in range(lvl_size):
                curr_node = q.pop(0)
                
                #this is leaf
                if not curr_node.left and not curr_node.right:
                    return min_depth
                
                if curr_node.right:
                    q.append(curr_node.right)
                if curr_node.left:
                    q.append(curr_node.left)
    
        return min_depth
    
