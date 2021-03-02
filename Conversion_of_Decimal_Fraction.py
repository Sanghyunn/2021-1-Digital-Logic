decimal, radix = input().split() # 10진수 숫자와 radix를 입력받는다.

d = float(decimal)
r = int(radix)

output = [] # 결과값을 담을 array

integer = int(d)  # decimal의 정수
fraction = round(d - integer, 6) # decimal의 소수부(6자리까지 표현)

# 정수부 변환
while integer != 0 : # 몫이 0이 될 때까지 반복
    remainder = integer % r
    if remainder >= 10 : # 나머지가 10 이상이면 A, B, C, D... 를 입력하고 digit에 적용한다.
        output += chr(remainder + 55)

    else :
        output += chr(remainder + 48)

    integer //= r # 남은 정수부에 한해서 반복


for i in range(0, len(output) // 2) : # output에 순서가 뒤집혀서 입력되었기에 정렬한다
    temp = output[i]
    output[i] = output[len(output) - 1 -i]
    output[len(output) - 1 - i] = temp

# 소수부 변환
if(fraction != 0) : # 소수부가 존재할 경우
    output += '.' # 소수점 입력

    for i in range(0, 6) : # 최대 소수 6자리까지 출력이므로 6번만 반복을 한다
        if fraction == 0 : break # 소수부가 없어지면 종료

        fraction *= r

        remainder = int(fraction) # digit에 적용할 정수부

        if remainder >= 10 : # 나머지가 10 이상이면 A, B, C, D... 를 입력하고 digit에 적용한다
            output += chr(remainder + 55)

        else :
            output += chr(remainder + 48)

        fraction = round(fraction - remainder, 6) # 남은 소수부에 한해서 다시 반복


# 출력 단계
for i in range(len(output)) :
    print(output[i] , end='')

print('(' + radix + ')')
