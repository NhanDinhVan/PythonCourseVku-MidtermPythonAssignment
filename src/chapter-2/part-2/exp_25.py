def tao_TD(Max):
      d=dict() 
      for i in range(1,Max+1): 
          d[i]=i**2
      return d 
   
  def Print_Item(TD):            
      for k,v in TD.items(): 
          print(k,v) 
  def Print_key(TD):
      for k in TD.keys(): 
          print(k) 
  def Print_value(TD):
      for v in TD.values(): 
          print(v) 

max = int(input("Nhập chỉ số Max:")
TD = tao_TD(max)
print("Các phần tử của từ điển là:")
Print_Item(TD) 
print("Khóa các ph.tử của từ điển:")
Print_key(TD) 
print("Giá trị các ph.tử của từ điển:")
Print_value(TD) 

