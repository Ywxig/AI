from Zoe import *
import CuteON

def main(message=[]):
    for word in message:

        
        if len(message) <= 1:
            data_set = CuteON.Get_.getAll("Data Set/ds.sws")
            return Zoe_Word(str(message[0]), data_set, messge=" ".join(message))
        if len(message) > 1:
            #return Zoe_Sentenses(" ".join(message))
            return Generator.generate_text(text = CuteON.Read_.Read("education/text.txt"), keywords = keywords(" ".join(message)))
           
        else:
            return Generator.generate_text(text = CuteON.Read_.Read("education/text.txt"), keywords = keywords(" ".join(message)))

