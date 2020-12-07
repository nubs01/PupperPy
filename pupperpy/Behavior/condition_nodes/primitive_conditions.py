import py_trees
import time


class FrontObstacleNode(py_trees.behaviour.Behaviour):
    """
    Primitive condition that senses if an object is in front of the robot.
    """

    def __init__(self, obstacle_data=None):
        super(ObstacleDetectNode, self).__init__(
            "Detect Front Obstacle")
        this.obstacle_data = obstacle_data

    def setup(self):
        return

    def initialise(self):
        return

    def update(self):
        if obstacle_data.front:
            self.feedback_message = "Detected front obstacle!"
            return py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = "No obstacles..."
            print(self.name)
            # update command interface
            return py_trees.common.Status.RUNNING

    def terminate(self, new_status):
        return


class LeftObstacleNode(py_trees.behaviour.Behaviour):
    """
    Primitive condition that senses if an object is to the right of the robot.
    """

    def __init__(self, obstacle_data=None):
        super(LeftObstacleNode, self).__init__(
            "Detect Left Obstacle")
        this.obstacle_data = obstacle_data

    def setup(self):
        return

    def initialise(self):
        return

    def update(self):
        if obstacle_data.left:
            self.feedback_message = "Detected left obstacle!"
            return py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = "No obstacles..."
            print(self.name)
            # update command interface
            return py_trees.common.Status.RUNNING

    def terminate(self, new_status):
        return


class RightObstacleNode(py_trees.behaviour.Behaviour):
    """
    Primitive condition that senses if an object is to the left of the robot.
    """

    def __init__(self, obstacle_data=None):
        super(RightObstacleNode, self).__init__(
            "Detect Right Obstacle")
        this.obstacle_data = obstacle_data

    def setup(self):
        return

    def initialise(self):
        return

    def update(self):
        if obstacle_data.left:
            self.feedback_message = "Detected right obstacle!"
            return py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = "No obstacles..."
            print(self.name)
            # update command interface
            return py_trees.common.Status.RUNNING

    def terminate(self, new_status):
        return


class TargetFoundNode(py_trees.behaviour.Behaviour):
    """
    Primitive condition that senses if a ball is in sight.
    """

    def __init__(self, obstacle_data=None):
        super(LeftObstacleNode, self).__init__(
            "Detect Target Found")
        this.vision_data = vision_data

    def setup(self):
        return

    def initialise(self):
        return

    def update(self):
        if vision_data.bbox_confidence:
            self.feedback_message = "Detected ball!"
            return py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = "Still looking..."
            print(self.name)
            # update command interface
            return py_trees.common.Status.RUNNING

    def terminate(self, new_status):
        return
