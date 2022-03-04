#스택
#while문, truck_weights가 모두 pop되면 종료
#while문: time+1,return(time)

def sumWeigth(truckIng):
    sum = 0
    for t in truckIng:
        sum+=t[0]
    return sum

def solution(bridge_length, weight, truck_weights):
    time = 0 #answer
    truck_weights.reverse() #[7,4,5,6] -> [6,5,4,7]
    truckIng = [] #현재 다리위에 있는 트럭 [[truck_weights,time]]
    bridge_weight = 0; #현재 다리위에 있는 트럭(들)의 무게
    truck = 0;#현재트럭
    
    #time: 1
    time = 1
    truck = truck_weights.pop()
    truckIng.append([truck,0])
    bridge_weight = sumWeigth(truckIng)

    #time: 2
    while(len(truckIng) !=0):
        #time+1
        time += 1
        truckIng=list(map(lambda x:[x[0],x[1]+1],truckIng))
    
        #트럭 빼기 (시간체크)
        truckIng = [t for t in truckIng if t[1]<bridge_length]

        #트럭 넣기 (무게체크)
        bridge_weight = sumWeigth(truckIng)
        if len(truck_weights)!=0:
            if truck_weights[-1]+bridge_weight <= weight:
                truck = truck_weights.pop() # truck_weights[-1]
                truckIng.append([truck,0])
    
    return time