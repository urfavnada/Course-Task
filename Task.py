{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1af19b78-2160-4969-ac95-fd0f65d982f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the number of list elements 6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please Enter the numbers\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 1\n",
      " 3\n",
      " 2\n",
      " 6\n",
      " 4\n",
      " 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Odd list = [1, 3, 5]\n",
      "The Even list = [2, 6, 4]\n"
     ]
    }
   ],
   "source": [
    "# Task.1\n",
    "\n",
    "num = int(input('Enter the number of list elements'))\n",
    "The_list = []\n",
    "print('Please Enter the numbers')\n",
    "\n",
    "for n in range(num):\n",
    "    n = int(input())\n",
    "    The_list.append(n)\n",
    "    \n",
    "odd_list = []\n",
    "even_list = []\n",
    "\n",
    "for x in The_list:\n",
    "    if x % 2 == 0 :\n",
    "        even_list.append(x)\n",
    "    else :\n",
    "        odd_list.append(x)\n",
    "\n",
    "print('The Odd list =',odd_list)\n",
    "print('The Even list =',even_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6d1087e2-c965-4972-a6a8-7602625fc314",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Your Sentence Ich bin Nada Eltemsah Eltemsah\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The count of Unique Words is  4\n"
     ]
    }
   ],
   "source": [
    "# Task.2 \n",
    "\n",
    "Sentence = input('Enter Your Sentence')\n",
    "Sentence_list = Sentence.split()\n",
    "The_list = []\n",
    "\n",
    "for x in Sentence_list:\n",
    "    if x not in The_list:\n",
    "        The_list.append(x)\n",
    "print('The count of Unique Words is ',len(The_list))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8eaaee18-19aa-40d6-89d3-6442622bbec2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Last number 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "# Task.3\n",
    "\n",
    "number = int(input('Enter Last number'))\n",
    "\n",
    "for x in range(number + 1) :\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b56d40ee-5708-448e-aaf4-c803cd02fc3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Your number range 100\n",
      "Enter Your number 20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Divisible numbers of your number is = [0, 20, 40, 60, 80, 100]\n"
     ]
    }
   ],
   "source": [
    "# Task.4\n",
    "num1 = int(input('Enter Your number range'))\n",
    "num2 = int(input('Enter Your number'))\n",
    "The_numbers = []\n",
    "for x in range(num1+1) :\n",
    "    if x % num2 == 0 :\n",
    "        The_numbers.append(x)\n",
    "print('The Divisible numbers of your number is =',The_numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a2b65267-3b83-406f-a922-903b59721953",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Your first number 10\n",
      "Enter Your second number 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Divisible numbers of your numbers is = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]\n"
     ]
    }
   ],
   "source": [
    "# Task.5\n",
    "number1 = int(input('Enter Your first number'))\n",
    "number2 = int(input('Enter Your second number'))\n",
    "\n",
    "The_numbers = []\n",
    "\n",
    "for x in range(101) : \n",
    "    if x % number1 == 0 & x % number2 == 0 :\n",
    "        The_numbers.append(x)\n",
    "        \n",
    "print('The Divisible numbers of your numbers is =',The_numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "75d4bd8e-3f20-4d5a-8f63-a9384c7ec6d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Games world\n",
      "            Please Select game number\n",
      "            1. Even & Odd \n",
      "            2. Unique Words\n",
      "            3. listing numbers\n",
      "            4. Divisible numbers v.1\n",
      "            5. Divisible numbers v.2 \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Game number : 1\n",
      "Enter the number of list elements 10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please Enter the numbers\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 1\n",
      " 2\n",
      " 4\n",
      " 5\n",
      " 3\n",
      " 6\n",
      " 8\n",
      " 9\n",
      " 10\n",
      " 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Odd list = [1, 5, 3, 9, 7]\n",
      "The Even list = [2, 4, 6, 8, 10]\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter yes to use another Game, x to exit yes\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Games world\n",
      "            Please Select game number\n",
      "            1. Even & Odd \n",
      "            2. Unique Words\n",
      "            3. listing numbers\n",
      "            4. Divisible numbers v.1\n",
      "            5. Divisible numbers v.2 \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Game number : 2\n",
      "Enter Your Sentence nada nada yasser\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The count of Unique Words is  2\n",
      "Unique Words : ['nada', 'yasser']\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter yes to use another Game, x to exit yes\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Games world\n",
      "            Please Select game number\n",
      "            1. Even & Odd \n",
      "            2. Unique Words\n",
      "            3. listing numbers\n",
      "            4. Divisible numbers v.1\n",
      "            5. Divisible numbers v.2 \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Game number : 3\n",
      "Enter Last number 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The numbers :\n",
      "0\n",
      "1\n",
      "2\n",
      "3\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter yes to use another Game, x to exit yes\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Games world\n",
      "            Please Select game number\n",
      "            1. Even & Odd \n",
      "            2. Unique Words\n",
      "            3. listing numbers\n",
      "            4. Divisible numbers v.1\n",
      "            5. Divisible numbers v.2 \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Game number : 4\n",
      "Enter Your number range 20\n",
      "Enter Your number 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Divisible numbers of your number is = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter yes to use another Game, x to exit yes\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Games world\n",
      "            Please Select game number\n",
      "            1. Even & Odd \n",
      "            2. Unique Words\n",
      "            3. listing numbers\n",
      "            4. Divisible numbers v.1\n",
      "            5. Divisible numbers v.2 \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Game number : 5\n",
      "Enter Your first number 200\n",
      "Enter Your second number 20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Divisible numbers of your numbers is = [0]\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter yes to use another Game, x to exit 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Games world\n",
      "            Please Select game number\n",
      "            1. Even & Odd \n",
      "            2. Unique Words\n",
      "            3. listing numbers\n",
      "            4. Divisible numbers v.1\n",
      "            5. Divisible numbers v.2 \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Game number : 5\n",
      "Enter Your first number 100\n",
      "Enter Your second number 20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Divisible numbers of your numbers is = [0, 100]\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter yes to use another Game, x to exit x\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "See You\n"
     ]
    }
   ],
   "source": [
    "class Games :\n",
    "    def __init__(self):\n",
    "        while True:\n",
    "            print('''Welcome to Games world\n",
    "            Please Select game number\n",
    "            1. Even & Odd \n",
    "            2. Unique Words\n",
    "            3. listing numbers\n",
    "            4. Divisible numbers v.1\n",
    "            5. Divisible numbers v.2 ''')\n",
    "    \n",
    "            user_choice = int(input('Enter Game number :'))\n",
    "            if user_choice == 1 :\n",
    "                num = int(input('Enter the number of list elements'))\n",
    "                self.even_odd(num)\n",
    "            elif user_choice == 2 :\n",
    "                Sentence = input('Enter Your Sentence')\n",
    "                self.unique_words(Sentence)\n",
    "            elif user_choice == 3 :\n",
    "                number = int(input('Enter Last number'))\n",
    "                self.listing_number(number)\n",
    "            elif user_choice == 4:\n",
    "                num1 = int(input('Enter Your number range'))\n",
    "                num2 = int(input('Enter Your number'))\n",
    "                self.divisible_number_v1(num1,num2)\n",
    "            elif user_choice == 5:\n",
    "                number1 = int(input('Enter Your first number'))\n",
    "                number2 = int(input('Enter Your second number'))\n",
    "                self.divisible_number_v2(number1,number2)\n",
    "                \n",
    "            use_another_Game = input('Enter yes to use another Game, x to exit')\n",
    "            if use_another_Game == 'x':\n",
    "                print('See You')\n",
    "                break\n",
    "\n",
    "# Game.1\n",
    "    def even_odd(self,num):\n",
    "        The_list = []\n",
    "        print('Please Enter the numbers')\n",
    "        for n in range(num):\n",
    "            n = int(input())\n",
    "            The_list.append(n)\n",
    "        \n",
    "        odd_list = []\n",
    "        even_list = []\n",
    "        \n",
    "        for x in The_list:\n",
    "            if x % 2 == 0 :\n",
    "                even_list.append(x)\n",
    "            else :\n",
    "                odd_list.append(x)\n",
    "        print('The Odd list =',odd_list)\n",
    "        print('The Even list =',even_list)   \n",
    "\n",
    "    \n",
    "# Game.2\n",
    "    def unique_words(self,Sentence):\n",
    "        Sentence_list = Sentence.split()\n",
    "        The_list = []\n",
    "        for x in Sentence_list:\n",
    "            if x not in The_list:\n",
    "                The_list.append(x)\n",
    "        print('The count of Unique Words is ',len(The_list))\n",
    "        print('Unique Words :',The_list)\n",
    "\n",
    "    \n",
    "# Game.3\n",
    "    def listing_number(self,number):\n",
    "        print('The numbers :')\n",
    "        for x in range(number + 1) :\n",
    "            print(x)\n",
    "\n",
    "\n",
    "# Game.4\n",
    "    def divisible_number_v1(self,num1,num2):\n",
    "        The_numbers = []\n",
    "        for x in range(num1+1) :\n",
    "            if x % num2 == 0 :\n",
    "                The_numbers.append(x)\n",
    "        print('The Divisible numbers of your number is =',The_numbers)\n",
    "\n",
    "\n",
    "# Game.5\n",
    "    def divisible_number_v2(self,number1,number2):\n",
    "        The_numbers = []\n",
    "        for x in range(101) : \n",
    "            if x % number1 == 0 & x % number2 == 0 :\n",
    "                The_numbers.append(x)\n",
    "                \n",
    "        print('The Divisible numbers of your numbers is =',The_numbers)\n",
    "        \n",
    "G = Games()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "87b0fa65-da8a-4c44-9f24-d3dce133426d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
