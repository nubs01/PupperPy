import py_trees


class TreeStateHandler():
    """
    Keeps track of the active node and what commands are supposed to be sent based off which node is running.
    """

    def __init__(self, control):
        self.node_count = 0
        self.active_node = None
        self.control = control
        self.node_id_dict = {}

    """
    def update_data(self):
        self.control.update_data()
    """

    # hack get into pre tick
    def update_data(self, tree):
        if self.active_node:
            print(self.node_id_dict[self.active_node])
            self.control.active_node = self.node_id_dict[self.active_node]
        self.control.update_data()

    def set_active_node(self, node):
        if not self.active_node == node:
            self.active_node = node
            print("Active node is now: " +
                  str(self.node_id_dict[self.active_node]))

    def get_active_node_id(self):
        return self.node_id_dict[self.active_node]
