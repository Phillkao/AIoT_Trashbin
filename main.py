from IotDeviceControl import *
from PiDeviceControl import *
    
if __name__ == '__main__':
    IotDeviceState_TrashCan100Per_On()
    IotDeviceState_TrashCan100Per_Off()
    IotDeviceState_TrashCount_PlusOne()
	
	ChoInBo_D = PiDevice_GetChoInBo_Distance()
