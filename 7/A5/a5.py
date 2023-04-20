#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File       :   a5.py
@Time       :   2023/04/20 11:34:14
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Define classes HeadsOrTails and RockPaperScissors that inherit Game class.

class Game(ABC):
    @abstractmethod
    def ask(self):
        '''returns string that asks for user's input'''
        pass

    @abstractmethod
    def check(self, user, machine):
        '''returns the result of the game (tie, win or lose) based on user's and machine's choices'''
        pass

    @abstractmethod
    def machine(self):
        '''generates and returns machines choice e.g. 1=heads or 1=rock'''
        pass

 

Override the necessary methods and test the games (Heads or Tails and Rock-Paper-Scissors) .

"""
from abc import ABC, abstractmethod
import random

class Game(ABC):
    @abstractmethod
    def ask(self):
        pass

    @abstractmethod
    def check(self, user, machine):
        pass

    @abstractmethod
    def machine(self):
        pass


class HeadsOrTails(Game):
    def ask(self):
        return "Choose heads or tails (h/t): "

    def check(self, user, machine):
        if user == machine:
            return "tie"
        elif user == "h" and machine == "t":
            return "lose"
        elif user == "t" and machine == "h":
            return "win"

    def machine(self):
        return random.choice(["h", "t"])


class RockPaperScissors(Game):
    def ask(self):
        return "Choose rock, paper or scissors (r/p/s): "

    def check(self, user, machine):
        if user == machine:
            return "tie"
        elif user == "r" and machine == "p":
            return "lose"
        elif user == "p" and machine == "s":
            return "lose"
        elif user == "s" and machine == "r":
            return "lose"
        else:
            return "win"

    def machine(self):
        return random.choice(["r", "p", "s"])

if __name__ == "__main__":
    # Test Heads or Tails game
    hot = HeadsOrTails()
    user_choice = input(hot.ask())
    machine_choice = hot.machine()
    result = hot.check(user_choice, machine_choice)
    print(f"You chose {user_choice}, machine chose {machine_choice}, result: {result}")

    # Test Rock-Paper-Scissors game
    rps = RockPaperScissors()
    user_choice = input(rps.ask())
    machine_choice = rps.machine()
    result = rps.check(user_choice, machine_choice)
    print(f"You chose {user_choice}, machine chose {machine_choice}, result: {result}")

