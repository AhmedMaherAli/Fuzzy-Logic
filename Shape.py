class Shape:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def calculate_centroid(self):
        sumA = 0
        sumCX = 0
        sumCY = 0
        for i in range(len(self.points)-1):
            temp = self.points[i][0] * self.points[i+1][1] - self.points[i+1][0] * self.points[i][1]
            sumA += temp
            sumCX += (self.points[i][0] + self.points[i+1][0]) * temp
            sumCY += (self.points[i][1] + self.points[i+1][1]) * temp
        A = sumA/2
        Cx = sumCX/(6*A)
        Cy = sumCY/(6*A)
        return Cx,Cy





    def membership(self, x):
        y = 0
        for i in range(len(self.points)-1):
            y1 = self.points[i][1]
            y2 = self.points[i + 1][1]
            x1 = self.points[i][0]
            x2 = self.points[i + 1][0]
            if x1 == x:
                y = y1
            if x1 < x <= x2:
                y = y1 + ((y2 - y1) * (x - x1) / (x2 - x1))
        return y
