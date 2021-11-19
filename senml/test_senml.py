from kpn_senml import *
import time
import datetime
import json

def main():
    pack = SenmlPack("device_name")
    temp = SenmlRecord("temperature", unit=SenmlUnits.SENML_UNIT_DEGREES_CELSIUS, value=23.5)
    door_pos = SenmlRecord("doorPos", update_time=20, value=True)
    int_val = SenmlRecord("int_val", sum=100)

    pack.add(temp)
    pack.add(door_pos)
    pack.add(int_val)

    random_time = datetime.datetime.strptime('Jan 1 2018  1:33PM', '%b %d %Y %I:%M%p')
    pack.base_time = time.mktime(random_time.timetuple())  # set a base time
    pack.base_value = 5
    pack.base_sum = 50
    temp.time = time.mktime(datetime.datetime.now().timetuple())  # all child objects will receive the time value

    print(pack.to_json())

    # Test of de-serialization
    # string_test = '[{"n": "temperature", "v": 18.5, "t": 122547872.0, "u": "Cel", "bn": "device_name", "bv": 5, "bs": 50, "bt": 1514809980.0}, {"n": "doorPos", "vb": true, "ut": -1514809960.0}, {"n": "int_val", "s": 50}]'
    # pack_2 = SenmlPack("device_name")
    # pack_2.from_json(string_test)


if __name__ == "__main__":
    main()
