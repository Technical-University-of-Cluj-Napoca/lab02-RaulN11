import os
import datetime
def smart_log(*args, **kwargs)->None:
    level=kwargs.get("level")
    timestamp=datetime.datetime.now().strftime("%H:%M:%S:")
    ts=kwargs.get("timestamp")
    save_to=kwargs.get("save_to",None)
    colored=kwargs.get("color",True)
    color=""
    default = "\033[0m"
    match level:
        case "DEBUG":
            color="\033[90m"
        case "INFO":
            color="\033[34m"
        case "WARNING":
            color="\033[33m"
        case "ERROR":
            color="\033[31m"

    message=timestamp
    message1 = " ".join(map(str, args))
    message=message+" ["+ level +"] "+message1
    if save_to:
        os.makedirs(os.path.dirname(save_to),exist_ok=True)
        with open(save_to,"a") as f:
            f.write(message+"\n")

    if colored:
        print(f"{color}{message}{default}")
    else:
        print(f"{message}{default}")

if __name__=="__main__":
    smart_log("Warning",level="WARNING")
    smart_log("Error",level="ERROR")
    smart_log("Info",level="INFO")
    pass