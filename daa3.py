def fractional_knapsack(values,weights,capacity):
    n=len(values)
    ratio=[]

    for i in range(n):
        if(weights[i]==0):
            print("Canoot divide by 0 ")
            continue
        ratio.append((values[i]/weights[i],i))

    ratio.sort(reverse=True)
    total_value=0.0
    fractions=[0.0]*n

    for r,i in ratio:
        if weights[i]<=capacity:
            total_value+=values[i]
            capacity-=weights[i]
            fractions[i]+=1.0

        else:
            fraction=capacity/weights[i]
            total_value+=values[i]*fraction
            capacity=0
            fractions[i]=fraction
            
    return total_value,fractions    



n=int(input("Enter no of items "))
capacity=float(input("Enter capacity of knapsack "))
values=[]
weights=[]
for i in range(n):
    value=float(input(f"enter profit of item {i+1}"))
    weight=float(input(f"enter weight of item {i+1}"))
    values.append(value)
    weights.append(weight)

total_valuet,fractions=fractional_knapsack(values,weights,capacity)

print("\nItem | Value | Weight | Fraction taken |")
print("------------------------------------------")
for i in range(n):
    print(f"\n{i+1} | {values[i]} | {weights[i]} | {fractions[i]} |")

print("Maximum profit is ",total_value)
    
