import math
A,B,H,M = map(int,input().split())
a_deg = 30*H+0.5*M
b_deg = 6*M
diff_deg = a_deg-b_deg
print(math.sqrt(A**2+B**2-(2*A*B*math.cos(math.radians(diff_deg)))))
