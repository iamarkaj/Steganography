import numpy as np


def _msg_to_bin(msg):
    if type(msg) == str:
        # add delimiter
        msg += "#"
        return ''.join([format(ord(i), "08b") for i in msg])

    elif type(msg) == int or type(msg) == np.uint8:
        return format(msg, "08b")


def encode(img, msg, lsb_pos=1, flip_next=False):
    msg = _msg_to_bin(msg)
    msg_idx = 0

    if flip_next and lsb_pos == 8:
        raise ValueError("Set flip_next to False")

    enc_img = np.copy(img)
    for pixel in enc_img:
        for channel in pixel:
            try:
                b, g, r = _msg_to_bin(channel[0]), _msg_to_bin(channel[1]), _msg_to_bin(channel[2])
                
                if flip_next:
                    b = b[:7-lsb_pos] + str(1 if b[7-lsb_pos] == '0' else 0) + b[8-lsb_pos:]
                    g = g[:7-lsb_pos] + str(1 if g[7-lsb_pos] == '0' else 0) + g[8-lsb_pos:]
                    r = r[:7-lsb_pos] + str(1 if r[7-lsb_pos] == '0' else 0) + r[8-lsb_pos:]

                channel[0] = int(b[:8-lsb_pos] + msg[msg_idx] + b[9-lsb_pos:], 2)
                channel[1] = int(g[:8-lsb_pos] + msg[msg_idx+1] + g[9-lsb_pos:], 2)   
                channel[2] = int(r[:8-lsb_pos] + msg[msg_idx+2] + r[9-lsb_pos:], 2)
                msg_idx += 3

            except:
                return enc_img

    raise ValueError(f"Maximum characters allowed is: {int((img.shape[0]*img.shape[1]*3)/8-1)}")
                

def decode(img, lsb_pos=1):
    msg = ""
    tmp = ""

    for pixel in img:
        for channel in pixel:
            tmp += _msg_to_bin(channel[0])[8-lsb_pos]
            tmp += _msg_to_bin(channel[1])[8-lsb_pos]
            tmp += _msg_to_bin(channel[2])[8-lsb_pos]

    for i in range(0, len(tmp), 8):
        msg += chr(int(tmp[i:i+8], 2))
        if msg[-1] == "#":
            return msg[:-1]


def mse(original_img, decoded_img):
    return np.square(np.subtract(original_img, decoded_img, dtype=np.float)).mean()
