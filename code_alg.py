from copy import deepcopy

class block_code():
    def __init__(self):
        matr = [
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1]
            ]
        k = len(matr)
        binary_str = [0 for j in range(2**k)]

        for i in range(2**k):
            binary_str[i] = str(bin(i))[2:]

            str_len = len(binary_str[i])

            if str_len < k:
                binary_str[i] = "0" * (k - str_len) + binary_str[i]

        binary_int = []
        for row in binary_str:
            string = list(row)
            string = list(map(int, string))
            binary_int.append(string)

        code_words = []
        for row in binary_int:
            code_words.append(self.multi_S(matr, row))

        self.info_words = binary_int
        self.code_words = code_words


    def multi_S(self, mat, vec):
        indexes = [i for i in range(len(vec)) if vec[i] == 0]
        k = len(mat[0])
        count = 0
        mat = deepcopy(mat)
        for numb in indexes:
            mat.pop(numb-count)
            count += 1

        e = [0 for j in range(k)]
        if mat:
            for numb in range(len(mat)):
                row = mat[numb]
                string = []
                for ind in range(len(row)):
                    if e[ind] == row[ind]:
                        string.append(0)
                    else:
                        string.append(1)
                e = string
            return e
        else:
            return e
        

    def plus(self, e, v):
        row = []
        for ind in range(len(v)):
            if e[ind] == v[ind]:
                row.append(0)
            else:
                row.append(1)
        return row


    def fix_error(self, vec):
        matrix_Hsys_trans = [
            [1, 0, 1, 1, 1], 
            [1, 1, 0, 1, 1], 
            [0, 1, 1, 0, 1], 
            [1, 1, 1, 0, 1], 
            [0, 0, 0, 1, 1], 
            [1, 0, 0, 1, 1], 
            [0, 0, 1, 1, 1], 
            [0, 1, 0, 0, 1], 
            [1, 0, 0, 0, 0], 
            [0, 1, 0, 0, 0], 
            [0, 0, 1, 0, 0], 
            [0, 0, 0, 1, 0], 
            [0, 0, 0, 0, 1]
            ]
        vectors = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        syndromes_Hsys = [
            '[0, 0, 0, 0, 1]', 
            '[0, 0, 0, 1, 0]', 
            '[0, 0, 1, 0, 0]', 
            '[0, 1, 0, 0, 0]', 
            '[1, 0, 0, 0, 0]', 
            '[0, 1, 0, 0, 1]', 
            '[0, 0, 1, 1, 1]', 
            '[1, 0, 0, 1, 1]', 
            '[0, 0, 0, 1, 1]', 
            '[1, 1, 1, 0, 1]', 
            '[0, 1, 1, 0, 1]', 
            '[1, 1, 0, 1, 1]', 
            '[1, 0, 1, 1, 1]'
            ]
        S = str(self.multi_S(matrix_Hsys_trans, vec))
        index_e = syndromes_Hsys.index(S)
        e = vectors[index_e]
        c = self.plus(e, vec)

        index_I = self.code_words.index(c)
        I = self.info_words[index_I]
        I = list(map(str, I))
        I = ''.join(I)
        return I


if __name__ == '__main__':
    # i = 1 1 0 1 0 1 1 0
    # C = 1 1 0 1 0 1 1 0 0 0 1 0 1
    # iw, cw = table_1()
    # result = enter_V([1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0], iw, cw)
    # print(result)
    code = block_code()
    print(code.fix_error([1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0]))

