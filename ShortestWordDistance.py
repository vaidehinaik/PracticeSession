def shortestWordDistance(words,word1,word2):
    word1_index = None
    word2_index = None
    min_dis = len(words)
    # print(min_dis)
    for i,v in enumerate(words):
        if v == word1:
            word1_index = i
        elif v == word2:
            word2_index = i
        if word1_index is not None and word2_index is not None and min_dis > abs(word1_index-word2_index):
            min_dis = abs(word1_index-word2_index)
    return min_dis
print("The shortest distance between two words is: {}".format(shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"],"makes","coding")))




