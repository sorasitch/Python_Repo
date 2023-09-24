# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 12:13:59 2021

@author: schomsin
"""

from time import sleep

epoch = 5



def train_nn():    
    result = 0
    for i in range(epoch):
        result += i * 2
        sleep(1)
    return result

train_nn()

def print_message(p=0): print("Hello callback")

def train_nn2(callback):    
    result = 0
    for i in range(epoch):
        result += i * 2
        sleep(1)
        if callback: callback()
    return result

train_nn2(print_message)


def train_nn3(callback):    
    result = 0
    for i in range(5):
        result += i * 2
        sleep(1)
        if callback: callback(i)
    return result

def print_message2(epoch_no):
    print(f'Finished train_nn Epoch No. {epoch_no}!')
    
train_nn3(print_message2)

class MessagePrinterCallback():
    def __init__(self, message="Finished"): self.message = message
    def __call__(self, epoch_no=0): print(f'{self.message} train_nn Epoch No. {epoch_no}!')
    
fs_cb1 = MessagePrinterCallback("Finished")
fs_cb2 = MessagePrinterCallback("Succeeded")


train_nn3(fs_cb1)
train_nn3(fs_cb2)