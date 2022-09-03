#coding:Utf-8
import  logging  
import re
import json


def guess_next_letter(pattern, used_letters=[], word_list=['about', 'abound']):
    """Returns a letter from the alphabet.
    Input parameters:
                pattern: current state of the game board, with underscores "_" in the
            places of spaces (for example, "____e", that is, four underscores
            followed by 'e').
        used_letters: letters you have guessed in previous turns for the same
            word (for example, ['a', 'e', 's']).
        word_list: list of words from which the game word is drawn.
    """
    next_letter = None
    try:
	    #1. 单词长度
	    xlen = len(pattern)
	    logging.warning("1. 单词长度，{}".format(xlen))

	    #2. 准备相同长度 && 规则匹配到 的单词 
	    prep_words = []
	    for word in word_list:
	        if len(word) != xlen:
	            continue
	        rt = re.match(pattern.replace("_", "\w"), word)
	        if rt:
	            logging.warning("匹配到了， {}".format(word))
	            prep_words.append(word)
	    logging.warning("2. 准备相同长度 && 规则匹配到 的单词  {}".format(','.join(prep_words)))
	    if prep_words==[]:
	    	raise Exception("表达式没有匹配到单词")

	    #3. 准备字母列表，排除用过的
	    prep_letters = ''.join(prep_words)
	    prep_letters = list(set(prep_letters).difference(set(used_letters)))
	    logging.warning("3. 准备字母列表，排除用过的 {}".format(prep_letters))
	    if prep_letters==[]:
	    	raise Exception("没有可用字母")


	    #4. 计算字母出现在单词中的出现频率
	    wp = {}
	    for w in prep_letters:
	        for word in prep_words:
	            if w in word:
	                wp[w] = wp.get(w, 0) + 1
	    logging.warning("4. 计算字母出现在单词中的出现频率 {}".format(str(wp)))

	    #5. 返回出现频率最高的，作为下一个
	    next_letter = max(wp, key=wp.get)
	    logging.warning("5. 返回出现频率最高的，作为下一个 {}".format(next_letter))

	    return next_letter
    except Exception as e:
    	logging.error("没有找到下一个字母. error: {}".format(e))
    	return None


def test_function_should_return_something():
    pattern = "____d"
    used_letters = list("ja")
    word_list = ['hello', 'world', 'aarld', 'carld', 'python', 'java']
    assert guess_next_letter(pattern, used_letters, word_list) is not None


if __name__ == '__main__':
    test_function_should_return_something()
