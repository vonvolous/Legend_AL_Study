* Q15

    출발 도시 X로부터 최단 거리가 정확히 K인 도시 번호 출력하기

    N : 도시 개수
    M : 도로 개수
    K : 최단 거리
    X : 출발 도시

    BFS 문제는 python에서 제공하는 deque(FIFO, 선입선출) 사용하기

    1. graph에는 [root node] [1번 도시 도로 정보] [2번 도시 ...] [3번 도시...] [...] ...
    2. 이제 이 graph에서 노드를 하나씩 제거해서 각 도시별로 최단 거리를 구하기
    3. 마지막에 최단 거리가 정확히 K인 도시만 번호 출력


* Q16 (어려워서 책 참고...ㅠ)

    연구소 크기가 NxM이고 연구소의 지도(0: 빈 칸, 1: 벽, 2: 바이러스)가 주어질 때 안전 영역의 최대 크기를 구하기

    [구현한 함수]
    - checkSafeArea():

        현재 설치한 3개의 벽 위치에 따른 안전 영역 크기 정하는 함수

        testWall[i][j] == 0인 경우만 count해서 return해주기

    - checkVirus(x, y):

        바이러스 좌표인 (x, y)가 상하좌우로 뻗어나가면서 testWall에 표시해주는 함수로 recursive하게 반복하면서 최종 바이러스 영역을 확인

    - dfs(wall) :

        전체 지도에서 순차적으로 벽을 세워가면서 안전 영역의 최대 크기를 구함
    

* Q17 (연구소 문제랑 거의 비슷!)

    NxN 크기의 시험관 특정 위치엔 바이러스 존재
    바이러스의 종류는 1~K번까지 K가지 있음

        - 매초마다 상하좌우로 증식
        - 매초 번호가 낮은 바이러스부터 증식 -> from collections의 deque(FIFO, 선입선출)이용
        - 특정 칸에 이미 바이러스 존재하면 증식 불가

    S초 뒤에 (X, Y)의 바이러스 종류 출력 없으면 0 출력

* Q18
    균형잡힌 괄호 문자열 p가 주어질 때 올바른 괄호 문자열로 변환한 결과를 return 하도록 solution 함수 작성

    - [균형잡힌 괄호 문자열] : '('와 ')'의 개수가 같은 문자열
    - [올바른 괄호 문자열] : 균형잡힌 괄호 문자열이면서 짝도 맞는 경우

    1. 입력이 빈 문자열이면 빈 문자열 반환
    2. 문자열 w를 두 개의 균형잡힌 괄호 문자열 u,v로 분리
    3. 수행 결과 u에 이어 붙여 반환
        3-1. u가 올바른 괄호 문자열이면 v에 대해 1단계부터 진행
    4. u가 올바른 문자열 아니면 
        4-1. 빈 문자열에 '(' + solution(v) + ')'
        4-2. u의 처음과 끝 문자 제거 후 나머지 문자열 괄호 방향 뒤집기
        4-3. 생성된 문자열 반환

* Q19

    입력 받은 수열의 순서는 바꿀 수 없을 때 받은 덧셈, 뺄셈, 곱셈, 나눗셈의 개수를 조합하여 수식을 만든 다음에 최댓값과 최솟값을 출력

    이를 위해 수열에 재귀적으로 기호를 더하고 빼가면서 최댓값과 최솟값을 각각 구함

* Q20 감시 피하기

    