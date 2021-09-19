import os
import sys
import cv2
from helper import *


def main():
    original_image = cv2.imread(os.path.join(os.getcwd(), str(sys.argv[1])))
    original_message = str(sys.argv[2])

    ################################################################################

    print("case 1: Change 1st LSB of each pixel/sample")
    lsb_pos = 1
    flip_next = False

    encoded_image = encode(original_image, original_message, lsb_pos, flip_next)
    decoded_message = decode(encoded_image, lsb_pos)

    print("Decoded message: ", decoded_message)
    cv2.imwrite(os.path.join(os.getcwd(), "case1.jpg"), encoded_image)
    print("MSE: {0:.8f}".format(mse(original_image, encoded_image)))

    ################################################################################

    print("\ncase 2: Change 4th LSB bit of each pixel/sample and perform no flip to next LSB bits")
    lsb_pos = 4
    flip_next = False

    encoded_image = encode(original_image, original_message, lsb_pos, flip_next)
    decoded_message = decode(encoded_image, lsb_pos)

    print("Decoded message: ", decoded_message)
    cv2.imwrite(os.path.join(os.getcwd(), "case2.jpg"), encoded_image)
    print("MSE: {0:.8f}".format(mse(original_image, encoded_image)))

    ################################################################################

    print("\ncase 3: Change 4th LSB bit of each pixel/sample and flip the next LSB bits")
    lsb_pos = 4
    flip_next = True

    encoded_image = encode(original_image, original_message, lsb_pos, flip_next)
    decoded_message = decode(encoded_image, lsb_pos)

    print("Decoded message: ", decoded_message)
    cv2.imwrite(os.path.join(os.getcwd(), "case3.jpg"), encoded_image)
    print("MSE: {0:.8f}".format(mse(original_image, encoded_image)))


if __name__ == "__main__":
    main()