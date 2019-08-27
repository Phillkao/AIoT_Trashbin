from IotDeviceControl import *
from PiDeviceControl import *

if __name__ == '__main__':
    IotDeviceState_TrashCan100Per_On()
    IotDeviceState_TrashCan100Per_Off()
    IotDeviceState_TrashCount_PlusOne()
    '''
    while(1):
        ChoInBo_D = PiDevice_GetChoInBo_Distance()
        print(ChoInBo_D)
        ChoInBo_D = PiDevice_GetChoInBo_Distance_2()
        print(ChoInBo_D)
    '''
    '''
    PiDevice_GetCamera_Picture()
    from keras.models import load_model
    import numpy as np
    import cv2
    
    image = cv2.imread("trash.png")
    model = load_model('output.h5')
    print(np.argmax(model.predict(image),1))
    '''
    PiDevice_Move4FuMata(0)
    time.sleep(2)
    PiDevice_Move4FuMata(180)
    time.sleep(2)
