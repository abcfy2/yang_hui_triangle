#!/usr/bin/env python3

n = 9  # 定义杨辉三角二项式的幂指数


def yh(n):
    if n == 0:
        layout = [1]
    elif n == 1:
        layout = [1, 1]
    else:
        tmp = yh(n-1)
        tmp = [tmp[x] + tmp[x-1] for x in range(len(tmp)) if x > 0]
        tmp.insert(0, 1)
        tmp.append(1)
        layout = tmp
    print(layout)
    return layout

if __name__ == '__main__':
    yh(n)
