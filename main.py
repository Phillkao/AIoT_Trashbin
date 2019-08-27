from IotDeviceControl import *
from PiDeviceControl import *

if __name__ == '__main__':
    IotDeviceState_TrashCan100Per_On()
    IotDeviceState_TrashCan100Per_Off()
    IotDeviceState_TrashCount_PlusOne()

    while(1):
        ChoInBo_D = PiDevice_GetChoInBo_Distance()
        print(ChoInBo_D)
        ChoInBo_D = PiDevice_GetChoInBo_Distance_2()
        print(ChoInBo_D)

    PiDevice_GetCamera_Picture()
