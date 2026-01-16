#생태학

import sys

# 1. 입력 받기
lines = sys.stdin.readlines()
dic = {}
total_count = 0

for line in lines:
    name = line.strip()
    if not name:
        continue

    # 2. 카운팅
    dic[name] = dic.get(name, 0) + 1
    total_count += 1

# 3. 사전순 정렬 (키값들을 정렬해서 리스트로 만듦)
sorted_keys = sorted(dic.keys())

# 4. 출력
for name in sorted_keys:
    # 비율 계산 (특정 나무 / 전체 나무 * 100)
    ratio = (dic[name] / total_count) * 100

    # 소수점 4째 자리까지 출력
    print(f"{name} {ratio:.4f}")