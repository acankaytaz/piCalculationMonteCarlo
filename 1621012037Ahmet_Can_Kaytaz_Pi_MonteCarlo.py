import random

SIMULATION = 1000   #simülasyonun kaç kere döneceğini belirledigimiz yer

def check_inside(x, y):
    return (x ** 2 + y ** 2) < 1 #birim çember formulu
          
def main():
    count = 0
    a = 37
    x = 53
    m = 100
    for _ in range(SIMULATION):
        x = (a*x)%m  
        y = (a*x)%m
        x1 = x/100     #degerleri 0 ve 1 arasına sabitlemek amacıyla    
        y1 = y/100
        #print('x1 degerleri', x1)
        #y1 = random.uniform(-1, 1)
        #print('y1 degerleri', y1)   
        if check_inside(x1, y1):
            count += 1 
        print('çemberin içine düşen değerler ile anlık pi degeri:',4*count/SIMULATION, [count])
    print(f'Toplam simülasyon sayısı: {SIMULATION}')
    print(f'Cember icine düşen nokta toplam sayısı: {count}')

    PI = 4 * count / SIMULATION
    print(f'Son hesaplanan pi degeri: {PI}')

if __name__ == '__main__':
    main()
    