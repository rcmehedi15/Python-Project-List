#pip installl speeedtest

from turtle import speed
import speedtest

ST = speedtest.Speedtest()

print("Download Speed : ")
print(ST.download())

print("\nUploading Speed : ")
print(ST.upload())

print("\nPing: ")
print(ST.results.ping)