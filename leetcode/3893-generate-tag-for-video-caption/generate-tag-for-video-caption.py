class Solution(object):

    def generateTag(self, caption):
        a = ""
        caption = caption.split(" ")

        first = True

        for i in range(len(caption)):
            word = ""

            for j in caption[i]:
                if j.isalpha():
                    word += j

            if word == "":
                continue

            if first:
                a += word.lower()
                first = False
            else:
                a += word[0].upper() + word[1:].lower()

        return "#" + a[:99]