
class coinChange:

    def __init__(self, change, coins):
        self.change = change
        self.coins = coins

    def __str__(self):
        return "Make Change for " + str(self.change) + " with coins : " +  str(self.coins)

    def solve(self):
        matrix = [[0 for i in range(self.change + 1)] for j in range(len(self.coins))]
        # default coins will have a 1 value
        matrix[0] = range(self.change + 1)

        for i in range(1, len(self.coins)):
            for j in range(0,self.change + 1):
                if j < self.coins[i]:
                    matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j - self.coins[i]] + 1)

                self.printMatrix(matrix)
        return matrix[-1][-1]

    def printMatrix(self, matrix):
        print "Print this iteration matrix"

        for i in range(len(self.coins)):
            print str(matrix[i]) + '\n'


if __name__ == '__main__':
    c = coinChange(160,[1,2,5,10,25])
    print c
    print c.solve()
