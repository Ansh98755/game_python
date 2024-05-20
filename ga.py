import pygame# we are importing the essetial tools for game development from the python lib

pygame.init()# we are initializing the python library it is very important as all the funtions of pygame works only then all its subparts (sound , animation , etc) it is the backend of pygame


screen=pygame.display.set_mode((1000,800))#here we are setting the window height and width which we will see it appears onlu for sec because the code ends  without any loops and condition

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    #draw all our elements
    #update all our everything
    pygame.display.update()#to update our display // here we won't be able to close the display so we have to set the player input for closing the game , as if we run the code here it won't close
    #we encounter an error although our code is running the error is video system not initialized  it is becouse we are initializing the pygame using init() but at the same time we are quiting it also it gives an error becouse our while loop remained open and unable to perform further operation after the quit statement