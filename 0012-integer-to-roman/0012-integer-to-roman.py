class Solution:
    def intToRoman(self, num: int) -> str:
        tousand = num//1000
        undered= (num%1000)//100
        tens=(num%100)//10
        ones=(num%10)
        roman = {
            1000:"M",
            500:"D",
            100:"C",
            50:"L",
            10:"X",
            5:"V",
            1:"I"
        }
        #for 1000
        r_tousand=tousand*roman[1000]
        #for 100
        if -1<undered<4:
            r_undered=undered*roman[100]
        elif undered==4:
            r_undered=roman[100]+roman[500]
        elif 4<undered<9:
            r_undered=roman[500]+(undered-5)*roman[100]
        else:
            r_undered=roman[100]+roman[1000]
        #for 10
        if -1<tens<4:
            r_tens=tens*roman[10]
        elif tens==4:
            r_tens=roman[10]+roman[50]
        elif 4<tens<9:
            r_tens=roman[50]+(tens-5)*roman[10]
        else:
            r_tens=roman[10]+roman[100]
        #for 1
        if -1<ones<4:
            r_ones=ones*roman[1]
        elif ones==4:
            r_ones=roman[1]+roman[5]
        elif 4<ones<9:
            r_ones=roman[5]+(ones-5)*roman[1]
        else:
            r_ones=roman[1]+roman[10]
        return r_tousand + r_undered + r_tens + r_ones
        

        
        