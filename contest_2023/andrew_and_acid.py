# https://contest.yandex.ru/contest/28412/problems/?nc=xyKsnAoC&success=85437174#46814/2021_01_15/l2nQrDNWlO

reservoir_qty = int(input())
volumes = list(map(int, input().split()))


if volumes != sorted(volumes):
    print('-1')
else:
    print(max(volumes) - min(volumes))
