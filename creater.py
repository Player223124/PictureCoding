from PIL import Image, ImageDraw
import random
from code_alg import block_code
from copy import deepcopy
import json


class image_handler(block_code):
    def __init__(self, path):
        super().__init__()
        self.path = path
        if self.path[-1] == 'g':
            self.image = Image.open(path)
            self.draw = ImageDraw.Draw(self.image)
            self.width = self.image.size[0]
            self.height = self.image.size[1]
            self.pix = self.image.load()
        elif self.path[-1] == 'n':
            with open(self.path, 'r') as file:
                self.mass_colors = json.load(file)
                self.width = len(self.mass_colors)
                self.height = len(self.mass_colors[0])
                self.image = Image.new('RGB', (self.width, self.height), (255, 255, 255))
                self.draw = ImageDraw.Draw(self.image)


    def errors(self, numb, t):
        count = []
        numb = bin(numb)[2:]
        numb = list(numb)
        dif = 8 - len(numb)
        if dif != 0:
            var = ['0' for i in range(dif)]
            numb = var + numb

        while len(count) < t:
            ind = random.randint(0, 7)
            if not ind in count:
                count.append(ind)
                if numb[ind] == '0':
                    numb[ind] = '1'
                else:
                    numb[ind] = '0'
        numb = ''.join(numb)
        numb = int(numb, 2)
        return numb


    def image_with_errors(self, quantity):
        for x in range(self.width):
            for y in range(self.height):
                r = self.pix[x, y][0]
                g = self.pix[x, y][1]
                b = self.pix[x, y][2]

                r = self.errors(r, quantity)
                g = self.errors(g, quantity)
                b = self.errors(b, quantity)
                self.draw.point((x, y), (r, g, b))
    
        file_path = self.create_path('noise')
        self.image.save(file_path)


    def code(self, numb):
        code_word = deepcopy(self.code_words[numb])
        ind = random.randint(0, 12)
        if code_word[ind] == 0:
            code_word[ind] = 1
        else:
            code_word[ind] = 0
        return code_word   


    def image_to_json(self):
        encoded_pic = []
        for x in range(self.width):
            encoded_y = []
            for y in range(self.height):
                r = self.pix[x, y][0]
                g = self.pix[x, y][1]
                b = self.pix[x, y][2]

                r = self.code(r)
                g = self.code(g)
                b = self.code(b)
                pixel = [r, g, b]
                encoded_y.append(pixel)
            encoded_pic.append(encoded_y)

        file_path = self.create_path('encode')
        with open(file_path, 'w') as file:
            json.dump(encoded_pic, file)


    def decode(self, mass):
        c = self.width * self.height
        for x in range(self.width):
            for y in range(self.height):
                print(c)
                c -= 1
                r = mass[x][y][0]
                g = mass[x][y][1]
                b = mass[x][y][2]

                r = int(self.fix_error(r), 2)
                g = int(self.fix_error(g), 2)
                b = int(self.fix_error(b), 2)
                self.draw.point((x, y), (r, g, b))
        return self.image


    def image_to_jpg(self):
        file_path = self.create_path('decode')
        picture = self.decode(self.mass_colors)
        picture.save(file_path)


    def create_path(self, operator):
        path_list = self.path.split('/')
        file = path_list.pop()
        new_path = '/'.join(path_list) + '/'
        if operator == 'encode':
            file = file[:-4]
            file += '_encoded.json'
            new_path += file
        if operator == 'decode':
            file = file[:-5]
            file += '_decoded.jpg'
            new_path += file
        if operator == 'noise':
            file = file[:-4]
            file += '_noisy.jpg'
            new_path += file
        return new_path


if __name__ == '__main__':
    # new_file = image_handler('C:Dstu/InfTheory/Labs/Laba3/photos/sf_encoded.json')
    # new_file.image_with_errors(3)
    # new_file.image_to_json()
    # new_file.image_to_jpg()
    # print(new_file.__doc__)
    pass
