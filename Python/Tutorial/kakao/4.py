def solution(words, queries):
    cached_words = [[] for i in range(10001)]  # 단어의 최대길이 10,000
    cached_querys = {}

    # cache_word init
    for word in words:
        cached_words[len(word)].append(word)
    answer = []

    for query in queries:
        if query in cached_querys.keys():
            answer.append(cached_querys[query])
            continue
        idx = query.index("?")
        tmp_words = cached_words[len(query)]

        if idx == 0:
            end = query.count("?")
            postfix = query[end:]
            filtered = list(filter(lambda w: w.endswith(postfix), tmp_words))
        else:
            prefix = query[:idx]
            filtered = list(filter(lambda w: w.startswith(prefix), tmp_words))

        cached_querys[query] = len(filtered)
        answer.append(len(filtered))
    return answer


if __name__ == "__main__":
    solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
