all=set(['John','Mary','Tina','Fiona','Clair','Eva','Ben','Bill','Bert'])
eng=set(['John','Mary','Fiona','Clair','Ben','Bill'])
math=set(['Mary','Fiona','Clair','Eva','Ben'])
print("英文與數學都及格",eng&math)
print("數學不及格",all-math)
print("英文及格且數學不及格",eng&(all-math))