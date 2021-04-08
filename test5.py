array = [1, 5, 2, 6, 3, 7, 4]        # 리스트 array 
commands = [[2,5,3],[2,5,4],[2,5,2]] # 리스트 commands

def solution(array, commands):       # solution 함수 선언함
    answer = []
    
    for command in commands:
        array1 = array[command[0]-1:command[1]] # array1에 i번째부터 j번째까지 배열을 복사함
        array1.sort()                           # sort 함수로 정렬함
        answer.append(array1[command[2]-1])     # k번째 수를 찾아서 answer 배열에 저장함
    
    return answer

print(solution(array, commands)) # solution 함수 출력함
