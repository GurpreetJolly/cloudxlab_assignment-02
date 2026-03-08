class DecisionTreeNode:
    def __init__(self, att, attv, left=None, right=None):
        self.att = att
        self.attv = attv
        if left:
            self.left = left
        else:
            self.left = NoNode()
        if right:
            self.right = right
        else:
            self.right = YesNode()
            
    def check(self, jd):
        if jd[self.att] < self.attv:
            return self.left.check(jd)
        else:
            return self.right.check(jd)

class YesNode(DecisionTreeNode):
    def __init__(self):
        pass
    def check(self, jd):
        return True

class NoNode(DecisionTreeNode):
    def __init__(self):
        pass
    def check(self, jd):
        return False

def main():
    # The following code creates decision tree shown below in the comments.
    nightshift_1 = DecisionTreeNode("is_nightshift", 1, YesNode(), NoNode())
    nightshift_2 = DecisionTreeNode("is_nightshift", 1, YesNode(), YesNode())
    coffee = DecisionTreeNode("coffee", 1, nightshift_1, nightshift_2)
    distance =  DecisionTreeNode("distance", 10, coffee, NoNode())
    tree = DecisionTreeNode("salary", 20000, distance, YesNode())

    # Test the decision tree with a job offer
    job_offer = {'salary': 19000, 'distance': 9, 'coffee': 0, 'is_nightshift': 1}
    decision = tree.check(job_offer)
    print(f"Decision for the job offer {job_offer}: {'Accept' if decision else 'Reject'}")

    job_offer = {'salary': 19000, 'distance': 12}
    decision = tree.check(job_offer)
    print(f"Decision for the job offer {job_offer}: {'Accept' if decision else 'Reject'}")

    job_offer = {'salary': 19000, 'distance': 9, 'coffee': 0, 'is_nightshift': 0}
    decision = tree.check(job_offer)
    print(f"Decision for the job offer {job_offer}: {'Accept' if decision else 'Reject'}")

if __name__ == "__main__":
    main()

#                                    (<20k)   Salary   (>=20k)
#                                  -------------------------------
#                                  /                             \
#                          (<10) distance (>=10)                 Yes
#                        ------------------------
#                        /                      \                 
#             (<1)    coffee   (>=1)            No
#            ------------------------
#             /                    \
#   (<1) is_nightshift (>=1)   (<1) is_nightshift (>=1)
#   -------------------------  --------------------------
#    /                     \           /            \
#  Yes                     No         Yes           Yes
#
