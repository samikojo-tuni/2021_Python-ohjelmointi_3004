#!/usr/bin/python3

import hashlib
import binascii
import sys

# You can add all kind of config values to this file, e.g. CSV separator and file path
PATH = "/home/<tunnus>/cgi-data/scores.csv"
SEP = ";"
MAX = 10

# this dictionary contains users, which are allowed to add new high score values
# Key: user name, Value: password in hashed format
users = {
    "sovellus": "f13931a8d34c0d538b98f7ff34c6302f5f274d5eac87c2af03011794c392a9a710b4a263127ae049384f27513f019fed4826bbbb8bddab7884cc984177ce8e953418f42d7556ffa083d52d835902988fab83b12dda126bfd9a1d3b9500aa1dc8",
    "testi": "ea8024faa89f5f03a95993f7bb5eddcd673d6907f4c8bf0520218e52b6b52ae931d80af0abf34f307bfcc5bf9cc493b909bd8a32cdc172d48d81aedf5398e72eaba512928940fb2ff9f1f186d2b85d4739dd37724d71e4a33b7e52d4e3b001c9"
}


def verify_password(user, provided_password):
  # use the global users variable
  global users
  # Verify a stored password against one provided by user
  if user not in users:
    return False

  stored_password = users[user]
  salt = stored_password[:64]
  stored_password = stored_password[64:]
  pwdhash = hashlib.pbkdf2_hmac('sha512',
                                provided_password.encode('utf-8'),
                                salt.encode('ascii'),
                                100000)
  pwdhash = binascii.hexlify(pwdhash).decode('ascii')
  return pwdhash == stored_password


def main():
  if len(sys.argv) != 3:
    print("Invalid arguments!")
    sys.exit(3)

  user = sys.argv[1]
  password = sys.argv[2]
  isValid = verify_password(user, password)
  if isValid:
    print("Oikea salasana")
  else:
    print("Väärä käyttäjätunnus ja/tai salasana!")


if __name__ == '__main__':
  main()
