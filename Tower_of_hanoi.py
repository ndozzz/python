NUMBER_OF_DISKS = 4
number_of_moves = 2**NUMBER_OF_DISKS - 1
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}

def make_allowed_move(rod1, rod2):    
    forward = False
    if not rods[rod2]:
        forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        forward = True
                      
    if forward:
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
        rods[rod2].append(rods[rod1].pop())
    else:
        print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
        rods[rod1].append(rods[rod2].pop())
    
    # display our progress
    print(rods, '\n')

def move(n, source, auxiliary, target):
    # display starting configuration
    print(rods, '\n')
    for i in range(number_of_moves):
        remainder = (i + 1) % 3
        if remainder == 1:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            else:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                # make_allowed_move(source, auxiliary)            

        elif remainder == 2:
            print(f'Move {i + 1} allowed between {source} and {auxiliary}')
            make_allowed_move(source, auxiliary)
        
        elif remainder == 0:
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')
            make_allowed_move(auxiliary, target)
           
# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')

#ini menggunakan recursive, pelajari lebih lanjut
Jumlah_disk = 3
A = list(range(Jumlah_disk, 0, -1))
B = []
C = []

def move2(n, source, auxiliary, target):
    if n <= 0:
        return
        # move2 n - 1 disks from source to auxiliary, so they are out of the way
    move2(n - 1, source, target, auxiliary)
        
        # move2 the nth disk from source to target
    target.append(source.pop())
        
        # display our progress
    print(A, B, C, '\n')
        
        # move2 the n - 1 disks that we left on auxiliary onto target
    move2(n - 1,  auxiliary, source, target)
              
# initiate call from source A to target C with auxiliary B
move2(Jumlah_disk, A, B, C)