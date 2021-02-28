#!/usr/bin/env python
# coding: utf-8

# ### 1. 모험가 길드
# - n명의 모험가
# - 각 모험가의 '공포도'를 측정
# - 공포도 x인 모함가는 반드시 x명 이상으로 구성된 모험가 그룹에 참여해야 도전 가능
# - 도전할 수 있는 그룹 수의 최댓값을 출력
# - 단 모든 모험가를 특정 그룹에 넣어야 할 필요는 없음

# In[4]:


#기본 입력값들
n = int(input())
x = list(map(int, input().split()))
x.sort() #오름차순으로 정렬 해버리고 (최소값 볼 수 있으니까)

#code
group = 0 #그룹의 수
num = 0 #그룹 내 포함된 인원 수

for i in x: #모험가들에 대해서
    num += 1 #그룹에 한명 들어오고
    if num >= i: #만약에 그룹에 포함된 인원수가 지금 i값, 그러니까 공포도 이상이면
        group += 1 #그룹이 결성되는거고
        num = 0 #그룹내의 인원수는 초기화 시켜주고

print(group)


# ### 2. 곱하기? 더하기?
# - 왼쪽부터 오른쪽까지 하나씩 모든 숫자를 확인하며 숫자 사이에 곱하기 혹은 더하기 연산자를 넣기
# - 가능한 경우의 수 중 가장 큰 수를 구하는 프로그램 작성

# In[3]:


data = input()

result = int(data[0])

for i in range(1, len(data)):
    #0 이나 1이 앞뒤중에 있으면 당연히 곱하는 것보다는 더하는게 더 큰 수를 배출
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)


# ### 3. 뒤집기 ( baekjoon #1439 )
# - 0 과 1로만 구성되어 있는 1,000,000보다 작은 문자열
# - 1을 뒤집으면 0, 0을 뒤집으면 1 이 된다
# - 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것만 가능하다

# In[5]:


data = input()
count0 = 0
count1 = 1

#우선 첫번째 원소에 대한 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1
    
#두번째 원소부터 모든 원소를 확인해서 처리
for i in range(len(data) -1):
    if data[i]!= data[i+1]:
        #다음 수에서 1로 바뀌는 경우
        if data[i+1] == '1':
            count0 += 1
        #0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))


# ### 4. 만들 수 없는 금액
# - n개의 동전을 가지고 있음
# - 이를 이용하여 만들 수 없는 양의 정수 금액 중 최솟값 구하는 프로그램

# In[7]:


n = int(input())
data=list(map(int, input().split()))
data.sort()

#1부터 시작해야지. 목표 금액이 0이 될 수는 없으니까
target = 1
#만약에 타겟보다 커버리면 
for x in data:
    if target < x:#타겟 값을 만족시킬 수 없으니까
        break #끊어주고
    target += x #아니면 x를 더해서 타겟으로 새로 잡아보고

print(target)


# ### 5. 볼링공 고르기
# - A,B 두 사람이 볼링을 치고 서로 무게가 다른 볼링공 고르려 함
# - 총 N개의 볼링공. 무게가 적혀있고 번호는 1부터 순서대로 부여
# - 같은 무게가 있을 수 있지만 다른 공으로 체크됨
# - 두 사람이 볼링공을 고르는 경우의 수 구하는 프로그램

# In[9]:


n, m = map(int, input().split())
data = list(map(int, input().split()))

# 볼링공 개수는 1000개 이하, 무게는 10까지
array = [0] * 11 #11개의 리스트를 만들어준다

for x in data:
    #각 무게에 해당하는 볼링공 체크
    array[x] += 1
    
result = 0
#1부터 m(무게)까지 정리
for i in range(1, m+1):
    n -= array[i] 
    result += array[i] * n
    
print(result)


# In[1]:


### 7. Lucky Straight


# In[2]:


n=input()
length = len(n) #점수값의 총 자릿수
summary = 0


# In[ ]:


for i in range(length // 2):
    summary += int(n[i])


# In[ ]:


for i in range(length // 2, length):
    summary -= int(n[i])


# In[ ]:


if summary ==0:
    print("LUCKY")
else:
    print("READY")


# In[ ]:


### Character Re-Arranging


# In[ ]:


data=input()
result=[]
value = 0


# In[ ]:


for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)


# In[ ]:


result.sort()


# In[ ]:


if value != 0:
    result.append(str(value))


# In[ ]:


print(''.join(result))

