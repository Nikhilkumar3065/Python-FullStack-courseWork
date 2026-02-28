media = ['sunset.png'
         ,'sunrise.png'
         ,'moon.png'
         ,'garden.png'
         ,'epstinfiles.mp4'
         ,'resort.mp4'
         ,'trip.mp4']
photos=[]
videos=[]
for i in media:
    if i.endswith('.mp4'):
        videos.append(i)
        
    else:
        photos.append(i)
print('\n--------photos---')
for i in photos:
    print(i)
print('\n--------videos--------')
for i in videos:
    print(i)

select =set(input("Enter the files to share (using comma):").split(','))
for i in select:
    if i in media:
        print(f'{i}-sent')
    else:
        print(f'{i}-not found')


        
