class LineModel:
    def fit(self, data):
        x1, y1 = data[0]
        x2, y2 = data[1]
        self.m = (y2 - y1) / (x2 - x1)
        self.c = y1 - self.m * x1
    
    def predict(self, x_new):
        return x_new * self.m + self.c

def main():
    data = [(2, 3), (4, 10)]
    model = LineModel()
    model.fit(data)
    
    x_new = 2
    y_pred = model.predict(x_new)
    print(f"Predicted value at x={x_new}: {y_pred}")

if __name__ == "__main__":
    main()

