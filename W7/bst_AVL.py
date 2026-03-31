class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1 # New node is initially added at leaf

    def height(node):
        if not node:
            return 0
        return node.height
    
    def get_balance(node):
        if not node:
            return 0
        return height(node.left) - height(node.right)
    
    def right_rotate(z):
        y = z.left
        T3 = y.right
        # Perform rotation
        y.right = z
        z.left = T3
        # Update heights
        z.height = 1 + max(height(z.left), height(z.right))
        y.height = 1 + max(height(y.left), height(y.right))
        # Return new root
        return y
    
    def left_rotate(z):
        y = z.right
        T2 = y.left
        # Perform rotation
        y.left = z
        z.right = T2
        # Update heights
        z.height = 1 + max(height(z.left), height(z.right))
        y.height = 1 + max(height(y.left), height(y.right))
        # Return new root
        return y
    
    def insert_avl(node, key):
        # 1. Perform standard BST insert
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = insert_avl(node.left, key)
        else:
            node.right = insert_avl(node.right, key)

        # 2. Update height
        node.height = 1 + max(height(node.left), height(node.right))

        # 3. Get balance factor
        balance = get_balance(node)

        # 4.Check for imbalance and do rotations
        
        # Left Left Case
        if balance > 1 and key < node.left.key:
            return right_rotate(node)
        
        # Right Right Case
        if balance < -1 and key > node.right.key:
            return left_rotate(node)
        
        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = left_rotate(node.left)
            return right_rotate(node)
        
        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = right_rotate(node.right)
            return left_rotate(node)
        
        return node
