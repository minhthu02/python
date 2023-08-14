#%%

# Tính tổng tất cả các chữ số có 3 chữ số 
# ví dụ 257 : 2+5+7
#hint 257 chia lấy dư 10 =7, chia lấy nguyên =25

#%% lý thuyết
""""
for biến in range(khởi đầu, kết thúc, bước nháy):
    lệnh
if điều kiện:
    lệnh
elif điều kiện:
    lệnh
else:
    lệnh
while điều kiện:
    lệnh
thoát while: dung break hoặc thay đổi điều 
kiện làm sao không thỏa
"""
    
# %%
#bài 1: tìm factorial của 1 số
# kiểm tra a có phải là ước của b hay không ví dụ 2 là ước của 8
# bài 2: tìm tất cả các ước của 1 số
# bài 3: tìm bội chung nhỏ nhất của 2 nhập vào
# bài 3: ước chung lớn nhất
#%%
a = int(input())
print("a là: ",a)
b = int(input())
print("b là: ",b)
if max(a,b)%min(a,b)==0:
    print(max(a,b),"là BCNN")
else: 
    for i in range(max(a,b),(a*b)+1):
        if i%a==0 and i%b==0:
            print(i ,"là BCNN")
#%%
a = int(input())
print("a là: ",a)
b = int(input())
print("b là: ",b)
ucln =1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0 :
        ucln=i
print(ucln)          
        
    
#%%
a = int(input())
print("a là: ",a)
b = int(input())
print("b là: ",b)
bcnn =-1
for i in range(1,min(a,b)):
    if (a%i ==0) and (b%i==0):
        ucln=i
        break       
        
#%%
a = int(input())
print("a là: ",a)
b = int(input())
print("b là: ",b)
bcnn =-1
for i in range(1,(a*b)):
    if (i%a ==0) and (i%b==0):
        bcnn=i
        break
print(bcnn)

#%%
number = int(input())
result = 1
resultfor =1
times = number

while times > 0:
    result = result*times
    times-=1
for i in range(1,number+1):
    resultfor*= i
print("final result: ",result)
print("for result", resultfor)
6
# %%
a = float(input())
print("a là: ",a)
b = float(input())
print("b là: ",b)
if b%a ==0:
    print("a là ước của b")
else:
    print("a không là ước của b")



# %%
number = int(input())
for i in range(1,number+1):
    if number%i ==0:
        print(i ,"là ước")
    else: 
        print(i ,"không là ước")

# %%

