# topic: ��ѧpython֮�б�list
# author��Liu Xiaoxia
# time��2020/4/22 22:40

# �������б�
empty = []
print(empty)

# �����ַ����б�
str_0 = ['abc', 'bcd', 'cde']
print(str_0)

# ���������б�
number = [1, 2, 3]
print(number)

# ��������б�
mix = ['abc', 2, 'def', 4]
print(mix)

# ���б����������ҽ���һ��Ԫ��
str_0.append('Ӣ�����')
print(str_0)
len(str_0)

# �����ҽ���һ���б���չ��һ���б���ͬʱ���б�ĩβ��Ӷ��Ԫ��
str_0.extend(['�ú�ѧϰ', '��������'])
print(str_0)

# ���б�̶�λ��(�±��0��ʼ)����Ԫ��
str_0.insert(0, 'aaaaa')
print(str_0)

# ���б�ɾ��Ԫ��(����)
str_0.remove('Ӣ�����')
print(str_0)

# ���б�ɾ��Ԫ��(����)
del str_0[0]
print(str_0)

# �����б���Ҫɾ����Ԫ��ֵ
# ɾ�����һ��Ԫ��
str_0.pop()
print(str_0)
# ɾ��ָ��Ԫ��
str_0.pop(1)
print(str_0)

# �б���Ƭ(��Ƭ)��һ���Ի�ȡ���Ԫ�أ� ԭ�б���
# Ԫ��1��Ԫ��3(������Ԫ��3)
print(str_0[1:3])
# ���б�ͷ��Ԫ��3(������Ԫ��3)
print(str_0[:3])
# ��Ԫ��3���б�ĩβ
print(str_0[3:])
# ��������б�
# ��str_1 = str_0��ͬ
# str_1 = str_0ʱ��str_0��str_1ָ��ͬһ��ռ䣻��str_0[:]�����ǽ�ֵ����str_1һ�ݣ�ָ�����鲻ͬ�Ŀռ�
str_1 = str_0[:]
print(str_1)

# ƴ�������б�
str_0 = str_0 + number
print(str_0)

# �����б�Ԫ��
# ���ƺ�ֱ�������ԭ�б���
print(number)
print(number * 3)
# ���ƺ�ֵ��ԭ�б�
number *= 2
print(number)

# �ж�Ԫ���Ƿ����б���
print('�ú�ѧϰ' in str_0)
print('������' not in str_0)

# �ж�Ԫ���Ƿ����б��е��б���
str_0.extend([['������', 'wuwuwu']])
print(str_0)
print('������' in str_0)
print('������' in str_0[len(str_0) - 1])

# �б��е��б��е�Ԫ��
print(str_0[6][1])

# �б������ݳ��ֵĴ���
print(number.count(2))

# ���ز������б��е�һ�γ��ֵ�λ��
print(str_0.index('cde'))
# ָ�����ҷ�Χ
print(str_0.index('cde', 0, 5))

# �������б�ת(�޲���)
str_0.reverse()
print(str_0)

# sort����
# ��С��������
number.sort()
print(number)
# �Ӵ�С����
number.sort(reverse=True)
print(number)
