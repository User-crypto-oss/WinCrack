'''
    WinCrack is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    WinCrack is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with WinCrack.  If not, see <https://www.gnu.org/licenses/>.
'''

import os

os.system("sudo fdisk -l")
print("\nEnter the disk location: ")
disk = input()
os.system("sudo mount -rw " + disk + " /mnt/hdml")

os.system("mv winc.py /mnt/hdml/Windows/System32/config")

os.system("./cont.sh")