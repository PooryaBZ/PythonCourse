"""
A, B, C are the name of towers
A is starting tower
B is helping tower

smaller number means smaller disc for example 1 is the smallest disc
"""


def TowersOfHanoi(n, s_tower, d_tower, h_tower):
    if n == 1:
        print("Move disc 1 from pole", s_tower, "to pole", d_tower)
        return
    TowersOfHanoi(n - 1, s_tower, h_tower, d_tower)
    print("Move disc", n, "from pole", s_tower, "to pole", d_tower)
    TowersOfHanoi(n - 1, h_tower, d_tower, s_tower)

n = int(input("please input the number of disks: "))
TowersOfHanoi(n, 'A', 'C', 'B')