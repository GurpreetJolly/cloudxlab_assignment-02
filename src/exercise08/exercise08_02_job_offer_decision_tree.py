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
    distance =  DecisionTreeNode("distance", 10, YesNode(), NoNode())
    wfh = DecisionTreeNode("wfh", 1, distance, YesNode())
    tree = DecisionTreeNode("salary", 20000, wfh, YesNode())

    # Test the decision tree with a job offer
    job_offer = {'salary': 19000, 'wfh': 1, 'distance': 12}
    decision = tree.check(job_offer)
    print(f"Decision for the job offer {job_offer}: {'Accept' if decision else 'Reject'}")

    job_offer = {'salary': 19000, 'wfh': 0, 'distance': 15}
    decision = tree.check(job_offer)
    print(f"Decision for the job offer {job_offer}: {'Accept' if decision else 'Reject'}")

if __name__ == "__main__":
    main()

#                                    (<20k)   Salary   (>=20k)
#                                   -----------------------------
#                                  /                             \
#                          (<1) WFH (>=1)                        Yes
#                        ------------------------
#                        /                      \                 
#             (<10k) Distance (>=10k)           Yes                    
#            ------------------------   
#             /                    \                               
#            Yes                   No                                 
