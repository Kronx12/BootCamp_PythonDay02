class CsvReader():
    def __init__(self, filename=None, sep=',', header=False,
                 skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.parsed_header = []
        self.data = []
        self.f = None

    def __enter__(self):
        try:
            self.f = open(self.filename, "r")
            for i in range(self.skip_top):
                self.f.readline()
            if self.header:
                self.parsed_header = self.f.readline()[:-1].split(self.sep)
            tmp = self.f.readlines()
            tmp = tmp[:len(tmp) - self.skip_bottom]
            for i in tmp:
                self.data.append(i[:-1].split(self.sep))
        except FileNotFoundError:
            self = None
        return self

    def getdata(self):
        return self.data

    def getheader(self):
        return self.parsed_header

    def __exit__(self, *args):
        if self.f:
            self.f.close()


if __name__ == "__main__":
    with CsvReader('good.csv', sep=';', header=True, skip_top=3,
                   skip_bottom=7) as file:
        data = file.getdata()
        header = file.getheader()
        print(data)
        print(header)
    with CsvReader('bad.csv') as file:
        if not file:
            print("File is corrupted")
