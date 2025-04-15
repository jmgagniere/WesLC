class PlotData:
    def __init__(self, data):
        self.data = data
        self.date_time = []
        self. d_w1 = []
        self.d_w2 = []
        self.d_w3 = []
        self.d_pulse_1 = []
        self.d_pince_1 = []
        self.d_pince_2 = []
        self.d_ph1 = []
        self.d_ph2 = []
        self.d_ph3 = []
        self.d_pa = []
        self.d_base = []

        self.data_len = len(self.data)

        for row in self.data:
            y = row[0][0:4]
            m = row[0][5:7]
            d = row[0][8:10]
            dt = d + '/' + m + '/' + y + row[0][10:16]
            self.date_time.append(dt)
            self.d_w1.append(self.test_none(row[1]))
            self.d_w2.append(self.test_none(row[2]))
            self.d_w3.append(self.test_none(row[3]))
            self.d_pulse_1.append(self.test_none(row[4]) * 60)
            self.d_pince_1.append(self.test_none(row[5]) * 0.220)
            self.d_pince_2.append(self.test_none(row[6]) * 0.220)
            self.d_ph1.append(self.test_none(row[7]) * 0.220)
            self.d_ph2.append(self.test_none(row[8]) * 0.220)
            self.d_ph3.append(self.test_none(row[9]) * 0.220)
            self.d_pa.append(self.test_none(row[10]) / 1000)
            self.d_base.append(row[11])

    def test_none(self, row):
        val = 0.0 if row is None else row
        return val
